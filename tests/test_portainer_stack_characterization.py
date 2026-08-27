"""Characterization tests for ``register_stack_tools.portainer_stack``.

Pins the pre-refactor behavior of the CCN-95 ``portainer_stack`` dispatcher in
``portainer_agent/mcp_server.py`` (params_json parsing, the ``get_val``
resolver's params_json-first precedence, backward-compatible action-name
routing, FieldInfo cleanup, and the per-action client calls) so a subsequent
decomposition can be verified behavior-preserving. Part of the
CXA-FL-PORTAINERAGENT-01 complexity-reduction program.
"""

import asyncio
import importlib
from unittest.mock import MagicMock

import pytest
from fastmcp import FastMCP
from pydantic.fields import FieldInfo


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
def stack_fn():
    m = importlib.import_module("portainer_agent.mcp_server")
    return _capture_tool(m.register_stack_tools, "portainer_stack")


def test_get_stacks_wraps_list_result(stack_fn):
    client = MagicMock()
    client.get_stacks.return_value = [{"Id": 1}]
    result = _run(stack_fn(action="get_stacks", client=client))
    assert result == {"data": [{"Id": 1}]}


def test_get_stacks_passes_through_dict_result(stack_fn):
    client = MagicMock()
    client.get_stacks.return_value = {"already": "a dict"}
    result = _run(stack_fn(action="get_stacks", client=client))
    assert result == {"already": "a dict"}


def test_get_stack_requires_stack_id(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="Missing parameter: stack_id"):
        _run(stack_fn(action="get_stack", client=client))


def test_get_stack_field_info_default_treated_as_missing(stack_fn):
    """Directly-called tool (as tests do) receives the raw pydantic FieldInfo
    default rather than None; the FieldInfo-cleanup block must normalize it."""
    client = MagicMock()
    field_info_default = FieldInfo(default=None, description="stack id")
    with pytest.raises(ValueError, match="Missing parameter: stack_id"):
        _run(stack_fn(action="get_stack", stack_id=field_info_default, client=client))


def test_get_stack_calls_client_with_int_id(stack_fn):
    client = MagicMock()
    client.get_stack.return_value = {"Id": 42}
    result = _run(stack_fn(action="get_stack", stack_id=42, client=client))
    client.get_stack.assert_called_once_with(stack_id=42)
    assert result == {"Id": 42}


def test_get_stack_by_name_requires_name(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="Missing parameter: name"):
        _run(stack_fn(action="get_stack_by_name", client=client))


def test_get_stack_file_requires_stack_id(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="Missing parameter: stack_id"):
        _run(stack_fn(action="get_stack_file", client=client))


def test_create_standalone_stack_routes_to_repository_when_repo_url_present(stack_fn):
    """Backward-compat routing: create_standalone_stack -> _from_repository."""
    client = MagicMock()
    client.create_standalone_stack_from_repository.return_value = {"Id": 5}
    result = _run(
        stack_fn(
            action="create_standalone_stack",
            name="n1",
            repo_url="http://git.example/x.git",
            endpoint_id=1,
            client=client,
        )
    )
    client.create_standalone_stack_from_repository.assert_called_once_with(
        name="n1", repo_url="http://git.example/x.git", endpoint_id=1
    )
    client.create_standalone_stack_from_string.assert_not_called()
    assert result == {"Id": 5}


def test_create_standalone_stack_routes_to_string_when_no_repo_url(stack_fn):
    """Backward-compat routing: create_standalone_stack -> _from_string."""
    client = MagicMock()
    client.create_standalone_stack_from_string.return_value = {"Id": 6}
    result = _run(
        stack_fn(
            action="create_standalone_stack",
            name="n1",
            stack_file_content="version: '3'",
            endpoint_id=1,
            client=client,
        )
    )
    client.create_standalone_stack_from_string.assert_called_once()
    client.create_standalone_stack_from_repository.assert_not_called()
    assert result == {"Id": 6}


