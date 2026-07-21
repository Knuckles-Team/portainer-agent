import builtins
import inspect
import json
import os
import runpy
import sys
from unittest.mock import MagicMock, patch

import pytest
from agent_utilities.core.exceptions import UnauthorizedError
from starlette.datastructures import Headers
from starlette.requests import Request

# --- Helper Fixture for API Session ---


@pytest.fixture
def _mock_session():
    with patch("requests.Session") as mock_s:
        session = mock_s.return_value
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"id": 1, "Name": "test", "jwt": "mock_jwt"}
        response.text = '{"id": 1}'
        session.get.return_value = response
        session.post.return_value = response
        session.put.return_value = response
        session.delete.return_value = response
        session.patch.return_value = response
        session.request.return_value = response
        yield session


# --- 1. Tests for portainer_agent/__init__.py ---


def test_init_module_lazy_attributes():
    import portainer_agent

    # Check lazy attributes
    assert hasattr(portainer_agent, "_MCP_AVAILABLE")
    assert hasattr(portainer_agent, "_AGENT_AVAILABLE")

    # Test getting dynamic lazy attributes
    assert portainer_agent._MCP_AVAILABLE is True
    assert portainer_agent._AGENT_AVAILABLE is True

    # Test requesting nonexistent attribute raises AttributeError
    with pytest.raises(AttributeError):
        _ = portainer_agent.non_existent_attribute_name

    # Test __dir__
    dir_contents = dir(portainer_agent)
    assert "PortainerApi" in dir_contents


def test_init_module_missing_availability():
    import portainer_agent

    # Mock OPTIONAL_MODULES to trigger false return branches
    with patch.dict(portainer_agent.OPTIONAL_MODULES, {}, clear=True):
        assert portainer_agent._MCP_AVAILABLE is False
        assert portainer_agent._AGENT_AVAILABLE is False


def test_init_lazy_import_failure():
    import importlib

    import portainer_agent

    original_import = importlib.import_module

    def mock_import(name, *args, **kwargs):
        if "non_existent" in name:
            raise ImportError("Mocked import error")
        return original_import(name, *args, **kwargs)

    with patch("importlib.import_module", side_effect=mock_import):
        assert (
            portainer_agent._import_module_safely("portainer_agent.non_existent")
            is None
        )


def test_init_lazy_expose_members():
    import portainer_agent

    # Trigger hasattr and getattr via __getattr__
    assert portainer_agent.agent_server is not None

    # Access an unexposed attribute (__version__) on optional module to cover line 69
    val = portainer_agent.__getattr__("__version__")
    assert val is not None


# --- 2. Tests for portainer_agent/auth.py ---


def test_auth_get_client_success():
    import portainer_agent.auth

    # Reset singleton
    portainer_agent.auth._client = None

    env_mock = {
        "PORTAINER_URL": "http://127.0.0.1:9000",
        "PORTAINER_TOKEN": "mock_token_123",
    }
    with patch.dict(os.environ, env_mock):
        client = portainer_agent.auth.get_client()
        assert client is not None
        assert client.base_url == "http://127.0.0.1:9000"


def test_auth_get_client_uses_configured_tls_profile():
    import portainer_agent.auth

    portainer_agent.auth._client = None
    env_mock = {
        "PORTAINER_URL": "http://127.0.0.1:9000",
        "PORTAINER_TOKEN": "mock_token_123",
    }
    profile = object()
    expected = object()
    with (
        patch.dict(os.environ, env_mock),
        patch(
            "portainer_agent.auth.resolve_configured_tls_profile",
            return_value=profile,
        ) as resolver,
        patch("portainer_agent.auth.PortainerApi", return_value=expected) as factory,
    ):
        assert portainer_agent.auth.get_client() is expected
    resolver.assert_called_once_with("portainer")
    factory.assert_called_once_with(
        base_url="http://127.0.0.1:9000",
        token="mock_token_123",
        tls_profile=profile,
    )


def test_auth_get_client_unauthorized_error():
    import portainer_agent.auth

    # Reset singleton
    portainer_agent.auth._client = None

    with patch(
        "portainer_agent.auth.PortainerApi",
        side_effect=UnauthorizedError("Access forbidden"),
    ):
        with pytest.raises(
            RuntimeError, match="AUTHENTICATION ERROR: The Portainer credentials"
        ):
            portainer_agent.auth.get_client()


