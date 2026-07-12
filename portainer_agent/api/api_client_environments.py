#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


def _entitled(namespace: str, names: list[str]) -> list[str]:
    """Filter ``names`` to the subset the calling identity's Okta/Keycloak groups
    entitle (CONCEPT:AU-OS.identity.identity-scoped-resource-autoload). Degrades
    to the full list if agent-utilities predates the resolver.
    """
    try:
        from agent_utilities.security.entitlements import identity_scoped_resources
    except Exception:
        return list(names)
    return list(identity_scoped_resources(namespace, names))


class Api(BaseApiClient):
    def get_endpoints(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> Any:
        """List all environments (endpoints) the caller is entitled to."""
        endpoints = self._list("endpoints", limit=limit, offset=offset, **filters)
        if isinstance(endpoints, list):
            names = [
                e["Name"] for e in endpoints if isinstance(e, dict) and e.get("Name")
            ]
            entitled = set(_entitled("portainer", names))
            endpoints = [
                e
                for e in endpoints
                if not isinstance(e, dict) or not e.get("Name") or e["Name"] in entitled
            ]
        return endpoints

    def get_endpoint(self, endpoint_id: int) -> dict:
        """Get a specific environment by ID. Denied if not entitled."""
        endpoint = self._get(f"endpoints/{endpoint_id}")
        name = endpoint.get("Name") if isinstance(endpoint, dict) else None
        if name and name not in _entitled("portainer", [name]):
            raise PermissionError(
                f"Your identity is not entitled to the Portainer environment '{name}'."
            )
        return endpoint

    def create_endpoint(
        self, name: str, endpoint_type: int, url: str = "", **kwargs
    ) -> dict:
        """Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes."""
        data = {
            "Name": name,
            "EndpointCreationType": endpoint_type,
            "URL": url,
            **kwargs,
        }
        return self._post("endpoints", data=data)

    def update_endpoint(self, endpoint_id: int, **kwargs) -> dict:
        """Update an environment."""
        return self._put(f"endpoints/{endpoint_id}", data=kwargs)

    def delete_endpoints(self, endpoint_ids: list[int]) -> bool:
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

    def get_endpoint_settings(self, endpoint_id: int) -> dict:
        """Get environment settings."""
        return self._get(f"endpoints/{endpoint_id}/settings")

    def update_endpoint_settings(self, endpoint_id: int, **kwargs) -> dict:
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

    def get_endpoint_groups(self) -> Any:
        """List all endpoint groups."""
        return self._get("endpoint_groups")

    def get_endpoint_group(self, group_id: int) -> dict:
        """Get a specific endpoint group."""
        return self._get(f"endpoint_groups/{group_id}")

    def create_endpoint_group(self, name: str, description: str = "", **kwargs) -> dict:
        """Create an endpoint group."""
        data = {"Name": name, "Description": description, **kwargs}
        return self._post("endpoint_groups", data=data)

    def update_endpoint_group(self, group_id: int, **kwargs) -> dict:
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
