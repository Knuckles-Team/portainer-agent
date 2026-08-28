"""Characterization tests for the ``portainer_agent.mcp.mcp_*`` action-dispatch
tools (auth, edge, environment, registry, stack, system, template, user).

These modules are an ORPHANED, independently-drifted copy of the tools the
live server actually serves (see ``tests/test_mcp_kubernetes_orphan_characterization.py``
for the full explanation: the running server's ``get_mcp_instance()`` in
``mcp_server.py`` discovers tools by inspecting its OWN module namespace via
``register_tool_surface(..., tools_module=sys.modules[__name__])``, never
importing the ``portainer_agent.mcp`` subpackage). Before the
CXA-WD11-FL-03 complexity-collapse pass, none of these eight modules had any
test coverage at all -- each ``register_*_tools.portainer_*`` function was a
long if/elif chain at 10-35 cyclomatic / 18-68 cognitive complexity. They are
now table dispatch through ``portainer_agent.mcp.action_kwargs``; this file
pins that every action still resolves to the same client call and the same
"unknown action" error text (including two files' pre-existing quoting bugs,
see repo BUGS FOUND) as the pre-refactor if/elif bodies.
"""

import asyncio

import pytest
from fastmcp import FastMCP
from unittest.mock import MagicMock

import portainer_agent.mcp.mcp_auth as mcp_auth_module
import portainer_agent.mcp.mcp_edge as mcp_edge_module
import portainer_agent.mcp.mcp_environment as mcp_environment_module
import portainer_agent.mcp.mcp_registry as mcp_registry_module
import portainer_agent.mcp.mcp_stack as mcp_stack_module
import portainer_agent.mcp.mcp_system as mcp_system_module
import portainer_agent.mcp.mcp_template as mcp_template_module
import portainer_agent.mcp.mcp_user as mcp_user_module


def _capture_tool(register_fn, tool_name):
    """Register a tool against a throwaway FastMCP and return the raw coroutine fn."""
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
def auth_fn():
    return _capture_tool(mcp_auth_module.register_auth_tools, "portainer_auth")


@pytest.fixture
def edge_fn():
    return _capture_tool(mcp_edge_module.register_edge_tools, "portainer_edge")


@pytest.fixture
def environment_fn():
    return _capture_tool(
        mcp_environment_module.register_environment_tools, "portainer_environment"
    )


@pytest.fixture
def registry_fn():
    return _capture_tool(mcp_registry_module.register_registry_tools, "portainer_registry")


@pytest.fixture
def stack_fn():
    return _capture_tool(mcp_stack_module.register_stack_tools, "portainer_stack")


@pytest.fixture
def system_fn():
    return _capture_tool(mcp_system_module.register_system_tools, "portainer_system")


@pytest.fixture
def template_fn():
    return _capture_tool(mcp_template_module.register_template_tools, "portainer_template")


@pytest.fixture
def user_fn():
    return _capture_tool(mcp_user_module.register_user_tools, "portainer_user")


