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

from agent_utilities.core.config import load_config
from agent_utilities.mcp.action_dispatch import resolve_action
from agent_utilities.mcp.concurrency import run_blocking
from agent_utilities.mcp.server_factory import create_mcp_server
from agent_utilities.mcp.verbose_tools import register_tool_surface
from starlette.requests import Request
from starlette.responses import JSONResponse

from portainer_agent.api_client import PortainerApi
from portainer_agent.auth import get_client

__version__ = "2.1.0"

logger = get_logger(name="portainer-agent")
logger.setLevel(logging.INFO)


def wrap_list(res: Any) -> Any:
    return {"data": res} if isinstance(res, list) else res


def _none_if_field_info(value: Any) -> Any:
    """Normalize a raw pydantic FieldInfo default (seen when a tool coroutine
    is invoked directly -- e.g. in tests -- rather than through FastMCP) to
    None. Extracted verbatim from register_stack_tools.portainer_stack's
    former inline FieldInfo-cleanup block (CXA-FL-PORTAINERAGENT-01); no
    logic change."""
    from pydantic.fields import FieldInfo

    return None if isinstance(value, FieldInfo) else value


def _filtered_kwargs(**raw: Any) -> dict[str, Any]:
    """Build a kwargs dict from named values, dropping any that are None.

    Shared replacement for the flat dict-dispatch tables across the
    portainer_* tools (CX complexity-collapse, wD3-FL-06); equivalent to
    each tool's own former inline
    ``kwargs = {k: v for k, v in kwargs.items() if v is not None}`` filter
    -- no behavior change."""
    return {k: v for k, v in raw.items() if v is not None}


def _parse_stack_params_json(params_json: Any) -> dict:
    """Parse portainer_stack's ``params_json`` argument into a dict.

    Extracted verbatim from register_stack_tools.portainer_stack
    (CXA-FL-PORTAINERAGENT-01); no logic change."""
    import json

    if not params_json:
        return {}
    try:
        params = json.loads(params_json)
    except Exception as e:
        raise ValueError(f"Invalid params_json: {type(e).__name__}") from e
    return params if isinstance(params, dict) else {}


def _normalize_stack_action(action_normalized: str, get_val: Any) -> str:
    """Backward-compatible action-name routing for portainer_stack.

    Extracted verbatim from register_stack_tools.portainer_stack
    (CXA-FL-PORTAINERAGENT-01); no logic change."""
    if action_normalized == "create_standalone_stack":
        # Backward compatible check: if repo_url exists, route to repo
        url_val = get_val(["repo_url", "RepositoryURL", "repository_url"])
        if url_val:
            return "create_standalone_stack_from_repository"
        return "create_standalone_stack_from_string"
    if action_normalized == "create_standalone_stack_from_repo":
        return "create_standalone_stack_from_repository"
    return action_normalized


def _strip_explicit_stack_keys(resolved_kwargs: dict, explicit_keys: list) -> dict:
    """Remove explicitly-parsed parameter keys (and case variants) from
    portainer_stack's dynamic kwargs dict in place, so they aren't passed
    twice to the underlying client method. Extracted verbatim from
    register_stack_tools.portainer_stack (CXA-FL-PORTAINERAGENT-01); no
    logic change."""
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
    return resolved_kwargs


