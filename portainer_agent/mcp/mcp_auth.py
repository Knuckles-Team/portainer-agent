"""MCP tools for auth operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp_utilities import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
        kwargs: dict[str, Any]
        if action == "authenticate":
            kwargs = {"username": username, "password": password}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.authenticate, **kwargs)
        if action == "logout":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.logout, **kwargs)
        if action == "validate_oauth":
            kwargs = {"code": code}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.validate_oauth, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: authenticate', 'logout', 'validate_oauth"
        )
