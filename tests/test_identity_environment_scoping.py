"""Identity-scoped environment auto-load (CONCEPT:AU-OS.identity.identity-scoped-resource-autoload).

The caller's entitled Portainer environments (endpoints) auto-load in
``get_endpoints``; a non-entitled endpoint id is denied in ``get_endpoint``.
Tests the filtering/enforcement logic with the entitlement source mocked (the
resolver itself is tested in agent-utilities).
"""

import pytest

from portainer_agent.api import api_client_environments
from portainer_agent.api.api_client_environments import Api


def _client(monkeypatch, entitled):
    monkeypatch.setattr(
        api_client_environments,
        "_entitled",
        lambda namespace, names: [n for n in names if n in entitled],
    )
    api = object.__new__(Api)  # bypass BaseApiClient.__init__ (no network)
    return api


def test_get_endpoints_filters_to_entitled(monkeypatch):
    api = _client(monkeypatch, {"prod"})
    monkeypatch.setattr(
        api,
        "_list",
        lambda *a, **k: [
            {"Id": 1, "Name": "prod"},
            {"Id": 2, "Name": "dev"},
        ],
    )
    result = api.get_endpoints()
    assert [e["Name"] for e in result] == ["prod"]


def test_get_endpoint_denies_non_entitled(monkeypatch):
    api = _client(monkeypatch, {"prod"})
    monkeypatch.setattr(api, "_get", lambda *a, **k: {"Id": 2, "Name": "dev"})
    with pytest.raises(PermissionError):
        api.get_endpoint(2)


def test_get_endpoint_allows_entitled(monkeypatch):
    api = _client(monkeypatch, {"prod"})
    monkeypatch.setattr(api, "_get", lambda *a, **k: {"Id": 1, "Name": "prod"})
    assert api.get_endpoint(1) == {"Id": 1, "Name": "prod"}


def test_missing_resolver_degrades_to_full_list(monkeypatch):
    """A broken/absent import of the shared resolver fails open to the full list."""
    import builtins

    real_import = builtins.__import__

    def _blocked_import(name, *args, **kwargs):
        if name == "agent_utilities.security.entitlements":
            raise ImportError("simulated: resolver not available")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _blocked_import)
    assert api_client_environments._entitled("portainer", ["a", "b"]) == ["a", "b"]
