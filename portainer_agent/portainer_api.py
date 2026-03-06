#!/usr/bin/python
# coding: utf-8
"""
Portainer API Wrapper — Complete REST client for the Portainer CE API v2.39.0.

Covers 185 endpoints across 10 domain groups:
  Auth, Environments, Docker, Stacks, Kubernetes, Edge,
  Templates, Users, Registries, System.

Authentication: JWT token via X-API-Key header or Bearer token.
Pagination: List methods support limit/offset via query params.
"""

import logging
from typing import Any, Dict, List, Optional

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class PortainerApi:
    """REST client for the Portainer CE API."""

    def __init__(
        self,
        base_url: str = "http://localhost:9000",
        token: str = "",
        verify: bool = True,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_base = f"{self.base_url}/api"
        self.session = requests.Session()
        self.session.verify = verify
        if token:
            self.session.headers.update({"X-API-Key": token})
        self.session.headers.update({"Accept": "application/json"})

    # ── Generic helpers ──────────────────────────────────────────────────

    def _url(self, endpoint: str) -> str:
        return f"{self.api_base}/{endpoint.strip('/')}"

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        resp = self.session.get(self._url(endpoint), params=params)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _post(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.post(self._url(endpoint), json=data)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _put(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.put(self._url(endpoint), json=data)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _patch(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.patch(self._url(endpoint), json=data)
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _delete(self, endpoint: str, params: Optional[Dict] = None) -> bool:
        resp = self.session.delete(self._url(endpoint), params=params)
        resp.raise_for_status()
        return True

    def _list(
        self,
        endpoint: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **filters,
    ) -> Any:
        params = {k: v for k, v in filters.items() if v is not None}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["start"] = offset
        return self._get(endpoint, params=params)

    # ══════════════════════════════════════════════════════════════════════
    #  AUTH endpoints
    # ══════════════════════════════════════════════════════════════════════

    def authenticate(self, username: str, password: str) -> Dict:
        """Authenticate and get a JWT token."""
        return self._post("auth", data={"Username": username, "Password": password})

    def logout(self) -> bool:
        """Logout and invalidate the current token."""
        return self._post("auth/logout")

    def validate_oauth(self, code: str) -> Dict:
        """Validate an OAuth code."""
        return self._post("auth/oauth/validate", data={"Code": code})

    # ══════════════════════════════════════════════════════════════════════
    #  ENVIRONMENTS (endpoints) endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_endpoints(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Any:
        """List all environments (endpoints)."""
        return self._list("endpoints", limit=limit, offset=offset, **filters)

    def get_endpoint(self, endpoint_id: int) -> Dict:
        """Get a specific environment by ID."""
        return self._get(f"endpoints/{endpoint_id}")

    def create_endpoint(
        self, name: str, endpoint_type: int, url: str = "", **kwargs
    ) -> Dict:
        """Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes."""
        data = {
            "Name": name,
            "EndpointCreationType": endpoint_type,
            "URL": url,
            **kwargs,
        }
        return self._post("endpoints", data=data)

    def update_endpoint(self, endpoint_id: int, **kwargs) -> Dict:
        """Update an environment."""
        return self._put(f"endpoints/{endpoint_id}", data=kwargs)

    def delete_endpoints(self, endpoint_ids: List[int]) -> bool:
        """Delete multiple environments."""
        return self._post("endpoints/delete", data={"endpoints": endpoint_ids})

    def delete_endpoint(self, endpoint_id: int) -> bool:
        """Delete a single environment."""
        return self._delete(f"endpoints/{endpoint_id}")

    def snapshot_endpoint(self, endpoint_id: int) -> bool:
        """Take a snapshot of a specific environment."""
        return self._post(f"endpoints/{endpoint_id}/snapshot")

    def snapshot_all_endpoints(self) -> bool:
        """Take a snapshot of all environments."""
        return self._post("endpoints/snapshot")

    def get_endpoint_settings(self, endpoint_id: int) -> Dict:
        """Get environment settings."""
        return self._get(f"endpoints/{endpoint_id}/settings")

    def update_endpoint_settings(self, endpoint_id: int, **kwargs) -> Dict:
        """Update environment settings."""
        return self._put(f"endpoints/{endpoint_id}/settings", data=kwargs)

    def get_endpoint_registries(self, endpoint_id: int) -> Any:
        """List registries for an environment."""
        return self._get(f"endpoints/{endpoint_id}/registries")

    def get_endpoint_relations(self) -> Any:
        """Get environment relations."""
        return self._get("endpoints/relations")

    def remove_endpoint_association(self, endpoint_id: int) -> bool:
        """Remove edge environment association."""
        return self._put(f"endpoints/{endpoint_id}/association")

    # ── Endpoint groups ──────────────────────────────────────────────────

    def get_endpoint_groups(self) -> Any:
        """List all endpoint groups."""
        return self._get("endpoint_groups")

    def get_endpoint_group(self, group_id: int) -> Dict:
        """Get a specific endpoint group."""
        return self._get(f"endpoint_groups/{group_id}")

    def create_endpoint_group(self, name: str, description: str = "", **kwargs) -> Dict:
        """Create an endpoint group."""
        data = {"Name": name, "Description": description, **kwargs}
        return self._post("endpoint_groups", data=data)

    def update_endpoint_group(self, group_id: int, **kwargs) -> Dict:
        """Update an endpoint group."""
        return self._put(f"endpoint_groups/{group_id}", data=kwargs)

    def delete_endpoint_group(self, group_id: int) -> bool:
        """Delete an endpoint group."""
        return self._delete(f"endpoint_groups/{group_id}")

    def add_endpoint_to_group(self, group_id: int, endpoint_id: int) -> bool:
        """Add an environment to a group."""
        return self._put(f"endpoint_groups/{group_id}/endpoints/{endpoint_id}")

    def remove_endpoint_from_group(self, group_id: int, endpoint_id: int) -> bool:
        """Remove an environment from a group."""
        return self._delete(f"endpoint_groups/{group_id}/endpoints/{endpoint_id}")

    # ══════════════════════════════════════════════════════════════════════
    #  DOCKER endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_docker_dashboard(self, environment_id: int) -> Dict:
        """Get Docker dashboard data for an environment."""
        return self._get(f"docker/{environment_id}/dashboard")

    def get_docker_images(self, environment_id: int) -> Any:
        """List Docker images in an environment."""
        return self._get(f"docker/{environment_id}/images")

    def get_container_gpus(self, environment_id: int, container_id: str) -> Dict:
        """Get GPU info for a container."""
        return self._get(f"docker/{environment_id}/containers/{container_id}/gpus")

    # ══════════════════════════════════════════════════════════════════════
    #  STACKS endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_stacks(self, **filters) -> Any:
        """List all stacks."""
        return self._list("stacks", **filters)

    def get_stack(self, stack_id: int) -> Dict:
        """Get a specific stack."""
        return self._get(f"stacks/{stack_id}")

    def get_stack_by_name(self, name: str) -> Dict:
        """Get a stack by name."""
        return self._get(f"stacks/name/{name}")

    def get_stack_file(self, stack_id: int) -> Dict:
        """Get the compose file content for a stack."""
        return self._get(f"stacks/{stack_id}/file")

    def create_standalone_stack_from_string(
        self, name: str, file_content: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a standalone Docker Compose stack from a string."""
        data = {"Name": name, "StackFileContent": file_content, **kwargs}
        return self._post(
            f"stacks/create/standalone/string?endpointId={endpoint_id}", data=data
        )

    def create_standalone_stack_from_repository(
        self, name: str, repo_url: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a standalone stack from a Git repository."""
        data = {"Name": name, "RepositoryURL": repo_url, **kwargs}
        return self._post(
            f"stacks/create/standalone/repository?endpointId={endpoint_id}", data=data
        )

    def create_swarm_stack_from_string(
        self, name: str, file_content: str, swarm_id: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a Swarm stack from a string."""
        data = {
            "Name": name,
            "StackFileContent": file_content,
            "SwarmID": swarm_id,
            **kwargs,
        }
        return self._post(
            f"stacks/create/swarm/string?endpointId={endpoint_id}", data=data
        )

    def create_swarm_stack_from_repository(
        self, name: str, repo_url: str, swarm_id: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a Swarm stack from a Git repository."""
        data = {"Name": name, "RepositoryURL": repo_url, "SwarmID": swarm_id, **kwargs}
        return self._post(
            f"stacks/create/swarm/repository?endpointId={endpoint_id}", data=data
        )

    def create_kubernetes_stack_from_string(
        self, name: str, file_content: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a Kubernetes stack from a string."""
        data = {"StackName": name, "StackFileContent": file_content, **kwargs}
        return self._post(
            f"stacks/create/kubernetes/string?endpointId={endpoint_id}", data=data
        )

    def create_kubernetes_stack_from_repository(
        self, name: str, repo_url: str, endpoint_id: int, **kwargs
    ) -> Dict:
        """Create a Kubernetes stack from a Git repository."""
        data = {"StackName": name, "RepositoryURL": repo_url, **kwargs}
        return self._post(
            f"stacks/create/kubernetes/repository?endpointId={endpoint_id}", data=data
        )

    def update_stack(self, stack_id: int, endpoint_id: int, **kwargs) -> Dict:
        """Update a stack."""
        return self._put(f"stacks/{stack_id}?endpointId={endpoint_id}", data=kwargs)

    def delete_stack(self, stack_id: int, endpoint_id: int) -> bool:
        """Delete a stack."""
        return self._delete(f"stacks/{stack_id}", params={"endpointId": endpoint_id})

    def start_stack(self, stack_id: int, endpoint_id: int) -> Dict:
        """Start a stopped stack."""
        return self._post(f"stacks/{stack_id}/start", data={"endpointId": endpoint_id})

    def stop_stack(self, stack_id: int, endpoint_id: int) -> Dict:
        """Stop a running stack."""
        return self._post(f"stacks/{stack_id}/stop", data={"endpointId": endpoint_id})

    def migrate_stack(
        self, stack_id: int, endpoint_id: int, target_endpoint_id: int, **kwargs
    ) -> Dict:
        """Migrate a stack to another environment."""
        data = {"EndpointID": target_endpoint_id, **kwargs}
        return self._post(
            f"stacks/{stack_id}/migrate?endpointId={endpoint_id}", data=data
        )

    def update_stack_git(self, stack_id: int, endpoint_id: int, **kwargs) -> Dict:
        """Update a stack's Git settings."""
        return self._put(f"stacks/{stack_id}/git?endpointId={endpoint_id}", data=kwargs)

    def redeploy_stack_git(self, stack_id: int, endpoint_id: int, **kwargs) -> Dict:
        """Redeploy a stack from its Git config."""
        return self._put(
            f"stacks/{stack_id}/git/redeploy?endpointId={endpoint_id}", data=kwargs
        )

    def associate_stack(self, stack_id: int, endpoint_id: int, **kwargs) -> Dict:
        """Associate an orphaned stack."""
        return self._put(
            f"stacks/{stack_id}/associate?endpointId={endpoint_id}", data=kwargs
        )

    # ══════════════════════════════════════════════════════════════════════
    #  KUBERNETES endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_kubernetes_config(self) -> Dict:
        """Get Kubernetes global configuration."""
        return self._get("kubernetes/config")

    def get_kubernetes_dashboard(self, environment_id: int) -> Dict:
        """Get Kubernetes dashboard data."""
        return self._get(f"kubernetes/{environment_id}/dashboard")

    def get_kubernetes_namespaces(self, environment_id: int) -> Any:
        """List Kubernetes namespaces."""
        return self._get(f"kubernetes/{environment_id}/namespaces")

    def get_kubernetes_namespace(self, environment_id: int, namespace: str) -> Dict:
        """Get a specific Kubernetes namespace."""
        return self._get(f"kubernetes/{environment_id}/namespaces/{namespace}")

    def create_kubernetes_namespace(
        self, environment_id: int, namespace: str, **kwargs
    ) -> Dict:
        """Create a Kubernetes namespace."""
        return self._post(
            f"kubernetes/{environment_id}/namespaces/{namespace}", data=kwargs
        )

    def update_kubernetes_namespace(
        self, environment_id: int, namespace: str, **kwargs
    ) -> Dict:
        """Update a Kubernetes namespace."""
        return self._put(
            f"kubernetes/{environment_id}/namespaces/{namespace}", data=kwargs
        )

    def delete_kubernetes_namespace(self, environment_id: int, namespace: str) -> bool:
        """Delete a Kubernetes namespace."""
        return self._delete(f"kubernetes/{environment_id}/namespaces/{namespace}")

    def get_kubernetes_namespace_count(self, environment_id: int) -> Dict:
        """Get namespace count."""
        return self._get(f"kubernetes/{environment_id}/namespaces/count")

    def get_kubernetes_applications(self, environment_id: int, **filters) -> Any:
        """List Kubernetes applications (deployments, statefulsets, daemonsets)."""
        return self._list(f"kubernetes/{environment_id}/applications", **filters)

    def get_kubernetes_application_count(self, environment_id: int) -> Dict:
        """Get application count."""
        return self._get(f"kubernetes/{environment_id}/applications/count")

    def get_kubernetes_services(self, environment_id: int, **filters) -> Any:
        """List Kubernetes services."""
        return self._list(f"kubernetes/{environment_id}/services", **filters)

    def get_kubernetes_service_count(self, environment_id: int) -> Dict:
        """Get service count."""
        return self._get(f"kubernetes/{environment_id}/services/count")

    def delete_kubernetes_services(
        self, environment_id: int, payload: List[Dict]
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

    def get_kubernetes_ingress_count(self, environment_id: int) -> Dict:
        """Get ingress count."""
        return self._get(f"kubernetes/{environment_id}/ingresses/count")

    def delete_kubernetes_ingresses(
        self, environment_id: int, payload: List[Dict]
    ) -> bool:
        """Delete Kubernetes ingresses."""
        return self._post(f"kubernetes/{environment_id}/ingresses/delete", data=payload)

    def get_kubernetes_configmaps(self, environment_id: int, **filters) -> Any:
        """List Kubernetes configmaps."""
        return self._list(f"kubernetes/{environment_id}/configmaps", **filters)

    def get_kubernetes_configmap_count(self, environment_id: int) -> Dict:
        """Get configmap count."""
        return self._get(f"kubernetes/{environment_id}/configmaps/count")

    def get_kubernetes_secrets(self, environment_id: int, **filters) -> Any:
        """List Kubernetes secrets."""
        return self._list(f"kubernetes/{environment_id}/secrets", **filters)

    def get_kubernetes_secret_count(self, environment_id: int) -> Dict:
        """Get secret count."""
        return self._get(f"kubernetes/{environment_id}/secrets/count")

    def get_kubernetes_volumes(self, environment_id: int, **filters) -> Any:
        """List Kubernetes persistent volume claims."""
        return self._list(f"kubernetes/{environment_id}/volumes", **filters)

    def get_kubernetes_volume_count(self, environment_id: int) -> Dict:
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

    def describe_kubernetes_resource(self, environment_id: int, **kwargs) -> Dict:
        """Describe a Kubernetes resource."""
        return self._get(f"kubernetes/{environment_id}/describe", params=kwargs)

    def get_kubernetes_nodes_limits(self, environment_id: int) -> Dict:
        """Get Kubernetes node resource limits."""
        return self._get(f"kubernetes/{environment_id}/nodes_limits")

    def get_kubernetes_max_resource_limits(self, environment_id: int) -> Dict:
        """Get max resource limits for the cluster."""
        return self._get(f"kubernetes/{environment_id}/max_resource_limits")

    def drain_kubernetes_node(self, environment_id: int, node_name: str) -> bool:
        """Drain a Kubernetes node."""
        return self._post(f"kubernetes/{environment_id}/nodes/{node_name}/drain")

    def get_kubernetes_rbac_enabled(self, environment_id: int) -> Dict:
        """Check if RBAC is enabled on the cluster."""
        return self._get(f"kubernetes/{environment_id}/rbac_enabled")

    def get_kubernetes_metrics_nodes(self, environment_id: int) -> Any:
        """Get metrics for Kubernetes nodes."""
        return self._get(f"kubernetes/{environment_id}/metrics/nodes")

    def get_kubernetes_metrics_node(self, environment_id: int, node_name: str) -> Dict:
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

    # ── Helm ─────────────────────────────────────────────────────────────

    def get_helm_releases(self, endpoint_id: int) -> Any:
        """List Helm releases for an environment."""
        return self._get(f"endpoints/{endpoint_id}/kubernetes/helm")

    def install_helm_chart(self, endpoint_id: int, chart_name: str, **kwargs) -> Dict:
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
    ) -> Dict:
        """Rollback a Helm release to a specific revision."""
        return self._post(
            f"endpoints/{endpoint_id}/kubernetes/helm/{release_name}/rollback",
            data={"Revision": revision},
        )

    # ══════════════════════════════════════════════════════════════════════
    #  EDGE endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_edge_groups(self) -> Any:
        """List edge groups."""
        return self._get("edge_groups")

    def get_edge_group(self, group_id: int) -> Dict:
        """Get a specific edge group."""
        return self._get(f"edge_groups/{group_id}")

    def create_edge_group(self, name: str, **kwargs) -> Dict:
        """Create an edge group."""
        data = {"Name": name, **kwargs}
        return self._post("edge_groups", data=data)

    def update_edge_group(self, group_id: int, **kwargs) -> Dict:
        """Update an edge group."""
        return self._put(f"edge_groups/{group_id}", data=kwargs)

    def delete_edge_group(self, group_id: int) -> bool:
        """Delete an edge group."""
        return self._delete(f"edge_groups/{group_id}")

    # ── Edge Jobs ────────────────────────────────────────────────────────

    def get_edge_jobs(self) -> Any:
        """List edge jobs."""
        return self._get("edge_jobs")

    def get_edge_job(self, job_id: int) -> Dict:
        """Get a specific edge job."""
        return self._get(f"edge_jobs/{job_id}")

    def create_edge_job_from_string(
        self, name: str, file_content: str, **kwargs
    ) -> Dict:
        """Create an edge job from a string."""
        data = {"Name": name, "FileContent": file_content, **kwargs}
        return self._post("edge_jobs/create/string", data=data)

    def update_edge_job(self, job_id: int, **kwargs) -> Dict:
        """Update an edge job."""
        return self._put(f"edge_jobs/{job_id}", data=kwargs)

    def delete_edge_job(self, job_id: int) -> bool:
        """Delete an edge job."""
        return self._delete(f"edge_jobs/{job_id}")

    def get_edge_job_file(self, job_id: int) -> Dict:
        """Get the script file content for an edge job."""
        return self._get(f"edge_jobs/{job_id}/file")

    def get_edge_job_tasks(self, job_id: int) -> Any:
        """List tasks for an edge job."""
        return self._get(f"edge_jobs/{job_id}/tasks")

    def get_edge_job_task_logs(self, job_id: int, task_id: int) -> Dict:
        """Get logs for an edge job task."""
        return self._get(f"edge_jobs/{job_id}/tasks/{task_id}/logs")

    # ── Edge Stacks ──────────────────────────────────────────────────────

    def get_edge_stacks(self) -> Any:
        """List edge stacks."""
        return self._get("edge_stacks")

    def get_edge_stack(self, stack_id: int) -> Dict:
        """Get a specific edge stack."""
        return self._get(f"edge_stacks/{stack_id}")

    def create_edge_stack_from_string(
        self, name: str, file_content: str, edge_groups: List[int], **kwargs
    ) -> Dict:
        """Create an edge stack from a string."""
        data = {
            "Name": name,
            "StackFileContent": file_content,
            "EdgeGroups": edge_groups,
            **kwargs,
        }
        return self._post("edge_stacks/create/string", data=data)

    def create_edge_stack_from_repository(
        self, name: str, repo_url: str, edge_groups: List[int], **kwargs
    ) -> Dict:
        """Create an edge stack from a Git repository."""
        data = {
            "Name": name,
            "RepositoryURL": repo_url,
            "EdgeGroups": edge_groups,
            **kwargs,
        }
        return self._post("edge_stacks/create/repository", data=data)

    def update_edge_stack(self, stack_id: int, **kwargs) -> Dict:
        """Update an edge stack."""
        return self._put(f"edge_stacks/{stack_id}", data=kwargs)

    def delete_edge_stack(self, stack_id: int) -> bool:
        """Delete an edge stack."""
        return self._delete(f"edge_stacks/{stack_id}")

    def get_edge_stack_file(self, stack_id: int) -> Dict:
        """Get the compose file content for an edge stack."""
        return self._get(f"edge_stacks/{stack_id}/file")

    def get_edge_stack_status(self, stack_id: int) -> Dict:
        """Get edge stack deployment status."""
        return self._get(f"edge_stacks/{stack_id}/status")

    # ══════════════════════════════════════════════════════════════════════
    #  TEMPLATES endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_templates(self) -> Any:
        """List app templates."""
        return self._get("templates")

    def get_template_file(self, template_id: int) -> Dict:
        """Get template compose file."""
        return self._get(f"templates/{template_id}/file")

    def get_helm_templates(self) -> Any:
        """List Helm chart templates."""
        return self._get("templates/helm")

    # ── Custom Templates ─────────────────────────────────────────────────

    def get_custom_templates(self) -> Any:
        """List custom templates."""
        return self._get("custom_templates")

    def get_custom_template(self, template_id: int) -> Dict:
        """Get a specific custom template."""
        return self._get(f"custom_templates/{template_id}")

    def create_custom_template_from_string(
        self,
        title: str,
        description: str,
        file_content: str,
        template_type: int = 2,
        **kwargs,
    ) -> Dict:
        """Create a custom template from a string. Types: 1=swarm, 2=compose, 3=kubernetes."""
        data = {
            "Title": title,
            "Description": description,
            "FileContent": file_content,
            "Type": template_type,
            **kwargs,
        }
        return self._post("custom_templates/create/string", data=data)

    def create_custom_template_from_repository(
        self,
        title: str,
        description: str,
        repo_url: str,
        template_type: int = 2,
        **kwargs,
    ) -> Dict:
        """Create a custom template from a Git repository."""
        data = {
            "Title": title,
            "Description": description,
            "RepositoryURL": repo_url,
            "Type": template_type,
            **kwargs,
        }
        return self._post("custom_templates/create/repository", data=data)

    def update_custom_template(self, template_id: int, **kwargs) -> Dict:
        """Update a custom template."""
        return self._put(f"custom_templates/{template_id}", data=kwargs)

    def delete_custom_template(self, template_id: int) -> bool:
        """Delete a custom template."""
        return self._delete(f"custom_templates/{template_id}")

    def get_custom_template_file(self, template_id: int) -> Dict:
        """Get custom template compose file content."""
        return self._get(f"custom_templates/{template_id}/file")

    def git_fetch_custom_template(self, template_id: int) -> Dict:
        """Fetch latest version of a custom template from Git."""
        return self._put(f"custom_templates/{template_id}/git_fetch")

    # ══════════════════════════════════════════════════════════════════════
    #  USERS / TEAMS / ROLES endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_users(self) -> Any:
        """List all users."""
        return self._get("users")

    def get_user(self, user_id: int) -> Dict:
        """Get a specific user."""
        return self._get(f"users/{user_id}")

    def get_current_user(self) -> Dict:
        """Get the currently authenticated user."""
        return self._get("users/me")

    def create_user(self, username: str, password: str, role: int = 2) -> Dict:
        """Create a user. Roles: 1=admin, 2=standard."""
        return self._post(
            "users", data={"Username": username, "Password": password, "Role": role}
        )

    def update_user(self, user_id: int, **kwargs) -> Dict:
        """Update a user."""
        return self._put(f"users/{user_id}", data=kwargs)

    def delete_user(self, user_id: int) -> bool:
        """Delete a user."""
        return self._delete(f"users/{user_id}")

    def change_user_password(
        self, user_id: int, password: str, new_password: str
    ) -> bool:
        """Change a user's password."""
        return self._put(
            f"users/{user_id}/passwd",
            data={"Password": password, "NewPassword": new_password},
        )

    def check_admin_init(self) -> Dict:
        """Check if admin user has been initialized."""
        return self._get("users/admin/check")

    def init_admin(self, username: str, password: str) -> Dict:
        """Initialize the admin user (first-time setup)."""
        return self._post(
            "users/admin/init", data={"Username": username, "Password": password}
        )

    def get_user_memberships(self, user_id: int) -> Any:
        """Get team memberships for a user."""
        return self._get(f"users/{user_id}/memberships")

    def get_user_tokens(self, user_id: int) -> Any:
        """List API tokens for a user."""
        return self._get(f"users/{user_id}/tokens")

    def create_user_token(self, user_id: int, description: str = "", **kwargs) -> Dict:
        """Create an API token for a user."""
        return self._post(
            f"users/{user_id}/tokens", data={"Description": description, **kwargs}
        )

    def delete_user_token(self, user_id: int, key_id: int) -> bool:
        """Delete an API token."""
        return self._delete(f"users/{user_id}/tokens/{key_id}")

    # ── Teams ────────────────────────────────────────────────────────────

    def get_teams(self) -> Any:
        """List all teams."""
        return self._get("teams")

    def get_team(self, team_id: int) -> Dict:
        """Get a specific team."""
        return self._get(f"teams/{team_id}")

    def create_team(self, name: str) -> Dict:
        """Create a team."""
        return self._post("teams", data={"Name": name})

    def update_team(self, team_id: int, name: str) -> Dict:
        """Update a team."""
        return self._put(f"teams/{team_id}", data={"Name": name})

    def delete_team(self, team_id: int) -> bool:
        """Delete a team."""
        return self._delete(f"teams/{team_id}")

    def get_team_memberships_by_team(self, team_id: int) -> Any:
        """List memberships for a team."""
        return self._get(f"teams/{team_id}/memberships")

    # ── Team memberships ─────────────────────────────────────────────────

    def get_team_memberships(self) -> Any:
        """List all team memberships."""
        return self._get("team_memberships")

    def create_team_membership(self, user_id: int, team_id: int, role: int = 2) -> Dict:
        """Create a team membership. Roles: 1=leader, 2=member."""
        return self._post(
            "team_memberships",
            data={"UserID": user_id, "TeamID": team_id, "Role": role},
        )

    def update_team_membership(self, membership_id: int, **kwargs) -> Dict:
        """Update a team membership."""
        return self._put(f"team_memberships/{membership_id}", data=kwargs)

    def delete_team_membership(self, membership_id: int) -> bool:
        """Delete a team membership."""
        return self._delete(f"team_memberships/{membership_id}")

    # ── Roles ────────────────────────────────────────────────────────────

    def get_roles(self) -> Any:
        """List all roles."""
        return self._get("roles")

    # ── Resource controls ────────────────────────────────────────────────

    def get_resource_controls(self) -> Any:
        """List all resource controls."""
        return self._get("resource_controls")

    def create_resource_control(
        self, resource_id: str, resource_type: str, **kwargs
    ) -> Dict:
        """Create a resource control."""
        data = {"ResourceID": resource_id, "Type": resource_type, **kwargs}
        return self._post("resource_controls", data=data)

    def update_resource_control(self, control_id: int, **kwargs) -> Dict:
        """Update a resource control."""
        return self._put(f"resource_controls/{control_id}", data=kwargs)

    def delete_resource_control(self, control_id: int) -> bool:
        """Delete a resource control."""
        return self._delete(f"resource_controls/{control_id}")

    # ══════════════════════════════════════════════════════════════════════
    #  REGISTRIES endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_registries(self) -> Any:
        """List all Docker registries."""
        return self._get("registries")

    def get_registry(self, registry_id: int) -> Dict:
        """Get a specific registry."""
        return self._get(f"registries/{registry_id}")

    def create_registry(
        self, name: str, registry_type: int, url: str, **kwargs
    ) -> Dict:
        """Create a registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub."""
        data = {"Name": name, "Type": registry_type, "URL": url, **kwargs}
        return self._post("registries", data=data)

    def update_registry(self, registry_id: int, **kwargs) -> Dict:
        """Update a registry."""
        return self._put(f"registries/{registry_id}", data=kwargs)

    def delete_registry(self, registry_id: int) -> bool:
        """Delete a registry."""
        return self._delete(f"registries/{registry_id}")

    def configure_registry(self, registry_id: int, **kwargs) -> Dict:
        """Configure registry access for an environment."""
        return self._post(f"registries/{registry_id}/configure", data=kwargs)

    def ping_registry(self) -> Dict:
        """Test registry connectivity."""
        return self._get("registries/ping")

    # ══════════════════════════════════════════════════════════════════════
    #  SYSTEM endpoints
    # ══════════════════════════════════════════════════════════════════════

    def get_status(self) -> Dict:
        """Get Portainer instance status."""
        return self._get("status")

    def get_system_info(self) -> Dict:
        """Get system information."""
        return self._get("system/info")

    def get_system_status(self) -> Dict:
        """Get detailed system status."""
        return self._get("system/status")

    def get_system_version(self) -> Dict:
        """Get Portainer version information."""
        return self._get("system/version")

    def get_system_nodes(self) -> Any:
        """Get system nodes."""
        return self._get("system/nodes")

    def upgrade_system(self) -> Dict:
        """Trigger a system upgrade."""
        return self._post("system/upgrade")

    # ── Settings ─────────────────────────────────────────────────────────

    def get_settings(self) -> Dict:
        """Get Portainer settings."""
        return self._get("settings")

    def update_settings(self, **kwargs) -> Dict:
        """Update Portainer settings."""
        return self._put("settings", data=kwargs)

    def get_public_settings(self) -> Dict:
        """Get public (unauthenticated) settings."""
        return self._get("settings/public")

    # ── SSL ───────────────────────────────────────────────────────────────

    def get_ssl_settings(self) -> Dict:
        """Get SSL settings."""
        return self._get("ssl")

    def update_ssl_settings(self, **kwargs) -> Dict:
        """Update SSL settings."""
        return self._put("ssl", data=kwargs)

    # ── Backup / Restore ─────────────────────────────────────────────────

    def backup(self, password: str = "") -> Any:
        """Create a backup of Portainer data."""
        resp = self.session.post(self._url("backup"), json={"Password": password})
        resp.raise_for_status()
        return resp.content

    def restore(self, file_content: bytes, password: str = "") -> bool:
        """Restore Portainer data from a backup."""
        resp = self.session.post(
            self._url("restore"),
            json={"Password": password, "FileContent": list(file_content)},
        )
        resp.raise_for_status()
        return True

    # ── Tags ─────────────────────────────────────────────────────────────

    def get_tags(self) -> Any:
        """List all tags."""
        return self._get("tags")

    def create_tag(self, name: str) -> Dict:
        """Create a tag."""
        return self._post("tags", data={"Name": name})

    def delete_tag(self, tag_id: int) -> bool:
        """Delete a tag."""
        return self._delete(f"tags/{tag_id}")

    # ── LDAP ─────────────────────────────────────────────────────────────

    def check_ldap(self, **kwargs) -> Dict:
        """Check LDAP connectivity."""
        return self._post("ldap/check", data=kwargs)

    # ── MOTD ─────────────────────────────────────────────────────────────

    def get_motd(self) -> Dict:
        """Get the message of the day."""
        return self._get("motd")

    # ── Webhooks ─────────────────────────────────────────────────────────

    def get_webhooks(self) -> Any:
        """List all webhooks."""
        return self._get("webhooks")

    def create_webhook(
        self, resource_id: str, endpoint_id: int, webhook_type: int = 1, **kwargs
    ) -> Dict:
        """Create a webhook."""
        data = {
            "ResourceID": resource_id,
            "EndpointID": endpoint_id,
            "WebhookType": webhook_type,
            **kwargs,
        }
        return self._post("webhooks", data=data)

    def update_webhook(self, webhook_id: int, **kwargs) -> Dict:
        """Update a webhook."""
        return self._put(f"webhooks/{webhook_id}", data=kwargs)

    def delete_webhook(self, webhook_id: int) -> bool:
        """Delete a webhook."""
        return self._delete(f"webhooks/{webhook_id}")

    # ── GitOps ───────────────────────────────────────────────────────────

    def preview_git_file(
        self, repo_url: str, file_path: str = "docker-compose.yml", **kwargs
    ) -> Dict:
        """Preview a file from a Git repository."""
        data = {
            "RepositoryURL": repo_url,
            "ComposeFilePathInRepository": file_path,
            **kwargs,
        }
        return self._post("gitops/repo/file/preview", data=data)

    # ── Helm repositories (user-level) ───────────────────────────────────

    def get_user_helm_repositories(self, user_id: int) -> Any:
        """List Helm repositories for a user."""
        return self._get(f"users/{user_id}/helm/repositories")

    def create_user_helm_repository(self, user_id: int, url: str) -> Dict:
        """Add a Helm repository for a user."""
        return self._post(f"users/{user_id}/helm/repositories", data={"URL": url})

    def delete_user_helm_repository(self, user_id: int, repository_id: int) -> bool:
        """Remove a Helm repository for a user."""
        return self._delete(f"users/{user_id}/helm/repositories/{repository_id}")
