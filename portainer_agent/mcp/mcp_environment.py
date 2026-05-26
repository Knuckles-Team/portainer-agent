"""MCP tools for environment operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
