"""MCP tools for stack operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_STACK_ACTIONS: dict[str, ActionCall] = {
    "get_stacks": ActionCall(wrap_list_as_data=True),
    "get_stack": ActionCall(params=("stack_id",)),
    "get_stack_file": ActionCall(params=("stack_id",)),
    "create_standalone_stack": ActionCall(),
    "create_standalone_stack_from_repo": ActionCall(),
    "update_stack": ActionCall(
        params=(
            "stack_id",
            "endpoint_id",
            ("StackFileContent", "stack_file_content"),
            ("Env", "env"),
            ("Prune", "prune"),
        )
    ),
    "delete_stack": ActionCall(params=("stack_id", "endpoint_id")),
    "start_stack": ActionCall(params=("stack_id", "endpoint_id")),
    "stop_stack": ActionCall(params=("stack_id", "endpoint_id")),
    "update_stack_git": ActionCall(params=("stack_id", "endpoint_id", "env", "prune")),
    "redeploy_stack_git": ActionCall(
        params=("stack_id", "endpoint_id", "env", "prune")
    ),
}


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(tags={"Stack"})
    async def portainer_stack(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'update_stack_git', 'redeploy_stack_git'"
        ),
        stack_id: int | None = Field(default=None, description="stack id"),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        stack_file_content: str | None = Field(
            default=None, description="compose file content for update_stack"
        ),
        env: list | None = Field(
            default=None, description="environment variables list for update_stack"
        ),
        prune: bool | None = Field(
            default=None, description="whether to prune for update_stack"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage stack operations."""
        if action not in _STACK_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: 'get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'update_stack_git', 'redeploy_stack_git'"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={
                "stack_id": stack_id,
                "endpoint_id": endpoint_id,
                "stack_file_content": stack_file_content,
                "env": env,
                "prune": prune,
            },
            actions=_STACK_ACTIONS,
        )
