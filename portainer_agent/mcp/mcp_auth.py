"""MCP tools for auth operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_AUTH_ACTIONS: dict[str, ActionCall] = {
    "authenticate": ActionCall(params=("username", "password")),
    "logout": ActionCall(),
    "validate_oauth": ActionCall(params=("code",)),
}


def register_auth_tools(mcp: FastMCP):
    @mcp.tool(tags={"Auth"})
    async def portainer_auth(
        action: str = Field(
            description="Action to perform. Must be one of: 'authenticate', 'logout', 'validate_oauth'"
        ),
        username: str | None = Field(default=None, description="username"),
        password: str | None = Field(default=None, description="password"),
        code: str | None = Field(default=None, description="code"),
        client=Depends(get_client),
    ) -> dict:
        """Manage auth operations."""
        if action not in _AUTH_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: authenticate', 'logout', 'validate_oauth"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={"username": username, "password": password, "code": code},
            actions=_AUTH_ACTIONS,
        )
