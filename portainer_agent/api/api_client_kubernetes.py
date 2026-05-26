#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_kubernetes_config(self) -> dict:
        """Get Kubernetes global configuration."""
        return self._get("kubernetes/config")

    def get_kubernetes_dashboard(self, environment_id: int) -> dict:
        """Get Kubernetes dashboard data."""
        return self._get(f"kubernetes/{environment_id}/dashboard")

    def get_kubernetes_namespaces(self, environment_id: int) -> Any:
        """List Kubernetes namespaces."""
        return self._get(f"kubernetes/{environment_id}/namespaces")

    def get_kubernetes_namespace(self, environment_id: int, namespace: str) -> dict:
        """Get a specific Kubernetes namespace."""
        return self._get(f"kubernetes/{environment_id}/namespaces/{namespace}")

    def create_kubernetes_namespace(
        self, environment_id: int, namespace: str, **kwargs
    ) -> dict:
        """Create a Kubernetes namespace."""
        return self._post(
            f"kubernetes/{environment_id}/namespaces/{namespace}", data=kwargs
        )

    def update_kubernetes_namespace(
        self, environment_id: int, namespace: str, **kwargs
    ) -> dict:
        """Update a Kubernetes namespace."""
        return self._put(
            f"kubernetes/{environment_id}/namespaces/{namespace}", data=kwargs
        )

    def delete_kubernetes_namespace(self, environment_id: int, namespace: str) -> bool:
        """Delete a Kubernetes namespace."""
        return self._delete(f"kubernetes/{environment_id}/namespaces/{namespace}")

    def get_kubernetes_namespace_count(self, environment_id: int) -> dict:
        """Get namespace count."""
        return self._get(f"kubernetes/{environment_id}/namespaces/count")

    def get_kubernetes_applications(self, environment_id: int, **filters) -> Any:
        """List Kubernetes applications (deployments, statefulsets, daemonsets)."""
        return self._list(f"kubernetes/{environment_id}/applications", **filters)

    def get_kubernetes_application_count(self, environment_id: int) -> dict:
        """Get application count."""
        return self._get(f"kubernetes/{environment_id}/applications/count")

    def get_kubernetes_services(self, environment_id: int, **filters) -> Any:
        """List Kubernetes services."""
        return self._list(f"kubernetes/{environment_id}/services", **filters)

    def get_kubernetes_service_count(self, environment_id: int) -> dict:
        """Get service count."""
        return self._get(f"kubernetes/{environment_id}/services/count")

    def delete_kubernetes_services(
        self, environment_id: int, payload: list[dict]
    ) -> bool:
        """Delete Kubernetes services."""
        return self._post(f"kubernetes/{environment_id}/services/delete", data=payload)

    def get_kubernetes_namespace_services(
        self, environment_id: int, namespace: str
    ) -> Any:
        """List services in a specific namespace."""
        return self._get(f"kubernetes/{environment_id}/namespaces/{namespace}/services")

    def get_kubernetes_ingresses(self, environment_id: int, **filters) -> Any:
        """List Kubernetes ingresses."""
        return self._list(f"kubernetes/{environment_id}/ingresses", **filters)

    def get_kubernetes_ingress_count(self, environment_id: int) -> dict:
        """Get ingress count."""
        return self._get(f"kubernetes/{environment_id}/ingresses/count")

    def delete_kubernetes_ingresses(
        self, environment_id: int, payload: list[dict]
    ) -> bool:
        """Delete Kubernetes ingresses."""
        return self._post(f"kubernetes/{environment_id}/ingresses/delete", data=payload)

    def get_kubernetes_configmaps(self, environment_id: int, **filters) -> Any:
        """List Kubernetes configmaps."""
        return self._list(f"kubernetes/{environment_id}/configmaps", **filters)

    def get_kubernetes_configmap_count(self, environment_id: int) -> dict:
        """Get configmap count."""
        return self._get(f"kubernetes/{environment_id}/configmaps/count")

    def get_kubernetes_secrets(self, environment_id: int, **filters) -> Any:
        """List Kubernetes secrets."""
        return self._list(f"kubernetes/{environment_id}/secrets", **filters)

    def get_kubernetes_secret_count(self, environment_id: int) -> dict:
        """Get secret count."""
        return self._get(f"kubernetes/{environment_id}/secrets/count")

    def get_kubernetes_volumes(self, environment_id: int, **filters) -> Any:
        """List Kubernetes persistent volume claims."""
        return self._list(f"kubernetes/{environment_id}/volumes", **filters)

    def get_kubernetes_volume_count(self, environment_id: int) -> dict:
        """Get volume count."""
        return self._get(f"kubernetes/{environment_id}/volumes/count")

    def delete_kubernetes_volume(
        self, environment_id: int, namespace: str, volume: str
    ) -> bool:
        """Delete a Kubernetes volume."""
        return self._delete(f"kubernetes/{environment_id}/volumes/{namespace}/{volume}")

    def get_kubernetes_events(self, environment_id: int) -> Any:
        """List Kubernetes events."""
        return self._get(f"kubernetes/{environment_id}/events")

    def get_kubernetes_namespace_events(
        self, environment_id: int, namespace: str
    ) -> Any:
        """List events in a specific namespace."""
        return self._get(f"kubernetes/{environment_id}/namespaces/{namespace}/events")

    def describe_kubernetes_resource(self, environment_id: int, **kwargs) -> dict:
        """Describe a Kubernetes resource."""
        return self._get(f"kubernetes/{environment_id}/describe", params=kwargs)

    def get_kubernetes_nodes_limits(self, environment_id: int) -> dict:
        """Get Kubernetes node resource limits."""
        return self._get(f"kubernetes/{environment_id}/nodes_limits")

    def get_kubernetes_max_resource_limits(self, environment_id: int) -> dict:
        """Get max resource limits for the cluster."""
        return self._get(f"kubernetes/{environment_id}/max_resource_limits")

    def drain_kubernetes_node(self, environment_id: int, node_name: str) -> bool:
        """Drain a Kubernetes node."""
        return self._post(f"kubernetes/{environment_id}/nodes/{node_name}/drain")

    def get_kubernetes_rbac_enabled(self, environment_id: int) -> dict:
        """Check if RBAC is enabled on the cluster."""
        return self._get(f"kubernetes/{environment_id}/rbac_enabled")

    def get_kubernetes_metrics_nodes(self, environment_id: int) -> Any:
        """Get metrics for Kubernetes nodes."""
        return self._get(f"kubernetes/{environment_id}/metrics/nodes")

    def get_kubernetes_metrics_node(self, environment_id: int, node_name: str) -> dict:
        """Get metrics for a specific node."""
        return self._get(f"kubernetes/{environment_id}/metrics/nodes/{node_name}")

    def get_kubernetes_metrics_applications(self, environment_id: int) -> Any:
        """Get application resource metrics."""
        return self._get(f"kubernetes/{environment_id}/metrics/applications_resources")

    def get_kubernetes_ingress_controllers(self, environment_id: int) -> Any:
        """List Kubernetes ingress controllers."""
        return self._get(f"kubernetes/{environment_id}/ingresscontrollers")

    def get_kubernetes_roles(self, environment_id: int) -> Any:
        """List Kubernetes roles."""
        return self._get(f"kubernetes/{environment_id}/roles")

    def get_kubernetes_cluster_roles(self, environment_id: int) -> Any:
        """List Kubernetes cluster roles."""
        return self._get(f"kubernetes/{environment_id}/clusterroles")

    def get_kubernetes_role_bindings(self, environment_id: int) -> Any:
        """List Kubernetes role bindings."""
        return self._get(f"kubernetes/{environment_id}/rolebindings")

    def get_kubernetes_cluster_role_bindings(self, environment_id: int) -> Any:
        """List Kubernetes cluster role bindings."""
        return self._get(f"kubernetes/{environment_id}/clusterrolebindings")

    def get_kubernetes_service_accounts(self, environment_id: int) -> Any:
        """List Kubernetes service accounts."""
        return self._get(f"kubernetes/{environment_id}/serviceaccounts")

    def get_kubernetes_jobs(self, environment_id: int) -> Any:
        """List Kubernetes jobs."""
        return self._get(f"kubernetes/{environment_id}/jobs")

    def get_kubernetes_cron_jobs(self, environment_id: int) -> Any:
        """List Kubernetes cron jobs."""
        return self._get(f"kubernetes/{environment_id}/cron_jobs")

    def get_helm_releases(self, endpoint_id: int) -> Any:
        """List Helm releases for an environment."""
        return self._get(f"endpoints/{endpoint_id}/kubernetes/helm")

    def install_helm_chart(self, endpoint_id: int, chart_name: str, **kwargs) -> dict:
        """Install a Helm chart."""
        data = {"ChartName": chart_name, **kwargs}
        return self._post(f"endpoints/{endpoint_id}/kubernetes/helm", data=data)

    def delete_helm_release(self, endpoint_id: int, release_name: str) -> bool:
        """Delete a Helm release."""
        return self._delete(f"endpoints/{endpoint_id}/kubernetes/helm/{release_name}")

    def get_helm_release_history(self, endpoint_id: int, release_name: str) -> Any:
        """Get Helm release history."""
        return self._get(
            f"endpoints/{endpoint_id}/kubernetes/helm/{release_name}/history"
        )

    def rollback_helm_release(
        self, endpoint_id: int, release_name: str, revision: int
    ) -> dict:
        """Rollback a Helm release to a specific revision."""
        return self._post(
            f"endpoints/{endpoint_id}/kubernetes/helm/{release_name}/rollback",
            data={"Revision": revision},
        )
