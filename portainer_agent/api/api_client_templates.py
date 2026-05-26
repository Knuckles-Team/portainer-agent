#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_templates(self) -> Any:
        """List app templates."""
        return self._get("templates")

    def get_template_file(self, template_id: int) -> dict:
        """Get template compose file."""
        return self._get(f"templates/{template_id}/file")

    def get_helm_templates(self) -> Any:
        """List Helm chart templates."""
        return self._get("templates/helm")

    def get_custom_templates(self) -> Any:
        """List custom templates."""
        return self._get("custom_templates")

    def get_custom_template(self, template_id: int) -> dict:
        """Get a specific custom template."""
        return self._get(f"custom_templates/{template_id}")

    def create_custom_template_from_string(
        self,
        title: str,
        description: str,
        file_content: str,
        template_type: int = 2,
        **kwargs,
    ) -> dict:
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
    ) -> dict:
        """Create a custom template from a Git repository."""
        data = {
            "Title": title,
            "Description": description,
            "RepositoryURL": repo_url,
            "Type": template_type,
            **kwargs,
        }
        return self._post("custom_templates/create/repository", data=data)

    def update_custom_template(self, template_id: int, **kwargs) -> dict:
        """Update a custom template."""
        return self._put(f"custom_templates/{template_id}", data=kwargs)

    def delete_custom_template(self, template_id: int) -> bool:
        """Delete a custom template."""
        return self._delete(f"custom_templates/{template_id}")

    def get_custom_template_file(self, template_id: int) -> dict:
        """Get custom template compose file content."""
        return self._get(f"custom_templates/{template_id}/file")

    def git_fetch_custom_template(self, template_id: int) -> dict:
        """Fetch latest version of a custom template from Git."""
        return self._put(f"custom_templates/{template_id}/git_fetch")
