#!/usr/bin/python
import warnings

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import sys
from typing import Any

from agent_utilities.mcp_utilities import (
    create_mcp_server,
    load_config,
    register_tool_surface,
    resolve_action,
    run_blocking,
)
from starlette.requests import Request
from starlette.responses import JSONResponse

from portainer_agent.api_client import PortainerApi
from portainer_agent.auth import get_client

__version__ = "1.0.0"

logger = get_logger(name="portainer-agent")
logger.setLevel(logging.INFO)


def wrap_list(res: Any) -> Any:
    return {"data": res} if isinstance(res, list) else res


def register_auth_tools(mcp: FastMCP):
    @mcp.tool(tags={"Auth"})
    async def portainer_auth(
        action: str = Field(
            description="Action to perform. Must be one of: 'authenticate', 'logout', 'validate_oauth'"
        ),
        username: str | None = Field(default=None, description="username"),
        password: str | None = Field(default=None, description="password"),
        code: str | None = Field(default=None, description="code"),
        client=Depends(get_client),
    ) -> dict:
        """Manage auth operations."""
        kwargs: dict[str, Any]
        valid_actions = ("authenticate", "logout", "validate_oauth")
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "authenticate":
            kwargs = {"username": username, "password": password}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.authenticate, **kwargs)
        if action == "logout":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.logout, **kwargs)
        if action == "validate_oauth":
            kwargs = {"code": code}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.validate_oauth, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: authenticate', 'logout', 'validate_oauth"
        )


