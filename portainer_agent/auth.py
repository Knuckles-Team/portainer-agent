#!/usr/bin/python

from agent_utilities.core.config import setting
from agent_utilities.core.exceptions import AuthError, UnauthorizedError
from agent_utilities.core.transport_security import resolve_configured_tls_profile

from portainer_agent.api_client import PortainerApi

_client = None


def get_client() -> PortainerApi:
    """Get or create a singleton PortainerApi client instance."""
    global _client
    if _client is None:
        base_url = setting("PORTAINER_URL", "http://localhost:9000")
        token = setting("PORTAINER_TOKEN", "")
        try:
            _client = PortainerApi(
                base_url=base_url,
                token=token,
                tls_profile=resolve_configured_tls_profile("portainer"),
            )
        except (AuthError, UnauthorizedError) as e:
            raise RuntimeError(
                "AUTHENTICATION ERROR: The configured credentials were rejected. "
                f"Please check your PORTAINER_TOKEN and PORTAINER_URL environment variables. "
                f"Error details: {type(e).__name__}"
            ) from e

    return _client
