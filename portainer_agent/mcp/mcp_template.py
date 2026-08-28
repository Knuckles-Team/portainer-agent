"""MCP tools for template operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_TEMPLATE_ACTIONS: dict[str, ActionCall] = {
    "get_templates": ActionCall(),
    "get_custom_templates": ActionCall(),
    "get_custom_template": ActionCall(params=("template_id",)),
    "create_custom_template": ActionCall(),
    "delete_custom_template": ActionCall(params=("template_id",)),
    "get_custom_template_file": ActionCall(params=("template_id",)),
    "get_helm_templates": ActionCall(),
}


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
        if action not in _TEMPLATE_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_templates', 'get_custom_templates', 'get_custom_template', 'create_custom_template', 'delete_custom_template', 'get_custom_template_file', 'get_helm_templates"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={"template_id": template_id},
            actions=_TEMPLATE_ACTIONS,
        )
