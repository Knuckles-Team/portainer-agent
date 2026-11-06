"""Kubernetes RBAC reads and the Helm chart listing call the routes Portainer serves.

Portainer serves the RBAC listings as ``cluster_role_bindings``, ``cluster_roles``,
``role_bindings`` and ``service_accounts``; the unseparated spellings return 404.
``templates/helm`` answers 400 without its required ``repo`` query parameter.
"""

from unittest.mock import MagicMock

import pytest

from portainer_agent.api_client import PortainerApi


def _client() -> PortainerApi:
    client = PortainerApi.__new__(PortainerApi)
    client._get = MagicMock(return_value=[])
    return client


@pytest.mark.parametrize(
    "method,route",
    [
        ("get_kubernetes_cluster_role_bindings", "kubernetes/7/cluster_role_bindings"),
        ("get_kubernetes_cluster_roles", "kubernetes/7/cluster_roles"),
        ("get_kubernetes_role_bindings", "kubernetes/7/role_bindings"),
        ("get_kubernetes_service_accounts", "kubernetes/7/service_accounts"),
        ("get_kubernetes_roles", "kubernetes/7/roles"),
    ],
)
def test_kubernetes_rbac_reads_use_served_routes(method, route):
    client = _client()
    getattr(client, method)(7)
    client._get.assert_called_once_with(route)


def test_helm_templates_pass_the_required_repo():
    client = _client()
    client.get_helm_templates(repo="https://charts.example.org")
    client._get.assert_called_once_with(
        "templates/helm", params={"repo": "https://charts.example.org"}
    )
