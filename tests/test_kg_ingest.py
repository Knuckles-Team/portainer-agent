"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_environments`` / ``ingest_stacks`` /
``ingest_containers`` seam with a fake engine client (no engine required), asserting the
txn add_node/commit + edge calls and the Portainer record -> :Environment/:Stack/:Container
mapping. CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from portainer_agent.kg_ingest import (
    ingest_containers,
    ingest_entities,
    ingest_environments,
    ingest_stacks,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def commit(self, txn):
        self.committed = True
        return True


class _FakeEdges:
    def __init__(self):
        self.edges = []

    def add(self, src, dst, props):
        self.edges.append((src, dst, props))


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()
        self.edges = _FakeEdges()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "type": "Environment", "name": "prod"},
            {"id": "b", "type": "Stack"},
        ],
        [{"source": "b", "target": "a", "type": "inEnvironment"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "portainer-agent"
    assert c.txn.nodes["a"]["domain"] == "portainer"
    assert c.edges.edges == [("b", "a", {"type": "inEnvironment"})]


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
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    env = c.txn.nodes["portainer:environment:1"]
    assert env["type"] == "Environment"
    assert env["environmentType"] == 2
    assert env["endpointUrl"] == "tcp://node:9001"
    assert env["status"] == "up"
    assert env["portainerId"] == "1"
    assert c.txn.nodes["portainer:endpointgroup:3"]["type"] == "EndpointGroup"
    assert c.edges.edges == [
        (
            "portainer:environment:1",
            "portainer:endpointgroup:3",
            {"type": "partOfEndpointGroup"},
        )
    ]


def test_ingest_stacks_links_environment():
    c = _FakeClient()
    res = ingest_stacks(
        [{"Id": 5, "Name": "web", "Type": 2, "Status": 1, "EndpointId": 1}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    st = c.txn.nodes["portainer:stack:5"]
    assert st["type"] == "Stack"
    assert st["stackType"] == 2
    assert st["status"] == "active"
    assert c.edges.edges == [
        ("portainer:stack:5", "portainer:environment:1", {"type": "inEnvironment"})
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
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 2}
    st = c.txn.nodes["portainer:stack:5"]
    assert st["repositoryUrl"] == "https://github.com/acme/web-stack"
    assert st["repositoryRef"] == "refs/heads/main"
    # explicit GitConfig.ConfigFilePath wins over the top-level EntryPoint
    assert st["composePath"] == "deploy/docker-compose.yml"

    repo_node = "git:repo:github.com/acme/web-stack"
    repo = c.txn.nodes[repo_node]
    assert repo["type"] == "Repository"
    assert repo["url"] == "https://github.com/acme/web-stack"
    assert (
        "portainer:stack:5",
        repo_node,
        {"type": "deployedFrom"},
    ) in c.edges.edges
    assert (
        "portainer:stack:5",
        "portainer:environment:1",
        {"type": "inEnvironment"},
    ) in c.edges.edges


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
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    st = c.txn.nodes["portainer:stack:6"]
    assert st["repositoryUrl"] == "https://gitlab.example.com/team/api"
    # no ReferenceName/ConfigFilePath supplied -> falls back to EntryPoint, no ref
    assert st["composePath"] == "docker-compose.yml"
    assert "repositoryRef" not in st
    assert c.txn.nodes["git:repo:gitlab.example.com/team/api"]["type"] == "Repository"


def test_ingest_stacks_without_git_config_has_no_repository_node():
    c = _FakeClient()
    res = ingest_stacks(
        [{"Id": 7, "Name": "plain", "EndpointId": 1, "GitConfig": None}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    st = c.txn.nodes["portainer:stack:7"]
    assert "repositoryUrl" not in st
    assert "repositoryRef" not in st
    assert "composePath" not in st
    assert not any(n.startswith("git:repo:") for n in c.txn.nodes)
    assert c.edges.edges == [
        ("portainer:stack:7", "portainer:environment:1", {"type": "inEnvironment"})
    ]


def test_ingest_stacks_git_backed_noops_without_engine():
    # No injected client + no reachable engine -> clean no-op, even for a git-backed stack.
    assert (
        ingest_stacks(
            [
                {
                    "Id": 8,
                    "Name": "web",
                    "GitConfig": {"URL": "https://github.com/acme/web.git"},
                }
            ]
        )
        is None
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
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 2}
    node = c.txn.nodes["portainer:container:1_abc123"]
    assert node["type"] == "Container"
    assert node["name"] == "web_1"
    assert node["imageName"] == "nginx:latest"
    assert node["status"] == "running"
    assert node["dockerId"] == "abc123"
    assert (
        "portainer:container:1_abc123",
        "portainer:environment:1",
        {"type": "inEnvironment"},
    ) in c.edges.edges
    assert (
        "portainer:container:1_abc123",
        "portainer:stack:name:web",
        {"type": "deployedByStack"},
    ) in c.edges.edges


def test_ingest_noops_without_engine():
    # No injected client + no reachable engine -> clean no-op.
    assert ingest_entities([{"id": "a", "type": "Environment"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_environments([], client=_FakeClient()) is None
    assert ingest_stacks([], client=_FakeClient()) is None
    assert ingest_containers([], environment_id=1, client=_FakeClient()) is None