def test_create_standalone_stack_from_repo_alias(stack_fn):
    client = MagicMock()
    client.create_standalone_stack_from_repository.return_value = {"Id": 7}
    _run(
        stack_fn(
            action="create_standalone_stack_from_repo",
            name="n1",
            repo_url="http://git.example/x.git",
            endpoint_id=1,
            client=client,
        )
    )
    client.create_standalone_stack_from_repository.assert_called_once()


def test_create_standalone_stack_from_string_missing_params(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="create_standalone_stack_from_string"):
        _run(stack_fn(action="create_standalone_stack_from_string", client=client))


@pytest.mark.parametrize(
    "action,method_name,extra_kwargs",
    [
        (
            "create_swarm_stack_from_string",
            "create_swarm_stack_from_string",
            {"stack_file_content": "version: '3'", "swarm_id": "sw1"},
        ),
        (
            "create_swarm_stack_from_repository",
            "create_swarm_stack_from_repository",
            {"repo_url": "http://git.example/x.git", "swarm_id": "sw1"},
        ),
        (
            "create_kubernetes_stack_from_string",
            "create_kubernetes_stack_from_string",
            {"stack_file_content": "version: '3'"},
        ),
        (
            "create_kubernetes_stack_from_repository",
            "create_kubernetes_stack_from_repository",
            {"repo_url": "http://git.example/x.git"},
        ),
    ],
)
def test_create_stack_variants_call_expected_client_method(
    stack_fn, action, method_name, extra_kwargs
):
    client = MagicMock()
    getattr(client, method_name).return_value = {"created": action}
    result = _run(
        stack_fn(action=action, name="n1", endpoint_id=1, client=client, **extra_kwargs)
    )
    getattr(client, method_name).assert_called_once()
    assert result == {"created": action}


@pytest.mark.parametrize(
    "action",
    [
        "create_swarm_stack_from_string",
        "create_swarm_stack_from_repository",
        "create_kubernetes_stack_from_string",
        "create_kubernetes_stack_from_repository",
    ],
)
def test_create_stack_variants_missing_required_params_raise(stack_fn, action):
    client = MagicMock()
    with pytest.raises(ValueError, match=action):
        _run(stack_fn(action=action, client=client))


@pytest.mark.parametrize(
    "action,method_name",
    [
        ("delete_stack", "delete_stack"),
        ("start_stack", "start_stack"),
        ("stop_stack", "stop_stack"),
        ("associate_stack", "associate_stack"),
    ],
)
def test_simple_stack_id_endpoint_id_actions(stack_fn, action, method_name):
    client = MagicMock()
    getattr(client, method_name).return_value = {"ok": True}
    result = _run(stack_fn(action=action, stack_id=1, endpoint_id=2, client=client))
    getattr(client, method_name).assert_called_once_with(stack_id=1, endpoint_id=2)
    assert result == {"ok": True}


@pytest.mark.parametrize(
    "action", ["delete_stack", "start_stack", "stop_stack", "associate_stack"]
)
def test_simple_stack_id_endpoint_id_actions_missing_params_raise(stack_fn, action):
    client = MagicMock()
    with pytest.raises(ValueError, match=action):
        _run(stack_fn(action=action, client=client))


def test_update_stack_requires_stack_id_and_endpoint_id(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="update_stack"):
        _run(stack_fn(action="update_stack", client=client))


def test_update_stack_reinjects_env_and_prune(stack_fn):
    client = MagicMock()
    client.update_stack.return_value = {"ok": True}
    _run(
        stack_fn(
            action="update_stack",
            stack_id=1,
            endpoint_id=2,
            env=[{"name": "X", "value": "Y"}],
            prune=True,
            client=client,
        )
    )
    _, kwargs = client.update_stack.call_args
    assert kwargs["stack_id"] == 1
    assert kwargs["endpoint_id"] == 2
    assert kwargs["Env"] == [{"name": "X", "value": "Y"}]
    assert kwargs["Prune"] is True


def test_migrate_stack_requires_target_endpoint_id(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="migrate_stack"):
        _run(stack_fn(action="migrate_stack", stack_id=1, endpoint_id=2, client=client))


