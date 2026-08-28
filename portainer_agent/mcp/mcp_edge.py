"""MCP tools for edge operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client
from portainer_agent.mcp.action_kwargs import ActionCall, dispatch_client_action

_EDGE_ACTIONS: dict[str, ActionCall] = {
    "get_edge_groups": ActionCall(),
    "create_edge_group": ActionCall(params=("name",)),
    "delete_edge_group": ActionCall(params=("group_id",)),
    "get_edge_stacks": ActionCall(),
    "get_edge_stack": ActionCall(params=("stack_id",)),
    "create_edge_stack": ActionCall(),
    "delete_edge_stack": ActionCall(params=("stack_id",)),
    "get_edge_jobs": ActionCall(),
    "get_edge_job": ActionCall(params=("job_id",)),
    "create_edge_job": ActionCall(),
    "delete_edge_job": ActionCall(params=("job_id",)),
}


def register_edge_tools(mcp: FastMCP):
    @mcp.tool(tags={"Edge"})
    async def portainer_edge(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job'"
        ),
        name: str | None = Field(default=None, description="name"),
        group_id: int | None = Field(default=None, description="group id"),
        job_id: int | None = Field(default=None, description="job id"),
        stack_id: int | None = Field(default=None, description="stack id"),
        client=Depends(get_client),
    ) -> dict:
        """Manage edge operations."""
        if action not in _EDGE_ACTIONS:
            raise ValueError(
                f"Unknown action: {action}. Must be one of: get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job"
            )
        return await dispatch_client_action(
            action=action,
            client=client,
            values={
                "name": name,
                "group_id": group_id,
                "job_id": job_id,
                "stack_id": stack_id,
            },
            actions=_EDGE_ACTIONS,
        )
