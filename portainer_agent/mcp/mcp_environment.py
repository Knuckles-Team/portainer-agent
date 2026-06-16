"""MCP tools for environment operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp_utilities import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
        if action == "get_endpoints":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_endpoints, **kwargs)
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
            return await run_blocking(client.get_endpoint_groups, **kwargs)
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
