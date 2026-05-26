"""MCP tools for user operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
