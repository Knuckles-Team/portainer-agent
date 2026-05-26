#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_status(self) -> dict:
        """Get Portainer instance status."""
        return self._get("status")

    def get_system_info(self) -> dict:
        """Get system information."""
        return self._get("system/info")

    def get_system_status(self) -> dict:
        """Get detailed system status."""
        return self._get("system/status")

    def get_system_version(self) -> dict:
        """Get Portainer version information."""
        return self._get("system/version")

    def get_system_nodes(self) -> Any:
        """Get system nodes."""
        return self._get("system/nodes")

    def upgrade_system(self) -> dict:
        """Trigger a system upgrade."""
        return self._post("system/upgrade")

    def get_settings(self) -> dict:
        """Get Portainer settings."""
        return self._get("settings")

    def update_settings(self, **kwargs) -> dict:
        """Update Portainer settings."""
        return self._put("settings", data=kwargs)

    def get_public_settings(self) -> dict:
        """Get public (unauthenticated) settings."""
        return self._get("settings/public")

    def get_ssl_settings(self) -> dict:
        """Get SSL settings."""
        return self._get("ssl")

    def update_ssl_settings(self, **kwargs) -> dict:
        """Update SSL settings."""
        return self._put("ssl", data=kwargs)

    def backup(self, password: str = "") -> Any:  # nosec B107
        """Create a backup of Portainer data."""
        resp = self.session.post(self._url("backup"), json={"Password": password})
        resp.raise_for_status()
        return resp.content

    def restore(self, file_content: bytes, password: str = "") -> bool:  # nosec B107
        """Restore Portainer data from a backup."""
        resp = self.session.post(
            self._url("restore"),
            json={"Password": password, "FileContent": list(file_content)},
        )
        resp.raise_for_status()
        return True

    def get_tags(self) -> Any:
        """List all tags."""
        return self._get("tags")

    def create_tag(self, name: str) -> dict:
        """Create a tag."""
        return self._post("tags", data={"Name": name})

    def delete_tag(self, tag_id: int) -> bool:
        """Delete a tag."""
        return self._delete(f"tags/{tag_id}")

    def check_ldap(self, **kwargs) -> dict:
        """Check LDAP connectivity."""
        return self._post("ldap/check", data=kwargs)

    def get_motd(self) -> dict:
        """Get the message of the day."""
        return self._get("motd")

    def get_webhooks(self) -> Any:
        """List all webhooks."""
        return self._get("webhooks")

    def create_webhook(
        self, resource_id: str, endpoint_id: int, webhook_type: int = 1, **kwargs
    ) -> dict:
        """Create a webhook."""
        data = {
            "ResourceID": resource_id,
            "EndpointID": endpoint_id,
            "WebhookType": webhook_type,
            **kwargs,
        }
        return self._post("webhooks", data=data)

    def update_webhook(self, webhook_id: int, **kwargs) -> dict:
        """Update a webhook."""
        return self._put(f"webhooks/{webhook_id}", data=kwargs)

    def delete_webhook(self, webhook_id: int) -> bool:
        """Delete a webhook."""
        return self._delete(f"webhooks/{webhook_id}")

    def preview_git_file(
        self, repo_url: str, file_path: str = "docker-compose.yml", **kwargs
    ) -> dict:
        """Preview a file from a Git repository."""
        data = {
            "RepositoryURL": repo_url,
            "ComposeFilePathInRepository": file_path,
            **kwargs,
        }
        return self._post("gitops/repo/file/preview", data=data)
