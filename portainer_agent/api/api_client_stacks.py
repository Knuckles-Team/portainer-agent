#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_stacks(self, **filters) -> Any:
        """List all stacks."""
        return self._list("stacks", **filters)

    def get_stack(self, stack_id: int) -> dict:
        """Get a specific stack."""
        return self._get(f"stacks/{stack_id}")

    def get_stack_by_name(self, name: str) -> dict:
        """Get a stack by name."""
        return self._get(f"stacks/name/{name}")

    def get_stack_file(self, stack_id: int) -> dict:
        """Get the compose file content for a stack."""
        return self._get(f"stacks/{stack_id}/file")

    def export_all_stacks(self, target_dir: str) -> dict:
        """Export all stacks' compose definitions to a target directory."""
        import os

        os.makedirs(target_dir, exist_ok=True)
        stacks = self.get_stacks()
        if not isinstance(stacks, list):
            return {"error": f"Failed to list stacks: {stacks}"}

        exported = []
        errors = {}
        for s in stacks:
            s_id = s.get("Id") or s.get("id")
            s_name = s.get("Name") or s.get("name")
            if not s_id or not s_name:
                continue
            try:
                file_resp = self.get_stack_file(stack_id=s_id)
                content = file_resp.get("StackFileContent") or file_resp.get(
                    "stackFileContent"
                )
                if content:
                    file_path = os.path.join(target_dir, f"{s_name}.yml")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    exported.append(s_name)
                else:
                    errors[s_name] = (
                        f"No stack file content found in response: {file_resp}"
                    )
            except Exception as e:
                errors[s_name] = str(e)

        return {
            "status": "success",
            "exported_stacks": exported,
            "errors": errors,
            "target_directory": target_dir,
        }

    def create_standalone_stack_from_string(
        self, name: str, file_content: str, endpoint_id: int, **kwargs
    ) -> dict:
        """Create a standalone Docker Compose stack from a string."""
        data = {"Name": name, "StackFileContent": file_content, **kwargs}
        return self._post(
            f"stacks/create/standalone/string?endpointId={endpoint_id}", data=data
        )

    def create_standalone_stack_from_repository(
        self, name: str, repo_url: str, endpoint_id: int, **kwargs
    ) -> dict:
        """Create a standalone stack from a Git repository."""
        data = {"Name": name, "RepositoryURL": repo_url, **kwargs}
        return self._post(
            f"stacks/create/standalone/repository?endpointId={endpoint_id}", data=data
        )

    def create_swarm_stack_from_string(
        self, name: str, file_content: str, swarm_id: str, endpoint_id: int, **kwargs
    ) -> dict:
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
    ) -> dict:
        """Create a Swarm stack from a Git repository."""
        data = {"Name": name, "RepositoryURL": repo_url, "SwarmID": swarm_id, **kwargs}
        return self._post(
            f"stacks/create/swarm/repository?endpointId={endpoint_id}", data=data
        )

    def create_kubernetes_stack_from_string(
        self, name: str, file_content: str, endpoint_id: int, **kwargs
    ) -> dict:
        """Create a Kubernetes stack from a string."""
        data = {"StackName": name, "StackFileContent": file_content, **kwargs}
        return self._post(
            f"stacks/create/kubernetes/string?endpointId={endpoint_id}", data=data
        )

    def create_kubernetes_stack_from_repository(
        self, name: str, repo_url: str, endpoint_id: int, **kwargs
    ) -> dict:
        """Create a Kubernetes stack from a Git repository."""
        data = {"StackName": name, "RepositoryURL": repo_url, **kwargs}
        return self._post(
            f"stacks/create/kubernetes/repository?endpointId={endpoint_id}", data=data
        )

    def update_stack(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Update a stack."""
        return self._put(f"stacks/{stack_id}?endpointId={endpoint_id}", data=kwargs)

    def delete_stack(self, stack_id: int, endpoint_id: int) -> bool:
        """Delete a stack."""
        return self._delete(f"stacks/{stack_id}", params={"endpointId": endpoint_id})

    def start_stack(self, stack_id: int, endpoint_id: int) -> dict:
        """Start a stopped stack."""
        return self._post(
            f"stacks/{stack_id}/start", params={"endpointId": endpoint_id}
        )

    def stop_stack(self, stack_id: int, endpoint_id: int) -> dict:
        """Stop a running stack."""
        return self._post(f"stacks/{stack_id}/stop", params={"endpointId": endpoint_id})

    def migrate_stack(
        self, stack_id: int, endpoint_id: int, target_endpoint_id: int, **kwargs
    ) -> dict:
        """Migrate a stack to another environment."""
        data = {"EndpointID": target_endpoint_id, **kwargs}
        return self._post(
            f"stacks/{stack_id}/migrate?endpointId={endpoint_id}", data=data
        )

    def update_stack_git(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Update a stack's Git settings."""
        return self._put(f"stacks/{stack_id}/git?endpointId={endpoint_id}", data=kwargs)

    def redeploy_stack_git(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Redeploy a stack from its Git config."""
        return self._put(
            f"stacks/{stack_id}/git/redeploy?endpointId={endpoint_id}", data=kwargs
        )

    def associate_stack(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Associate an orphaned stack."""
        return self._put(
            f"stacks/{stack_id}/associate?endpointId={endpoint_id}", data=kwargs
        )
