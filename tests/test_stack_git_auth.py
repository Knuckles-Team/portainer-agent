#!/usr/bin/env python
"""Tests for git-auth injection + env preservation on stack git (re)deploys."""

import pytest

from portainer_agent.api.api_client_stacks import Api


@pytest.fixture
def api():
    # base_url/token irrelevant; we mock the HTTP verbs.
    return Api(base_url="http://portainer.test", token="x")


def _capture_put(api):
    """Replace _put with a recorder; return the captured-calls list."""
    calls = []

    def fake_put(endpoint, data=None, params=None, timeout=None):
        calls.append({"endpoint": endpoint, "data": data})
        return {"ok": True}

    api._put = fake_put  # type: ignore[assignment]
    return calls


def test_inject_git_auth_adds_token(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "glpat-secret")
    monkeypatch.delenv("GITLAB_TOKEN", raising=False)
    out = api._inject_git_auth({})
    assert out["repositoryAuthentication"] is True
    assert out["repositoryUsername"] == "oauth2"
    assert out["repositoryPassword"] == "glpat-secret"


def test_inject_git_auth_respects_caller_creds(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "glpat-secret")
    out = api._inject_git_auth({"repositoryUsername": "me", "repositoryPassword": "p"})
    # caller-supplied creds must not be overwritten
    assert out["repositoryPassword"] == "p"
    assert out["repositoryUsername"] == "me"


def test_inject_git_auth_noop_without_token(monkeypatch, api):
    monkeypatch.delenv("PORTAINER_GIT_TOKEN", raising=False)
    monkeypatch.delenv("GITLAB_TOKEN", raising=False)
    out = api._inject_git_auth({})
    assert out == {}


def test_inject_git_auth_custom_username(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "t")
    monkeypatch.setenv("PORTAINER_GIT_USERNAME", "gitlab-bot")
    out = api._inject_git_auth({})
    assert out["repositoryUsername"] == "gitlab-bot"


def test_inject_git_auth_falls_back_to_gitlab_token(monkeypatch, api):
    monkeypatch.delenv("PORTAINER_GIT_TOKEN", raising=False)
    fallback_token = "synthetic-" + "fallback"
    monkeypatch.setenv("GITLAB_TOKEN", fallback_token)
    out = api._inject_git_auth({})
    assert out["repositoryPassword"] == fallback_token


def test_redeploy_preserves_env_and_injects_auth(monkeypatch, api):
    deployment_token = "synthetic-" + "deployment-token"
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", deployment_token)
    api.get_stack = lambda sid: {"Id": sid, "Env": [{"name": "SERVER", "value": "R820"}]}
    calls = _capture_put(api)
    api.redeploy_stack_git(stack_id=226, endpoint_id=3, pullImage=False)
    data = calls[0]["data"]
    assert "stacks/226/git/redeploy?endpointId=3" in calls[0]["endpoint"]
    assert data["Env"] == [{"name": "SERVER", "value": "R820"}]  # preserved
    assert data["repositoryPassword"] == deployment_token  # injected
    assert data["pullImage"] is False


def test_redeploy_does_not_clobber_explicit_env(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "glpat-secret")
    called = {"n": 0}

    def _gs(sid):
        called["n"] += 1
        return {"Env": [{"name": "X", "value": "1"}]}

    api.get_stack = _gs
    _capture_put(api)
    api.redeploy_stack_git(stack_id=1, endpoint_id=3, env=[{"name": "A", "value": "B"}])
    # caller passed env -> get_stack must not be consulted
    assert called["n"] == 0


def _capture_post(api):
    """Replace _post with a recorder; return the captured-calls list."""
    calls = []

    def fake_post(endpoint, data=None, params=None, timeout=None):
        calls.append({"endpoint": endpoint, "data": data})
        return {"ok": True}

    api._post = fake_post  # type: ignore[assignment]
    return calls


def test_create_swarm_from_repository_injects_auth(monkeypatch, api):
    # Regression: GitOps stack CREATION (not just redeploy) must auto-authenticate
    # private repos, else Portainer 400s on the clone.
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "glpat-secret")
    calls = _capture_post(api)
    api.create_swarm_stack_from_repository(
        name="data-science-mcp",
        repo_url="http://gitlab.example/homelab/containers/services/data-science-mcp.git",
        swarm_id="sw1",
        endpoint_id=3,
        repositoryReferenceName="refs/heads/main",
        composeFile="compose.yml",
    )
    data = calls[0]["data"]
    assert data["repositoryAuthentication"] is True
    assert data["repositoryPassword"] == "glpat-secret"
    assert data["composeFile"] == "compose.yml"


def test_create_standalone_and_k8s_from_repository_inject_auth(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "t")
    for fn in (
        lambda: api.create_standalone_stack_from_repository(
            name="s", repo_url="http://g/r.git", endpoint_id=3
        ),
        lambda: api.create_kubernetes_stack_from_repository(
            name="k", repo_url="http://g/r.git", endpoint_id=3
        ),
    ):
        calls = _capture_post(api)
        fn()
        assert calls[0]["data"]["repositoryPassword"] == "t"
