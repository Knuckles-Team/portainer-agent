"""MCP tools for docker operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from agent_utilities.mcp_utilities import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp_server import (
    _handle_container_actions,
    _handle_exec_stack_actions,
    _handle_resource_actions,
    _handle_service_actions,
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
