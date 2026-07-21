"""Native epistemic-graph ingestion for Portainer infrastructure records.

All writes use the required ``agent_utilities.knowledge_graph.memory.native_ingest``
primitive. Nodes use canonical ``node_type`` and edges use canonical ``relationship``;
nodes and edges commit in one native transaction. Missing engine dependencies, rejected
records, conflicts, and transaction failures propagate as ``NativeIngestError``.
"""

from __future__ import annotations

import logging
from typing import Any
from urllib.parse import urlsplit

from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _native_ingest_entities,
)

logger = logging.getLogger("portainer_agent.kg")

_SOURCE = "portainer-agent"
_DOMAIN = "portainer"


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write canonical typed nodes and relationships in one native transaction."""
    return _native_ingest_entities(
        entities,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


def _get(rec: dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Return the first present, non-None value among ``keys`` (Portainer/Docker vary case)."""
    for k in keys:
        if k in rec and rec[k] is not None:
            return rec[k]
    return default


def ingest_environments(
    endpoints: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Portainer endpoint records → ``:Environment`` (+ ``:EndpointGroup``) nodes."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for ep in endpoints or []:
        eid = _get(ep, "Id", "id")
        if eid is None:
            continue
        entities.append(
            {
                "id": f"portainer:environment:{eid}",
                "node_type": "Environment",
                "name": _get(ep, "Name", "name"),
                "environmentType": _get(ep, "Type", "type"),
                "endpointUrl": _get(ep, "URL", "url"),
                "status": _status_label(_get(ep, "Status", "status")),
                "portainerId": str(eid),
            }
        )
        gid = _get(ep, "GroupId", "groupId")
        if gid:
            entities.append(
                {
                    "id": f"portainer:endpointgroup:{gid}",
                    "node_type": "EndpointGroup",
                    "portainerId": str(gid),
                }
            )
            relationships.append(
                {
                    "source": f"portainer:environment:{eid}",
                    "target": f"portainer:endpointgroup:{gid}",
                    "relationship": "partOfEndpointGroup",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def _normalize_repo_url(url: Any) -> tuple[str, str] | None:
    """Normalize a git remote URL -> ``(clean_url, repo_node_id)``, or ``None``.

    Strips embedded credentials, a trailing ``.git``, and a trailing slash so the id is
    stable regardless of protocol/auth. Handles HTTP(S) and SCP-style
    (``git@host:owner/name.git``) remotes.

    The source-code connectors (``gitlab-api``, ``github-agent``) key their own
    ``:Project``/``:Repository`` nodes by *that system's internal numeric id*
    (``gitlab:project:<id>``, ``github:repository:<id>``) — an id Portainer's
    ``GitConfig`` does not carry, only the remote URL. So this uses a clean
    normalized-URL id instead (``git:repo:<host>/<path>``); it intentionally does not
    (and cannot) collide with those ids.
    """
    if not url or not isinstance(url, str):
        return None
    raw = url.strip()
    if not raw:
        return None
    if "://" in raw:
        parts = urlsplit(raw)
        host = (parts.hostname or "").lower()
        path = parts.path or ""
    elif "@" in raw and ":" in raw:
        # SCP-style remote, e.g. git@github.com:owner/name.git
        _, _, rest = raw.partition("@")
        host, _, path = rest.partition(":")
        host = host.lower()
    else:
        return None
    path = path.strip("/")
    if path.endswith(".git"):
        path = path[: -len(".git")]
    if not host or not path:
        return None
    return f"https://{host}/{path}", f"git:repo:{host}/{path}"


def _repo_from_git_config(
    stack: dict[str, Any],
) -> tuple[str, str, Any, Any] | None:
    """Extract ``(repo_node_id, clean_url, ref, compose_path)`` from a Stack's ``GitConfig``."""
    git_conf = _get(stack, "GitConfig", "gitConfig")
    if not git_conf:
        return None
    normalized = _normalize_repo_url(_get(git_conf, "URL", "url"))
    if not normalized:
        return None
    clean_url, repo_node = normalized
    ref = _get(git_conf, "ReferenceName", "referenceName")
    compose_path = _get(git_conf, "ConfigFilePath", "configFilePath") or _get(
        stack, "EntryPoint", "entryPoint"
    )
    return repo_node, clean_url, ref, compose_path


def ingest_stacks(
    stacks: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Portainer stack records → ``:Stack`` nodes linked to their ``:Environment``.

    Git-backed stacks (``GitConfig``) additionally get ``repositoryUrl`` /
    ``repositoryRef`` / ``composePath`` stamped onto the ``:Stack`` node, plus a
    ``:Repository`` node and a ``:deployedFrom`` edge, so the deployed stack traces
    back to its source repo.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for st in stacks or []:
        sid = _get(st, "Id", "id")
        if sid is None:
            continue
        stack_node = f"portainer:stack:{sid}"
        stack_entity: dict[str, Any] = {
            "id": stack_node,
            "node_type": "Stack",
            "name": _get(st, "Name", "name"),
            "stackType": _get(st, "Type", "type"),
            "status": _stack_status(_get(st, "Status", "status")),
            "portainerId": str(sid),
        }
        repo = _repo_from_git_config(st)
        if repo:
            repo_node, repo_url, repo_ref, compose_path = repo
            stack_entity["repositoryUrl"] = repo_url
            if repo_ref:
                stack_entity["repositoryRef"] = repo_ref
            if compose_path:
                stack_entity["composePath"] = compose_path
            entities.append(
                {"id": repo_node, "node_type": "Repository", "url": repo_url}
            )
            relationships.append(
                {
                    "source": stack_node,
                    "target": repo_node,
                    "relationship": "deployedFrom",
                }
            )
        entities.append(stack_entity)
        env = _get(st, "EndpointId", "endpointId")
        if env is not None:
            relationships.append(
                {
                    "source": stack_node,
                    "target": f"portainer:environment:{env}",
                    "relationship": "inEnvironment",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_containers(
    containers: list[dict[str, Any]],
    environment_id: int | str,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Docker container records → ``:Container`` nodes in an ``:Environment``.

    Links each container to the stack it was deployed by (``com.docker.compose.project``
    / ``com.docker.stack.namespace`` label) when present.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    env_node = f"portainer:environment:{environment_id}"
    for c in containers or []:
        cid = _get(c, "Id", "id")
        if cid is None:
            continue
        node_id = f"portainer:container:{environment_id}_{cid}"
        names = _get(c, "Names", "names", default=[])
        name = (
            names[0] if isinstance(names, list) and names else _get(c, "Name", "name")
        )
        if isinstance(name, str):
            name = name.lstrip("/")
        entities.append(
            {
                "id": node_id,
                "node_type": "Container",
                "name": name,
                "imageName": _get(c, "Image", "image"),
                "status": _get(c, "State", "state"),
                "dockerId": str(cid),
            }
        )
        relationships.append(
            {"source": node_id, "target": env_node, "relationship": "inEnvironment"}
        )
        labels = _get(c, "Labels", "labels", default={}) or {}
        project = labels.get("com.docker.stack.namespace") or labels.get(
            "com.docker.compose.project"
        )
        if project:
            relationships.append(
                {
                    "source": node_id,
                    "target": f"portainer:stack:name:{project}",
                    "relationship": "deployedByStack",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def _status_label(val: Any) -> Any:
    """Portainer endpoint Status is 1=up, 2=down; pass strings through unchanged."""
    if val == 1:
        return "up"
    if val == 2:
        return "down"
    return val


def _stack_status(val: Any) -> Any:
    """Portainer stack Status is 1=active, 2=inactive; pass strings through unchanged."""
    if val == 1:
        return "active"
    if val == 2:
        return "inactive"
    return val
