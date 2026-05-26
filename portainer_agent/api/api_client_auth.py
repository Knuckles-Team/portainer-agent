#!/usr/bin/env python
from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def authenticate(self, username: str, password: str) -> dict:
        """Authenticate and get a JWT token."""
        return self._post("auth", data={"Username": username, "Password": password})

    def logout(self) -> bool:
        """Logout and invalidate the current token."""
        return self._post("auth/logout")

    def validate_oauth(self, code: str) -> dict:
        """Validate an OAuth code."""
        return self._post("auth/oauth/validate", data={"Code": code})
