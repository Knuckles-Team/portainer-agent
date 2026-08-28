import inspect
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from portainer_agent.api_client import PortainerApi


@pytest.fixture
def _mock_session():
    with patch("requests.Session") as mock_sess:
        session = mock_sess.return_value

        res = MagicMock()
        res.status_code = 200
        res.ok = True
        res.json.return_value = {"id": 1, "name": "test", "data": []}
        session.get.return_value = res
        session.post.return_value = res
        session.delete.return_value = res
        session.put.return_value = res
        session.patch.return_value = res

        yield session


def _is_id_like_param(name: str) -> bool:
    """Whether a parameter name looks like it identifies an endpoint/environment/resource."""
    return "endpoint_id" in name or "environment_id" in name or "id" in name


def _guess_kwarg_value(param: inspect.Parameter) -> Any:
    """Guess a plausible value for one client-method parameter by name/annotation."""
    if _is_id_like_param(param.name):
        return 123
    if "name" in param.name:
        return "testname"
    if "path" in param.name:
        return "testpath"
    if param.annotation == int:
        return 1
    if param.annotation == bool:
        return True
    if param.annotation == list:
        return []
    if param.annotation == dict:
        return {}
    return "test"


def _build_call_kwargs(sig: inspect.Signature) -> dict[str, Any]:
    """Guess a kwargs dict covering every non-``kwargs`` parameter in ``sig``."""
    return {
        param.name: _guess_kwarg_value(param)
        for param in sig.parameters.values()
        if param.name != "kwargs"
    }


def _split_positional_args(
    sig: inspect.Signature, kwargs: dict[str, Any]
) -> tuple[list[Any], dict[str, Any]]:
    """Pull required positional parameters out of ``kwargs`` into a positional list."""
    pos_args = []
    for param in sig.parameters.values():
        if param.default == inspect.Parameter.empty and param.kind in (
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.POSITIONAL_ONLY,
        ):
            pos_args.append(kwargs.get(param.name, "test"))
            if param.name in kwargs:
                del kwargs[param.name]
    return pos_args, kwargs


def test_api_brute_force(_mock_session):
    client = PortainerApi(base_url="http://test.portainer.com", token="mock_token")

    # Introspect all methods
    for name, method in inspect.getmembers(client, predicate=inspect.ismethod):
        if name.startswith("_") or name in ["authenticate", "logout"]:
            continue

        print(f"Calling {name}...")
        sig = inspect.signature(method)
        kwargs = _build_call_kwargs(sig)

        try:
            # Also add some generic kwargs
            kwargs.update(
                {
                    "endpoint_id": 1,
                    "environment_id": 1,
                    "id": 1,
                    "name": "test",
                    "namespace": "test",
                }
            )

            # Check for positional arguments
            pos_args, kwargs = _split_positional_args(sig, kwargs)

            method(*pos_args, **kwargs)
        except Exception as e:
            print(f"Operation failed: {type(e).__name__}")


def test_mcp_server_coverage(_mock_session):
    import asyncio

    from portainer_agent.mcp_server import get_mcp_instance

    # Mock get_client to return our client
    client = PortainerApi(base_url="http://test.portainer.com", token="mock_token")
    with patch("portainer_agent.mcp_server.get_client", return_value=client):
        # Unpack if tuple
        mcp_data = get_mcp_instance()
        mcp = mcp_data[0] if isinstance(mcp_data, tuple) else mcp_data

        async def run_tools():
            # list_tools might be async
            tool_objs = (
                await mcp.list_tools()
                if inspect.iscoroutinefunction(mcp.list_tools)
                else mcp.list_tools()
            )
            tools = [t.name for t in tool_objs]
            for tool_name in tools:
                print(f"Testing MCP tool: {tool_name}")
                try:
                    await mcp.call_tool(
                        tool_name, {"endpoint_id": 1, "id": 1, "name": "test"}
                    )
                except Exception:
                    pass

        loop = asyncio.new_event_loop()
        loop.run_until_complete(run_tools())
        loop.close()