# --- auth ---------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        (
            "authenticate",
            {"username": "u", "password": "p"},
            {"username": "u", "password": "p"},
        ),
        ("logout", {}, {}),
        ("validate_oauth", {"code": "abc"}, {"code": "abc"}),
    ],
)
def test_auth_actions_call_client(auth_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(auth_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_auth_unknown_action_raises_original_text(auth_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="authenticate', 'logout', 'validate_oauth"):
        _run(auth_fn(action="bogus", client=client))


# --- edge -----------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_edge_groups", {}, {}),
        ("create_edge_group", {"name": "g1"}, {"name": "g1"}),
        ("delete_edge_group", {"group_id": 1}, {"group_id": 1}),
        ("get_edge_stacks", {}, {}),
        ("get_edge_stack", {"stack_id": 2}, {"stack_id": 2}),
        ("create_edge_stack", {}, {}),
        ("delete_edge_stack", {"stack_id": 2}, {"stack_id": 2}),
        ("get_edge_jobs", {}, {}),
        ("get_edge_job", {"job_id": 3}, {"job_id": 3}),
        ("create_edge_job", {}, {}),
        ("delete_edge_job", {"job_id": 3}, {"job_id": 3}),
    ],
)
def test_edge_actions_call_client(edge_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(edge_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_edge_unknown_action_raises_original_text(edge_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_edge_groups', 'create_edge_group"):
        _run(edge_fn(action="bogus", client=client))


# --- environment ------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_endpoints", {"limit": 5, "offset": 0}, {"limit": 5, "offset": 0}),
        ("get_endpoint", {"endpoint_id": 1}, {"endpoint_id": 1}),
        (
            "create_endpoint",
            {"name": "e1", "endpoint_type": 1, "url": "http://x"},
            {"name": "e1", "endpoint_type": 1, "url": "http://x"},
        ),
        ("update_endpoint", {"endpoint_id": 1}, {"endpoint_id": 1}),
        ("delete_endpoint", {"endpoint_id": 1}, {"endpoint_id": 1}),
        ("snapshot_endpoint", {"endpoint_id": 1}, {"endpoint_id": 1}),
        ("snapshot_all_endpoints", {}, {}),
        ("get_endpoint_groups", {}, {}),
        (
            "create_endpoint_group",
            {"name": "g1", "description": "d"},
            {"name": "g1", "description": "d"},
        ),
        ("delete_endpoint_group", {"group_id": 9}, {"group_id": 9}),
    ],
)
def test_environment_actions_call_client(environment_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(environment_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_environment_get_endpoint_settings_passes_endpoint_id_even_when_none(
    environment_fn,
):
    """Unlike every other action, get_endpoint_settings does NOT filter out a
    None endpoint_id -- it always forwards it explicitly."""
    client = MagicMock()
    client.get_endpoint_settings.return_value = {"ok": True}
    _run(environment_fn(action="get_endpoint_settings", endpoint_id=None, client=client))
    client.get_endpoint_settings.assert_called_once_with(endpoint_id=None)


def test_environment_update_endpoint_settings_merges_payload(environment_fn):
    client = MagicMock()
    client.update_endpoint_settings.return_value = {"ok": True}
    _run(
        environment_fn(
            action="update_endpoint_settings",
            endpoint_id=7,
            settings={"IngressClass": "nginx"},
            client=client,
        )
    )
    client.update_endpoint_settings.assert_called_once_with(
        endpoint_id=7, IngressClass="nginx"
    )


def test_environment_update_endpoint_settings_ignores_non_dict_settings(environment_fn):
    client = MagicMock()
    client.update_endpoint_settings.return_value = {"ok": True}
    _run(
        environment_fn(
            action="update_endpoint_settings",
            endpoint_id=7,
            settings="not-a-dict",
            client=client,
        )
    )
    client.update_endpoint_settings.assert_called_once_with(endpoint_id=7)


def test_environment_unknown_action_raises_original_text(environment_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_endpoints', 'get_endpoint"):
        _run(environment_fn(action="bogus", client=client))


# --- registry ---------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_registries", {}, {}),
        ("get_registry", {"registry_id": 1}, {"registry_id": 1}),
        (
            "create_registry",
            {"name": "r1", "registry_type": 1, "url": "http://reg"},
            {"name": "r1", "registry_type": 1, "url": "http://reg"},
        ),
        ("delete_registry", {"registry_id": 1}, {"registry_id": 1}),
    ],
)
def test_registry_actions_call_client(registry_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(registry_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_registry_unknown_action_raises_original_text(registry_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_registries', 'get_registry"):
        _run(registry_fn(action="bogus", client=client))


# --- stack --------------------------------------------------------------


def test_stack_get_stacks_wraps_list_result(stack_fn):
    client = MagicMock()
    client.get_stacks.return_value = [{"Id": 1}]
    result = _run(stack_fn(action="get_stacks", client=client))
    assert result == {"data": [{"Id": 1}]}


def test_stack_get_stacks_passes_through_dict_result(stack_fn):
    client = MagicMock()
    client.get_stacks.return_value = {"already": "a dict"}
    result = _run(stack_fn(action="get_stacks", client=client))
    assert result == {"already": "a dict"}


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_stack", {"stack_id": 1}, {"stack_id": 1}),
        ("get_stack_file", {"stack_id": 1}, {"stack_id": 1}),
        ("create_standalone_stack", {}, {}),
        ("create_standalone_stack_from_repo", {}, {}),
        (
            "delete_stack",
            {"stack_id": 1, "endpoint_id": 2},
            {"stack_id": 1, "endpoint_id": 2},
        ),
        (
            "start_stack",
            {"stack_id": 1, "endpoint_id": 2},
            {"stack_id": 1, "endpoint_id": 2},
        ),
        (
            "stop_stack",
            {"stack_id": 1, "endpoint_id": 2},
            {"stack_id": 1, "endpoint_id": 2},
        ),
    ],
)
def test_stack_simple_actions_call_client(stack_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(stack_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_stack_update_stack_renames_content_env_prune(stack_fn):
    client = MagicMock()
    client.update_stack.return_value = {"ok": True}
    _run(
        stack_fn(
            action="update_stack",
            stack_id=1,
            endpoint_id=2,
            stack_file_content="version: '3'",
            env=[{"name": "X", "value": "Y"}],
            prune=True,
            client=client,
        )
    )
    client.update_stack.assert_called_once_with(
        stack_id=1,
        endpoint_id=2,
        StackFileContent="version: '3'",
        Env=[{"name": "X", "value": "Y"}],
        Prune=True,
    )


@pytest.mark.parametrize("action", ["update_stack_git", "redeploy_stack_git"])
def test_stack_git_actions_keep_lowercase_env_and_prune(stack_fn, action):
    """Unlike plain update_stack, the git variants do NOT rename env/prune to
    Env/Prune -- they forward the lowercase names verbatim."""
    client = MagicMock()
    getattr(client, action).return_value = {"ok": True}
    _run(
        stack_fn(
            action=action,
            stack_id=1,
            endpoint_id=2,
            env=[{"name": "A", "value": "B"}],
            prune=False,
            client=client,
        )
    )
    _, kwargs = getattr(client, action).call_args
    assert kwargs["env"] == [{"name": "A", "value": "B"}]
    assert kwargs["prune"] is False
    assert kwargs["stack_id"] == 1
    assert kwargs["endpoint_id"] == 2


def test_stack_unknown_action_raises_original_text(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_stacks', 'get_stack'"):
        _run(stack_fn(action="bogus", client=client))


# --- system -------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_status", {}, {}),
        ("get_system_info", {}, {}),
        ("get_system_version", {}, {}),
        ("get_settings", {}, {}),
        ("update_settings", {}, {}),
        ("get_tags", {}, {}),
        ("create_tag", {"name": "t1"}, {"name": "t1"}),
        ("delete_tag", {"tag_id": 1}, {"tag_id": 1}),
        ("get_motd", {}, {}),
        ("backup_portainer", {}, {}),
    ],
)
def test_system_actions_call_client(system_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(system_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_system_unknown_action_raises_original_text(system_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_status', 'get_system_info"):
        _run(system_fn(action="bogus", client=client))


# --- template -------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_templates", {}, {}),
        ("get_custom_templates", {}, {}),
        ("get_custom_template", {"template_id": 1}, {"template_id": 1}),
        ("create_custom_template", {}, {}),
        ("delete_custom_template", {"template_id": 1}, {"template_id": 1}),
        ("get_custom_template_file", {"template_id": 1}, {"template_id": 1}),
        ("get_helm_templates", {}, {}),
    ],
)
def test_template_actions_call_client(template_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(template_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_template_unknown_action_raises_original_text(template_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_templates', 'get_custom_templates"):
        _run(template_fn(action="bogus", client=client))


# --- user -----------------------------------------------------------------


@pytest.mark.parametrize(
    "action,call_kwargs,expected",
    [
        ("get_users", {}, {}),
        ("get_user", {"user_id": 1}, {"user_id": 1}),
        ("get_current_user", {}, {}),
        (
            "create_user",
            {"username": "u", "password": "p", "role": 1},
            {"username": "u", "password": "p", "role": 1},
        ),
        ("delete_user", {"user_id": 1}, {"user_id": 1}),
        ("get_teams", {}, {}),
        ("create_team", {"name": "t1"}, {"name": "t1"}),
        ("delete_team", {"team_id": 1}, {"team_id": 1}),
        ("get_roles", {}, {}),
        ("get_user_tokens", {"user_id": 1}, {"user_id": 1}),
    ],
)
def test_user_actions_call_client(user_fn, action, call_kwargs, expected):
    client = MagicMock()
    getattr(client, action).return_value = {"ok": action}
    result = _run(user_fn(action=action, client=client, **call_kwargs))
    getattr(client, action).assert_called_once_with(**expected)
    assert result == {"ok": action}


def test_user_unknown_action_raises_original_text(user_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="get_users', 'get_user'"):
        _run(user_fn(action="bogus", client=client))
