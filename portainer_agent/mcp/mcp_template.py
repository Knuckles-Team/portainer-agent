"""MCP tools for template operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp.concurrency import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


def register_template_tools(mcp: FastMCP):
    @mcp.tool(tags={"Template"})
    async def portainer_template(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates'"
        ),
        template_id: int | None = Field(default=None, description="template id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage template operations."""
        kwargs: dict[str, Any]
        if action == "get_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_templates, **kwargs)
        if action == "get_custom_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_templates, **kwargs)
        if action == "get_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_template, **kwargs)
        if action == "create_custom_template":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.create_custom_template, **kwargs)
        if action == "delete_custom_template":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.delete_custom_template, **kwargs)
        if action == "get_custom_template_file":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_custom_template_file, **kwargs)
        if action == "get_helm_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(client.get_helm_templates, **kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates"
        )
