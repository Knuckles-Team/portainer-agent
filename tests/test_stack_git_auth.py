#!/usr/bin/env python
"""Tests for git-auth injection + env preservation on stack git (re)deploys."""
import os

import pytest

from portainer_agent.api.api_client_stacks import Api


@pytest.fixture
def api():
    # base_url/token irrelevant; we mock the HTTP verbs.
    return Api(base_url="http://portainer.test", token="x", verify=False)


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
    monkeypatch.setenv("GITLAB_TOKEN", "glpat-fallback")
    out = api._inject_git_auth({})
    assert out["repositoryPassword"] == "glpat-fallback"


def test_redeploy_preserves_env_and_injects_auth(monkeypatch, api):
    monkeypatch.setenv("PORTAINER_GIT_TOKEN", "glpat-secret")
    api.get_stack = lambda sid: {"Id": sid, "Env": [{"name": "SERVER", "value": "R820"}]}
    calls = _capture_put(api)
    api.redeploy_stack_git(stack_id=226, endpoint_id=3, pullImage=False)
    data = calls[0]["data"]
    assert "stacks/226/git/redeploy?endpointId=3" in calls[0]["endpoint"]
    assert data["Env"] == [{"name": "SERVER", "value": "R820"}]  # preserved
    assert data["repositoryPassword"] == "glpat-secret"  # injected
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
