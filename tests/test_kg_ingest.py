"""Epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_environments`` / ``ingest_stacks`` /
``ingest_containers`` seam against a fake transport one level below the SDK's own
``SourceIngest`` request builder (per the fleet SDK migration recipe), asserting the
committed nodes/edges and the Portainer record -> :Environment/:Stack/:Container
mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.

This file no longer needs the ``agent_utilities[graphos]`` opt-in extra (WD4-FIX-01
defect (d)) -- ``kg_ingest.py`` now rides ``agent_connector_sdk.ingest`` exclusively.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

from portainer_agent.kg_ingest import (
    ingest_containers,
    ingest_entities,
    ingest_environments,
    ingest_stacks,
)


class _FakeTransport:
    def __init__(self) -> None:
        self.requests: list[Any] = []

    async def source_status(self, connector: str, stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: Any) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data: bytes) -> str:
        raise AssertionError("this connector's ingestion carries no media")


@pytest.fixture
def ingest() -> tuple[KnowledgeIngest, _FakeTransport]:
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


def _node(transport: _FakeTransport, node_id: str) -> dict[str, Any]:
    for request in transport.requests:
        for record in request.records:
            if record.record_id == node_id:
                return dict(record.payload)
    raise AssertionError(f"no committed record {node_id!r}")


def _edges(transport: _FakeTransport) -> set[tuple[str, str, str]]:
    edges: set[tuple[str, str, str]] = set()
    for request in transport.requests:
        for rel in request.relationships:
            relationship_name = rel.relation_reference.rsplit("/relations/", 1)[-1]
            edges.add((rel.source.record_id, rel.target.record_id, relationship_name))
    return edges


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "Environment", "name": "prod"},
            {"id": "b", "node_type": "Stack"},
        ],
        [{"source": "b", "target": "a", "relationship": "inEnvironment"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    record_ids = {record.record_id for record in transport.requests[0].records}
    assert record_ids == {"a", "b"}
    assert _edges(transport) == {("b", "a", "inEnvironment")}


@pytest.mark.asyncio
async def test_ingest_environments_maps_env_and_group(ingest):
    service, transport = ingest
    res = await ingest_environments(
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
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    env = _node(transport, "portainer:environment:1")
    assert env["environmentType"] == 2
    assert env["endpointUrl"] == "tcp://node:9001"
    assert env["status"] == "up"
    assert env["portainerId"] == "1"
    _node(transport, "portainer:endpointgroup:3")
    assert _edges(transport) == {
        ("portainer:environment:1", "portainer:endpointgroup:3", "partOfEndpointGroup")
    }


@pytest.mark.asyncio
async def test_ingest_stacks_links_environment(ingest):
    service, transport = ingest
    res = await ingest_stacks(
        [{"Id": 5, "Name": "web", "Type": 2, "Status": 1, "EndpointId": 1}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    st = _node(transport, "portainer:stack:5")
    assert st["stackType"] == 2
    assert st["status"] == "active"
    assert _edges(transport) == {
        ("portainer:stack:5", "portainer:environment:1", "inEnvironment")
    }


@pytest.mark.asyncio
async def test_ingest_stacks_git_backed_creates_repository_and_deployed_from_edge(
    ingest,
):
    service, transport = ingest
    res = await ingest_stacks(
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
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 2}
    st = _node(transport, "portainer:stack:5")
    assert st["repositoryUrl"] == "https://github.com/acme/web-stack"
    assert st["repositoryRef"] == "refs/heads/main"
    # explicit GitConfig.ConfigFilePath wins over the top-level EntryPoint
    assert st["composePath"] == "deploy/docker-compose.yml"

    repo_node = "git:repo:github.com/acme/web-stack"
    repo = _node(transport, repo_node)
    # agent_connector_sdk.privacy.PersistencePrivacyGuard redacts any property
    # literally named "url" by field name (not content) before it crosses the
    # ingest boundary -- a new SDK-wide behavior this migration surfaces, not a
    # mapping bug. The stack's own "repositoryUrl" property (checked above) is
    # unaffected since that exact field name isn't in the guard's location set.
    assert repo["url"] == "[REDACTED_LOCATION]"
    edges = _edges(transport)
    assert ("portainer:stack:5", repo_node, "deployedFrom") in edges
    assert ("portainer:stack:5", "portainer:environment:1", "inEnvironment") in edges


@pytest.mark.asyncio
async def test_ingest_stacks_git_backed_scp_style_and_entrypoint_fallback(ingest):
    service, transport = ingest
    res = await ingest_stacks(
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
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    st = _node(transport, "portainer:stack:6")
    assert st["repositoryUrl"] == "https://gitlab.example.com/team/api"
    # no ReferenceName/ConfigFilePath supplied -> falls back to EntryPoint, no ref
    assert st["composePath"] == "docker-compose.yml"
    assert "repositoryRef" not in st
    _node(transport, "git:repo:gitlab.example.com/team/api")


@pytest.mark.asyncio
async def test_ingest_stacks_without_git_config_has_no_repository_node(ingest):
    service, transport = ingest
    res = await ingest_stacks(
        [{"Id": 7, "Name": "plain", "EndpointId": 1, "GitConfig": None}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    st = _node(transport, "portainer:stack:7")
    assert "repositoryUrl" not in st
    assert "repositoryRef" not in st
    assert "composePath" not in st
    all_ids = {
        record.record_id for req in transport.requests for record in req.records
    }
    assert not any(n.startswith("git:repo:") for n in all_ids)
    assert _edges(transport) == {
        ("portainer:stack:7", "portainer:environment:1", "inEnvironment")
    }


@pytest.mark.asyncio
async def test_ingest_stacks_propagates_ingest_failure(monkeypatch, ingest):
    service, _transport = ingest

    async def _fail(*_args, **_kwargs):
        raise IngestError("epistemic-graph is unavailable")

    monkeypatch.setattr(service, "submit", _fail)
    with pytest.raises(IngestError, match="unavailable"):
        await ingest_stacks(
            [
                {
                    "Id": 8,
                    "Name": "web",
                    "GitConfig": {"URL": "https://github.com/acme/web.git"},
                }
            ],
            ingest=service,
        )


@pytest.mark.asyncio
async def test_ingest_containers_links_env_and_stack(ingest):
    service, transport = ingest
    res = await ingest_containers(
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
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 2}
    node = _node(transport, "portainer:container:1_abc123")
    assert node["name"] == "web_1"
    assert node["imageName"] == "nginx:latest"
    assert node["status"] == "running"
    assert node["dockerId"] == "abc123"
    edges = _edges(transport)
    assert ("portainer:container:1_abc123", "portainer:environment:1", "inEnvironment") in edges
    assert (
        "portainer:container:1_abc123",
        "portainer:stack:name:web",
        "deployedByStack",
    ) in edges


@pytest.mark.asyncio
async def test_retired_structural_alias_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="node_type"):
        await ingest_entities(
            [{"id": "a", "type": "Environment"}], ingest=service
        )


@pytest.mark.asyncio
async def test_empty_ingest_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="at least one entity"):
        await ingest_entities([], ingest=service)
