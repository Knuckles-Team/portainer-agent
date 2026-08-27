"""Characterization tests for ``register_kubernetes_tools.portainer_kubernetes``
in ``portainer_agent/mcp/mcp_kubernetes.py`` (CCN 51) -- an ORPHANED,
independently-drifted copy.

Per the CXA-FL-PORTAINERAGENT-01 lane brief: this module is reachable only
through ``portainer_agent/mcp/__init__.py`` (which this lane does not own
and must not edit), and nothing in the running server
(``get_mcp_instance()`` in ``mcp_server.py``) ever imports the
``portainer_agent.mcp`` subpackage -- tool discovery there works by
inspecting ``mcp_server.py``'s own module namespace via
``register_tool_surface(..., tools_module=sys.modules[__name__])``. So this
copy is dead from the live server's perspective, but not deletable given
this lane's file partition (see BUGS FOUND). It is decomposed in place as
its own independent target and is NOT kept in sync with
``mcp_server.py``'s ``portainer_kubernetes`` -- `inspect.getsource()`
comparison confirms the two bodies have already drifted apart (this copy
has no ``resolve_action()`` call at all: plain string-equality dispatch,
no typo/fuzzy correction, no ``list_actions``/``help``/``actions``
discovery keywords, and its own trailing "Unknown action" raise is
genuinely reachable, unlike the mcp_server.py copy's -- and its message
string has a real quoting bug, see BUGS FOUND).

No test anywhere in the repo covers this module before this file. Loaded
by its full module path so the module-under-test is unambiguous.
"""

import asyncio
from unittest.mock import MagicMock

import pytest
from fastmcp import FastMCP

import portainer_agent.mcp.mcp_kubernetes as mcp_kubernetes_module


def _capture_tool(register_fn, tool_name):
    mcp = FastMCP("test")
    captured = {}
    original = mcp.tool

    def cap(*args, **kwargs):
        def deco(fn):
            captured[fn.__name__] = fn
            return original(*args, **kwargs)(fn)

        return deco

    mcp.tool = cap  # type: ignore[method-assign]
    register_fn(mcp)
    return captured[tool_name]


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


@pytest.fixture
def k8s_fn():
    return _capture_tool(
        mcp_kubernetes_module.register_kubernetes_tools, "portainer_kubernetes"
    )


@pytest.mark.parametrize(
    "action,method_name",
    [
        ("get_k8s_dashboard", "get_k8s_dashboard"),
        ("get_k8s_namespaces", "get_k8s_namespaces"),
        ("get_k8s_applications", "get_k8s_applications"),
        ("get_k8s_services", "get_k8s_services"),
        ("get_k8s_ingresses", "get_k8s_ingresses"),
        ("get_k8s_configmaps", "get_k8s_configmaps"),
        ("get_k8s_secrets", "get_k8s_secrets"),
        ("get_k8s_volumes", "get_k8s_volumes"),
        ("get_k8s_events", "get_k8s_events"),
        ("get_k8s_nodes_limits", "get_k8s_nodes_limits"),
        ("get_k8s_metrics_nodes", "get_k8s_metrics_nodes"),
    ],
)
def test_no_arg_actions_call_client_with_no_kwargs(k8s_fn, action, method_name):
    client = MagicMock()
    getattr(client, method_name).return_value = {"ok": action}
    result = _run(
        k8s_fn(action=action, endpoint_id=99, namespace="should-not-leak", client=client)
    )
    getattr(client, method_name).assert_called_once_with()
    assert result == {"ok": action}


def test_get_helm_releases_passes_endpoint_id_when_present(k8s_fn):
    client = MagicMock()
    client.get_helm_releases.return_value = {"releases": []}
    _run(k8s_fn(action="get_helm_releases", endpoint_id=5, client=client))
    client.get_helm_releases.assert_called_once_with(endpoint_id=5)


def test_get_helm_releases_omits_endpoint_id_when_explicitly_none(k8s_fn):
    client = MagicMock()
    client.get_helm_releases.return_value = {"releases": []}
    _run(k8s_fn(action="get_helm_releases", endpoint_id=None, client=client))
    client.get_helm_releases.assert_called_once_with()


