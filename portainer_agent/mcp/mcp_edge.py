"""MCP tools for edge operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


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
        kwargs: dict[str, Any]
        if action == "get_edge_groups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_groups(**kwargs)
        if action == "create_edge_group":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_group(**kwargs)
        if action == "delete_edge_group":
            kwargs = {"group_id": group_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_group(**kwargs)
        if action == "get_edge_stacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_stacks(**kwargs)
        if action == "get_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_stack(**kwargs)
        if action == "create_edge_stack":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_stack(**kwargs)
        if action == "delete_edge_stack":
            kwargs = {"stack_id": stack_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_stack(**kwargs)
        if action == "get_edge_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_jobs(**kwargs)
        if action == "get_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_edge_job(**kwargs)
        if action == "create_edge_job":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_edge_job(**kwargs)
        if action == "delete_edge_job":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_edge_job(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_edge_groups', 'create_edge_group', 'delete_edge_group', 'get_edge_stacks', 'get_edge_stack', 'create_edge_stack', 'delete_edge_stack', 'get_edge_jobs', 'get_edge_job', 'create_edge_job', 'delete_edge_job"
        )