def test_migrate_stack_calls_client(stack_fn):
    client = MagicMock()
    client.migrate_stack.return_value = {"ok": True}
    result = _run(
        stack_fn(
            action="migrate_stack",
            stack_id=1,
            endpoint_id=2,
            params_json='{"target_endpoint_id": 3}',
            client=client,
        )
    )
    client.migrate_stack.assert_called_once_with(
        stack_id=1, endpoint_id=2, target_endpoint_id=3
    )
    assert result == {"ok": True}


@pytest.mark.parametrize(
    "action,method_name",
    [
        ("update_stack_git", "update_stack_git"),
        ("redeploy_stack_git", "redeploy_stack_git"),
    ],
)
def test_git_stack_actions_reinject_env_and_prune(stack_fn, action, method_name):
    client = MagicMock()
    getattr(client, method_name).return_value = {"ok": True}
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
    _, kwargs = getattr(client, method_name).call_args
    assert kwargs["Env"] == [{"name": "A", "value": "B"}]
    assert kwargs["Prune"] is False


@pytest.mark.parametrize("action", ["update_stack_git", "redeploy_stack_git"])
def test_git_stack_actions_missing_params_raise(stack_fn, action):
    client = MagicMock()
    with pytest.raises(ValueError, match=action):
        _run(stack_fn(action=action, client=client))


def test_export_all_stacks_requires_target_dir(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="target_dir"):
        _run(stack_fn(action="export_all_stacks", client=client))


def test_export_all_stacks_named_param_is_silently_ignored(stack_fn):
    """BUG (see BUGS FOUND): ``target_dir`` is a real ``Field(...)`` parameter
    on the tool signature but is never added to ``field_map``, so ``get_val``
    can only ever see it via ``params_json`` -- passing it as a normal named
    kwarg is silently dropped and this still raises "missing" even though the
    caller supplied it."""
    client = MagicMock()
    with pytest.raises(ValueError, match="target_dir"):
        _run(stack_fn(action="export_all_stacks", target_dir="/tmp/x", client=client))
    client.export_all_stacks.assert_not_called()


def test_export_all_stacks_calls_client_via_params_json(stack_fn):
    """Because of the field_map gap above, params_json is the ONLY way to
    actually reach ``client.export_all_stacks`` today."""
    client = MagicMock()
    client.export_all_stacks.return_value = {"ok": True}
    result = _run(
        stack_fn(
            action="export_all_stacks",
            params_json='{"target_dir": "/tmp/x"}',
            client=client,
        )
    )
    client.export_all_stacks.assert_called_once_with(target_dir="/tmp/x")
    assert result == {"ok": True}


def test_invalid_params_json_raises(stack_fn):
    client = MagicMock()
    with pytest.raises(ValueError, match="Invalid params_json"):
        _run(
            stack_fn(
                action="get_stacks", params_json="{not valid json", client=client
            )
        )


def test_params_json_takes_precedence_over_named_field(stack_fn):
    """get_val checks params_json (case-insensitive variants) BEFORE named
    kwargs -- so a params_json value overrides an explicitly-passed field."""
    client = MagicMock()
    client.get_stack.return_value = {"Id": 99}
    _run(
        stack_fn(
            action="get_stack",
            stack_id=1,
            params_json='{"stack_id": 99}',
            client=client,
        )
    )
    client.get_stack.assert_called_once_with(stack_id=99)


def test_unknown_action_raises_with_discovery_hint(stack_fn):
    """resolve_action's unknown_action_error fires -- NOT the function's own
    trailing 'Unknown action: {action}. Must be one of: ...' raise, which is
    unreachable dead code (see BUGS FOUND)."""
    client = MagicMock()
    with pytest.raises(ValueError) as excinfo:
        _run(stack_fn(action="totally_bogus_action_xyz", client=client))
    msg = str(excinfo.value)
    assert "list_actions" in msg
    assert "Must be one of" not in msg


def test_list_actions_discovery(stack_fn):
    client = MagicMock()
    result = _run(stack_fn(action="list_actions", client=client))
    assert isinstance(result, dict)
    assert "get_stacks" in result["actions"]
    assert result["service"] == "portainer-agent"
