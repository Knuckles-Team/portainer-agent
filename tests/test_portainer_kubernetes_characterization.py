"""Characterization tests for ``register_kubernetes_tools.portainer_kubernetes``
in ``portainer_agent/mcp_server.py`` (CCN 52) -- the LIVE copy reachable
through ``get_mcp_instance()``.

Pins two distinct dispatch shapes present in the pre-refactor code: a first
group of 14 actions that build a local ``kwargs`` dict and filter out ``None``
values before calling the client (``get_k8s_dashboard`` .. ``delete_helm_release``),
and a second group of 8 namespace/node-management actions that pass their
parameters straight through to the client WITHOUT None-filtering. This
asymmetry must survive the refactor unchanged. Also pins the
resolve_action-driven unknown-action/list_actions discovery path. Part of
the CXA-FL-PORTAINERAGENT-01 complexity-reduction program.
"""

import asyncio
import importlib
from unittest.mock import MagicMock

import pytest
from fastmcp import FastMCP


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
    m = importlib.import_module("portainer_agent.mcp_server")
    return _capture_tool(m.register_kubernetes_tools, "portainer_kubernetes")


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
    ]
)
def test_no_arg_actions_call_client_with_no_kwargs(k8s_fn, action, method_name):
    """These 11 actions build an always-empty kwargs dict -- proves neither
    endpoint_id nor any other param leaks through even when supplied."""
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


def test_get_helm_releases_omits_endpoint_id_when_none(k8s_fn):
    """None-filtering: an explicit endpoint_id=None kwarg isn't passed at
    all."""
    client = MagicMock()
    client.get_helm_releases.return_value = {"releases": []}
    _run(k8s_fn(action="get_helm_releases", endpoint_id=None, client=client))
    client.get_helm_releases.assert_called_once_with()


def test_get_helm_releases_omits_endpoint_id_when_omitted_entirely(k8s_fn):
    """BUG-CX-036 FIX (CX complexity-collapse, wD3-FL-06): omitting
    endpoint_id entirely (rather than passing it explicitly as None) used to
    leak the raw pydantic FieldInfo default through to the client, because
    -- unlike portainer_stack -- this function had no FieldInfo-cleanup
    block. portainer_kubernetes now normalizes every named parameter with
    `_none_if_field_info()` before dispatch, same as portainer_stack, so
    omitting endpoint_id now behaves identically to passing it explicitly as
    None: it is filtered out of the call, not leaked as a FieldInfo object.

    This test FAILED before the fix (it asserted
    ``isinstance(kwargs["endpoint_id"], FieldInfo)``) and PASSES after."""
    client = MagicMock()
    client.get_helm_releases.return_value = {"releases": []}
    _run(k8s_fn(action="get_helm_releases", client=client))
    client.get_helm_releases.assert_called_once_with()


def test_install_helm_chart_filters_none_chart_name(k8s_fn):
    client = MagicMock()
    client.install_helm_chart.return_value = {"ok": True}
    _run(
        k8s_fn(
            action="install_helm_chart",
            endpoint_id=5,
            chart_name=None,
            client=client,
        )
    )
    client.install_helm_chart.assert_called_once_with(endpoint_id=5)


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


def test_get_k8s_namespace_passes_none_through_when_omitted(k8s_fn):
    """Unlike the first group, this second group does NOT filter out None --
    calling with an explicit namespace=None still passes namespace=None
    straight through."""
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


def test_get_k8s_namespace_passes_none_through_when_namespace_omitted_entirely(k8s_fn):
    """BUG-CX-036 FIX companion (CX complexity-collapse, wD3-FL-06): this
    group (Group 3) still does NOT filter None out -- that asymmetry vs.
    Group 2 is preserved on purpose. What changed is what "no value
    provided" resolves to: omitting namespace entirely now normalizes to
    None (via `_none_if_field_info()`) and is passed through as
    namespace=None, identical to passing it explicitly -- instead of
    leaking the raw pydantic FieldInfo default object."""
    client = MagicMock()
    client.get_kubernetes_namespace.return_value = {}
    _run(k8s_fn(action="get_k8s_namespace", environment_id=3, client=client))
    client.get_kubernetes_namespace.assert_called_once_with(
        environment_id=3, namespace=None
    )


def test_unknown_action_raises_with_discovery_hint(k8s_fn):
    """resolve_action's unknown_action_error fires -- NOT the function's own
    trailing 'Unknown action: {action}. Must be one of: ...' raise, which is
    unreachable dead code (see BUGS FOUND)."""
    client = MagicMock()
    with pytest.raises(ValueError) as excinfo:
        _run(k8s_fn(action="totally_bogus_action_xyz", client=client))
    msg = str(excinfo.value)
    assert "list_actions" in msg
    assert "Must be one of" not in msg


def test_list_actions_discovery(k8s_fn):
    client = MagicMock()
    result = _run(k8s_fn(action="list_actions", client=client))
    assert isinstance(result, dict)
    assert "get_k8s_dashboard" in result["actions"]
    assert result["service"] == "portainer-agent"
