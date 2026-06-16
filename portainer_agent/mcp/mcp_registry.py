"""MCP tools for registry operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp_utilities import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
