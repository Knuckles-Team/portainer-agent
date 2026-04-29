#!/usr/bin/python
import warnings

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

# General urllib3/chardet mismatch warnings
warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import warnings

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
import logging
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import (
    create_mcp_server,
    ctx_confirm_destructive,
    ctx_progress,
    ctx_set_state,
)
from dotenv import find_dotenv, load_dotenv
from fastmcp import Context, FastMCP
from fastmcp.utilities.logging import get_logger
from pydantic import Field

from portainer_agent.auth import get_client

__version__ = "0.1.29"


logger = get_logger(name="TokenMiddleware")
logger.setLevel(logging.DEBUG)


def register_prompts(mcp: FastMCP):
    @mcp.prompt(
        name="deploy_stack",
        description="Deploy a new Docker Compose stack to a Portainer environment.",
    )
    def deploy_stack_prompt(stack_name: str, environment: str = "local") -> str:
        """Generate a deploy stack prompt."""
        return f"Deploy a new stack named '{stack_name}' to the '{environment}' environment. Use the Portainer tools to list environments, then create the stack."

    @mcp.prompt(
        name="environment_health",
        description="Check the health and status of all Portainer environments.",
    )
    def environment_health_prompt() -> str:
        """Generate an environment health check prompt."""
        return "Check the health of all Portainer environments. List all endpoints, check their status, and report any issues."


