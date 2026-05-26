"""Shared test fixtures for Portainer Agent."""

import pytest


@pytest.fixture
def mock_env(monkeypatch):
    """Set standard test environment variables."""
    monkeypatch.setenv("PORTAINER_URL", "https://test.example.com")
    monkeypatch.setenv("PORTAINER_TOKEN", "test-token-12345")
    monkeypatch.setenv("PORTAINER_SSL_VERIFY", "False")
