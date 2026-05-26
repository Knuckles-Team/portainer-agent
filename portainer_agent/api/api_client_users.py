#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_users(self) -> Any:
        """List all users."""
        return self._get("users")

    def get_user(self, user_id: int) -> dict:
        """Get a specific user."""
        return self._get(f"users/{user_id}")

    def get_current_user(self) -> dict:
        """Get the currently authenticated user."""
        return self._get("users/me")

    def create_user(self, username: str, password: str, role: int = 2) -> dict:
        """Create a user. Roles: 1=admin, 2=standard."""
        return self._post(
            "users", data={"Username": username, "Password": password, "Role": role}
        )

    def update_user(self, user_id: int, **kwargs) -> dict:
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

    def check_admin_init(self) -> dict:
        """Check if admin user has been initialized."""
        return self._get("users/admin/check")

    def init_admin(self, username: str, password: str) -> dict:
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

    def create_user_token(self, user_id: int, description: str = "", **kwargs) -> dict:
        """Create an API token for a user."""
        return self._post(
            f"users/{user_id}/tokens", data={"Description": description, **kwargs}
        )

    def delete_user_token(self, user_id: int, key_id: int) -> bool:
        """Delete an API token."""
        return self._delete(f"users/{user_id}/tokens/{key_id}")

    def get_teams(self) -> Any:
        """List all teams."""
        return self._get("teams")

    def get_team(self, team_id: int) -> dict:
        """Get a specific team."""
        return self._get(f"teams/{team_id}")

    def create_team(self, name: str) -> dict:
        """Create a team."""
        return self._post("teams", data={"Name": name})

    def update_team(self, team_id: int, name: str) -> dict:
        """Update a team."""
        return self._put(f"teams/{team_id}", data={"Name": name})

    def delete_team(self, team_id: int) -> bool:
        """Delete a team."""
        return self._delete(f"teams/{team_id}")

    def get_team_memberships_by_team(self, team_id: int) -> Any:
        """List memberships for a team."""
        return self._get(f"teams/{team_id}/memberships")

    def get_team_memberships(self) -> Any:
        """List all team memberships."""
        return self._get("team_memberships")

    def create_team_membership(self, user_id: int, team_id: int, role: int = 2) -> dict:
        """Create a team membership. Roles: 1=leader, 2=member."""
        return self._post(
            "team_memberships",
            data={"UserID": user_id, "TeamID": team_id, "Role": role},
        )

    def update_team_membership(self, membership_id: int, **kwargs) -> dict:
        """Update a team membership."""
        return self._put(f"team_memberships/{membership_id}", data=kwargs)

    def delete_team_membership(self, membership_id: int) -> bool:
        """Delete a team membership."""
        return self._delete(f"team_memberships/{membership_id}")

    def get_roles(self) -> Any:
        """List all roles."""
        return self._get("roles")

    def get_resource_controls(self) -> Any:
        """List all resource controls."""
        return self._get("resource_controls")

    def create_resource_control(
        self, resource_id: str, resource_type: str, **kwargs
    ) -> dict:
        """Create a resource control."""
        data = {"ResourceID": resource_id, "Type": resource_type, **kwargs}
        return self._post("resource_controls", data=data)

    def update_resource_control(self, control_id: int, **kwargs) -> dict:
        """Update a resource control."""
        return self._put(f"resource_controls/{control_id}", data=kwargs)

    def delete_resource_control(self, control_id: int) -> bool:
        """Delete a resource control."""
        return self._delete(f"resource_controls/{control_id}")

    def get_user_helm_repositories(self, user_id: int) -> Any:
        """List Helm repositories for a user."""
        return self._get(f"users/{user_id}/helm/repositories")

    def create_user_helm_repository(self, user_id: int, url: str) -> dict:
        """Add a Helm repository for a user."""
        return self._post(f"users/{user_id}/helm/repositories", data={"URL": url})

    def delete_user_helm_repository(self, user_id: int, repository_id: int) -> bool:
        """Remove a Helm repository for a user."""
        return self._delete(f"users/{user_id}/helm/repositories/{repository_id}")