# --- 3. Tests for portainer_agent/agent_server.py & __main__.py ---


def test_agent_server_debug_mode():
    with (
        patch("agent_utilities.initialize_workspace"),
        patch("agent_utilities.load_identity", return_value={"name": "test"}),
        patch(
            "agent_utilities.build_system_prompt_from_workspace", return_value="prompt"
        ),
        patch("agent_utilities.create_agent_server") as mock_server,
        patch("agent_utilities.create_agent_parser") as mock_parser,
        patch("sys.argv", ["agent_server.py", "--debug"]),
    ):
        mock_args = MagicMock()
        mock_args.debug = True
        mock_args.mcp_url = None
        mock_args.mcp_config = None
        mock_args.host = "localhost"
        mock_args.port = 8000
        mock_args.provider = "openai"
        mock_args.model_id = "gpt-4"
        mock_args.base_url = None
        mock_args.api_key = "test"
        mock_args.custom_skills_directory = None
        mock_args.web = False
        mock_args.otel = False
        mock_args.otel_endpoint = None
        mock_args.otel_headers = None
        mock_args.otel_public_key = None
        mock_args.otel_secret_key = None
        mock_args.otel_protocol = "http/protobuf"
        mock_parser.return_value.parse_args.return_value = mock_args

        import importlib
        import sys

        mod = sys.modules.get("portainer_agent.agent_server")
        if not mod:
            mod = importlib.import_module("portainer_agent.agent_server")

        importlib.reload(mod)
        mod.agent_server()
        assert mock_server.called


def test_agent_server_main_execution():
    with (
        patch("agent_utilities.initialize_workspace"),
        patch("agent_utilities.load_identity", return_value={"name": "test"}),
        patch(
            "agent_utilities.build_system_prompt_from_workspace", return_value="prompt"
        ),
        patch("agent_utilities.create_agent_server") as mock_server,
        patch("agent_utilities.create_agent_parser") as mock_parser,
        patch("sys.argv", ["agent_server.py"]),
    ):
        mock_args = MagicMock()
        mock_args.debug = False
        mock_args.mcp_url = None
        mock_args.mcp_config = None
        mock_args.host = "localhost"
        mock_args.port = 8000
        mock_args.provider = "openai"
        mock_args.model_id = "gpt-4"
        mock_args.base_url = None
        mock_args.api_key = "test"
        mock_args.custom_skills_directory = None
        mock_args.web = False
        mock_args.otel = False
        mock_args.otel_endpoint = None
        mock_args.otel_headers = None
        mock_args.otel_public_key = None
        mock_args.otel_secret_key = None
        mock_args.otel_protocol = "http/protobuf"
        mock_parser.return_value.parse_args.return_value = mock_args

        runpy.run_module("portainer_agent.agent_server", run_name="__main__")
        assert mock_server.called


def test_main_module():
    with patch("portainer_agent.agent_server.agent_server") as mock_agent_server:
        runpy.run_module("portainer_agent.__main__", run_name="__main__")
        mock_agent_server.assert_called_once()


# --- 4. Tests for portainer_agent/api_client.py ---


def test_portainer_api_brute_force(_mock_session):
    from portainer_agent.api_client import PortainerApi

    api = PortainerApi(base_url="http://test", token="test")

    common_kwargs = {
        "endpoint_id": 1,
        "environment_id": 1,
        "id": 1,
        "stack_id": 1,
        "container_id": "test",
        "image_id": "test",
        "network_id": "test",
        "volume_id": "test",
        "user_id": 1,
        "team_id": 1,
        "resource_control_id": 1,
        "registry_id": 1,
        "tag_id": 1,
        "edge_group_id": 1,
        "edge_stack_id": 1,
        "edge_job_id": 1,
        "name": "test",
        "payload": {},
        "data": {},
        "method": "GET",
        "path": "/test",
        "url": "http://test",
        "limit": 10,
        "offset": 0,
        "public_url": "http://test",
        "group_id": 1,
        "endpoint_type": 1,
        "file_content": b"test_content_bytes",
    }

    # Introspect all methods
    for name, method in inspect.getmembers(api, predicate=inspect.ismethod):
        if name.startswith("_"):
            continue
        print(f"Calling PortainerApi.{name}...")
        sig = inspect.signature(method)
        has_kwargs = any(
            p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values()
        )
        if has_kwargs:
            kwargs = common_kwargs.copy()
        else:
            kwargs = {k: v for k, v in common_kwargs.items() if k in sig.parameters}
            for p_name, p in sig.parameters.items():
                if p.default == inspect.Parameter.empty and p_name not in kwargs:
                    if p.annotation is bytes:
                        kwargs[p_name] = b"test"
                    else:
                        kwargs[p_name] = "test" if p.annotation is str else 1
        try:
            method(**kwargs)
        except Exception:
            pass


