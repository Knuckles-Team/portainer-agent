#!/usr/bin/env python

try:
    from agent_utilities.core.exceptions import AuthError, UnauthorizedError
except ImportError:

    class AuthError(Exception):  # type: ignore[no-redef]
        pass

    class UnauthorizedError(Exception):  # type: ignore[no-redef]
        pass


from portainer_agent.api.api_client_auth import Api as AuthApi
from portainer_agent.api.api_client_docker import Api as DockerApi
from portainer_agent.api.api_client_edge import Api as EdgeApi
from portainer_agent.api.api_client_environments import Api as EnvironmentsApi
from portainer_agent.api.api_client_kubernetes import Api as KubernetesApi
from portainer_agent.api.api_client_registries import Api as RegistriesApi
from portainer_agent.api.api_client_stacks import Api as StacksApi
from portainer_agent.api.api_client_system import Api as SystemApi
from portainer_agent.api.api_client_templates import Api as TemplatesApi
from portainer_agent.api.api_client_users import Api as UsersApi


class PortainerApi(
    AuthApi,
    EnvironmentsApi,
    DockerApi,
    StacksApi,
    KubernetesApi,
    EdgeApi,
    TemplatesApi,
    UsersApi,
    RegistriesApi,
    SystemApi,
):
    """Unified API client for Portainer, composed of domain-specific sub-clients."""

    pass
