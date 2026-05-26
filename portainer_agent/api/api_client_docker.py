#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_docker_dashboard(self, environment_id: int) -> dict:
        """Get Docker dashboard data for an environment."""
        return self._get(f"docker/{environment_id}/dashboard")

    def get_docker_images(self, environment_id: int) -> Any:
        """List Docker images in an environment."""
        return self._get(f"docker/{environment_id}/images")

    def get_container_gpus(self, environment_id: int, container_id: str) -> dict:
        """Get GPU info for a container."""
        return self._get(f"docker/{environment_id}/containers/{container_id}/gpus")

    def _docker_url(self, endpoint_id: int, path: str) -> str:
        """Format a Docker proxy URL."""
        return f"endpoints/{endpoint_id}/docker/{path.lstrip('/')}"

    def list_containers(self, endpoint_id: int, **params) -> list[dict]:
        """List containers in an environment."""
        return self._get(
            self._docker_url(endpoint_id, "containers/json"), params=params
        )

    def create_container(
        self, endpoint_id: int, config: dict, name: str | None = None
    ) -> dict:
        """Create a container."""
        params = {"name": name} if name else {}
        return self._post(
            self._docker_url(endpoint_id, "containers/create"),
            data=config,
            params=params,
        )

    def inspect_container(self, endpoint_id: int, container_id: str) -> dict:
        """Inspect a container."""
        return self._get(
            self._docker_url(endpoint_id, f"containers/{container_id}/json")
        )

    def get_container_logs(self, endpoint_id: int, container_id: str, **params) -> str:
        """Get container logs."""

        if "stdout" not in params:
            params["stdout"] = True
        if "stderr" not in params:
            params["stderr"] = True
        if "timestamps" not in params:
            params["timestamps"] = True
        if "tail" not in params:
            params["tail"] = 50
        return self._get(
            self._docker_url(endpoint_id, f"containers/{container_id}/logs"),
            params=params,
        )

    def get_container_stats(
        self, endpoint_id: int, container_id: str, stream: bool = False
    ) -> Any:
        """Get container stats."""
        return self._get(
            self._docker_url(endpoint_id, f"containers/{container_id}/stats"),
            params={"stream": stream},
        )

    def start_container(self, endpoint_id: int, container_id: str) -> bool:
        """Start a container."""
        self._post(self._docker_url(endpoint_id, f"containers/{container_id}/start"))
        return True

    def stop_container(
        self, endpoint_id: int, container_id: str, timeout: int | None = None
    ) -> bool:
        """Stop a container."""
        params = {"t": timeout} if timeout else {}
        self._post(
            self._docker_url(endpoint_id, f"containers/{container_id}/stop"),
            params=params,
        )
        return True

    def restart_container(
        self, endpoint_id: int, container_id: str, timeout: int | None = None
    ) -> bool:
        """Restart a container."""
        params = {"t": timeout} if timeout else {}
        self._post(
            self._docker_url(endpoint_id, f"containers/{container_id}/restart"),
            params=params,
        )
        return True

    def remove_container(self, endpoint_id: int, container_id: str, **params) -> bool:
        """Remove a container."""
        return self._delete(
            self._docker_url(endpoint_id, f"containers/{container_id}"), params=params
        )

    def prune_containers(self, endpoint_id: int, filters: dict | None = None) -> dict:
        """Delete unused containers."""
        params = {"filters": filters} if filters else {}
        return self._post(
            self._docker_url(endpoint_id, "containers/prune"), data=params
        )

    def list_services(self, endpoint_id: int, **params) -> list[dict]:
        """List Swarm services."""
        return self._get(self._docker_url(endpoint_id, "services"), params=params)

    def inspect_service(self, endpoint_id: int, service_id: str) -> dict:
        """Inspect a Swarm service."""
        return self._get(self._docker_url(endpoint_id, f"services/{service_id}"))

    def get_service_logs(self, endpoint_id: int, service_id: str, **params) -> str:
        """Get Swarm service logs."""
        if "stdout" not in params:
            params["stdout"] = True
        if "stderr" not in params:
            params["stderr"] = True
        if "timestamps" not in params:
            params["timestamps"] = True
        if "tail" not in params:
            params["tail"] = 50
        return self._get(
            self._docker_url(endpoint_id, f"services/{service_id}/logs"), params=params
        )

    def remove_service(self, endpoint_id: int, service_id: str) -> bool:
        """Remove a Swarm service."""
        return self._delete(self._docker_url(endpoint_id, f"services/{service_id}"))

    def list_images(self, endpoint_id: int, **params) -> list[dict]:
        """List images in an environment."""
        return self._get(self._docker_url(endpoint_id, "images/json"), params=params)

    def inspect_image(self, endpoint_id: int, image_name: str) -> dict:
        """Inspect an image."""
        return self._get(self._docker_url(endpoint_id, f"images/{image_name}/json"))

    def get_image_history(self, endpoint_id: int, image_name: str) -> list[dict]:
        """Get image history."""
        return self._get(self._docker_url(endpoint_id, f"images/{image_name}/history"))

    def remove_image(self, endpoint_id: int, image_name: str, **params) -> bool:
        """Remove an image."""
        return self._delete(
            self._docker_url(endpoint_id, f"images/{image_name}"), params=params
        )

    def prune_images(self, endpoint_id: int, filters: dict | None = None) -> dict:
        """Delete unused images."""
        params = {"filters": filters} if filters else {}
        return self._post(self._docker_url(endpoint_id, "images/prune"), data=params)

    def list_networks(self, endpoint_id: int, **params) -> list[dict]:
        """List networks."""
        return self._get(self._docker_url(endpoint_id, "networks"), params=params)

    def inspect_network(self, endpoint_id: int, network_id: str) -> dict:
        """Inspect a network."""
        return self._get(self._docker_url(endpoint_id, f"networks/{network_id}"))

    def create_network(self, endpoint_id: int, config: dict) -> dict:
        """Create a network."""
        return self._post(self._docker_url(endpoint_id, "networks/create"), data=config)

    def remove_network(self, endpoint_id: int, network_id: str) -> bool:
        """Remove a network."""
        return self._delete(self._docker_url(endpoint_id, f"networks/{network_id}"))

    def prune_networks(self, endpoint_id: int, filters: dict | None = None) -> dict:
        """Delete unused networks."""
        params = {"filters": filters} if filters else {}
        return self._post(self._docker_url(endpoint_id, "networks/prune"), data=params)

    def list_volumes(self, endpoint_id: int, **params) -> dict:
        """List volumes."""
        return self._get(self._docker_url(endpoint_id, "volumes"), params=params)

    def inspect_volume(self, endpoint_id: int, volume_name: str) -> dict:
        """Inspect a volume."""
        return self._get(self._docker_url(endpoint_id, f"volumes/{volume_name}"))

    def create_volume(self, endpoint_id: int, config: dict) -> dict:
        """Create a volume."""
        return self._post(self._docker_url(endpoint_id, "volumes/create"), data=config)

    def remove_volume(
        self, endpoint_id: int, volume_name: str, force: bool = False
    ) -> bool:
        """Remove a volume."""
        return self._delete(
            self._docker_url(endpoint_id, f"volumes/{volume_name}"),
            params={"force": force},
        )

    def prune_volumes(self, endpoint_id: int, filters: dict | None = None) -> dict:
        """Delete unused volumes."""
        params = {"filters": filters} if filters else {}
        return self._post(self._docker_url(endpoint_id, "volumes/prune"), data=params)

    def create_exec(self, endpoint_id: int, container_id: str, config: dict) -> dict:
        """Create an exec instance."""
        return self._post(
            self._docker_url(endpoint_id, f"containers/{container_id}/exec"),
            data=config,
        )

    def start_exec(self, endpoint_id: int, exec_id: str, config: dict) -> Any:
        """Start an exec instance."""
        return self._post(
            self._docker_url(endpoint_id, f"exec/{exec_id}/start"), data=config
        )

    def inspect_exec(self, endpoint_id: int, exec_id: str) -> dict:
        """Inspect an exec instance."""
        return self._get(self._docker_url(endpoint_id, f"exec/{exec_id}/json"))

    def get_docker_info(self, endpoint_id: int) -> dict:
        """Get Docker system information."""
        return self._get(self._docker_url(endpoint_id, "info"))

    def get_docker_version(self, endpoint_id: int) -> dict:
        """Get Docker version information."""
        return self._get(self._docker_url(endpoint_id, "version"))

    def get_docker_events(self, endpoint_id: int, **params) -> Any:
        """Get Docker events."""
        return self._get(self._docker_url(endpoint_id, "events"), params=params)

    def get_docker_df(self, endpoint_id: int) -> dict:
        """Get Docker data usage information."""
        return self._get(self._docker_url(endpoint_id, "system/df"))

    def get_stack_logs(self, endpoint_id: int, stack_id: int, **params) -> str:
        """Get logs for all containers/services in a stack."""
        stack = self.get_stack(stack_id)  # type: ignore[attr-defined]
        stack_name = stack.get("Name")
        stack_type = stack.get("Type")

        logs = []
        if stack_type == 1:
            services = self.list_services(
                endpoint_id,
                filters=f'{{"label": ["com.docker.stack.namespace={stack_name}"]}}',
            )
            for svc in services:
                svc_id = str(svc.get("ID", ""))
                svc_name = svc.get("Spec", {}).get("Name", svc_id)
                svc_logs = self.get_service_logs(endpoint_id, svc_id, **params)
                logs.append(f"--- Service: {svc_name} ---\n{svc_logs}")
        else:
            filters = f'{{"label": ["com.docker.compose.project={stack_name}"]}}'
            containers = self.list_containers(endpoint_id, filters=filters, all=True)
            if not containers:
                filters = f'{{"label": ["com.portainer.stack.name={stack_name}"]}}'
                containers = self.list_containers(
                    endpoint_id, filters=filters, all=True
                )

            for container in containers:
                container_id = str(container.get("Id", ""))
                container_name = container.get("Names", [container_id])[0].lstrip("/")
                container_logs = self.get_container_logs(
                    endpoint_id, container_id, **params
                )
                logs.append(f"--- Container: {container_name} ---\n{container_logs}")

        return "\n\n".join(logs)