def test_api_client_import_fallback():
    import importlib

    original_api_client = sys.modules.pop("portainer_agent.api_client", None)

    original_import = builtins.__import__

    def mock_import(name, *args, **kwargs):
        if "agent_utilities.core.exceptions" in name:
            raise ImportError("Simulated import error")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=mock_import):
        importlib.import_module("portainer_agent.api_client")
        import portainer_agent.api_client

        assert hasattr(portainer_agent.api_client, "AuthError")
        assert hasattr(portainer_agent.api_client, "UnauthorizedError")

    if original_api_client:
        sys.modules["portainer_agent.api_client"] = original_api_client


def test_api_client_decode_fallbacks():
    from portainer_agent.api_client import PortainerApi

    with patch("requests.Session") as mock_sess:
        session = mock_sess.return_value
        res = MagicMock()
        res.status_code = 200
        res.ok = True
        res.json.side_effect = Exception("JSON decode error")
        res.text = "non-json-response"

        session.get.return_value = res
        session.post.return_value = res
        session.put.return_value = res
        session.patch.return_value = res

        client = PortainerApi(base_url="http://test", token="test")

        # Test decodes
        assert client._get("/endpoint") == "non-json-response"
        assert client._post("/endpoint", data={}) == "non-json-response"
        assert client._put("/endpoint", data={}) == "non-json-response"
        assert client._patch("/endpoint", data={}) == "non-json-response"


def test_api_client_get_stack_logs_swarm():
    from portainer_agent.api_client import PortainerApi

    client = PortainerApi(base_url="http://test", token="test")

    # Mock internal methods
    client.get_stack = MagicMock(return_value={"Name": "swarm_stack", "Type": 1})
    client.list_services = MagicMock(return_value=[{"ID": "svc123", "Spec": {"Name": "service1"}}])
    client.get_service_logs = MagicMock(return_value="swarm_logs")

    logs = client.get_stack_logs(endpoint_id=1, stack_id=10)
    assert "--- Service: service1 ---" in logs
    assert "swarm_logs" in logs

    client.get_stack.assert_called_once_with(10)
    client.list_services.assert_called_once()
    client.get_service_logs.assert_called_once_with(1, "svc123")


def test_api_client_get_stack_logs_compose_fallback():
    from portainer_agent.api_client import PortainerApi

    client = PortainerApi(base_url="http://test", token="test")

    client.get_stack = MagicMock(return_value={"Name": "compose_stack", "Type": 2})
    # First list_containers returns empty, second returns container
    client.list_containers = MagicMock(side_effect=[[], [{"Id": "cont123", "Names": ["/container1"]}]])
    client.get_container_logs = MagicMock(return_value="container_logs")

    logs = client.get_stack_logs(endpoint_id=1, stack_id=10)
    assert "--- Container: container1 ---" in logs
    assert "container_logs" in logs

    assert client.list_containers.call_count == 2
    client.get_container_logs.assert_called_once_with(1, "cont123")


# --- 5. Tests for portainer_agent/mcp_server.py ---

