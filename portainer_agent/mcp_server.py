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
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

from portainer_agent.auth import get_client

__version__ = "0.11.1"

logger = get_logger(name="portainer-agent")
logger.setLevel(logging.INFO)


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
        if action == "authenticate":
            kwargs = {"username": username, "password": password}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.authenticate(**kwargs)
        if action == "logout":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.logout(**kwargs)
        if action == "validate_oauth":
            kwargs = {"code": code}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validate_oauth(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: authenticate', 'logout', 'validate_oauth"
        )


def register_environment_tools(mcp: FastMCP):
    @mcp.tool(tags={"Environment"})
    async def portainer_environment(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        name: str | None = Field(default=None, description="name"),
        endpoint_type: int | None = Field(default=None, description="endpoint type"),
        url: str | None = Field(default=None, description="url"),
        description: str | None = Field(default=None, description="description"),
        group_id: int | None = Field(default=None, description="group id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage environment operations."""
        kwargs: dict[str, Any]
        if action == "get_endpoints":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_endpoints(**kwargs)
        if action == "get_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_endpoint(**kwargs)
        if action == "create_endpoint":
            kwargs = {
                "name": name,
                "endpoint_type": endpoint_type,
                "url": url,
            }  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_endpoint(**kwargs)
        if action == "update_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_endpoint(**kwargs)
        if action == "delete_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_endpoint(**kwargs)
        if action == "snapshot_endpoint":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.snapshot_endpoint(**kwargs)
        if action == "snapshot_all_endpoints":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.snapshot_all_endpoints(**kwargs)
        if action == "get_endpoint_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_endpoint_groups(**kwargs)
        if action == "create_endpoint_group":
            kwargs = {"name": name, "description": description}  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_endpoint_group(**kwargs)
        if action == "delete_endpoint_group":
            kwargs = {"group_id": group_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_endpoint_group(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group"
        )


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
        if environment_id is None and endpoint_id is not None:
            environment_id = endpoint_id

        kwargs: dict[str, Any]
        if action == "get_docker_dashboard":
            kwargs = {"environment_id": environment_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_docker_dashboard(**kwargs)
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
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_docker_dashboard', 'get_container_gpus', 'docker_list_containers', 'docker_inspect_container', 'docker_get_container_logs', 'docker_get_container_stats', 'docker_start_container', 'docker_stop_container', 'docker_restart_container', 'docker_remove_container', 'docker_list_services', 'docker_inspect_service', 'docker_get_service_logs', 'docker_list_images', 'docker_inspect_image', 'docker_list_networks', 'docker_inspect_network', 'docker_list_volumes', 'docker_inspect_volume', 'docker_get_info', 'docker_get_version', 'docker_get_system_df', 'docker_create_container', 'docker_create_network', 'docker_create_volume', 'docker_create_exec', 'docker_start_exec', 'docker_inspect_exec', 'docker_get_stack_logs"
        )


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(tags={"Stack"})
    async def portainer_stack(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'redeploy_stack_git'"
        ),
        stack_id: int | None = Field(default=None, description="stack id"),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        stack_file_content: str | None = Field(
            default=None, description="compose file content for update_stack"
        ),
        env: list | None = Field(
            default=None, description="environment variables list for update_stack"
        ),
        prune: bool | None = Field(
            default=None, description="whether to prune for update_stack"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage stack operations."""
        kwargs: dict[str, Any]
        if action == "get_stacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            res = client.get_stacks(**kwargs)
            return {"data": res} if isinstance(res, list) else res
        if action == "get_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_stack(**kwargs)
        if action == "get_stack_file":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_stack_file(**kwargs)
        if action == "create_standalone_stack":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_standalone_stack(**kwargs)
        if action == "create_standalone_stack_from_repo":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_standalone_stack_from_repo(**kwargs)
        if action == "update_stack":
            kwargs = {
                "stack_id": stack_id,
                "endpoint_id": endpoint_id,
                "StackFileContent": stack_file_content,
                "Env": env,
                "Prune": prune,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_stack(**kwargs)
        if action == "delete_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_stack(**kwargs)
        if action == "start_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.start_stack(**kwargs)
        if action == "stop_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.stop_stack(**kwargs)
        if action == "redeploy_stack_git":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.redeploy_stack_git(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'redeploy_stack_git"
        )


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(tags={"Kubernetes"})
    async def portainer_kubernetes(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release'"
        ),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        chart_name: str | None = Field(default=None, description="chart name"),
        release_name: str | None = Field(default=None, description="release name"),
        client=Depends(get_client),
    ) -> dict:
        """Manage kubernetes operations."""
        kwargs: dict[str, Any]
        if action == "get_k8s_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_dashboard(**kwargs)
        if action == "get_k8s_namespaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_namespaces(**kwargs)
        if action == "get_k8s_applications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_applications(**kwargs)
        if action == "get_k8s_services":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_services(**kwargs)
        if action == "get_k8s_ingresses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_ingresses(**kwargs)
        if action == "get_k8s_configmaps":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_configmaps(**kwargs)
        if action == "get_k8s_secrets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_secrets(**kwargs)
        if action == "get_k8s_volumes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_volumes(**kwargs)
        if action == "get_k8s_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_events(**kwargs)
        if action == "get_k8s_nodes_limits":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_nodes_limits(**kwargs)
        if action == "get_k8s_metrics_nodes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_metrics_nodes(**kwargs)
        if action == "get_helm_releases":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_helm_releases(**kwargs)
        if action == "install_helm_chart":
            kwargs = {
                "endpoint_id": endpoint_id,
                "chart_name": chart_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.install_helm_chart(**kwargs)
        if action == "delete_helm_release":
            kwargs = {
                "endpoint_id": endpoint_id,
                "release_name": release_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_helm_release(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release"
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
        if action == "get_edge_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_groups(**kwargs)
        if action == "create_edge_group":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_group(**kwargs)
        if action == "delete_edge_group":
            kwargs = {"group_id": group_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_group(**kwargs)
        if action == "get_edge_stacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_stacks(**kwargs)
        if action == "get_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_stack(**kwargs)
        if action == "create_edge_stack":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_stack(**kwargs)
        if action == "delete_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_stack(**kwargs)
        if action == "get_edge_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_jobs(**kwargs)
        if action == "get_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_job(**kwargs)
        if action == "create_edge_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_job(**kwargs)
        if action == "delete_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_job(**kwargs)
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
        if action == "get_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_templates(**kwargs)
        if action == "get_custom_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_templates(**kwargs)
        if action == "get_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_template(**kwargs)
        if action == "create_custom_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_custom_template(**kwargs)
        if action == "delete_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_custom_template(**kwargs)
        if action == "get_custom_template_file":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_template_file(**kwargs)
        if action == "get_helm_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_helm_templates(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates"
        )


def register_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"User"})
    async def portainer_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_users', 'get_user', 'get_current_user', 'create_user', 'delete_user', 'get_teams', 'create_team', 'delete_team', 'get_roles', 'get_user_tokens'"
        ),
        user_id: int | None = Field(default=None, description="user id"),
        username: str | None = Field(default=None, description="username"),
        password: str | None = Field(default=None, description="password"),
        role: int | None = Field(default=None, description="role"),
        name: str | None = Field(default=None, description="name"),
        team_id: int | None = Field(default=None, description="team id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage user operations."""
        kwargs: dict[str, Any]
        if action == "get_users":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_users(**kwargs)
        if action == "get_user":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user(**kwargs)
        if action == "get_current_user":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_current_user(**kwargs)
        if action == "create_user":
            kwargs = {
                "username": username,
                "password": password,
                "role": role,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_user(**kwargs)
        if action == "delete_user":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_user(**kwargs)
        if action == "get_teams":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_teams(**kwargs)
        if action == "create_team":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_team(**kwargs)
        if action == "delete_team":
            kwargs = {"team_id": team_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_team(**kwargs)
        if action == "get_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_roles(**kwargs)
        if action == "get_user_tokens":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_tokens(**kwargs)
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
        if action == "get_registries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_registries(**kwargs)
        if action == "get_registry":
            kwargs = {"registry_id": registry_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_registry(**kwargs)
        if action == "create_registry":
            kwargs = {
                "name": name,
                "registry_type": registry_type,
                "url": url,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_registry(**kwargs)
        if action == "delete_registry":
            kwargs = {"registry_id": registry_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_registry(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_registries', 'get_registry', 'create_registry', 'delete_registry"
        )


def register_system_tools(mcp: FastMCP):
    @mcp.tool(tags={"System"})
    async def portainer_system(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer'"
        ),
        name: str | None = Field(default=None, description="name"),
        tag_id: int | None = Field(default=None, description="tag id"),
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
        """
        kwargs: dict[str, Any]
        if action == "get_status":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_status(**kwargs)
        if action == "get_system_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_system_info(**kwargs)
        if action == "get_system_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_system_version(**kwargs)
        if action == "get_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_settings(**kwargs)
        if action == "update_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_settings(**kwargs)
        if action == "get_tags":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_tags(**kwargs)
        if action == "create_tag":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_tag(**kwargs)
        if action == "delete_tag":
            kwargs = {"tag_id": tag_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_tag(**kwargs)
        if action == "get_motd":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_motd(**kwargs)
        if action == "backup_portainer":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.backup_portainer(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer"
        )


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="portainer-agent MCP",
        version=__version__,
        instructions="portainer-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_AUTHTOOL = to_boolean(os.getenv("AUTHTOOL", "True"))
    if DEFAULT_AUTHTOOL:
        register_auth_tools(mcp)
    DEFAULT_ENVIRONMENTTOOL = to_boolean(os.getenv("ENVIRONMENTTOOL", "True"))
    if DEFAULT_ENVIRONMENTTOOL:
        register_environment_tools(mcp)
    DEFAULT_DOCKERTOOL = to_boolean(os.getenv("DOCKERTOOL", "True"))
    if DEFAULT_DOCKERTOOL:
        register_docker_tools(mcp)
    DEFAULT_STACKTOOL = to_boolean(os.getenv("STACKTOOL", "True"))
    if DEFAULT_STACKTOOL:
        register_stack_tools(mcp)
    DEFAULT_KUBERNETESTOOL = to_boolean(os.getenv("KUBERNETESTOOL", "True"))
    if DEFAULT_KUBERNETESTOOL:
        register_kubernetes_tools(mcp)
    DEFAULT_EDGETOOL = to_boolean(os.getenv("EDGETOOL", "True"))
    if DEFAULT_EDGETOOL:
        register_edge_tools(mcp)
    DEFAULT_TEMPLATETOOL = to_boolean(os.getenv("TEMPLATETOOL", "True"))
    if DEFAULT_TEMPLATETOOL:
        register_template_tools(mcp)
    DEFAULT_USERTOOL = to_boolean(os.getenv("USERTOOL", "True"))
    if DEFAULT_USERTOOL:
        register_user_tools(mcp)
    DEFAULT_REGISTRYTOOL = to_boolean(os.getenv("REGISTRYTOOL", "True"))
    if DEFAULT_REGISTRYTOOL:
        register_registry_tools(mcp)
    DEFAULT_SYSTEMTOOL = to_boolean(os.getenv("SYSTEMTOOL", "True"))
    if DEFAULT_SYSTEMTOOL:
        register_system_tools(mcp)

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
