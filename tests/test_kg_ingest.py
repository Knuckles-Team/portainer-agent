"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_environments`` / ``ingest_stacks`` /
``ingest_containers`` seam with a fake engine client (no engine required), asserting the
txn add_node/commit + edge calls and the Portainer record -> :Environment/:Stack/:Container
mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest

# `agent_utilities.knowledge_graph.memory` unconditionally imports
# `agent_utilities.numeric` at module-load time, which in turn requires the
# compiled `epistemic_graph.numeric` kernel. agent-utilities moved that
# kernel out of its base dependency set into the opt-in `graphos` extra
# (GOC-73); this repo depends only on `agent-utilities[mcp]`, which does not
# pull it in. Left unguarded, importing it here raises a bare
# ModuleNotFoundError/ImportError chain that pytest reports as a COLLECTION
# ERROR — which (a) reads exactly like a regression in THIS repo and
# (b) aborts collection of the entire `tests/` suite, not just this file
# (`pytest tests/ -q` reports "0 tests collected, 1 error" for the whole
# run, which is why lanes have been passing `--ignore=tests/test_kg_ingest.py`
# and silently losing coverage on both sides of every before/after
# comparison). This is an ENVIRONMENT/packaging gap, not application-code
# breakage — install `agent-utilities[graphos]>=2.27.0` to exercise these
# tests. See plans/complex/waves/wD4/WD4-FIX-01.md defect (d). Turn it into
# a clean, LOUD, explained skip of just this file instead.
pytest.importorskip(
    "agent_utilities.knowledge_graph.memory.native_ingest",
    # pytest 9.1 changed importorskip()'s default `exc_type` from
    # ImportError to ModuleNotFoundError (see the versionchanged note in
    # pytest.importorskip's own docstring). agent_utilities.numeric
    # deliberately re-raises a plain ImportError (not ModuleNotFoundError)
    # with an explanatory message, so the new default silently fails to
    # catch it and the "skip" degrades right back into the collection
    # error this guard exists to prevent. Pin exc_type explicitly so the
    # guard keeps working regardless of installed pytest version.
    exc_type=ImportError,
    reason=(
        "agent_utilities.numeric requires the compiled epistemic_graph.numeric "
        "kernel, shipped only behind agent-utilities' opt-in `graphos` extra "
        "(GOC-73); not installed by this repo's `agent-utilities[mcp]` "
        "dependency — install `agent-utilities[graphos]>=2.27.0` to run "
        "KG-ingestion tests (WD4-FIX-01 defect (d))"
    ),
)

from agent_utilities.knowledge_graph.core.session import GraphSession, use_session
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.models.company_brain import ActorType
from agent_utilities.security.brain_context import ActorContext, use_actor