def _reinject_stack_env_prune(resolved_kwargs: dict, get_val: Any) -> dict:
    """Re-inject env/prune into portainer_stack's dynamic kwargs dict, if
    present, in place. Extracted verbatim from
    register_stack_tools.portainer_stack (CXA-FL-PORTAINERAGENT-01); no
    logic change."""
    env_val = get_val(["env", "Env"])
    if env_val is not None:
        resolved_kwargs["Env"] = env_val
    prune_val = get_val(["prune", "Prune"])
    if prune_val is not None:
        resolved_kwargs["Prune"] = prune_val
    return resolved_kwargs


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
        valid_actions = ("authenticate", "logout", "validate_oauth")
        resolved = resolve_action(action, valid_actions, service="portainer-agent")
        if isinstance(resolved, dict):
            return resolved
        action = resolved

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "authenticate": (
                client.authenticate,
                _filtered_kwargs(username=username, password=password),
            ),
            "logout": (client.logout, _filtered_kwargs()),
            "validate_oauth": (client.validate_oauth, _filtered_kwargs(code=code)),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: authenticate', 'logout', 'validate_oauth"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)


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

        # get_endpoint_settings / update_endpoint_settings don't follow the
        # flat filtered-kwargs shape below (settings is spread as **payload).
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

        # (method, kwargs, wrap_as_list) -- wrap_as_list mirrors the two
        # actions that formerly called wrap_list() on their result.
        specs: dict[str, tuple[Any, dict[str, Any], bool]] = {
            "get_endpoints": (
                client.get_endpoints,
                _filtered_kwargs(limit=limit, offset=offset),
                True,
            ),
            "get_endpoint": (
                client.get_endpoint,
                _filtered_kwargs(endpoint_id=endpoint_id),
                False,
            ),
            "create_endpoint": (
                client.create_endpoint,
                _filtered_kwargs(name=name, endpoint_type=endpoint_type, url=url),
                False,
            ),
            "update_endpoint": (
                client.update_endpoint,
                _filtered_kwargs(endpoint_id=endpoint_id),
                False,
            ),
            "delete_endpoint": (
                client.delete_endpoint,
                _filtered_kwargs(endpoint_id=endpoint_id),
                False,
            ),
            "snapshot_endpoint": (
                client.snapshot_endpoint,
                _filtered_kwargs(endpoint_id=endpoint_id),
                False,
            ),
            "snapshot_all_endpoints": (
                client.snapshot_all_endpoints,
                _filtered_kwargs(),
                False,
            ),
            "get_endpoint_groups": (
                client.get_endpoint_groups,
                _filtered_kwargs(),
                True,
            ),
            "create_endpoint_group": (
                client.create_endpoint_group,
                _filtered_kwargs(name=name, description=description),
                False,
            ),
            "delete_endpoint_group": (
                client.delete_endpoint_group,
                _filtered_kwargs(group_id=group_id),
                False,
            ),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group', 'get_endpoint_settings', 'update_endpoint_settings"
            )
        method, kwargs, as_list = specs[action]
        result = await run_blocking(method, **kwargs)
        return wrap_list(result) if as_list else result


