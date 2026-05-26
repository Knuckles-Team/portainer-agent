#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_registries(self) -> Any:
        """List all Docker registries."""
        return self._get("registries")

    def get_registry(self, registry_id: int) -> dict:
        """Get a specific registry."""
        return self._get(f"registries/{registry_id}")

    def create_registry(
        self, name: str, registry_type: int, url: str, **kwargs
    ) -> dict:
        """Create a registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub."""
        data = {"Name": name, "Type": registry_type, "URL": url, **kwargs}
        return self._post("registries", data=data)

    def update_registry(self, registry_id: int, **kwargs) -> dict:
        """Update a registry."""
        return self._put(f"registries/{registry_id}", data=kwargs)

    def delete_registry(self, registry_id: int) -> bool:
        """Delete a registry."""
        return self._delete(f"registries/{registry_id}")

    def configure_registry(self, registry_id: int, **kwargs) -> dict:
        """Configure registry access for an environment."""
        return self._post(f"registries/{registry_id}/configure", data=kwargs)

    def ping_registry(self) -> dict:
        """Test registry connectivity."""
        return self._get("registries/ping")
