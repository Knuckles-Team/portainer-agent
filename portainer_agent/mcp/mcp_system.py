"""MCP tools for system operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp_utilities import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
            return await run_blocking(client.get_status, **kwargs)
        if action == "get_system_info":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_system_info, **kwargs)
        if action == "get_system_version":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_system_version, **kwargs)
        if action == "get_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_settings, **kwargs)
        if action == "update_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.update_settings, **kwargs)
        if action == "get_tags":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_tags, **kwargs)
        if action == "create_tag":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_tag, **kwargs)
        if action == "delete_tag":
            kwargs = {"tag_id": tag_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_tag, **kwargs)
        if action == "get_motd":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_motd, **kwargs)
        if action == "backup_portainer":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.backup_portainer, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_status', 'get_system_info', 'get_system_version', 'get_settings', 'update_settings', 'get_tags', 'create_tag', 'delete_tag', 'get_motd', 'backup_portainer"
        )