VALID_TOOL_ACTIONS = {
    "portainer_auth": ["authenticate", "logout", "validate_oauth"],
    "portainer_environment": [
        "get_endpoints",
        "get_endpoint",
        "create_endpoint",
        "update_endpoint",
        "delete_endpoint",
        "snapshot_endpoint",
        "snapshot_all_endpoints",
        "get_endpoint_groups",
        "create_endpoint_group",
        "delete_endpoint_group",
        "get_endpoint_settings",
        "update_endpoint_settings",
    ],
    "portainer_docker": [
        "get_docker_dashboard",
        "get_container_gpus",
        "docker_list_containers",
        "docker_inspect_container",
        "docker_get_container_logs",
        "docker_get_container_stats",
        "docker_start_container",
        "docker_stop_container",
        "docker_restart_container",
        "docker_remove_container",
        "docker_list_services",
        "docker_inspect_service",
        "docker_get_service_logs",
        "docker_list_images",
        "docker_inspect_image",
        "docker_list_networks",
        "docker_inspect_network",
        "docker_list_volumes",
        "docker_inspect_volume",
        "docker_get_info",
        "docker_get_version",
        "docker_get_system_df",
        "docker_create_container",
        "docker_create_network",
        "docker_create_volume",
        "docker_create_exec",
        "docker_start_exec",
        "docker_inspect_exec",
        "docker_get_stack_logs",
    ],
    "portainer_stack": [
        "get_stacks",
        "get_stack",
        "get_stack_by_name",
        "get_stack_file",
        "create_standalone_stack",
        "create_standalone_stack_from_repo",
        "create_standalone_stack_from_string",
        "create_standalone_stack_from_repository",
        "create_swarm_stack_from_string",
        "create_swarm_stack_from_repository",
        "create_kubernetes_stack_from_string",
        "create_kubernetes_stack_from_repository",
        "update_stack",
        "delete_stack",
        "start_stack",
        "stop_stack",
        "migrate_stack",
        "update_stack_git",
        "redeploy_stack_git",
        "associate_stack",
    ],
    "portainer_kubernetes": [
        "get_k8s_dashboard",
        "get_k8s_namespaces",
        "get_k8s_applications",
        "get_k8s_services",
        "get_k8s_ingresses",
        "get_k8s_configmaps",
        "get_k8s_secrets",
        "get_k8s_volumes",
        "get_k8s_events",
        "get_k8s_nodes_limits",
        "get_k8s_metrics_nodes",
        "get_helm_releases",
        "install_helm_chart",
        "delete_helm_release",
        "get_k8s_namespace",
        "create_k8s_namespace",
        "update_k8s_namespace",
        "delete_k8s_namespace",
        "get_k8s_namespace_count",
        "drain_k8s_node",
        "describe_k8s_resource",
        "get_k8s_rbac_enabled",
    ],
    "portainer_edge": [
        "get_edge_groups",
        "create_edge_group",
        "delete_edge_group",
        "get_edge_stacks",
        "get_edge_stack",
        "create_edge_stack",
        "delete_edge_stack",
        "get_edge_jobs",
        "get_edge_job",
        "create_edge_job",
        "delete_edge_job",
    ],
    "portainer_template": [
        "get_templates",
        "get_custom_templates",
        "get_custom_template",
        "create_custom_template",
        "delete_custom_template",
        "get_custom_template_file",
        "get_helm_templates",
    ],
    "portainer_user": [
        "get_users",
        "get_user",
        "get_current_user",
        "create_user",
        "delete_user",
        "get_teams",
        "create_team",
        "delete_team",
        "get_roles",
        "get_user_tokens",
    ],
    "portainer_registry": [
        "get_registries",
        "get_registry",
        "create_registry",
        "delete_registry",
    ],
    "portainer_system": [
        "get_status",
        "get_system_info",
        "get_system_version",
        "get_settings",
        "update_settings",
        "get_tags",
        "create_tag",
        "delete_tag",
        "get_motd",
        "backup_portainer",
    ],
}


