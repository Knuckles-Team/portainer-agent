"""MCP tools for user operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_USER_ACTIONS: dict[str, ActionCall] = {
    "get_users": ActionCall(),
    "get_user": ActionCall(params=("user_id",)),
    "get_current_user": ActionCall(),
    "create_user": ActionCall(params=("username", "password", "role")),
    "delete_user": ActionCall(params=("user_id",)),
    "get_teams": ActionCall(),
    "create_team": ActionCall(params=("name",)),
    "delete_team": ActionCall(params=("team_id",)),
    "get_roles": ActionCall(),
    "get_user_tokens": ActionCall(params=("user_id",)),
}


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
        if action not in _USER_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_users', 'get_user', 'get_current_user', 'create_user', 'delete_user', 'get_teams', 'create_team', 'delete_team', 'get_roles', 'get_user_tokens"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={
                "user_id": user_id,
                "username": username,
                "password": password,
                "role": role,
                "name": name,
                "team_id": team_id,
            },
            actions=_USER_ACTIONS,
        )
