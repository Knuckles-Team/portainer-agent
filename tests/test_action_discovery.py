"""Action-discovery standardization tests.

Verifies that the action-routed MCP tools expose ``list_actions`` discovery and
a rich did-you-mean error on unknown actions via the shared agent-utilities
helper.
"""

import asyncio
import importlib
from unittest.mock import MagicMock

from fastmcp import FastMCP


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


def test_list_actions_returns_names():
    m = importlib.import_module("portainer_agent.mcp_server")
    fn = _capture_tool(m.register_registry_tools, "portainer_registry")
    result = _run(fn(action="list_actions", client=MagicMock()))
    assert isinstance(result, dict)
    assert "get_registries" in result["actions"]
    assert result["service"] == "portainer-agent"


def test_bogus_action_raises_with_list_actions_hint():
    m = importlib.import_module("portainer_agent.mcp_server")
    fn = _capture_tool(m.register_registry_tools, "portainer_registry")
    try:
        _run(fn(action="totally_bogus_action", client=MagicMock()))
    except ValueError as exc:
        assert "list_actions" in str(exc)
    else:
        raise AssertionError("expected ValueError for unknown action")


def test_stack_tool_discovery():
    m = importlib.import_module("portainer_agent.mcp_server")
    fn = _capture_tool(m.register_stack_tools, "portainer_stack")
    result = _run(fn(action="list_actions", client=MagicMock()))
    assert isinstance(result, dict)
    assert "get_stacks" in result["actions"]