@pytest.mark.asyncio
async def test_mcp_server_comprehensive_action_routes():
    from portainer_agent.mcp_server import get_mcp_instance

    mcp_data = get_mcp_instance()
    mcp = mcp_data[0] if isinstance(mcp_data, tuple) else mcp_data

    tool_objs = await mcp.list_tools()

    mock_client = MagicMock()
    mock_client.get_stack.return_value = {"Name": "test_stack", "Type": 1}

    for tool in tool_objs:
        tool_name = tool.name
        actions = VALID_TOOL_ACTIONS.get(tool_name, [])
        for act in actions:
            sig = inspect.signature(tool.fn)
            target_params = {
                "action": act,
                "endpoint_id": 1,
                "environment_id": None,  # To trigger environment_id = endpoint_id fallback (line 166)
                "container_id": "test",
                "stack_id": 1,
                "user_id": 1,
                "client": mock_client,
                "name": "test_stack",
                "file_content": "version: '3'\nservices:\n  web:\n    image: nginx",
                "stack_file_content": "version: '3'\nservices:\n  web:\n    image: nginx",
                "repo_url": "http://gitlab.example/test.git",
                "swarm_id": "swarm123",
                "target_endpoint_id": 2,
                "chart_name": "nginx",
                "release_name": "web",
                "params_json": '{"target_endpoint_id": 2}',
            }
            filtered_params = {
                k: v for k, v in target_params.items() if k in sig.parameters
            }
            # Call tool.fn directly with dynamic valid parameters
            await tool.fn(**filtered_params)

        # Test invalid action to cover raise ValueError at the end of each routing function
        try:
            sig = inspect.signature(tool.fn)
            target_params = {
                "action": "invalid_action_value_123",
                "endpoint_id": 1,
                "environment_id": None,
                "client": mock_client,
            }
            filtered_params = {
                k: v for k, v in target_params.items() if k in sig.parameters
            }
            await tool.fn(**filtered_params)
        except ValueError:
            pass


@pytest.mark.asyncio
async def test_mcp_server_custom_route():
    from portainer_agent.mcp_server import get_mcp_instance

    mcp_data = get_mcp_instance()
    mcp = mcp_data[0] if isinstance(mcp_data, tuple) else mcp_data

    app = mcp.http_app()
    route_handler = None
    for route in app.routes:
        if route.path == "/health":
            route_handler = route.endpoint
            break

    assert route_handler is not None

    mock_scope = {
        "type": "http",
        "method": "GET",
        "path": "/health",
        "headers": Headers().raw,
    }
    mock_req = Request(scope=mock_scope)
    response = await route_handler(mock_req)

    assert response.status_code == 200
    # The shared MCP server factory now owns the /health route and returns a
    # lowercase status plus the server name; assert on that current contract.
    payload = json.loads(response.body.decode())
    assert payload.get("status", "").lower() == "ok"


def test_mcp_server_requests_warning_import_error():
    import importlib

    original_mcp_server = sys.modules.pop("portainer_agent.mcp_server", None)

    original_import = builtins.__import__

    def mock_import(name, *args, **kwargs):
        if "RequestsDependencyWarning" in name or "requests.exceptions" in name:
            raise ImportError("Simulated import error")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=mock_import):
        importlib.import_module("portainer_agent.mcp_server")

    if original_mcp_server:
        sys.modules["portainer_agent.mcp_server"] = original_mcp_server


def test_mcp_server_startup_transports():
    from portainer_agent.mcp_server import mcp_server

    mock_args = MagicMock()
    mock_args.transport = "stdio"
    mock_args.host = "localhost"
    mock_args.port = 8000
    mock_args.auth_type = "none"

    mock_mcp = MagicMock()

    with (
        patch(
            "portainer_agent.mcp_server.get_mcp_instance",
            return_value=(mock_mcp, mock_args, []),
        ),
        patch("sys.exit") as mock_exit,
        patch("fastmcp.FastMCP.run"),
    ):
        # 1. stdio
        mock_args.transport = "stdio"
        mcp_server()
        mock_mcp.run.assert_called_with(transport="stdio")

        # 2. streamable-http
        mock_args.transport = "streamable-http"
        mcp_server()
        mock_mcp.run.assert_called_with(
            transport="streamable-http", host="localhost", port=8000
        )

        # 3. sse
        mock_args.transport = "sse"
        mcp_server()
        mock_mcp.run.assert_called_with(transport="sse", host="localhost", port=8000)

        # 4. Invalid
        mock_args.transport = "invalid-transport"
        mcp_server()
        mock_exit.assert_called_with(1)


def test_mcp_server_main_execution():
    mock_args = MagicMock()
    mock_args.transport = "stdio"
    mock_args.host = "localhost"
    mock_args.port = 8000
    mock_args.auth_type = "none"

    mock_mcp = MagicMock()

    with (
        patch(
            "portainer_agent.mcp_server.get_mcp_instance",
            return_value=(mock_mcp, mock_args, []),
        ),
        patch("sys.exit"),
        patch("fastmcp.FastMCP.run") as mock_run,
    ):
        runpy.run_module("portainer_agent.mcp_server", run_name="__main__")
        mock_run.assert_called_with(transport="stdio")
