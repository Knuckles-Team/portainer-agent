"""Native epistemic-graph ingestion for Portainer records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The connector natively pushes its
data into the ONE epistemic-graph knowledge graph as **typed OWL nodes**
(``:Environment``, ``:Stack``, ``:Container``, ``:Service``, …) + links, using the
lightweight engine client (``GraphComputeEngine()._client`` + ``txn``) — the same fast
client the blob ``MediaStore`` uses, NOT the heavy in-process ingestion engine.

It is a thin mapper over the shared primitive
``agent_utilities.knowledge_graph.memory.native_ingest``; when that primitive (or a
reachable engine) is absent, every entry point **no-ops** (returns ``None``) via a
self-contained txn fallback, so the connector keeps working with zero KG infrastructure.
Nodes carry the shared provenance (``domain``/``source``) and match the classes federated
by ``portainer_agent.ontology`` (``portainer.ttl``). Node ids follow
``portainer:<class>:<externalId>``.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("portainer_agent.kg")

_SOURCE = "portainer-agent"
_DOMAIN = "portainer"
_DEFAULT_GRAPH = "__commons__"


def _client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        return client, (getattr(engine, "graph_name", None) or _DEFAULT_GRAPH)
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph via the fast engine client.

    Prefers the shared ``native_ingest`` primitive; falls back to a self-contained txn
    write when it (or a reachable engine) is absent. ``entities``:
    ``[{"id":..., "type":<owl:Class>, ...props}]``; ``relationships``:
    ``[{"source":id, "target":id, "type":rel}]``. Returns ``{"nodes":n, "edges":m}`` or
    ``None`` (no engine / failure; never raises). ``client``/``graph`` may be injected
    (tests); otherwise resolved on demand.
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None

    # Preferred path: the shared fleet primitive (once shipped in agent_utilities).
    if client is None:
        try:
            from agent_utilities.knowledge_graph.memory.native_ingest import (
                ingest_entities as _shared_ingest,
            )

            return _shared_ingest(entities, relationships, source=source, domain=domain)
        except Exception as e:  # noqa: BLE001 — primitive absent: self-contained fallback
            logger.debug("KG ingest: shared primitive unavailable: %s", e)

    if client is None:
        client, graph = _client()
    if client is None:
        return None
    graph = graph or _DEFAULT_GRAPH

    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", source)
            props.setdefault("domain", domain)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


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
) -> dict[str, int] | None:
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
                "type": "Environment",
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
                    "type": "EndpointGroup",
                    "portainerId": str(gid),
                }
            )
            relationships.append(
                {
                    "source": f"portainer:environment:{eid}",
                    "target": f"portainer:endpointgroup:{gid}",
                    "type": "partOfEndpointGroup",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_stacks(
    stacks: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map Portainer stack records → ``:Stack`` nodes linked to their ``:Environment``."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for st in stacks or []:
        sid = _get(st, "Id", "id")
        if sid is None:
            continue
        entities.append(
            {
                "id": f"portainer:stack:{sid}",
                "type": "Stack",
                "name": _get(st, "Name", "name"),
                "stackType": _get(st, "Type", "type"),
                "status": _stack_status(_get(st, "Status", "status")),
                "portainerId": str(sid),
            }
        )
        env = _get(st, "EndpointId", "endpointId")
        if env is not None:
            relationships.append(
                {
                    "source": f"portainer:stack:{sid}",
                    "target": f"portainer:environment:{env}",
                    "type": "inEnvironment",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_containers(
    containers: list[dict[str, Any]],
    environment_id: int | str,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "Container",
                "name": name,
                "imageName": _get(c, "Image", "image"),
                "status": _get(c, "State", "state"),
                "dockerId": str(cid),
            }
        )
        relationships.append(
            {"source": node_id, "target": env_node, "type": "inEnvironment"}
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
                    "type": "deployedByStack",
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
