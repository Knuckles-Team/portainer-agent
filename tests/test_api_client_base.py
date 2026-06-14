"""Facade-parity tests for the strangled BaseApiClient.

The public verb surface must keep its legacy return shapes while the
plumbing (typed error mapping, rate-limit capture, bounded 429 backoff)
comes from the shared agent_utilities.http fleet base. Transport is a fake
requests-style session — no live Portainer.
"""

from types import SimpleNamespace

import pytest
from agent_utilities.core.exceptions import AuthError, ParameterError

from portainer_agent.api.api_client_base import BaseApiClient


class FakeSession:
    """Minimal requests.Session stand-in returning scripted responses."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.headers = {}
        self.verify = True

    def _respond(self, method, url, **kwargs):
        self.calls.append({"method": method, "url": url, **kwargs})
        response = self.responses.pop(0)
        return response

    def get(self, url, **kwargs):
        return self._respond("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self._respond("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self._respond("PUT", url, **kwargs)

    def patch(self, url, **kwargs):
        return self._respond("PATCH", url, **kwargs)

    def delete(self, url, **kwargs):
        return self._respond("DELETE", url, **kwargs)


def _response(status_code=200, text="", headers=None):
    return SimpleNamespace(
        status_code=status_code,
        text=text,
        content=text.encode("utf-8"),
        headers=headers or {"Content-Type": "application/json"},
    )


def _client(responses, **kwargs):
    client = BaseApiClient(base_url="http://portainer.test", **kwargs)
    fake = FakeSession(responses)
    # Swap the transport's session for the scripted fake (the adapter is the
    # only network touchpoint).
    client._fleet._client._transport._session = fake
    return client, fake


def test_get_returns_parsed_json_and_hits_api_base():
    client, fake = _client([_response(text='[{"Id": 1}]')])
    assert client._get("stacks") == [{"Id": 1}]
    assert fake.calls[0]["url"] == "http://portainer.test/api/stacks"


def test_post_sends_json_body_and_decodes():
    client, fake = _client([_response(text='{"Id": 9}')])
    assert client._post("stacks", data={"Name": "web"}) == {"Id": 9}
    assert b'"Name"' in fake.calls[0]["data"]


def test_delete_returns_true():
    client, _ = _client([_response(status_code=204, text="")])
    assert client._delete("stacks/1") is True


def test_list_builds_limit_start_params():
    client, fake = _client([_response(text="[]")])
    client._list("stacks", limit=5, offset=10, filters=None)
    assert "limit=5" in fake.calls[0]["url"]
    assert "start=10" in fake.calls[0]["url"]


def test_non_json_body_returns_text():
    client, _ = _client(
        [_response(text="plain logs", headers={"Content-Type": "text/plain"})]
    )
    assert client._get("endpoints/1/docker/containers/x/logs") == "plain logs"


def test_typed_error_mapping():
    client, _ = _client([_response(status_code=401, text='{"message": "denied"}')])
    with pytest.raises(AuthError):
        client._get("stacks")
    client, _ = _client([_response(status_code=404, text='{"message": "nope"}')])
    with pytest.raises(ParameterError):
        client._get("stacks/999")


def test_429_backoff_retries_through_session(monkeypatch):
    sleeps: list[float] = []
    monkeypatch.setattr("agent_utilities.http.client.time.sleep", sleeps.append)
    client, fake = _client(
        [
            _response(status_code=429, headers={"Retry-After": "1"}),
            _response(text='{"ok": true}'),
        ]
    )
    assert client._get("stacks") == {"ok": True}
    assert len(fake.calls) == 2
    assert sleeps == [1.0]


def test_api_key_header_reaches_session_call():
    client, fake = _client([_response(text="{}")], token="secret-key")
    client._get("status")
    assert fake.calls[0]["headers"]["x-api-key"] == "secret-key"
    # The real session object keeps the legacy header too (backup/restore).
    assert client.session.headers["X-API-Key"] == "secret-key"
