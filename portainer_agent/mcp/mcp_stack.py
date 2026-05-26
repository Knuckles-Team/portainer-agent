"""MCP tools for stack operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(tags={"Stack"})
    async def portainer_stack(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'redeploy_stack_git'"
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
        kwargs: dict[str, Any]
        if action == "get_stacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            res = client.get_stacks(**kwargs)
            return {"data": res} if isinstance(res, list) else res
        if action == "get_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_stack(**kwargs)
        if action == "get_stack_file":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_stack_file(**kwargs)
        if action == "create_standalone_stack":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_standalone_stack(**kwargs)
        if action == "create_standalone_stack_from_repo":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_standalone_stack_from_repo(**kwargs)
        if action == "update_stack":
            kwargs = {
                "stack_id": stack_id,
                "endpoint_id": endpoint_id,
                "StackFileContent": stack_file_content,
                "Env": env,
                "Prune": prune,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_stack(**kwargs)
        if action == "delete_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_stack(**kwargs)
        if action == "start_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.start_stack(**kwargs)
        if action == "stop_stack":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.stop_stack(**kwargs)
        if action == "redeploy_stack_git":
            kwargs = {"stack_id": stack_id, "endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.redeploy_stack_git(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_stacks', 'get_stack', 'get_stack_file', 'create_standalone_stack', 'create_standalone_stack_from_repo', 'update_stack', 'delete_stack', 'start_stack', 'stop_stack', 'redeploy_stack_git"
        )