def register_auth_tools(mcp: FastMCP):
    @mcp.tool(
        name="authenticate",
        description="Authenticate against Portainer with username and password to get a JWT token.",
        tags={"Auth"},
    )
    async def authenticate_tool(
        username: str = Field(description="Username."),
        password: str = Field(description="Password."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Authenticate."""
        result = get_client().authenticate(username=username, password=password)
        await ctx_set_state(
            ctx,
            "portainer",
            "auth_token",
            result.get("jwt") if isinstance(result, dict) else None,
        )
        return result

    @mcp.tool(
        name="logout",
        description="Logout and invalidate the current authentication token.",
        tags={"Auth"},
    )
    async def logout_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Logout."""
        if not await ctx_confirm_destructive(ctx, "logout"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().logout()

    @mcp.tool(
        name="validate_oauth",
        description="Validate an OAuth authorization code.",
        tags={"Auth"},
    )
    def validate_oauth_tool(
        code: str = Field(description="OAuth code."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Validate OAuth."""
        return get_client().validate_oauth(code=code)


def register_environment_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_endpoints",
        description="List all Portainer environments (endpoints). Each environment represents a Docker host, Swarm cluster, or Kubernetes cluster.",
        tags={"Environment"},
    )
    def get_endpoints_tool(
        limit: int | None = Field(default=None, description="Max results."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List environments."""
        return get_client().get_endpoints(limit=limit, offset=offset)

    @mcp.tool(
        name="get_endpoint",
        description="Get details of a specific environment (endpoint) by ID.",
        tags={"Environment"},
    )
    def get_endpoint_tool(
        endpoint_id: int = Field(description="Environment/endpoint ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get environment."""
        return get_client().get_endpoint(endpoint_id)

    @mcp.tool(
        name="create_endpoint",
        description="Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes.",
        tags={"Environment"},
    )
    def create_endpoint_tool(
        name: str = Field(description="Environment name."),
        endpoint_type: int = Field(description="Environment type (1-7)."),
        url: str = Field(default="", description="URL of the Docker/Kubernetes host."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create environment."""
        return get_client().create_endpoint(
            name=name, endpoint_type=endpoint_type, url=url
        )

    @mcp.tool(
        name="update_endpoint",
        description="Update an existing environment's configuration.",
        tags={"Environment"},
    )
    def update_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID."),
        name: str | None = Field(default=None, description="New name."),
        url: str | None = Field(default=None, description="New URL."),
        public_url: str | None = Field(default=None, description="Public URL."),
        group_id: int | None = Field(default=None, description="Group ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Update environment."""
        kwargs: dict[str, Any] = {}
        if name:
            kwargs["Name"] = name
        if url:
            kwargs["URL"] = url
        if public_url:
            kwargs["PublicURL"] = public_url
        if group_id is not None:
            kwargs["GroupID"] = group_id
        return get_client().update_endpoint(endpoint_id, **kwargs)

    @mcp.tool(
        name="delete_endpoint",
        description="Delete an environment (endpoint).",
        tags={"Environment"},
    )
    async def delete_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID to delete."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete environment."""
        if not await ctx_confirm_destructive(ctx, "delete endpoint"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_endpoint(endpoint_id)

    @mcp.tool(
        name="snapshot_endpoint",
        description="Take a snapshot of an environment to refresh its state.",
        tags={"Environment"},
    )
    def snapshot_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Snapshot environment."""
        return get_client().snapshot_endpoint(endpoint_id)

    @mcp.tool(
        name="snapshot_all_endpoints",
        description="Take a snapshot of all environments.",
        tags={"Environment"},
    )
    def snapshot_all_endpoints_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Snapshot all environments."""
        return get_client().snapshot_all_endpoints()

    @mcp.tool(
        name="get_endpoint_groups",
        description="List all environment groups.",
        tags={"Environment"},
    )
    def get_endpoint_groups_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List groups."""
        return get_client().get_endpoint_groups()

    @mcp.tool(
        name="create_endpoint_group",
        description="Create a new environment group.",
        tags={"Environment"},
    )
    def create_endpoint_group_tool(
        name: str = Field(description="Group name."),
        description: str = Field(default="", description="Group description."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create group."""
        return get_client().create_endpoint_group(name=name, description=description)

    @mcp.tool(
        name="delete_endpoint_group",
        description="Delete an environment group.",
        tags={"Environment"},
    )
    async def delete_endpoint_group_tool(
        group_id: int = Field(description="Group ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete group."""
        if not await ctx_confirm_destructive(ctx, "delete endpoint group"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_endpoint_group(group_id)


def register_docker_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_docker_dashboard",
        description="Get Docker dashboard data (containers, images, volumes, networks summary) for an environment.",
        tags={"Docker"},
    )
    def get_docker_dashboard_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get Docker dashboard."""
        return get_client().get_docker_dashboard(environment_id)

    @mcp.tool(
        name="get_container_gpus",
        description="Get GPU information for a Docker container.",
        tags={"Docker"},
    )
    def get_container_gpus_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get container GPUs."""
        return get_client().get_container_gpus(environment_id, container_id)

    @mcp.tool(
        name="docker_list_containers",
        description="List containers in a Docker environment.",
        tags={"Docker"},
    )
    def docker_list_containers_tool(
        environment_id: int = Field(description="Environment ID."),
        all_containers: bool = Field(
            default=False,
            alias="all",
            description="Show all containers (default shows just running).",
        ),
        limit: int | None = Field(
            default=None,
            description="Return this number of most recently created containers.",
        ),
        filters: str | None = Field(
            default=None,
            description="A JSON encoded value of the filters to process on the containers list.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List containers."""
        params: dict[str, Any] = {"all": all_containers}
        if limit:
            params["limit"] = limit
        if filters:
            params["filters"] = filters
        return get_client().list_containers(environment_id, **params)

    @mcp.tool(
        name="docker_inspect_container",
        description="Return low-level information about a container.",
        tags={"Docker"},
    )
    def docker_inspect_container_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect container."""
        return get_client().inspect_container(environment_id, container_id)

    @mcp.tool(
        name="docker_get_container_logs",
        description="Get stdout and stderr logs from a container.",
        tags={"Docker"},
    )
    def docker_get_container_logs_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        tail: str = Field(
            default="all",
            description="Output specified number of lines at the end of logs.",
        ),
        since: int | None = Field(
            default=None,
            description="Only return logs since this time, as a UNIX timestamp.",
        ),
        timestamps: bool = Field(default=True, description="Show timestamps in logs."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get container logs."""
        params = {"tail": tail, "timestamps": timestamps}
        if since:
            params["since"] = since
        return get_client().get_container_logs(environment_id, container_id, **params)

    @mcp.tool(
        name="docker_get_container_stats",
        description="Get resource usage statistics for a container.",
        tags={"Docker"},
    )
    def docker_get_container_stats_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get container stats."""
        return get_client().get_container_stats(environment_id, container_id)

    @mcp.tool(
        name="docker_start_container",
        description="Start a container.",
        tags={"Docker"},
    )
    def docker_start_container_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Start container."""
        return get_client().start_container(environment_id, container_id)

    @mcp.tool(
        name="docker_stop_container",
        description="Stop a container.",
        tags={"Docker"},
    )
    async def docker_stop_container_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        timeout: int | None = Field(
            default=None,
            description="Number of seconds to wait before killing the container.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Stop container."""
        if not await ctx_confirm_destructive(ctx, "docker stop container"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().stop_container(
            environment_id, container_id, timeout=timeout
        )

    @mcp.tool(
        name="docker_restart_container",
        description="Restart a container.",
        tags={"Docker"},
    )
    async def docker_restart_container_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        timeout: int | None = Field(
            default=None,
            description="Number of seconds to wait before killing the container.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Restart container."""
        if not await ctx_confirm_destructive(ctx, "docker restart container"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().restart_container(
            environment_id, container_id, timeout=timeout
        )

    @mcp.tool(
        name="docker_remove_container",
        description="Remove a container.",
        tags={"Docker"},
    )
    async def docker_remove_container_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        v: bool = Field(
            default=False,
            description="Remove the volumes associated with the container.",
        ),
        force: bool = Field(
            default=False,
            description="If the container is running, kill it before removing it.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Remove container."""
        if not await ctx_confirm_destructive(ctx, "docker remove container"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().remove_container(
            environment_id, container_id, v=v, force=force
        )

    @mcp.tool(
        name="docker_list_services",
        description="List Swarm services in a Docker environment.",
        tags={"Docker"},
    )
    def docker_list_services_tool(
        environment_id: int = Field(description="Environment ID."),
        filters: str | None = Field(
            default=None,
            description="A JSON encoded value of the filters to process on the services list.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List services."""
        params: dict[str, Any] = {}
        if filters:
            params["filters"] = filters
        return get_client().list_services(environment_id, **params)

    @mcp.tool(
        name="docker_inspect_service",
        description="Return low-level information about a Swarm service.",
        tags={"Docker"},
    )
    def docker_inspect_service_tool(
        environment_id: int = Field(description="Environment ID."),
        service_id: str = Field(description="Service ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect service."""
        return get_client().inspect_service(environment_id, service_id)

    @mcp.tool(
        name="docker_get_service_logs",
        description="Get stdout and stderr logs from a Swarm service.",
        tags={"Docker"},
    )
    def docker_get_service_logs_tool(
        environment_id: int = Field(description="Environment ID."),
        service_id: str = Field(description="Service ID or name."),
        tail: str = Field(
            default="all",
            description="Output specified number of lines at the end of logs.",
        ),
        since: int | None = Field(
            default=None,
            description="Only return logs since this time, as a UNIX timestamp.",
        ),
        timestamps: bool = Field(default=True, description="Show timestamps in logs."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get service logs."""
        params = {"tail": tail, "timestamps": timestamps}
        if since:
            params["since"] = since
        return get_client().get_service_logs(environment_id, service_id, **params)

    @mcp.tool(
        name="docker_list_images",
        description="List images in a Docker environment.",
        tags={"Docker"},
    )
    def docker_list_images_tool(
        environment_id: int = Field(description="Environment ID."),
        all_images: bool = Field(
            default=False,
            alias="all",
            description="Show all images. Only intermediate image layers are filtered out by default.",
        ),
        filters: str | None = Field(
            default=None,
            description="A JSON encoded value of the filters to process on the images list.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List images."""
        params: dict[str, Any] = {"all": all_images}
        if filters:
            params["filters"] = filters
        return get_client().list_images(environment_id, **params)

    @mcp.tool(
        name="docker_inspect_image",
        description="Return low-level information about an image.",
        tags={"Docker"},
    )
    def docker_inspect_image_tool(
        environment_id: int = Field(description="Environment ID."),
        image_name: str = Field(description="Image ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect image."""
        return get_client().inspect_image(environment_id, image_name)

    @mcp.tool(
        name="docker_list_networks",
        description="List networks in a Docker environment.",
        tags={"Docker"},
    )
    def docker_list_networks_tool(
        environment_id: int = Field(description="Environment ID."),
        filters: str | None = Field(
            default=None,
            description="A JSON encoded value of the filters to process on the networks list.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List networks."""
        params: dict[str, Any] = {}
        if filters:
            params["filters"] = filters
        return get_client().list_networks(environment_id, **params)

    @mcp.tool(
        name="docker_inspect_network",
        description="Return low-level information about a network.",
        tags={"Docker"},
    )
    def docker_inspect_network_tool(
        environment_id: int = Field(description="Environment ID."),
        network_id: str = Field(description="Network ID or name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect network."""
        return get_client().inspect_network(environment_id, network_id)

    @mcp.tool(
        name="docker_list_volumes",
        description="List volumes in a Docker environment.",
        tags={"Docker"},
    )
    def docker_list_volumes_tool(
        environment_id: int = Field(description="Environment ID."),
        filters: str | None = Field(
            default=None,
            description="A JSON encoded value of the filters to process on the volumes list.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List volumes."""
        params: dict[str, Any] = {}
        if filters:
            params["filters"] = filters
        return get_client().list_volumes(environment_id, **params)

    @mcp.tool(
        name="docker_inspect_volume",
        description="Return low-level information about a volume.",
        tags={"Docker"},
    )
    def docker_inspect_volume_tool(
        environment_id: int = Field(description="Environment ID."),
        volume_name: str = Field(description="Volume name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect volume."""
        return get_client().inspect_volume(environment_id, volume_name)

    @mcp.tool(
        name="docker_get_info",
        description="Get system-wide information for the Docker host.",
        tags={"Docker"},
    )
    def docker_get_info_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get Docker info."""
        return get_client().get_docker_info(environment_id)

    @mcp.tool(
        name="docker_get_version",
        description="Get Docker version information.",
        tags={"Docker"},
    )
    def docker_get_version_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get Docker version."""
        return get_client().get_docker_version(environment_id)

    @mcp.tool(
        name="docker_get_system_df",
        description="Get Docker data usage information.",
        tags={"Docker"},
    )
    def docker_get_system_df_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get Docker df."""
        return get_client().get_docker_df(environment_id)

    @mcp.tool(
        name="docker_create_container",
        description="Create a new container.",
        tags={"Docker"},
    )
    def docker_create_container_tool(
        environment_id: int = Field(description="Environment ID."),
        config: dict = Field(
            description="Container configuration (Docker API format)."
        ),
        name: str | None = Field(default=None, description="Container name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create container."""
        return get_client().create_container(environment_id, config, name=name)

    @mcp.tool(
        name="docker_create_network",
        description="Create a new network.",
        tags={"Docker"},
    )
    def docker_create_network_tool(
        environment_id: int = Field(description="Environment ID."),
        config: dict = Field(description="Network configuration (Docker API format)."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create network."""
        return get_client().create_network(environment_id, config)

    @mcp.tool(
        name="docker_create_volume",
        description="Create a new volume.",
        tags={"Docker"},
    )
    def docker_create_volume_tool(
        environment_id: int = Field(description="Environment ID."),
        config: dict = Field(description="Volume configuration (Docker API format)."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create volume."""
        return get_client().create_volume(environment_id, config)

    @mcp.tool(
        name="docker_create_exec",
        description="Create an exec instance in a container.",
        tags={"Docker"},
    )
    def docker_create_exec_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID or name."),
        config: dict = Field(description="Exec configuration (Docker API format)."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create exec."""
        return get_client().create_exec(environment_id, container_id, config)

    @mcp.tool(
        name="docker_start_exec",
        description="Start an exec instance.",
        tags={"Docker"},
    )
    def docker_start_exec_tool(
        environment_id: int = Field(description="Environment ID."),
        exec_id: str = Field(description="Exec ID."),
        config: dict = Field(
            default_factory=dict, description="Start configuration (Docker API format)."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Start exec."""
        return get_client().start_exec(environment_id, exec_id, config)

    @mcp.tool(
        name="docker_inspect_exec",
        description="Inspect an exec instance.",
        tags={"Docker"},
    )
    def docker_inspect_exec_tool(
        environment_id: int = Field(description="Environment ID."),
        exec_id: str = Field(description="Exec ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Inspect exec."""
        return get_client().inspect_exec(environment_id, exec_id)

    @mcp.tool(
        name="docker_get_stack_logs",
        description="Get aggregated logs for all containers or services in a Portainer stack.",
        tags={"Docker", "Stack"},
    )
    async def docker_get_stack_logs_tool(
        environment_id: int = Field(
            description="Environment ID where the stack resides."
        ),
        stack_id: int = Field(description="Portainer stack ID."),
        tail: str = Field(
            default="100",
            description="Output specified number of lines at the end of logs for each container/service.",
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Get stack logs."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_stack_logs(environment_id, stack_id, tail=tail)


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_stacks",
        description="List all stacks across all environments.",
        tags={"Stack"},
    )
    async def get_stacks_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """List stacks."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_stacks()

    @mcp.tool(
        name="get_stack",
        description="Get details of a specific stack by ID.",
        tags={"Stack"},
    )
    async def get_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Get stack."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_stack(stack_id)

    @mcp.tool(
        name="get_stack_file",
        description="Get the Docker Compose/manifest file content for a stack.",
        tags={"Stack"},
    )
    async def get_stack_file_tool(
        stack_id: int = Field(description="Stack ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Get stack file."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_stack_file(stack_id)

    @mcp.tool(
        name="create_standalone_stack",
        description="Create a standalone Docker Compose stack from compose file content.",
        tags={"Stack"},
    )
    async def create_standalone_stack_tool(
        name: str = Field(description="Stack name."),
        file_content: str = Field(description="Docker Compose YAML content."),
        endpoint_id: int = Field(description="Target environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Create standalone stack."""
        await ctx_progress(ctx, 100, 100)
        return get_client().create_standalone_stack_from_string(
            name=name, file_content=file_content, endpoint_id=endpoint_id
        )

    @mcp.tool(
        name="create_standalone_stack_from_repo",
        description="Create a standalone Docker Compose stack from a Git repository.",
        tags={"Stack"},
    )
    async def create_standalone_stack_from_repo_tool(
        name: str = Field(description="Stack name."),
        repo_url: str = Field(description="Git repository URL."),
        endpoint_id: int = Field(description="Target environment ID."),
        compose_file: str = Field(
            default="docker-compose.yml", description="Path to compose file in repo."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Create stack from repo."""
        await ctx_progress(ctx, 100, 100)
        return get_client().create_standalone_stack_from_repository(
            name=name,
            repo_url=repo_url,
            endpoint_id=endpoint_id,
            ComposeFilePathInRepository=compose_file,
        )

    @mcp.tool(
        name="update_stack",
        description="Update a stack's configuration.",
        tags={"Stack"},
    )
    async def update_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        file_content: str | None = Field(
            default=None, description="Updated compose file content."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Update stack."""
        kwargs = {}
        if file_content:
            kwargs["StackFileContent"] = file_content
        await ctx_progress(ctx, 100, 100)
        return get_client().update_stack(stack_id, endpoint_id, **kwargs)

    @mcp.tool(
        name="delete_stack",
        description="Delete a stack.",
        tags={"Stack"},
    )
    async def delete_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete stack."""
        if not await ctx_confirm_destructive(ctx, "delete stack"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="start_stack",
        description="Start a stopped stack.",
        tags={"Stack"},
    )
    async def start_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Start stack."""
        await ctx_progress(ctx, 100, 100)
        return get_client().start_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="stop_stack",
        description="Stop a running stack.",
        tags={"Stack"},
    )
    async def stop_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Stop stack."""
        if not await ctx_confirm_destructive(ctx, "stop stack"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().stop_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="redeploy_stack_git",
        description="Redeploy a stack from its Git repository (pull latest and redeploy).",
        tags={"Stack"},
    )
    async def redeploy_stack_git_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Redeploy from Git."""
        await ctx_progress(ctx, 100, 100)
        return get_client().redeploy_stack_git(stack_id, endpoint_id)


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_kubernetes_dashboard",
        description="Get Kubernetes dashboard data for an environment (pods, services, deployments summary).",
        tags={"Kubernetes"},
    )
    def get_k8s_dashboard_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get K8s dashboard."""
        return get_client().get_kubernetes_dashboard(environment_id)

    @mcp.tool(
        name="get_kubernetes_namespaces",
        description="List Kubernetes namespaces in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_namespaces_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List namespaces."""
        return get_client().get_kubernetes_namespaces(environment_id)

    @mcp.tool(
        name="get_kubernetes_applications",
        description="List Kubernetes applications (deployments, statefulsets, daemonsets) in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_applications_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List applications."""
        return get_client().get_kubernetes_applications(environment_id)

    @mcp.tool(
        name="get_kubernetes_services",
        description="List Kubernetes services in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_services_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List services."""
        return get_client().get_kubernetes_services(environment_id)

    @mcp.tool(
        name="get_kubernetes_ingresses",
        description="List Kubernetes ingresses in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_ingresses_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List ingresses."""
        return get_client().get_kubernetes_ingresses(environment_id)

    @mcp.tool(
        name="get_kubernetes_configmaps",
        description="List Kubernetes configmaps in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_configmaps_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List configmaps."""
        return get_client().get_kubernetes_configmaps(environment_id)

    @mcp.tool(
        name="get_kubernetes_secrets",
        description="List Kubernetes secrets in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_secrets_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List secrets."""
        return get_client().get_kubernetes_secrets(environment_id)

    @mcp.tool(
        name="get_kubernetes_volumes",
        description="List Kubernetes persistent volume claims in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_volumes_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List volumes."""
        return get_client().get_kubernetes_volumes(environment_id)

    @mcp.tool(
        name="get_kubernetes_events",
        description="List Kubernetes events in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_events_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List events."""
        return get_client().get_kubernetes_events(environment_id)

    @mcp.tool(
        name="get_kubernetes_nodes_limits",
        description="Get Kubernetes node resource limits for capacity planning.",
        tags={"Kubernetes"},
    )
    def get_k8s_nodes_limits_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get node limits."""
        return get_client().get_kubernetes_nodes_limits(environment_id)

    @mcp.tool(
        name="get_kubernetes_metrics_nodes",
        description="Get resource metrics for Kubernetes nodes.",
        tags={"Kubernetes"},
    )
    def get_k8s_metrics_nodes_tool(
        environment_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get node metrics."""
        return get_client().get_kubernetes_metrics_nodes(environment_id)

    @mcp.tool(
        name="get_helm_releases",
        description="List Helm releases installed in an environment.",
        tags={"Kubernetes"},
    )
    def get_helm_releases_tool(
        endpoint_id: int = Field(description="Environment ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List Helm releases."""
        return get_client().get_helm_releases(endpoint_id)

    @mcp.tool(
        name="install_helm_chart",
        description="Install a Helm chart in an environment.",
        tags={"Kubernetes"},
    )
    def install_helm_chart_tool(
        endpoint_id: int = Field(description="Environment ID."),
        chart_name: str = Field(description="Helm chart name."),
        release_name: str = Field(default="", description="Name for the Helm release."),
        namespace: str = Field(default="default", description="Target namespace."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Install Helm chart."""
        return get_client().install_helm_chart(
            endpoint_id, chart_name, ReleaseName=release_name, Namespace=namespace
        )

    @mcp.tool(
        name="delete_helm_release",
        description="Delete (uninstall) a Helm release.",
        tags={"Kubernetes"},
    )
    async def delete_helm_release_tool(
        endpoint_id: int = Field(description="Environment ID."),
        release_name: str = Field(description="Helm release name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete Helm release."""
        if not await ctx_confirm_destructive(ctx, "delete helm release"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_helm_release(endpoint_id, release_name)


def register_edge_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_edge_groups",
        description="List all edge groups.",
        tags={"Edge"},
    )
    def get_edge_groups_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List edge groups."""
        return get_client().get_edge_groups()

    @mcp.tool(
        name="create_edge_group",
        description="Create an edge group for organizing edge devices.",
        tags={"Edge"},
    )
    def create_edge_group_tool(
        name: str = Field(description="Edge group name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create edge group."""
        return get_client().create_edge_group(name=name)

    @mcp.tool(
        name="delete_edge_group",
        description="Delete an edge group.",
        tags={"Edge"},
    )
    async def delete_edge_group_tool(
        group_id: int = Field(description="Edge group ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete edge group."""
        if not await ctx_confirm_destructive(ctx, "delete edge group"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_edge_group(group_id)

    @mcp.tool(
        name="get_edge_stacks",
        description="List all edge stacks deployed to edge groups.",
        tags={"Edge"},
    )
    async def get_edge_stacks_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """List edge stacks."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_edge_stacks()

    @mcp.tool(
        name="get_edge_stack",
        description="Get details of a specific edge stack.",
        tags={"Edge"},
    )
    async def get_edge_stack_tool(
        stack_id: int = Field(description="Edge stack ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Get edge stack."""
        await ctx_progress(ctx, 100, 100)
        return get_client().get_edge_stack(stack_id)

    @mcp.tool(
        name="create_edge_stack",
        description="Create an edge stack from compose file content.",
        tags={"Edge"},
    )
    async def create_edge_stack_tool(
        name: str = Field(description="Stack name."),
        file_content: str = Field(description="Docker Compose YAML content."),
        edge_groups: list[int] = Field(
            description="List of edge group IDs to deploy to."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        await ctx_progress(ctx, 0, 100)
        """Create edge stack."""
        await ctx_progress(ctx, 100, 100)
        return get_client().create_edge_stack_from_string(
            name=name, file_content=file_content, edge_groups=edge_groups
        )

    @mcp.tool(
        name="delete_edge_stack",
        description="Delete an edge stack.",
        tags={"Edge"},
    )
    async def delete_edge_stack_tool(
        stack_id: int = Field(description="Edge stack ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete edge stack."""
        if not await ctx_confirm_destructive(ctx, "delete edge stack"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_edge_stack(stack_id)

    @mcp.tool(
        name="get_edge_jobs",
        description="List all edge jobs.",
        tags={"Edge"},
    )
    def get_edge_jobs_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List edge jobs."""
        return get_client().get_edge_jobs()

    @mcp.tool(
        name="get_edge_job",
        description="Get details of a specific edge job.",
        tags={"Edge"},
    )
    def get_edge_job_tool(
        job_id: int = Field(description="Edge job ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get edge job."""
        return get_client().get_edge_job(job_id)

    @mcp.tool(
        name="create_edge_job",
        description="Create an edge job to execute scripts on edge devices.",
        tags={"Edge"},
    )
    def create_edge_job_tool(
        name: str = Field(description="Job name."),
        file_content: str = Field(description="Script content."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create edge job."""
        return get_client().create_edge_job_from_string(
            name=name, file_content=file_content
        )

    @mcp.tool(
        name="delete_edge_job",
        description="Delete an edge job.",
        tags={"Edge"},
    )
    async def delete_edge_job_tool(
        job_id: int = Field(description="Edge job ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete edge job."""
        if not await ctx_confirm_destructive(ctx, "delete edge job"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_edge_job(job_id)


def register_template_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_templates",
        description="List available app templates.",
        tags={"Template"},
    )
    def get_templates_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List templates."""
        return get_client().get_templates()

    @mcp.tool(
        name="get_custom_templates",
        description="List custom templates created by users.",
        tags={"Template"},
    )
    def get_custom_templates_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List custom templates."""
        return get_client().get_custom_templates()

    @mcp.tool(
        name="get_custom_template",
        description="Get details of a specific custom template.",
        tags={"Template"},
    )
    def get_custom_template_tool(
        template_id: int = Field(description="Template ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get custom template."""
        return get_client().get_custom_template(template_id)

    @mcp.tool(
        name="create_custom_template",
        description="Create a custom template from compose file content. Types: 1=swarm, 2=compose, 3=kubernetes.",
        tags={"Template"},
    )
    def create_custom_template_tool(
        title: str = Field(description="Template title."),
        description: str = Field(description="Template description."),
        file_content: str = Field(description="Compose/manifest file content."),
        template_type: int = Field(
            default=2, description="Type: 1=swarm, 2=compose, 3=kubernetes."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create custom template."""
        return get_client().create_custom_template_from_string(
            title=title,
            description=description,
            file_content=file_content,
            template_type=template_type,
        )

    @mcp.tool(
        name="delete_custom_template",
        description="Delete a custom template.",
        tags={"Template"},
    )
    async def delete_custom_template_tool(
        template_id: int = Field(description="Template ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete custom template."""
        if not await ctx_confirm_destructive(ctx, "delete custom template"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_custom_template(template_id)

    @mcp.tool(
        name="get_custom_template_file",
        description="Get the compose file content of a custom template.",
        tags={"Template"},
    )
    def get_custom_template_file_tool(
        template_id: int = Field(description="Template ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get template file."""
        return get_client().get_custom_template_file(template_id)

    @mcp.tool(
        name="get_helm_templates",
        description="List available Helm chart templates.",
        tags={"Template"},
    )
    def get_helm_templates_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List Helm templates."""
        return get_client().get_helm_templates()


def register_user_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_users",
        description="List all Portainer users.",
        tags={"User"},
    )
    def get_users_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List users."""
        return get_client().get_users()

    @mcp.tool(
        name="get_user",
        description="Get details of a specific user.",
        tags={"User"},
    )
    def get_user_tool(
        user_id: int = Field(description="User ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get user."""
        return get_client().get_user(user_id)

    @mcp.tool(
        name="get_current_user",
        description="Get the currently authenticated user's profile.",
        tags={"User"},
    )
    def get_current_user_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get current user."""
        return get_client().get_current_user()

    @mcp.tool(
        name="create_user",
        description="Create a new Portainer user. Roles: 1=admin, 2=standard.",
        tags={"User"},
    )
    def create_user_tool(
        username: str = Field(description="Username."),
        password: str = Field(description="Password."),
        role: int = Field(default=2, description="Role: 1=admin, 2=standard."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create user."""
        return get_client().create_user(username=username, password=password, role=role)

    @mcp.tool(
        name="delete_user",
        description="Delete a Portainer user.",
        tags={"User"},
    )
    async def delete_user_tool(
        user_id: int = Field(description="User ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete user."""
        if not await ctx_confirm_destructive(ctx, "delete user"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_user(user_id)

    @mcp.tool(
        name="get_teams",
        description="List all teams.",
        tags={"User"},
    )
    def get_teams_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List teams."""
        return get_client().get_teams()

    @mcp.tool(
        name="create_team",
        description="Create a new team.",
        tags={"User"},
    )
    def create_team_tool(
        name: str = Field(description="Team name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create team."""
        return get_client().create_team(name=name)

    @mcp.tool(
        name="delete_team",
        description="Delete a team.",
        tags={"User"},
    )
    async def delete_team_tool(
        team_id: int = Field(description="Team ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete team."""
        if not await ctx_confirm_destructive(ctx, "delete team"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_team(team_id)

    @mcp.tool(
        name="get_roles",
        description="List all available roles.",
        tags={"User"},
    )
    def get_roles_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List roles."""
        return get_client().get_roles()

    @mcp.tool(
        name="get_user_tokens",
        description="List API tokens for a user.",
        tags={"User"},
    )
    def get_user_tokens_tool(
        user_id: int = Field(description="User ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List user tokens."""
        return get_client().get_user_tokens(user_id)


def register_registry_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_registries",
        description="List all configured Docker registries.",
        tags={"Registry"},
    )
    def get_registries_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List registries."""
        return get_client().get_registries()

    @mcp.tool(
        name="get_registry",
        description="Get details of a specific registry.",
        tags={"Registry"},
    )
    def get_registry_tool(
        registry_id: int = Field(description="Registry ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get registry."""
        return get_client().get_registry(registry_id)

    @mcp.tool(
        name="create_registry",
        description="Add a Docker registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub.",
        tags={"Registry"},
    )
    def create_registry_tool(
        name: str = Field(description="Registry name."),
        registry_type: int = Field(description="Registry type (1-8)."),
        url: str = Field(description="Registry URL."),
        username: str = Field(default="", description="Username for authentication."),
        password: str = Field(default="", description="Password for authentication."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create registry."""
        kwargs = {}
        if username:
            kwargs["Username"] = username
        if password:
            kwargs["Password"] = password
        return get_client().create_registry(
            name=name, registry_type=registry_type, url=url, **kwargs
        )

    @mcp.tool(
        name="delete_registry",
        description="Delete a Docker registry.",
        tags={"Registry"},
    )
    async def delete_registry_tool(
        registry_id: int = Field(description="Registry ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete registry."""
        if not await ctx_confirm_destructive(ctx, "delete registry"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_registry(registry_id)


def register_system_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_status",
        description="Get Portainer instance status (version, uptime, etc.).",
        tags={"System"},
    )
    def get_status_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get status."""
        return get_client().get_status()

    @mcp.tool(
        name="get_system_info",
        description="Get detailed system information (build info, dependencies, runtime).",
        tags={"System"},
    )
    def get_system_info_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get system info."""
        return get_client().get_system_info()

    @mcp.tool(
        name="get_system_version",
        description="Get Portainer version information.",
        tags={"System"},
    )
    def get_system_version_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get version."""
        return get_client().get_system_version()

    @mcp.tool(
        name="get_settings",
        description="Get Portainer settings (authentication, templates URL, edge agent, etc.).",
        tags={"System"},
    )
    def get_settings_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get settings."""
        return get_client().get_settings()

    @mcp.tool(
        name="update_settings",
        description="Update Portainer settings.",
        tags={"System"},
    )
    def update_settings_tool(
        authentication_method: int | None = Field(
            default=None, description="Auth method: 1=internal, 2=LDAP, 3=OAuth."
        ),
        enable_telemetry: bool | None = Field(
            default=None, description="Enable telemetry."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Update settings."""
        kwargs = {}
        if authentication_method is not None:
            kwargs["AuthenticationMethod"] = authentication_method
        if enable_telemetry is not None:
            kwargs["EnableTelemetry"] = enable_telemetry
        return get_client().update_settings(**kwargs)

    @mcp.tool(
        name="get_tags",
        description="List all tags used for organizing environments.",
        tags={"System"},
    )
    def get_tags_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """List tags."""
        return get_client().get_tags()

    @mcp.tool(
        name="create_tag",
        description="Create a tag for organizing environments.",
        tags={"System"},
    )
    def create_tag_tool(
        name: str = Field(description="Tag name."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create tag."""
        return get_client().create_tag(name=name)

    @mcp.tool(
        name="delete_tag",
        description="Delete a tag.",
        tags={"System"},
    )
    async def delete_tag_tool(
        tag_id: int = Field(description="Tag ID."),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Delete tag."""
        if not await ctx_confirm_destructive(ctx, "delete tag"):
            return {"status": "cancelled", "message": "Operation cancelled by user"}
        await ctx_progress(ctx, 0, 100)
        return get_client().delete_tag(tag_id)

    @mcp.tool(
        name="get_motd",
        description="Get the Portainer message of the day.",
        tags={"System"},
    )
    def get_motd_tool(
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Get MOTD."""
        return get_client().get_motd()

    @mcp.tool(
        name="backup_portainer",
        description="Create a backup of all Portainer data.",
        tags={"System"},
    )
    def backup_portainer_tool(
        password: str = Field(
            default="", description="Password to encrypt the backup."
        ),
        ctx: Context = Field(
            description="MCP context for progress reporting", default=None
        ),
    ) -> Any:
        """Create backup."""
        return get_client().backup(password=password)


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    """Initialize and return the MCP instance, args, and middlewares."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="Portainer MCP",
        version=__version__,
        instructions="Portainer MCP Server — Manage Docker environments, stacks, Kubernetes clusters, registries, users, edge devices, and system settings.",
    )

    if to_boolean(os.getenv("AUTHTOOL", "True")):
        register_auth_tools(mcp)
    if to_boolean(os.getenv("ENVIRONMENTTOOL", "True")):
        register_environment_tools(mcp)
    if to_boolean(os.getenv("DOCKERTOOL", "True")):
        register_docker_tools(mcp)
    if to_boolean(os.getenv("STACKTOOL", "True")):
        register_stack_tools(mcp)
    if to_boolean(os.getenv("KUBERNETESTOOL", "True")):
        register_kubernetes_tools(mcp)
    if to_boolean(os.getenv("EDGETOOL", "True")):
        register_edge_tools(mcp)
    if to_boolean(os.getenv("TEMPLATETOOL", "True")):
        register_template_tools(mcp)
    if to_boolean(os.getenv("USERTOOL", "True")):
        register_user_tools(mcp)
    if to_boolean(os.getenv("REGISTRYTOOL", "True")):
        register_registry_tools(mcp)
    if to_boolean(os.getenv("SYSTEMTOOL", "True")):
        register_system_tools(mcp)

    register_prompts(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    registered_tags: list[str] = []
    return mcp, args, middlewares, registered_tags


def mcp_server() -> None:
    mcp, args, middlewares, registered_tags = get_mcp_instance()

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