from portainer_agent.kg_ingest import (
    ingest_containers,
    ingest_entities,
    ingest_environments,
    ingest_stacks,
)


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "Environment", "name": "prod"},
            {"id": "b", "node_type": "Stack"},
        ],
        [{"source": "b", "target": "a", "relationship": "inEnvironment"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(c.changes.applied) == 1
    assert set(c.nodes.values) == {"a", "b"}
    # provenance is stamped
    assert c.nodes.values["a"]["source"] == "portainer-agent"
    assert c.nodes.values["a"]["domain"] == "portainer"
    assert c.changes.edges == [("b", "a", {"relationship": "inEnvironment"})]


def test_ingest_environments_maps_env_and_group():
    c = _FakeClient()
    res = ingest_environments(
        [
            {
                "Id": 1,
                "Name": "docker-prod",
                "Type": 2,
                "URL": "tcp://node:9001",
                "Status": 1,
                "GroupId": 3,
            }
        ],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    env = c.nodes.values["portainer:environment:1"]
    assert env["node_type"] == "Environment"
    assert env["environmentType"] == 2
    assert env["endpointUrl"] == "tcp://node:9001"
    assert env["status"] == "up"
    assert env["portainerId"] == "1"
    assert c.nodes.values["portainer:endpointgroup:3"]["node_type"] == "EndpointGroup"
    assert c.changes.edges == [
        (
            "portainer:environment:1",
            "portainer:endpointgroup:3",
            {"relationship": "partOfEndpointGroup"},
        )
    ]


def test_ingest_stacks_links_environment():
    c = _FakeClient()
    res = ingest_stacks(
        [{"Id": 5, "Name": "web", "Type": 2, "Status": 1, "EndpointId": 1}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 1}
    st = c.nodes.values["portainer:stack:5"]
    assert st["node_type"] == "Stack"
    assert st["stackType"] == 2
    assert st["status"] == "active"
    assert c.changes.edges == [
        (
            "portainer:stack:5",
            "portainer:environment:1",
            {"relationship": "inEnvironment"},
        )
    ]


def test_ingest_stacks_git_backed_creates_repository_and_deployed_from_edge():
    c = _FakeClient()
    res = ingest_stacks(
        [
            {
                "Id": 5,
                "Name": "web",
                "Type": 2,
                "Status": 1,
                "EndpointId": 1,
                "EntryPoint": "docker-compose.yml",
                "GitConfig": {
                    "URL": "https://oauth2:token123@github.com/acme/web-stack.git/",
                    "ReferenceName": "refs/heads/main",
                    "ConfigFilePath": "deploy/docker-compose.yml",
                },
            }
        ],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 2}
    st = c.nodes.values["portainer:stack:5"]
    assert st["repositoryUrl"] == "https://github.com/acme/web-stack"
    assert st["repositoryRef"] == "refs/heads/main"
    # explicit GitConfig.ConfigFilePath wins over the top-level EntryPoint
    assert st["composePath"] == "deploy/docker-compose.yml"

    repo_node = "git:repo:github.com/acme/web-stack"
    repo = c.nodes.values[repo_node]
    assert repo["node_type"] == "Repository"
    assert repo["url"] == "https://github.com/acme/web-stack"
    assert (
        "portainer:stack:5",
        repo_node,
        {"relationship": "deployedFrom"},
    ) in c.changes.edges
    assert (
        "portainer:stack:5",
        "portainer:environment:1",
        {"relationship": "inEnvironment"},
    ) in c.changes.edges


def test_ingest_stacks_git_backed_scp_style_and_entrypoint_fallback():
    c = _FakeClient()
    res = ingest_stacks(
        [
            {
                "Id": 6,
                "Name": "api",
                "EntryPoint": "docker-compose.yml",
                "GitConfig": {
                    "URL": "git@gitlab.example.com:team/api.git",
                },
            }
        ],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    st = c.nodes.values["portainer:stack:6"]
    assert st["repositoryUrl"] == "https://gitlab.example.com/team/api"
    # no ReferenceName/ConfigFilePath supplied -> falls back to EntryPoint, no ref
    assert st["composePath"] == "docker-compose.yml"
    assert "repositoryRef" not in st
    assert (
        c.nodes.values["git:repo:gitlab.example.com/team/api"]["node_type"]
        == "Repository"
    )


def test_ingest_stacks_without_git_config_has_no_repository_node():
    c = _FakeClient()
    res = ingest_stacks(
        [{"Id": 7, "Name": "plain", "EndpointId": 1, "GitConfig": None}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 1}
    st = c.nodes.values["portainer:stack:7"]
    assert "repositoryUrl" not in st
    assert "repositoryRef" not in st
    assert "composePath" not in st
    assert not any(n.startswith("git:repo:") for n in c.nodes.values)
    assert c.changes.edges == [
        (
            "portainer:stack:7",
            "portainer:environment:1",
            {"relationship": "inEnvironment"},
        )
    ]


def test_ingest_stacks_propagates_native_ingest_failure(monkeypatch):
    def _fail(*_args, **_kwargs):
        raise NativeIngestError("native ingest engine client is unavailable")

    monkeypatch.setattr("portainer_agent.kg_ingest._native_ingest_entities", _fail)
    with pytest.raises(NativeIngestError, match="engine client is unavailable"):
        ingest_stacks(
            [
                {
                    "Id": 8,
                    "Name": "web",
                    "GitConfig": {"URL": "https://github.com/acme/web.git"},
                }
            ]
        )


def test_ingest_containers_links_env_and_stack():
    c = _FakeClient()
    res = ingest_containers(
        [
            {
                "Id": "abc123",
                "Names": ["/web_1"],
                "Image": "nginx:latest",
                "State": "running",
                "Labels": {"com.docker.stack.namespace": "web"},
            }
        ],
        environment_id=1,
        client=c,
    )
    assert res == {"nodes": 1, "edges": 2}
    node = c.nodes.values["portainer:container:1_abc123"]
    assert node["node_type"] == "Container"
    assert node["name"] == "web_1"
    assert node["imageName"] == "nginx:latest"
    assert node["status"] == "running"
    assert node["dockerId"] == "abc123"
    assert (
        "portainer:container:1_abc123",
        "portainer:environment:1",
        {"relationship": "inEnvironment"},
    ) in c.changes.edges
    assert (
        "portainer:container:1_abc123",
        "portainer:stack:name:web",
        {"relationship": "deployedByStack"},
    ) in c.changes.edges


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Environment"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