def _handle_container_actions(
    client,
    action: str,
    environment_id: int | None,
    container_id: str | None,
    tail: int | None,
) -> dict:
    # (method, kwargs, wrap_as_data) -- wrap_as_data mirrors which branches
    # formerly returned {"data": client.X(**kwargs)} vs. the raw result.
    specs: dict[str, tuple[Any, dict[str, Any], bool]] = {
        "get_container_gpus": (
            client.get_container_gpus,
            _filtered_kwargs(environment_id=environment_id, container_id=container_id),
            False,
        ),
        "docker_list_containers": (
            client.list_containers,
            _filtered_kwargs(endpoint_id=environment_id),
            True,
        ),
        "docker_inspect_container": (
            client.inspect_container,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
        "docker_get_container_logs": (
            client.get_container_logs,
            _filtered_kwargs(
                endpoint_id=environment_id, container_id=container_id, tail=tail
            ),
            True,
        ),
        "docker_get_container_stats": (
            client.get_container_stats,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
        "docker_start_container": (
            client.start_container,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
        "docker_stop_container": (
            client.stop_container,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
        "docker_restart_container": (
            client.restart_container,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
        "docker_remove_container": (
            client.remove_container,
            _filtered_kwargs(endpoint_id=environment_id, container_id=container_id),
            True,
        ),
    }
    if action not in specs:
        raise ValueError(f"Unknown container action: {action}")
    method, kwargs, as_data = specs[action]
    result = method(**kwargs)
    return {"data": result} if as_data else result


def _handle_service_actions(
    client,
    action: str,
    environment_id: int | None,
    service_id: str | None,
    tail: int | None,
) -> dict:
    if action == "docker_list_services":
        res = client.list_services(**_filtered_kwargs(endpoint_id=environment_id))
        return {"data": res} if isinstance(res, list) else res

    specs: dict[str, tuple[Any, dict[str, Any]]] = {
        "docker_inspect_service": (
            client.inspect_service,
            _filtered_kwargs(endpoint_id=environment_id, service_id=service_id),
        ),
        "docker_get_service_logs": (
            client.get_service_logs,
            _filtered_kwargs(
                endpoint_id=environment_id, service_id=service_id, tail=tail
            ),
        ),
    }
    if action not in specs:
        raise ValueError(f"Unknown service action: {action}")
    method, kwargs = specs[action]
    return {"data": method(**kwargs)}


def _handle_resource_actions(
    client,
    action: str,
    environment_id: int | None,
) -> dict:
    if action == "get_docker_dashboard":
        return client.get_docker_dashboard(
            **_filtered_kwargs(environment_id=environment_id)
        )

    no_arg_methods: dict[str, Any] = {
        "docker_list_images": client.docker_list_images,
        "docker_inspect_image": client.docker_inspect_image,
        "docker_list_networks": client.docker_list_networks,
        "docker_inspect_network": client.docker_inspect_network,
        "docker_list_volumes": client.docker_list_volumes,
        "docker_inspect_volume": client.docker_inspect_volume,
        "docker_get_info": client.docker_get_info,
        "docker_get_version": client.docker_get_version,
        "docker_get_system_df": client.docker_get_system_df,
        "docker_create_container": client.docker_create_container,
        "docker_create_network": client.docker_create_network,
        "docker_create_volume": client.docker_create_volume,
    }
    if action not in no_arg_methods:
        raise ValueError(f"Unknown resource action: {action}")
    return no_arg_methods[action]()


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
    def _create_exec() -> dict:
        kwargs = _filtered_kwargs(endpoint_id=environment_id, container_id=container_id)
        kwargs["config"] = _filtered_kwargs(Cmd=cmd, Detach=detach, Tty=tty)
        return {"data": client.create_exec(**kwargs)}

    def _start_exec() -> dict:
        kwargs = _filtered_kwargs(endpoint_id=environment_id, exec_id=exec_id)
        kwargs["config"] = _filtered_kwargs(Detach=detach, Tty=tty)
        return {"data": client.start_exec(**kwargs)}

    def _inspect_exec() -> dict:
        kwargs = _filtered_kwargs(endpoint_id=environment_id, exec_id=exec_id)
        return {"data": client.inspect_exec(**kwargs)}

    def _get_stack_logs() -> dict:
        kwargs = _filtered_kwargs(endpoint_id=environment_id, stack_id=stack_id)
        res = client.get_stack_logs(**kwargs)
        return {"data": res} if isinstance(res, str) else res

    handlers: dict[str, Any] = {
        "docker_create_exec": _create_exec,
        "docker_start_exec": _start_exec,
        "docker_inspect_exec": _inspect_exec,
        "docker_get_stack_logs": _get_stack_logs,
    }
    handler = handlers.get(action)
    if handler is None:
        raise ValueError(f"Unknown exec/stack action: {action}")
    return handler()


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
        stack_id = _none_if_field_info(stack_id)
        endpoint_id = _none_if_field_info(endpoint_id)
        stack_file_content = _none_if_field_info(stack_file_content)
        env = _none_if_field_info(env)
        prune = _none_if_field_info(prune)
        name = _none_if_field_info(name)
        repo_url = _none_if_field_info(repo_url)
        swarm_id = _none_if_field_info(swarm_id)
        target_dir = _none_if_field_info(target_dir)
        params_json = _none_if_field_info(params_json)

        params = _parse_stack_params_json(params_json)

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
            # BUG-CX-033 fix (CX complexity-collapse, wD3-FL-06): target_dir
            # was accepted as a real Field(...) parameter but never added to
            # field_map, so get_val(["target_dir", "targetDir"]) could only
            # ever resolve it via params_json -- passing it as the named
            # tool parameter was silently ignored. See BUGS FOUND.
            "target_dir": target_dir,
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
        action_normalized = _normalize_stack_action(action_normalized, get_val)

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
        resolved_kwargs = _strip_explicit_stack_keys(resolved_kwargs, explicit_keys)

        # Re-inject env and prune if present
        resolved_kwargs = _reinject_stack_env_prune(resolved_kwargs, get_val)

        async def _get_stacks():
            res = await run_blocking(client.get_stacks, **resolved_kwargs)
            return {"data": res} if isinstance(res, list) else res

        async def _get_stack():
            s_id = get_val(["stack_id"])
            if s_id is None:
                raise ValueError("Missing parameter: stack_id")
            return await run_blocking(client.get_stack, stack_id=int(s_id))

        async def _get_stack_by_name():
            n = get_val(["name"])
            if not n:
                raise ValueError("Missing parameter: name")
            return await run_blocking(client.get_stack_by_name, name=str(n))

        async def _get_stack_file():
            s_id = get_val(["stack_id"])
            if s_id is None:
                raise ValueError("Missing parameter: stack_id")
            return await run_blocking(client.get_stack_file, stack_id=int(s_id))

        async def _create_standalone_stack_from_string():
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

        async def _create_standalone_stack_from_repository():
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

        async def _create_swarm_stack_from_string():
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

        async def _create_swarm_stack_from_repository():
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

        async def _create_kubernetes_stack_from_string():
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

        async def _create_kubernetes_stack_from_repository():
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

        async def _update_stack():
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

        async def _delete_stack():
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for delete_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.delete_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        async def _start_stack():
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for start_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.start_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        async def _stop_stack():
            s_id = get_val(["stack_id"])
            ep_id = get_val(["endpoint_id", "endpointId"])
            if s_id is None or ep_id is None:
                raise ValueError(
                    "Missing required parameters for stop_stack: stack_id, endpoint_id"
                )
            return await run_blocking(
                client.stop_stack, stack_id=int(s_id), endpoint_id=int(ep_id)
            )

        async def _migrate_stack():
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

        async def _update_stack_git():
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

        async def _redeploy_stack_git():
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

        async def _associate_stack():
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

        async def _export_all_stacks():
            t_dir = get_val(["target_dir", "targetDir"])
            if not t_dir:
                raise ValueError(
                    "Missing required parameter for export_all_stacks: target_dir"
                )
            return await run_blocking(client.export_all_stacks, target_dir=str(t_dir))

        handlers: dict[str, Any] = {
            "get_stacks": _get_stacks,
            "get_stack": _get_stack,
            "get_stack_by_name": _get_stack_by_name,
            "get_stack_file": _get_stack_file,
            "create_standalone_stack_from_string": _create_standalone_stack_from_string,
            "create_standalone_stack_from_repository": _create_standalone_stack_from_repository,
            "create_swarm_stack_from_string": _create_swarm_stack_from_string,
            "create_swarm_stack_from_repository": _create_swarm_stack_from_repository,
            "create_kubernetes_stack_from_string": _create_kubernetes_stack_from_string,
            "create_kubernetes_stack_from_repository": _create_kubernetes_stack_from_repository,
            "update_stack": _update_stack,
            "delete_stack": _delete_stack,
            "start_stack": _start_stack,
            "stop_stack": _stop_stack,
            "migrate_stack": _migrate_stack,
            "update_stack_git": _update_stack_git,
            "redeploy_stack_git": _redeploy_stack_git,
            "associate_stack": _associate_stack,
            "export_all_stacks": _export_all_stacks,
        }

        handler = handlers.get(action_normalized)
        if handler is not None:
            return await handler()

        # Unreachable in practice: resolve_action() above already guarantees
        # action_normalized is either a valid_actions member (handled by one
        # of the branches in `handlers`) or has already raised. Kept verbatim
        # as dead-code fallback -- see BUGS FOUND (not fixed, behavior-preserving).
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

        # BUG-CX-036 fix (CX complexity-collapse, wD3-FL-06): normalize raw
        # pydantic FieldInfo defaults to None. Unlike portainer_stack, this
        # function had no FieldInfo-cleanup block, so calling the coroutine
        # directly (bypassing FastMCP's own default resolution -- e.g. from
        # a test) with a parameter omitted left the raw Field(...) object in
        # place; Group 2's "filter out None" step does not catch it (a
        # FieldInfo is not None), and Group 3 never filters at all, so the
        # FieldInfo reached the client call as the argument value instead of
        # None. See BUGS FOUND / tests/test_portainer_kubernetes_characterization.py.
        endpoint_id = _none_if_field_info(endpoint_id)
        chart_name = _none_if_field_info(chart_name)
        release_name = _none_if_field_info(release_name)
        environment_id = _none_if_field_info(environment_id)
        namespace = _none_if_field_info(namespace)
        node_name = _none_if_field_info(node_name)

        # Group 1: no-argument passthrough reads -- kwargs is always {} (an
        # empty dict filtered by "v is not None" is still {}).
        no_arg_methods = {
            "get_k8s_dashboard": client.get_k8s_dashboard,
            "get_k8s_namespaces": client.get_k8s_namespaces,
            "get_k8s_applications": client.get_k8s_applications,
            "get_k8s_services": client.get_k8s_services,
            "get_k8s_ingresses": client.get_k8s_ingresses,
            "get_k8s_configmaps": client.get_k8s_configmaps,
            "get_k8s_secrets": client.get_k8s_secrets,
            "get_k8s_volumes": client.get_k8s_volumes,
            "get_k8s_events": client.get_k8s_events,
            "get_k8s_nodes_limits": client.get_k8s_nodes_limits,
            "get_k8s_metrics_nodes": client.get_k8s_metrics_nodes,
        }
        if action in no_arg_methods:
            return await run_blocking(no_arg_methods[action])

        # Group 2: helm actions -- kwargs built from named params, then
        # None-valued entries are filtered out before the call.
        filtered_specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_helm_releases": (
                client.get_helm_releases,
                {"endpoint_id": endpoint_id},
            ),
            "install_helm_chart": (
                client.install_helm_chart,
                {"endpoint_id": endpoint_id, "chart_name": chart_name},
            ),
            "delete_helm_release": (
                client.delete_helm_release,
                {"endpoint_id": endpoint_id, "release_name": release_name},
            ),
        }
        if action in filtered_specs:
            method, kwargs = filtered_specs[action]
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(method, **kwargs)

        # Group 3: namespace/node management -- params passed straight
        # through to the client WITHOUT None-filtering (unlike groups 1/2).
        direct_specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_k8s_namespace": (
                client.get_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "create_k8s_namespace": (
                client.create_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "update_k8s_namespace": (
                client.update_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "delete_k8s_namespace": (
                client.delete_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "get_k8s_namespace_count": (
                client.get_kubernetes_namespace_count,
                {"environment_id": environment_id},
            ),
            "drain_k8s_node": (
                client.drain_kubernetes_node,
                {"environment_id": environment_id, "node_name": node_name},
            ),
            "describe_k8s_resource": (
                client.describe_kubernetes_resource,
                {"environment_id": environment_id},
            ),
            "get_k8s_rbac_enabled": (
                client.get_kubernetes_rbac_enabled,
                {"environment_id": environment_id},
            ),
        }
        if action in direct_specs:
            method, kwargs = direct_specs[action]
            return await run_blocking(method, **kwargs)

        # Unreachable in practice: resolve_action() above already guarantees
        # action is either a valid_actions member (handled by one of the
        # three dispatch dicts above) or has already raised. Kept verbatim
        # as dead-code fallback -- see BUGS FOUND (not fixed,
        # behavior-preserving).
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

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_edge_groups": (client.get_edge_groups, _filtered_kwargs()),
            "create_edge_group": (
                client.create_edge_group,
                _filtered_kwargs(name=name),
            ),
            "delete_edge_group": (
                client.delete_edge_group,
                _filtered_kwargs(group_id=group_id),
            ),
            "get_edge_stacks": (client.get_edge_stacks, _filtered_kwargs()),
            "get_edge_stack": (
                client.get_edge_stack,
                _filtered_kwargs(stack_id=stack_id),
            ),
            "create_edge_stack": (client.create_edge_stack, _filtered_kwargs()),
            "delete_edge_stack": (
                client.delete_edge_stack,
                _filtered_kwargs(stack_id=stack_id),
            ),
            "get_edge_jobs": (client.get_edge_jobs, _filtered_kwargs()),
            "get_edge_job": (client.get_edge_job, _filtered_kwargs(job_id=job_id)),
            "create_edge_job": (client.create_edge_job, _filtered_kwargs()),
            "delete_edge_job": (
                client.delete_edge_job,
                _filtered_kwargs(job_id=job_id),
            ),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)


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

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_templates": (client.get_templates, _filtered_kwargs()),
            "get_custom_templates": (
                client.get_custom_templates,
                _filtered_kwargs(),
            ),
            "get_custom_template": (
                client.get_custom_template,
                _filtered_kwargs(template_id=template_id),
            ),
            "create_custom_template": (
                client.create_custom_template,
                _filtered_kwargs(),
            ),
            "delete_custom_template": (
                client.delete_custom_template,
                _filtered_kwargs(template_id=template_id),
            ),
            "get_custom_template_file": (
                client.get_custom_template_file,
                _filtered_kwargs(template_id=template_id),
            ),
            "get_helm_templates": (client.get_helm_templates, _filtered_kwargs()),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)


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

        # Git-credential actions: kept as closures (unlike the flat group
        # below) because each builds its kwargs differently -- some pass
        # user_id/credential_id straight through unfiltered, one only
        # conditionally adds authorization_type. Preserved verbatim.
        async def _get_user_git_credentials():
            return await run_blocking(client.get_user_git_credentials, user_id=user_id)

        async def _get_user_git_credential():
            return await run_blocking(
                client.get_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
            )

        async def _create_user_git_credential():
            kwargs: dict[str, Any] = {
                "user_id": user_id,
                "name": name,
                "username": username,
                "password": password,
            }
            if authorization_type is not None:
                kwargs["authorization_type"] = authorization_type
            return await run_blocking(client.create_user_git_credential, **kwargs)

        async def _update_user_git_credential():
            kwargs = _filtered_kwargs(name=name, username=username, password=password)
            return await run_blocking(
                client.update_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
                **kwargs,
            )

        async def _delete_user_git_credential():
            return await run_blocking(
                client.delete_user_git_credential,
                user_id=user_id,
                credential_id=credential_id,
            )

        git_credential_handlers: dict[str, Any] = {
            "get_user_git_credentials": _get_user_git_credentials,
            "get_user_git_credential": _get_user_git_credential,
            "create_user_git_credential": _create_user_git_credential,
            "update_user_git_credential": _update_user_git_credential,
            "delete_user_git_credential": _delete_user_git_credential,
        }
        if action in git_credential_handlers:
            return await git_credential_handlers[action]()

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_users": (client.get_users, _filtered_kwargs()),
            "get_user": (client.get_user, _filtered_kwargs(user_id=user_id)),
            "get_current_user": (client.get_current_user, _filtered_kwargs()),
            "create_user": (
                client.create_user,
                _filtered_kwargs(username=username, password=password, role=role),
            ),
            "delete_user": (client.delete_user, _filtered_kwargs(user_id=user_id)),
            "get_teams": (client.get_teams, _filtered_kwargs()),
            "create_team": (client.create_team, _filtered_kwargs(name=name)),
            "delete_team": (client.delete_team, _filtered_kwargs(team_id=team_id)),
            "get_roles": (client.get_roles, _filtered_kwargs()),
            "get_user_tokens": (
                client.get_user_tokens,
                _filtered_kwargs(user_id=user_id),
            ),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_users', 'get_user', 'get_current_user', 'create_user', 'delete_user', 'get_teams', 'create_team', 'delete_team', 'get_roles', 'get_user_tokens"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)


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

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_registries": (client.get_registries, _filtered_kwargs()),
            "get_registry": (
                client.get_registry,
                _filtered_kwargs(registry_id=registry_id),
            ),
            "create_registry": (
                client.create_registry,
                _filtered_kwargs(name=name, registry_type=registry_type, url=url),
            ),
            "delete_registry": (
                client.delete_registry,
                _filtered_kwargs(registry_id=registry_id),
            ),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_registries', 'get_registry', 'create_registry', 'delete_registry"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)


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

        specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_status": (client.get_status, _filtered_kwargs()),
            "get_system_info": (client.get_system_info, _filtered_kwargs()),
            "get_system_version": (client.get_system_version, _filtered_kwargs()),
            "get_settings": (client.get_settings, _filtered_kwargs()),
            "update_settings": (client.update_settings, _filtered_kwargs()),
            "get_tags": (client.get_tags, _filtered_kwargs()),
            "create_tag": (client.create_tag, _filtered_kwargs(name=name)),
            "delete_tag": (client.delete_tag, _filtered_kwargs(tag_id=tag_id)),
            "get_motd": (client.get_motd, _filtered_kwargs()),
            "backup_portainer": (client.backup_portainer, _filtered_kwargs()),
        }
        if action not in specs:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer"
            )
        method, kwargs = specs[action]
        return await run_blocking(method, **kwargs)

    @mcp.tool(tags={"System", "kg"})
    async def portainer_ingest_environments(
        include_stacks: bool = Field(
            default=True,
            description="Also list and ingest all stacks and link them to their environments.",
        ),
        client=Depends(get_client),
    ) -> dict:
        """Natively ingest Portainer environments (+ stacks) into epistemic-graph.

        Lists endpoints via the Portainer API and pushes them as typed ``:Environment``
        nodes (with ``:EndpointGroup`` + ``:partOfEndpointGroup`` links); when
        ``include_stacks`` is set, also pushes ``:Stack`` nodes linked ``:inEnvironment``.
        Best-effort: ``ingested`` is ``None`` when no engine is reachable.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        from portainer_agent.kg_ingest import ingest_environments, ingest_stacks

        def _records(res: Any) -> list[dict]:
            data = res.get("data", res) if isinstance(res, dict) else res
            data = data if isinstance(data, list) else [data]
            return [
                r.model_dump() if hasattr(r, "model_dump") else r
                for r in data
                if isinstance(r, dict) or hasattr(r, "model_dump")
            ]

        endpoints = _records(await run_blocking(client.get_endpoints))
        env_result = ingest_environments(endpoints)
        out: dict[str, Any] = {
            "environments_listed": len(endpoints),
            "environments_ingested": env_result,
        }
        if include_stacks:
            stacks = _records(await run_blocking(client.get_stacks))
            out["stacks_listed"] = len(stacks)
            out["stacks_ingested"] = ingest_stacks(stacks)
        return out

    @mcp.tool(tags={"System", "kg"})
    async def portainer_ingest_containers(
        environment_id: int = Field(
            description="Environment (endpoint) id to list containers in."
        ),
        client=Depends(get_client),
    ) -> dict:
        """Natively ingest an environment's Docker containers into epistemic-graph.

        Lists containers in ``environment_id`` and pushes them as typed ``:Container``
        nodes linked ``:inEnvironment`` (and ``:deployedByStack`` where a compose/stack
        label is present). Best-effort: ``ingested`` is ``None`` with no reachable engine.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        from portainer_agent.kg_ingest import ingest_containers

        res = await run_blocking(client.list_containers, endpoint_id=environment_id)
        data = res.get("data", res) if isinstance(res, dict) else res
        records = data if isinstance(data, list) else [data]
        containers = [
            r.model_dump() if hasattr(r, "model_dump") else r
            for r in records
            if isinstance(r, dict) or hasattr(r, "model_dump")
        ]
        result = ingest_containers(containers, environment_id)
        return {"listed": len(containers), "ingested": result}


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
