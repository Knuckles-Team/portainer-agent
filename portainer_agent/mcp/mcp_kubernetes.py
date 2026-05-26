"""MCP tools for kubernetes operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(tags={"Kubernetes"})
    async def portainer_kubernetes(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release'"
        ),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        chart_name: str | None = Field(default=None, description="chart name"),
        release_name: str | None = Field(default=None, description="release name"),
        client=Depends(get_client),
    ) -> dict:
        """Manage kubernetes operations."""
        kwargs: dict[str, Any]
        if action == "get_k8s_dashboard":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_dashboard(**kwargs)
        if action == "get_k8s_namespaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_namespaces(**kwargs)
        if action == "get_k8s_applications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_applications(**kwargs)
        if action == "get_k8s_services":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_services(**kwargs)
        if action == "get_k8s_ingresses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_ingresses(**kwargs)
        if action == "get_k8s_configmaps":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_configmaps(**kwargs)
        if action == "get_k8s_secrets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_secrets(**kwargs)
        if action == "get_k8s_volumes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_volumes(**kwargs)
        if action == "get_k8s_events":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_events(**kwargs)
        if action == "get_k8s_nodes_limits":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_nodes_limits(**kwargs)
        if action == "get_k8s_metrics_nodes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_k8s_metrics_nodes(**kwargs)
        if action == "get_helm_releases":
            kwargs = {"endpoint_id": endpoint_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_helm_releases(**kwargs)
        if action == "install_helm_chart":
            kwargs = {
                "endpoint_id": endpoint_id,
                "chart_name": chart_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.install_helm_chart(**kwargs)
        if action == "delete_helm_release":
            kwargs = {
                "endpoint_id": endpoint_id,
                "release_name": release_name,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_helm_release(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release"
        )