def register_environment_tools(mcp: FastMCP):
    @mcp.tool(tags={"Environment"})
    async def portainer_environment(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group', 'get_endpoint_settings', 'update_endpoint_settings'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        name: str | None = Field(default=None, description="name"),
        endpoint_type: int | None = Field(default=None, description="endpoint type"),
        url: str | None = Field(default=None, description="url"),
        description: str | None = Field(default=None, description="description"),
        group_id: int | None = Field(default=None, description="group id"),
        settings: dict | None = Field(
            default=None,
            description="endpoint settings payload for update_endpoint_settings (e.g. Kubernetes storage class, ingress class, RBAC, metrics toggles)",
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage environment operations."""
        kwargs: dict[str, Any]
        valid_actions = (
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
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_endpoints":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return wrap_list(await run_blocking(client.get_endpoints, **kwargs))
        if action == "get_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_endpoint, **kwargs)
        if action == "create_endpoint":
            kwargs = {
                "name": name,
                "endpoint_type": endpoint_type,
                "url": url,
            }  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_endpoint, **kwargs)
        if action == "update_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.update_endpoint, **kwargs)
        if action == "delete_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_endpoint, **kwargs)
        if action == "snapshot_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.snapshot_endpoint, **kwargs)
        if action == "snapshot_all_endpoints":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.snapshot_all_endpoints, **kwargs)
        if action == "get_endpoint_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return wrap_list(await run_blocking(client.get_endpoint_groups, **kwargs))
        if action == "create_endpoint_group":
            kwargs = {"name": name, "description": description}  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_endpoint_group, **kwargs)
        if action == "delete_endpoint_group":
            kwargs = {"group_id": group_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_endpoint_group, **kwargs)
        if action == "get_endpoint_settings":
            return await run_blocking(
                client.get_endpoint_settings, endpoint_id=endpoint_id
            )
        if action == "update_endpoint_settings":
            payload = settings if isinstance(settings, dict) else {}
            return await run_blocking(
                client.update_endpoint_settings,
                endpoint_id=endpoint_id,
                **payload,
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group', 'get_endpoint_settings', 'update_endpoint_settings"
        )


def _handle_container_actions(
    client,
    action: str,
    environment_id: int | None,
    container_id: str | None,
    tail: int | None,
) -> dict:
    kwargs: dict[str, Any]
    if action == "get_container_gpus":
        kwargs = {
            "environment_id": environment_id,
            "container_id": container_id,
        }  # type: ignore
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.get_container_gpus(**kwargs)
    if action == "docker_list_containers":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.list_containers(**kwargs)}
    if action == "docker_inspect_container":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.inspect_container(**kwargs)}
    if action == "docker_get_container_logs":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        if tail is not None:
            kwargs["tail"] = tail
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.get_container_logs(**kwargs)}
    if action == "docker_get_container_stats":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.get_container_stats(**kwargs)}
    if action == "docker_start_container":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.start_container(**kwargs)}
    if action == "docker_stop_container":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.stop_container(**kwargs)}
    if action == "docker_restart_container":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.restart_container(**kwargs)}
    if action == "docker_remove_container":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.remove_container(**kwargs)}
    raise ValueError(f"Unknown container action: {action}")


def _handle_service_actions(
    client,
    action: str,
    environment_id: int | None,
    service_id: str | None,
    tail: int | None,
) -> dict:
    kwargs: dict[str, Any]
    if action == "docker_list_services":
        kwargs = {"endpoint_id": environment_id}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        res = client.list_services(**kwargs)
        return {"data": res} if isinstance(res, list) else res
    if action == "docker_inspect_service":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if service_id is not None:
            kwargs["service_id"] = service_id
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.inspect_service(**kwargs)}
    if action == "docker_get_service_logs":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if service_id is not None:
            kwargs["service_id"] = service_id
        if tail is not None:
            kwargs["tail"] = tail
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return {"data": client.get_service_logs(**kwargs)}
    raise ValueError(f"Unknown service action: {action}")


def _handle_resource_actions(
    client,
    action: str,
    environment_id: int | None,
) -> dict:
    kwargs: dict[str, Any]
    if action == "get_docker_dashboard":
        kwargs = {"environment_id": environment_id}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.get_docker_dashboard(**kwargs)
    if action == "docker_list_images":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_list_images(**kwargs)
    if action == "docker_inspect_image":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_inspect_image(**kwargs)
    if action == "docker_list_networks":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_list_networks(**kwargs)
    if action == "docker_inspect_network":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_inspect_network(**kwargs)
    if action == "docker_list_volumes":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_list_volumes(**kwargs)
    if action == "docker_inspect_volume":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_inspect_volume(**kwargs)
    if action == "docker_get_info":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_get_info(**kwargs)
    if action == "docker_get_version":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_get_version(**kwargs)
    if action == "docker_get_system_df":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_get_system_df(**kwargs)
    if action == "docker_create_container":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_create_container(**kwargs)
    if action == "docker_create_network":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_create_network(**kwargs)
    if action == "docker_create_volume":
        kwargs = {}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return client.docker_create_volume(**kwargs)
    raise ValueError(f"Unknown resource action: {action}")


def _handle_exec_stack_actions(
    client,
    action: str,
    environment_id: int | None,
    container_id: str | None,
    stack_id: int | None,
    exec_id: str | None,
    cmd: list[str] | None,
    detach: bool | None,
    tty: bool | None,
) -> dict:
    kwargs: dict[str, Any]
    if action == "docker_create_exec":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if container_id is not None:
            kwargs["container_id"] = container_id
        config: dict[str, Any] = {}
        if cmd is not None:
            config["Cmd"] = cmd
        if detach is not None:
            config["Detach"] = detach
        if tty is not None:
            config["Tty"] = tty
        kwargs["config"] = config
        return {"data": client.create_exec(**kwargs)}
    if action == "docker_start_exec":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if exec_id is not None:
            kwargs["exec_id"] = exec_id
        exec_config: dict[str, Any] = {}
        if detach is not None:
            exec_config["Detach"] = detach
        if tty is not None:
            exec_config["Tty"] = tty
        kwargs["config"] = exec_config
        return {"data": client.start_exec(**kwargs)}
    if action == "docker_inspect_exec":
        kwargs = {}
        if environment_id is not None:
            kwargs["endpoint_id"] = environment_id
        if exec_id is not None:
            kwargs["exec_id"] = exec_id
        return {"data": client.inspect_exec(**kwargs)}
    if action == "docker_get_stack_logs":
        kwargs = {"endpoint_id": environment_id, "stack_id": stack_id}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        res = client.get_stack_logs(**kwargs)
        return {"data": res} if isinstance(res, str) else res
    raise ValueError(f"Unknown exec/stack action: {action}")


def register_docker_tools(mcp: FastMCP):
    @mcp.tool(tags={"Docker"})
    async def portainer_docker(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_docker_dashboard', 'get_container_gpus', 'docker_list_containers', 'docker_inspect_container', 'docker_get_container_logs', 'docker_get_container_stats', 'docker_start_container', 'docker_stop_container', 'docker_restart_container', 'docker_remove_container', 'docker_list_services', 'docker_inspect_service', 'docker_get_service_logs', 'docker_list_images', 'docker_inspect_image', 'docker_list_networks', 'docker_inspect_network', 'docker_list_volumes', 'docker_inspect_volume', 'docker_get_info', 'docker_get_version', 'docker_get_system_df', 'docker_create_container', 'docker_create_network', 'docker_create_volume', 'docker_create_exec', 'docker_start_exec', 'docker_inspect_exec', 'docker_get_stack_logs'"
        ),
        environment_id: int | None = Field(default=None, description="environment id"),
        endpoint_id: int | None = Field(
            default=None, description="endpoint id (alias for environment id)"
        ),
        container_id: str | None = Field(default=None, description="container id"),
        stack_id: int | None = Field(default=None, description="stack id"),
        service_id: str | None = Field(default=None, description="service id"),
        exec_id: str | None = Field(default=None, description="exec instance id"),
        cmd: list[str] | None = Field(
            default=None, description="Command to run in exec"
        ),
        detach: bool | None = Field(
            default=None, description="Detach from the command"
        ),
        tty: bool | None = Field(default=None, description="Allocate a pseudo-TTY"),
        tail: int | None = Field(
            default=None, description="Number of log lines to tail"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage docker operations."""
        valid_actions = (
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
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved

        if environment_id is None and endpoint_id is not None:
            environment_id = endpoint_id

        if action in (
            "get_container_gpus",
            "docker_list_containers",
            "docker_inspect_container",
            "docker_get_container_logs",
            "docker_get_container_stats",
            "docker_start_container",
            "docker_stop_container",
            "docker_restart_container",
            "docker_remove_container",
        ):
            return await run_blocking(
                _handle_container_actions,
                client,
                action,
                environment_id,
                container_id,
                tail,
            )

        if action in (
            "docker_list_services",
            "docker_inspect_service",
            "docker_get_service_logs",
        ):
            return await run_blocking(
                _handle_service_actions,
                client,
                action,
                environment_id,
                service_id,
                tail,
            )

        if action in (
            "get_docker_dashboard",
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
        ):
            return await run_blocking(
                _handle_resource_actions, client, action, environment_id
            )

        if action in (
            "docker_create_exec",
            "docker_start_exec",
            "docker_inspect_exec",
            "docker_get_stack_logs",
        ):
            return await run_blocking(
                _handle_exec_stack_actions,
                client,
                action,
                environment_id,
                container_id,
                stack_id,
                exec_id,
                cmd,
                detach,
                tty,
            )

        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_docker_dashboard', 'get_container_gpus', 'docker_list_containers', 'docker_inspect_container', 'docker_get_container_logs', 'docker_get_container_stats', 'docker_start_container', 'docker_stop_container', 'docker_restart_container', 'docker_remove_container', 'docker_list_services', 'docker_inspect_service', 'docker_get_service_logs', 'docker_list_images', 'docker_inspect_image', 'docker_list_networks', 'docker_inspect_network', 'docker_list_volumes', 'docker_inspect_volume', 'docker_get_info', 'docker_get_version', 'docker_get_system_df', 'docker_create_container', 'docker_create_network', 'docker_create_volume', 'docker_create_exec', 'docker_start_exec', 'docker_inspect_exec', 'docker_get_stack_logs"
        )


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(tags={"Stack"})
    async def portainer_stack(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_stacks', 'get_stack', 'get_stack_by_name', 'get_stack_file', 'export_all_stacks', 'create_standalone_stack_from_string', 'create_standalone_stack_from_repository', 'create_swarm_stack_from_string', 'create_swarm_stack_from_repository', 'create_kubernetes_stack_from_string', 'create_kubernetes_stack_from_repository', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'migrate_stack', 'update_stack_git', 'redeploy_stack_git', 'associate_stack'"
        ),
        stack_id: int | None = Field(default=None, description="stack id"),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        stack_file_content: str | None = Field(
            default=None, description="compose file content for stack creation/update"
        ),
        env: list | None = Field(
            default=None,
            description="environment variables list for stack creation/update",
        ),
        prune: bool | None = Field(
            default=None, description="whether to prune for update_stack"
        ),
        name: str | None = Field(default=None, description="stack name"),
        repo_url: str | None = Field(default=None, description="git repository url"),
        swarm_id: str | None = Field(default=None, description="swarm id"),
        target_dir: str | None = Field(
            default=None, description="target directory for export_all_stacks"
        ),
        params_json: str | None = Field(
            default=None,
            description="JSON string of dynamic/extra parameters to unpack",
        ),
        client=Depends(get_client),
    ) -> dict:
        # Clean up Pydantic FieldInfo default values when called directly in tests
        from pydantic.fields import FieldInfo

        if isinstance(stack_id, FieldInfo):
            stack_id = None
        if isinstance(endpoint_id, FieldInfo):
            endpoint_id = None
        if isinstance(stack_file_content, FieldInfo):
            stack_file_content = None
        if isinstance(env, FieldInfo):
            env = None
        if isinstance(prune, FieldInfo):
            prune = None
        if isinstance(name, FieldInfo):
            name = None
        if isinstance(repo_url, FieldInfo):
            repo_url = None
        if isinstance(swarm_id, FieldInfo):
            swarm_id = None
        if isinstance(params_json, FieldInfo):
            params_json = None

        import json

        params = {}
        if params_json:
            try:
                params = json.loads(params_json)
                if not isinstance(params, dict):
                    params = {}
            except Exception as e:
                raise ValueError(f"Invalid params_json: {e}") from e

        # Field map with defaults
        field_map = {
            "stack_id": stack_id,
            "endpoint_id": endpoint_id,
            "stack_file_content": stack_file_content,
            "env": env,
            "prune": prune,
            "name": name,
            "repo_url": repo_url,
            "swarm_id": swarm_id,
        }

        # Parameter resolver: searches case-insensitive variants in params_json first, then fields
        def get_val(keys: list[str], default: Any = None) -> Any:
            # Check params_json first (try direct, lower, upper, capitalized)
            for k in keys:
                for pk in [k, k.lower(), k.upper(), k.capitalize()]:
                    if pk in params:
                        return params[pk]
            # Check named parameters
            for k in keys:
                if k in field_map and field_map[k] is not None:
                    return field_map[k]
            return default

        # Clean/normalize action name & route backwards compatibility
        action_normalized = action.strip()
        if action_normalized == "create_standalone_stack":
            # Backward compatible check: if repo_url exists, route to repo
            url_val = get_val(["repo_url", "RepositoryURL", "repository_url"])
            if url_val:
                action_normalized = "create_standalone_stack_from_repository"
            else:
                action_normalized = "create_standalone_stack_from_string"
        elif action_normalized == "create_standalone_stack_from_repo":
            action_normalized = "create_standalone_stack_from_repository"

        valid_actions = (
            "get_stacks",
            "get_stack",
            "get_stack_by_name",
            "get_stack_file",
            "export_all_stacks",
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
        )
        resolved = resolve_action(
            action_normalized, valid_actions, service="portainer-agent"
        )
        if isinstance(resolved, dict):
            return resolved
        action_normalized = resolved

        # Extract remaining kwargs (exclude known parameter keys that are explicitly passed)
        resolved_kwargs = {**params}
        explicit_keys = [
            "stack_id",
            "endpoint_id",
            "endpointId",
            "stack_file_content",
            "StackFileContent",
            "file_content",
            "stack_file_content",
            "env",
            "Env",
            "prune",
            "Prune",
            "name",
            "Name",
            "StackName",
            "repo_url",
            "RepositoryURL",
            "repository_url",
            "swarm_id",
            "SwarmID",
            "target_endpoint_id",
            "TargetEndpointID",
            "targetEndpointId",
            "action",
            "params_json",
        ]
        # Remove explicitly parsed keys from resolved_kwargs to pass extra kwargs dynamically
        for ek in explicit_keys:
            variants = [ek, ek.lower(), ek.upper(), ek.capitalize()]
            if len(ek) > 1:
                variants.append(ek[0].lower() + ek[1:])
                variants.append(ek[0].upper() + ek[1:])
            for pk in variants:
                if pk in resolved_kwargs:
                    try:
                        del resolved_kwargs[pk]
                    except KeyError:
                        pass

        # Re-inject env and prune if present
        env_val = get_val(["env", "Env"])
        if env_val is not None:
            resolved_kwargs["Env"] = env_val
        prune_val = get_val(["prune", "Prune"])
        if prune_val is not None:
            resolved_kwargs["Prune"] = prune_val

        if action_normalized == "get_stacks":
            res = await run_blocking(client.get_stacks, **resolved_kwargs)
            return {"data": res} if isinstance(res, list) else res

        elif action_normalized == "get_stack":
            s_id = get_val(["stack_id"])
            if s_id is None:
                raise ValueError("Missing parameter: stack_id")
            return await run_blocking(client.get_stack, stack_id=int(s_id))

        elif action_normalized == "get_stack_by_name":
            n = get_val(["name"])
            if not n:
                raise ValueError("Missing parameter: name")
            return await run_blocking(client.get_stack_by_name, name=str(n))

        elif action_normalized == "get_stack_file":
            s_id = get_val(["stack_id"])
            if s_id is None:
                raise ValueError("Missing parameter: stack_id")
            return await run_blocking(client.get_stack_file, stack_id=int(s_id))

        elif action_normalized == "create_standalone_stack_from_string":
            n = get_val(["name", "Name", "StackName"])
            fc = get_val(["file_content", "StackFileContent", "stack_file_content"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not fc or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_standalone_stack_from_string: name, file_content/stack_file_content, endpoint_id"
                )
            return await run_blocking(
                client.create_standalone_stack_from_string,
                name=str(n),
                file_content=str(fc),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "create_standalone_stack_from_repository":
            n = get_val(["name", "Name", "StackName"])
            u = get_val(["repo_url", "RepositoryURL", "repository_url"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not u or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_standalone_stack_from_repository: name, repo_url/RepositoryURL, endpoint_id"
                )
            return await run_blocking(
                client.create_standalone_stack_from_repository,
                name=str(n),
                repo_url=str(u),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "create_swarm_stack_from_string":
            n = get_val(["name", "Name", "StackName"])
            fc = get_val(["file_content", "StackFileContent", "stack_file_content"])
            sw_id = get_val(["swarm_id", "SwarmID"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not fc or not sw_id or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_swarm_stack_from_string: name, file_content/stack_file_content, swarm_id, endpoint_id"
                )
            return await run_blocking(
                client.create_swarm_stack_from_string,
                name=str(n),
                file_content=str(fc),
                swarm_id=str(sw_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "create_swarm_stack_from_repository":
            n = get_val(["name", "Name", "StackName"])
            u = get_val(["repo_url", "RepositoryURL", "repository_url"])
            sw_id = get_val(["swarm_id", "SwarmID"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not u or not sw_id or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_swarm_stack_from_repository: name, repo_url/RepositoryURL, swarm_id, endpoint_id"
                )
            return await run_blocking(
                client.create_swarm_stack_from_repository,
                name=str(n),
                repo_url=str(u),
                swarm_id=str(sw_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "create_kubernetes_stack_from_string":
            n = get_val(["name", "Name", "StackName"])
            fc = get_val(["file_content", "StackFileContent", "stack_file_content"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not fc or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_kubernetes_stack_from_string: name, file_content/stack_file_content, endpoint_id"
                )
            return await run_blocking(
                client.create_kubernetes_stack_from_string,
                name=str(n),
                file_content=str(fc),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "create_kubernetes_stack_from_repository":
            n = get_val(["name", "Name", "StackName"])
            u = get_val(["repo_url", "RepositoryURL", "repository_url"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if not n or not u or ep_id is None:
                raise ValueError(
                    "Missing required parameters for create_kubernetes_stack_from_repository: name, repo_url/RepositoryURL, endpoint_id"
                )
            return await run_blocking(
                client.create_kubernetes_stack_from_repository,
                name=str(n),
                repo_url=str(u),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "update_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for update_stack: stack_id, endpoint_id"
                )

            # Map standard update options from direct arguments if not set in resolved_kwargs
            s_file_content = get_val(["stack_file_content", "StackFileContent"])
            if s_file_content is not None and "StackFileContent" not in resolved_kwargs:
                resolved_kwargs["StackFileContent"] = s_file_content
            s_env = get_val(["env", "Env"])
            if s_env is not None and "Env" not in resolved_kwargs:
                resolved_kwargs["Env"] = s_env
            s_prune = get_val(["prune", "Prune"])
            if s_prune is not None and "Prune" not in resolved_kwargs:
                resolved_kwargs["Prune"] = s_prune

            return await run_blocking(
                client.update_stack,
                stack_id=int(s_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "delete_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for delete_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.delete_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        elif action_normalized == "start_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for start_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.start_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        elif action_normalized == "stop_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for stop_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.stop_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        elif action_normalized == "migrate_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            target_ep_id = get_val(
                ["target_endpoint_id", "TargetEndpointID", "targetEndpointId"]
            )
            if s_id is None or ep_id is None or target_ep_id is None:
                raise ValueError(
                    "Missing required parameters for migrate_stack: stack_id, endpoint_id, target_endpoint_id"
                )
            return await run_blocking(
                client.migrate_stack,
                stack_id=int(s_id),
                endpoint_id=int(ep_id),
                target_endpoint_id=int(target_ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "update_stack_git":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for update_stack_git: stack_id, endpoint_id"
                )
            s_env = get_val(["env", "Env"])
            if s_env is not None:
                resolved_kwargs["Env"] = s_env
            s_prune = get_val(["prune", "Prune"])
            if s_prune is not None:
                resolved_kwargs["Prune"] = s_prune
            return await run_blocking(
                client.update_stack_git,
                stack_id=int(s_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "redeploy_stack_git":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for redeploy_stack_git: stack_id, endpoint_id"
                )
            s_env = get_val(["env", "Env"])
            if s_env is not None:
                resolved_kwargs["Env"] = s_env
            s_prune = get_val(["prune", "Prune"])
            if s_prune is not None:
                resolved_kwargs["Prune"] = s_prune
            return await run_blocking(
                client.redeploy_stack_git,
                stack_id=int(s_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "associate_stack":
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for associate_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.associate_stack,
                stack_id=int(s_id),
                endpoint_id=int(ep_id),
                **resolved_kwargs,
            )

        elif action_normalized == "export_all_stacks":
            t_dir = get_val(["target_dir", "targetDir"])
            if not t_dir:
                raise ValueError(
                    "Missing required parameter for export_all_stacks: target_dir"
                )
            return await run_blocking(client.export_all_stacks, target_dir=str(t_dir))

        raise ValueError(
            f"Unknown action: {action}. Must be one of: 'get_stacks', 'get_stack', 'get_stack_by_name', 'get_stack_file', 'export_all_stacks', 'create_standalone_stack_from_string', 'create_standalone_stack_from_repository', 'create_swarm_stack_from_string', 'create_swarm_stack_from_repository', 'create_kubernetes_stack_from_string', 'create_kubernetes_stack_from_repository', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'migrate_stack', 'update_stack_git', 'redeploy_stack_git', 'associate_stack'"
        )


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(tags={"Kubernetes"})
    async def portainer_kubernetes(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release', 'get_k8s_namespace', 'create_k8s_namespace', 'update_k8s_namespace', 'delete_k8s_namespace', 'get_k8s_namespace_count', 'drain_k8s_node', 'describe_k8s_resource', 'get_k8s_rbac_enabled'"
        ),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        chart_name: str | None = Field(default=None, description="chart name"),
        release_name: str | None = Field(default=None, description="release name"),
        environment_id: int | None = Field(
            default=None, description="kubernetes environment (endpoint) id"
        ),
        namespace: str | None = Field(default=None, description="namespace name"),
        node_name: str | None = Field(
            default=None, description="node name (for drain)"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage kubernetes operations."""
        kwargs: dict[str, Any]
        valid_actions = (
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
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_k8s_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_dashboard, **kwargs)
        if action == "get_k8s_namespaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_namespaces, **kwargs)
        if action == "get_k8s_applications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_applications, **kwargs)
        if action == "get_k8s_services":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_services, **kwargs)
        if action == "get_k8s_ingresses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_ingresses, **kwargs)
        if action == "get_k8s_configmaps":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_configmaps, **kwargs)
        if action == "get_k8s_secrets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_secrets, **kwargs)
        if action == "get_k8s_volumes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_volumes, **kwargs)
        if action == "get_k8s_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_events, **kwargs)
        if action == "get_k8s_nodes_limits":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_nodes_limits, **kwargs)
        if action == "get_k8s_metrics_nodes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_k8s_metrics_nodes, **kwargs)
        if action == "get_helm_releases":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_helm_releases, **kwargs)
        if action == "install_helm_chart":
            kwargs = {
                "endpoint_id": endpoint_id,
                "chart_name": chart_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.install_helm_chart, **kwargs)
        if action == "delete_helm_release":
            kwargs = {
                "endpoint_id": endpoint_id,
                "release_name": release_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_helm_release, **kwargs)
        if action == "get_k8s_namespace":
            return await run_blocking(
                client.get_kubernetes_namespace,
                environment_id=environment_id,
                namespace=namespace,
            )
        if action == "create_k8s_namespace":
            return await run_blocking(
                client.create_kubernetes_namespace,
                environment_id=environment_id,
                namespace=namespace,
            )
        if action == "update_k8s_namespace":
            return await run_blocking(
                client.update_kubernetes_namespace,
                environment_id=environment_id,
                namespace=namespace,
            )
        if action == "delete_k8s_namespace":
            return await run_blocking(
                client.delete_kubernetes_namespace,
                environment_id=environment_id,
                namespace=namespace,
            )
        if action == "get_k8s_namespace_count":
            return await run_blocking(
                client.get_kubernetes_namespace_count, environment_id=environment_id
            )
        if action == "drain_k8s_node":
            return await run_blocking(
                client.drain_kubernetes_node,
                environment_id=environment_id,
                node_name=node_name,
            )
        if action == "describe_k8s_resource":
            return await run_blocking(
                client.describe_kubernetes_resource, environment_id=environment_id
            )
        if action == "get_k8s_rbac_enabled":
            return await run_blocking(
                client.get_kubernetes_rbac_enabled, environment_id=environment_id
            )
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release', 'get_k8s_namespace', 'create_k8s_namespace', 'update_k8s_namespace', 'delete_k8s_namespace', 'get_k8s_namespace_count', 'drain_k8s_node', 'describe_k8s_resource', 'get_k8s_rbac_enabled"
        )


def register_edge_tools(mcp: FastMCP):
    @mcp.tool(tags={"Edge"})
    async def portainer_edge(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job'"
        ),
        name: str | None = Field(default=None, description="name"),
        group_id: int | None = Field(default=None, description="group id"),
        job_id: int | None = Field(default=None, description="job id"),
        stack_id: int | None = Field(default=None, description="stack id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage edge operations."""
        kwargs: dict[str, Any]
        valid_actions = (
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
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_edge_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_edge_groups, **kwargs)
        if action == "create_edge_group":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_edge_group, **kwargs)
        if action == "delete_edge_group":
            kwargs = {"group_id": group_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_edge_group, **kwargs)
        if action == "get_edge_stacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_edge_stacks, **kwargs)
        if action == "get_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_edge_stack, **kwargs)
        if action == "create_edge_stack":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_edge_stack, **kwargs)
        if action == "delete_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_edge_stack, **kwargs)
        if action == "get_edge_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_edge_jobs, **kwargs)
        if action == "get_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_edge_job, **kwargs)
        if action == "create_edge_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_edge_job, **kwargs)
        if action == "delete_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_edge_job, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job"
        )


def register_template_tools(mcp: FastMCP):
    @mcp.tool(tags={"Template"})
    async def portainer_template(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates'"
        ),
        template_id: int | None = Field(default=None, description="template id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage template operations."""
        kwargs: dict[str, Any]
        valid_actions = (
            "get_templates",
            "get_custom_templates",
            "get_custom_template",
            "create_custom_template",
            "delete_custom_template",
            "get_custom_template_file",
            "get_helm_templates",
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_templates, **kwargs)
        if action == "get_custom_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_templates, **kwargs)
        if action == "get_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_template, **kwargs)
        if action == "create_custom_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_custom_template, **kwargs)
        if action == "delete_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_custom_template, **kwargs)
        if action == "get_custom_template_file":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_template_file, **kwargs)
        if action == "get_helm_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_helm_templates, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates"
        )


def register_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"User"})
    async def portainer_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_users', 'get_user', 'get_current_user', 'create_user', 'delete_user', 'get_teams', 'create_team', 'delete_team', 'get_roles', 'get_user_tokens', 'get_user_git_credentials', 'get_user_git_credential', 'create_user_git_credential', 'update_user_git_credential', 'delete_user_git_credential'"
        ),
        user_id: int | None = Field(default=None, description="user id"),
        username: str | None = Field(default=None, description="username"),
        password: str | None = Field(default=None, description="password"),
        role: int | None = Field(default=None, description="role"),
        name: str | None = Field(default=None, description="name"),
        team_id: int | None = Field(default=None, description="team id"),
        credential_id: int | None = Field(
            default=None, description="git credential id"
        ),
        authorization_type: int | None = Field(
            default=None,
            description="git credential auth type (0 = basic auth username/password|PAT)",
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage user operations (incl. per-user Git credentials for binding to
        git-backed stacks via RepositoryGitCredentialID)."""
        kwargs: dict[str, Any]
        valid_actions = (
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
            "get_user_git_credentials",
            "get_user_git_credential",
            "create_user_git_credential",
            "update_user_git_credential",
            "delete_user_git_credential",
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_user_git_credentials":
            return await run_blocking(client.get_user_git_credentials, user_id=user_id)
        if action == "get_user_git_credential":
            return await run_blocking(
                client.get_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
            )
        if action == "create_user_git_credential":
            kwargs = {
                "user_id": user_id,
                "name": name,
                "username": username,
                "password": password,
            }
            if authorization_type is not None:
                kwargs["authorization_type"] = authorization_type
            return await run_blocking(client.create_user_git_credential, **kwargs)
        if action == "update_user_git_credential":
            kwargs = {
                "name": name,
                "username": username,
                "password": password,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(
                client.update_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
                **kwargs,
            )
        if action == "delete_user_git_credential":
            return await run_blocking(
                client.delete_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
            )
        if action == "get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_users, **kwargs)
        if action == "get_user":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_user, **kwargs)
        if action == "get_current_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_current_user, **kwargs)
        if action == "create_user":
            kwargs = {
                "username": username,
                "password": password,
                "role": role,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_user, **kwargs)
        if action == "delete_user":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_user, **kwargs)
        if action == "get_teams":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_teams, **kwargs)
        if action == "create_team":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_team, **kwargs)
        if action == "delete_team":
            kwargs = {"team_id": team_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_team, **kwargs)
        if action == "get_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_roles, **kwargs)
        if action == "get_user_tokens":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_user_tokens, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_users', 'get_user', 'get_current_user', 'create_user', 'delete_user', 'get_teams', 'create_team', 'delete_team', 'get_roles', 'get_user_tokens"
        )


def register_registry_tools(mcp: FastMCP):
    @mcp.tool(tags={"Registry"})
    async def portainer_registry(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_registries', 'get_registry', 'create_registry', 'delete_registry'"
        ),
        registry_id: int | None = Field(default=None, description="registry id"),
        name: str | None = Field(default=None, description="name"),
        registry_type: int | None = Field(default=None, description="registry type"),
        url: str | None = Field(default=None, description="url"),
        client=Depends(get_client),
    ) -> dict:
        """Manage registry operations."""
        kwargs: dict[str, Any]
        valid_actions = (
            "get_registries",
            "get_registry",
            "create_registry",
            "delete_registry",
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "get_registries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_registries, **kwargs)
        if action == "get_registry":
            kwargs = {"registry_id": registry_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_registry, **kwargs)
        if action == "create_registry":
            kwargs = {
                "name": name,
                "registry_type": registry_type,
                "url": url,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_registry, **kwargs)
        if action == "delete_registry":
            kwargs = {"registry_id": registry_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_registry, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_registries', 'get_registry', 'create_registry', 'delete_registry"
        )


def register_system_tools(mcp: FastMCP):
    @mcp.tool(tags={"System"})
    async def portainer_system(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer', 'raw_request'"
        ),
        name: str | None = Field(default=None, description="name"),
        tag_id: int | None = Field(default=None, description="tag id"),
        http_method: str | None = Field(
            default=None,
            description="raw_request: HTTP method (GET/POST/PUT/PATCH/DELETE)",
        ),
        api_path: str | None = Field(
            default=None,
            description="raw_request: API path relative to /api (e.g. 'users/3/gitcredentials')",
        ),
        query_json: str | None = Field(
            default=None, description="raw_request: JSON-encoded query params"
        ),
        body_json: str | None = Field(
            default=None, description="raw_request: JSON-encoded request body"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage system operations.

        Actions:
          - 'get_status': Get Portainer instance status.
          - 'get_system_info': Get system information.
          - 'get_system_version': Get Portainer version information.
          - 'get_settings': Get Portainer settings.
          - 'update_settings': Update Portainer settings.
          - 'get_tags': List all tags.
          - 'create_tag': Create a tag.
          - 'delete_tag': Delete a tag.
          - 'get_motd': Get the message of the day.
          - 'backup_portainer': Call backup_portainer
          - 'raw_request': Authenticated passthrough to ANY Portainer API endpoint
            (http_method + api_path [+ query_json/body_json]) — covers the full
            Portainer REST API surface, including operations without a typed action.
        """
        kwargs: dict[str, Any]
        valid_actions = (
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
            "raw_request",
        )
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved
        if action == "raw_request":
            import json as _json

            if not http_method or not api_path:
                raise ValueError("raw_request requires http_method and api_path")
            return await run_blocking(
                client.request,
                method=http_method,
                path=api_path,
                params=_json.loads(query_json) if query_json else None,
                data=_json.loads(body_json) if body_json else None,
            )
        if action == "get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_status, **kwargs)
        if action == "get_system_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_system_info, **kwargs)
        if action == "get_system_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_system_version, **kwargs)
        if action == "get_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_settings, **kwargs)
        if action == "update_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.update_settings, **kwargs)
        if action == "get_tags":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_tags, **kwargs)
        if action == "create_tag":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_tag, **kwargs)
        if action == "delete_tag":
            kwargs = {"tag_id": tag_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_tag, **kwargs)
        if action == "get_motd":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_motd, **kwargs)
        if action == "backup_portainer":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.backup_portainer, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer"
        )


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="portainer-agent MCP",
        version=__version__,
        instructions="portainer-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    register_tool_surface(
        mcp,
        client_cls=PortainerApi,
        get_client=get_client,
        service="portainer-agent",
        tools_module=sys.modules[__name__],
    )

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"portainer-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