def test_install_helm_chart_passes_both_when_present(k8s_fn):
    client = MagicMock()
    client.install_helm_chart.return_value = {"ok": True}
    _run(
        k8s_fn(
            action="install_helm_chart",
            endpoint_id=5,
            chart_name="nginx",
            client=client,
        )
    )
    client.install_helm_chart.assert_called_once_with(
        endpoint_id=5, chart_name="nginx"
    )


def test_delete_helm_release_passes_both_when_present(k8s_fn):
    client = MagicMock()
    client.delete_helm_release.return_value = {"ok": True}
    _run(
        k8s_fn(
            action="delete_helm_release",
            endpoint_id=5,
            release_name="web",
            client=client,
        )
    )
    client.delete_helm_release.assert_called_once_with(
        endpoint_id=5, release_name="web"
    )


@pytest.mark.parametrize(
    "action,method_name,extra_kwargs",
    [
        (
            "get_k8s_namespace",
            "get_kubernetes_namespace",
            {"environment_id": 3, "namespace": "prod"},
        ),
        (
            "create_k8s_namespace",
            "create_kubernetes_namespace",
            {"environment_id": 3, "namespace": "prod"},
        ),
        (
            "update_k8s_namespace",
            "update_kubernetes_namespace",
            {"environment_id": 3, "namespace": "prod"},
        ),
        (
            "delete_k8s_namespace",
            "delete_kubernetes_namespace",
            {"environment_id": 3, "namespace": "prod"},
        ),
        (
            "get_k8s_namespace_count",
            "get_kubernetes_namespace_count",
            {"environment_id": 3},
        ),
        (
            "drain_k8s_node",
            "drain_kubernetes_node",
            {"environment_id": 3, "node_name": "node-a"},
        ),
        (
            "describe_k8s_resource",
            "describe_kubernetes_resource",
            {"environment_id": 3},
        ),
        (
            "get_k8s_rbac_enabled",
            "get_kubernetes_rbac_enabled",
            {"environment_id": 3},
        ),
    ],
)
def test_namespace_and_node_actions_pass_through_directly(
    k8s_fn, action, method_name, extra_kwargs
):
    client = MagicMock()
    getattr(client, method_name).return_value = {"ok": action}
    result = _run(k8s_fn(action=action, client=client, **extra_kwargs))
    getattr(client, method_name).assert_called_once_with(**extra_kwargs)
    assert result == {"ok": action}


def test_get_k8s_namespace_passes_none_through_when_explicitly_none(k8s_fn):
    client = MagicMock()
    client.get_kubernetes_namespace.return_value = {}
    _run(
        k8s_fn(
            action="get_k8s_namespace", environment_id=3, namespace=None, client=client
        )
    )
    client.get_kubernetes_namespace.assert_called_once_with(
        environment_id=3, namespace=None
    )


def test_unknown_action_raises_genuine_reachable_error(k8s_fn):
    """Unlike the mcp_server.py copy (where resolve_action() intercepts
    unknown actions before the trailing raise), THIS copy has no
    resolve_action() call at all, so its own trailing
    "Unknown action: ... Must be one of: ..." raise really is reachable."""
    client = MagicMock()
    with pytest.raises(ValueError) as excinfo:
        _run(k8s_fn(action="totally_bogus_action_xyz", client=client))
    msg = str(excinfo.value)
    assert "Unknown action: totally_bogus_action_xyz" in msg
    # No discovery/fuzzy-match support in this drifted copy.
    assert "list_actions" not in msg


def test_list_actions_is_not_a_discovery_keyword_here(k8s_fn):
    """BUG (see BUGS FOUND -- drift from mcp_server.py's copy): this copy
    has no resolve_action() call, so action="list_actions" is NOT a
    discovery keyword -- it just falls through to the same generic
    "Unknown action" raise as any other unrecognized string."""
    client = MagicMock()
    with pytest.raises(ValueError, match="Unknown action: list_actions"):
        _run(k8s_fn(action="list_actions", client=client))


def test_unknown_action_error_message_has_malformed_quoting(k8s_fn):
    """BUG (see BUGS FOUND): the f-string building this message is missing
    the opening quote before the first action name and the closing quote
    after the last one."""
    client = MagicMock()
    with pytest.raises(ValueError) as excinfo:
        _run(k8s_fn(action="totally_bogus_action_xyz", client=client))
    msg = str(excinfo.value)
    assert "Must be one of: get_k8s_dashboard'," in msg  # no opening quote
    assert msg.rstrip().endswith("get_k8s_rbac_enabled")  # no closing quote
