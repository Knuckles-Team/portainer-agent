"""MCP tools for system operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_SYSTEM_ACTIONS: dict[str, ActionCall] = {
    "get_status": ActionCall(),
    "get_system_info": ActionCall(),
    "get_system_version": ActionCall(),
    "get_settings": ActionCall(),
    "update_settings": ActionCall(),
    "get_tags": ActionCall(),
    "create_tag": ActionCall(params=("name",)),
    "delete_tag": ActionCall(params=("tag_id",)),
    "get_motd": ActionCall(),
    "backup_portainer": ActionCall(),
}


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
        if action not in _SYSTEM_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={"name": name, "tag_id": tag_id},
            actions=_SYSTEM_ACTIONS,
        )
