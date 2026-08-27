"""MCP tools for kubernetes operations.

Auto-generated from mcp_server.py during ecosystem standardization.
"""

from typing import Any

from agent_utilities.mcp.concurrency import run_blocking
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from portainer_agent.auth import get_client


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(tags={"Kubernetes"})
    async def portainer_kubernetes(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release', 'get_k8s_namespace', 'create_k8s_namespace', 'update_k8s_namespace', 'delete_k8s_namespace', 'get_k8s_namespace_count', 'drain_k8s_node', 'describe_k8s_resource', 'get_k8s_rbac_enabled'"
        ),
        endpoint_id: int | None = Field(default=None, description="endpoint id"),
        chart_name: str | None = Field(default=None, description="chart name"),
        release_name: str | None = Field(default=None, description="release name"),
        environment_id: int | None = Field(
            default=None, description="kubernetes environment (endpoint) id"
        ),
        namespace: str | None = Field(default=None, description="namespace name"),
        node_name: str | None = Field(
            default=None, description="node name (for drain)"
        ),
        client=Depends(get_client),
    ) -> dict:
        """Manage kubernetes operations."""
        # Group 1: no-argument passthrough reads -- kwargs is always {} (an
        # empty dict filtered by "v is not None" is still {}).
        no_arg_methods = {
            "get_k8s_dashboard": client.get_k8s_dashboard,
            "get_k8s_namespaces": client.get_k8s_namespaces,
            "get_k8s_applications": client.get_k8s_applications,
            "get_k8s_services": client.get_k8s_services,
            "get_k8s_ingresses": client.get_k8s_ingresses,
            "get_k8s_configmaps": client.get_k8s_configmaps,
            "get_k8s_secrets": client.get_k8s_secrets,
            "get_k8s_volumes": client.get_k8s_volumes,
            "get_k8s_events": client.get_k8s_events,
            "get_k8s_nodes_limits": client.get_k8s_nodes_limits,
            "get_k8s_metrics_nodes": client.get_k8s_metrics_nodes,
        }
        if action in no_arg_methods:
            return await run_blocking(no_arg_methods[action])

        # Group 2: helm actions -- kwargs built from named params, then
        # None-valued entries are filtered out before the call.
        filtered_specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_helm_releases": (
                client.get_helm_releases,
                {"endpoint_id": endpoint_id},
            ),
            "install_helm_chart": (
                client.install_helm_chart,
                {"endpoint_id": endpoint_id, "chart_name": chart_name},
            ),
            "delete_helm_release": (
                client.delete_helm_release,
                {"endpoint_id": endpoint_id, "release_name": release_name},
            ),
        }
        if action in filtered_specs:
            method, kwargs = filtered_specs[action]
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return await run_blocking(method, **kwargs)

        # Group 3: namespace/node management -- params passed straight
        # through to the client WITHOUT None-filtering (unlike groups 1/2).
        direct_specs: dict[str, tuple[Any, dict[str, Any]]] = {
            "get_k8s_namespace": (
                client.get_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "create_k8s_namespace": (
                client.create_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "update_k8s_namespace": (
                client.update_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "delete_k8s_namespace": (
                client.delete_kubernetes_namespace,
                {"environment_id": environment_id, "namespace": namespace},
            ),
            "get_k8s_namespace_count": (
                client.get_kubernetes_namespace_count,
                {"environment_id": environment_id},
            ),
            "drain_k8s_node": (
                client.drain_kubernetes_node,
                {"environment_id": environment_id, "node_name": node_name},
            ),
            "describe_k8s_resource": (
                client.describe_kubernetes_resource,
                {"environment_id": environment_id},
            ),
            "get_k8s_rbac_enabled": (
                client.get_kubernetes_rbac_enabled,
                {"environment_id": environment_id},
            ),
        }
        if action in direct_specs:
            method, kwargs = direct_specs[action]
            return await run_blocking(method, **kwargs)

        # Unlike mcp_server.py's copy, this module has no resolve_action()
        # call, so this really is reachable for any action not covered by
        # the three dispatch dicts above (including no support for a
        # "list_actions"/"help"/"actions" discovery keyword -- see BUGS
        # FOUND). The malformed quoting in this message (missing the
        # opening quote before the first action name and the closing quote
        # after the last) is preserved verbatim, not fixed.
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_k8s_dashboard', 'get_k8s_namespaces', 'get_k8s_applications', 'get_k8s_services', 'get_k8s_ingresses', 'get_k8s_configmaps', 'get_k8s_secrets', 'get_k8s_volumes', 'get_k8s_events', 'get_k8s_nodes_limits', 'get_k8s_metrics_nodes', 'get_helm_releases', 'install_helm_chart', 'delete_helm_release', 'get_k8s_namespace', 'create_k8s_namespace', 'update_k8s_namespace', 'delete_k8s_namespace', 'get_k8s_namespace_count', 'drain_k8s_node', 'describe_k8s_resource', 'get_k8s_rbac_enabled"
        )
