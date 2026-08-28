"""MCP tools for registry operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_REGISTRY_ACTIONS: dict[str, ActionCall] = {
    "get_registries": ActionCall(),
    "get_registry": ActionCall(params=("registry_id",)),
    "create_registry": ActionCall(params=("name", "registry_type", "url")),
    "delete_registry": ActionCall(params=("registry_id",)),
}


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
        if action not in _REGISTRY_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_registries', 'get_registry', 'create_registry', 'delete_registry"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={
                "registry_id": registry_id,
                "name": name,
                "registry_type": registry_type,
                "url": url,
            },
            actions=_REGISTRY_ACTIONS,
        )
