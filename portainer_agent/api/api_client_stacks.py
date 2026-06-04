#!/usr/bin/env python
import os
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient

# Keys (either casing) that indicate the caller already supplied git credentials.
_GIT_AUTH_KEYS = (
    "repositoryUsername",
    "RepositoryUsername",
    "repositoryPassword",
    "RepositoryPassword",
    "repositoryGitCredentialID",
    "RepositoryGitCredentialID",
)


class Api(BaseApiClient):
    def _inject_git_auth(self, kwargs: dict) -> dict:
        """Auto-attach git credentials for repository (re)deploys.

        Portainer's stored per-stack git credentials are frequently ephemeral
        (e.g. GitLab CI job tokens) and expire, which makes git redeploys fail
        with 401/500. When a ``PORTAINER_GIT_TOKEN`` (or ``GITLAB_TOKEN``) is
        configured in the environment and the caller did not already pass
        explicit credentials, inject HTTP-basic auth so MCP-driven redeploys
        authenticate without relying on the (possibly stale) stored secret.
        """
        if any(k in kwargs for k in _GIT_AUTH_KEYS):
            return kwargs
        token = os.environ.get("PORTAINER_GIT_TOKEN") or os.environ.get("GITLAB_TOKEN")
        if not token:
            return kwargs
        username = os.environ.get("PORTAINER_GIT_USERNAME", "oauth2")
        kwargs.setdefault("repositoryAuthentication", True)
        kwargs.setdefault("repositoryUsername", username)
        kwargs["repositoryPassword"] = token
        return kwargs

    def _ensure_env_preserved(self, stack_id: int, kwargs: dict) -> dict:
        """Carry the stack's existing Env into a redeploy when none was given.

        Portainer resets a stack's environment to whatever the redeploy payload
        contains, so omitting Env silently wipes it. Re-fetch and pass it back.
        """
        if "Env" in kwargs or "env" in kwargs:
            return kwargs
        try:
            stack = self.get_stack(stack_id)
            if isinstance(stack, dict) and isinstance(stack.get("Env"), list):
                kwargs["Env"] = stack["Env"]
        except Exception:  # nosec B110 - best-effort env preservation
            pass
        return kwargs

    def get_stacks(self, **filters) -> Any:
        """List all stacks."""
        return self._list("stacks", **filters)

    def get_stack(self, stack_id: int) -> dict:
        """Get a specific stack."""
        return self._get(f"stacks/{stack_id}")

    def get_stack_by_name(self, name: str) -> dict:
        """Get a stack by name."""
        stacks = self.get_stacks()
        if isinstance(stacks, list):
            for s in stacks:
                if s.get("Name") == name or s.get("name") == name:
                    return s
        return {"error": f"Stack with name '{name}' not found."}

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
        """Update a stack's Git settings (auto-attaches configured git auth)."""
        if "env" in kwargs and "Env" not in kwargs:
            kwargs["Env"] = kwargs.pop("env")
        if "prune" in kwargs and "Prune" not in kwargs:
            kwargs["Prune"] = kwargs.pop("prune")
        kwargs = self._inject_git_auth(kwargs)
        return self._put(f"stacks/{stack_id}/git?endpointId={endpoint_id}", data=kwargs)

    def redeploy_stack_git(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Redeploy a stack from its Git config.

        Auto-attaches configured git credentials and preserves the stack's
        existing environment so a bare ``redeploy_stack_git(id, endpoint)`` call
        succeeds without the caller supplying secrets or re-specifying Env.
        """
        if "env" in kwargs and "Env" not in kwargs:
            kwargs["Env"] = kwargs.pop("env")
        if "prune" in kwargs and "Prune" not in kwargs:
            kwargs["Prune"] = kwargs.pop("prune")
        kwargs = self._ensure_env_preserved(stack_id, kwargs)
        kwargs = self._inject_git_auth(kwargs)
        return self._put(
            f"stacks/{stack_id}/git/redeploy?endpointId={endpoint_id}", data=kwargs
        )

    def associate_stack(self, stack_id: int, endpoint_id: int, **kwargs) -> dict:
        """Associate an orphaned stack."""
        return self._put(
            f"stacks/{stack_id}/associate?endpointId={endpoint_id}", data=kwargs
        )
