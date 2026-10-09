"""MCP tools for environment operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from agent_connector_sdk.mcp.concurrency import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_ENVIRONMENT_ACTIONS: dict[str, ActionCall] = {
    "get_endpoints": ActionCall(params=("limit", "offset")),
    "get_endpoint": ActionCall(params=("endpoint_id",)),
    "create_endpoint": ActionCall(params=("name", "endpoint_type", "url")),
    "update_endpoint": ActionCall(params=("endpoint_id",)),
    "delete_endpoint": ActionCall(params=("endpoint_id",)),
    "snapshot_endpoint": ActionCall(params=("endpoint_id",)),
    "snapshot_all_endpoints": ActionCall(),
    "get_endpoint_groups": ActionCall(),
    "create_endpoint_group": ActionCall(params=("name", "description")),
    "delete_endpoint_group": ActionCall(params=("group_id",)),
}


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
        if action not in _ENVIRONMENT_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_endpoints', 'get_endpoint', 'create_endpoint', 'update_endpoint', 'delete_endpoint', 'snapshot_endpoint', 'snapshot_all_endpoints', 'get_endpoint_groups', 'create_endpoint_group', 'delete_endpoint_group', 'get_endpoint_settings', 'update_endpoint_settings"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={
                "limit": limit,
                "offset": offset,
                "endpoint_id": endpoint_id,
                "name": name,
                "endpoint_type": endpoint_type,
                "url": url,
                "description": description,
                "group_id": group_id,
            },
            actions=_ENVIRONMENT_ACTIONS,
        )
