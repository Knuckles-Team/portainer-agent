#!/usr/bin/env python
"""Portainer HTTP base — strangled onto ``agent_utilities.http.BaseApiClient``.

CONCEPT:AU-ECO.ui.fleet-http-client-library (Fleet HTTP Client Library) adoption: the public surface
(``base_url``/``api_base``/``timeout``/``session``, ``_url`` and the
``_get/_post/_put/_patch/_delete/_list`` verbs with their legacy return
shapes) is unchanged, while the plumbing — typed error mapping, rate-limit
capture, bounded 429 backoff, and log redaction — now comes from the shared
fleet base.

The transport intentionally remains this client's ``requests.Session``
(``self.session``), adapted into the shared httpx stack by
:class:`_RequestsSessionTransport`. That keeps the raw-session call sites
(``backup``/``restore`` stream bytes through ``self.session`` directly) and
the existing ``patch("requests.Session")`` test fixtures observing every
request, exactly as before.
"""

import json
from typing import Any

import httpx
import requests
import urllib3
from agent_utilities.http import AuthHeaderInjector, TokenAuth
from agent_utilities.http import BaseApiClient as FleetApiClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#: Request headers managed by the session/transport rather than forwarded.
_HOP_HEADERS = {"host", "content-length"}


class _RequestsSessionTransport(httpx.BaseTransport):
    """httpx transport that delegates each request to a ``requests.Session``.

    The session stays the single network touchpoint (TLS ``verify``, the
    ``X-API-Key`` header, proxies/adapters configured on it all keep
    working), while the shared fleet client supplies the plumbing above it.
    """

    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        timeout = request.extensions.get("timeout", {}).get("read")
        headers = {
            name: value
            for name, value in request.headers.items()
            if name.lower() not in _HOP_HEADERS
        }
        verb = getattr(self._session, request.method.lower(), None)
        if verb is None:
            response = self._session.request(
                request.method,
                str(request.url),
                data=request.content or None,
                headers=headers,
                timeout=timeout,
            )
        else:
            response = verb(
                str(request.url),
                data=request.content or None,
                headers=headers,
                timeout=timeout,
            )
        return self._to_httpx_response(response, request)

    @staticmethod
    def _to_httpx_response(response: Any, request: httpx.Request) -> httpx.Response:
        """Convert a requests-style response (or test double) to httpx."""
        status_code = getattr(response, "status_code", None)
        if not isinstance(status_code, int):
            status_code = 200
        try:
            headers = dict(response.headers)
        except (TypeError, ValueError):
            headers = {}
        content = getattr(response, "content", None)
        if not isinstance(content, (bytes, bytearray)):
            text = getattr(response, "text", "")
            content = text.encode("utf-8") if isinstance(text, str) else b""
        return httpx.Response(
            status_code, headers=headers, content=bytes(content), request=request
        )


class BaseApiClient:
    # Default timeout in seconds for all HTTP requests.
    # Prevents indefinite blocking when Portainer waits on Docker daemon
    # operations (e.g., stack rm on crash-looping containers).
    DEFAULT_TIMEOUT = 30

    def __init__(
        self,
        base_url: str = "http://localhost:9000",
        token: str = "",  # nosec B107
        verify: bool = True,
        timeout: int | None = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_base = f"{self.base_url}/api"
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.session = requests.Session()
        self.session.verify = verify
        if token:
            self.session.headers.update({"X-API-Key": token})
        self.session.headers.update({"Accept": "application/json"})

        auth: AuthHeaderInjector | None = None
        if token:
            auth = TokenAuth(token, header="X-API-Key", prefix=None)
        self._fleet = FleetApiClient(
            self.api_base,
            auth=auth,
            verify=verify,
            timeout=float(self.timeout),
            transport=_RequestsSessionTransport(self.session),
        )

    def _url(self, endpoint: str) -> str:
        return f"{self.api_base}/{endpoint.strip('/')}"

    @staticmethod
    def _decode(body: Any) -> Any:
        """Legacy decode: JSON whenever the body parses as it, else raw text."""
        if isinstance(body, str):
            try:
                return json.loads(body)
            except ValueError:
                return body
        return body

    def _get(
        self, endpoint: str, params: dict | None = None, timeout: int | None = None
    ) -> Any:
        envelope = self._fleet.get(endpoint.strip("/"), params=params, timeout=timeout)
        return self._decode(envelope["data"])

    def _post(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        envelope = self._fleet.post(
            endpoint.strip("/"), json=data, params=params, timeout=timeout
        )
        return self._decode(envelope["data"])

    def _put(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        envelope = self._fleet.put(
            endpoint.strip("/"), json=data, params=params, timeout=timeout
        )
        return self._decode(envelope["data"])

    def _patch(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        envelope = self._fleet.patch(
            endpoint.strip("/"), json=data, params=params, timeout=timeout
        )
        return self._decode(envelope["data"])

    def _delete(
        self, endpoint: str, params: dict | None = None, timeout: int | None = None
    ) -> bool:
        self._fleet.delete(endpoint.strip("/"), params=params, timeout=timeout)
        return True

    def _list(
        self,
        endpoint: str,
        limit: int | None = None,
        offset: int | None = None,
        **filters,
    ) -> Any:
        params = {k: v for k, v in filters.items() if v is not None}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["start"] = offset
        return self._get(endpoint, params=params)

    def request(
        self,
        method: str,
        path: str,
        params: dict | None = None,
        data: Any = None,
        timeout: int | None = None,
    ) -> Any:
        """Generic authenticated passthrough to ANY Portainer API endpoint.

        Escape hatch for the long tail of the Portainer REST API that does not yet
        have a typed wrapper: ``method`` is GET/POST/PUT/PATCH/DELETE and ``path``
        is the API path **relative to ``/api``** (e.g. ``stacks/278/git/redeploy``,
        ``users/3/gitcredentials``, ``backup/s3/settings``). The session's
        ``X-API-Key`` auth, base URL, and timeout all apply. Returns parsed JSON
        (or text), or ``True`` for a bodyless DELETE.
        """
        m = method.strip().upper()
        resp = self.session.request(
            m,
            self._url(path),
            params=params,
            json=data if m in ("POST", "PUT", "PATCH") else None,
            timeout=timeout or self.timeout,
        )
        resp.raise_for_status()
        if m == "DELETE" and not resp.content:
            return True
        try:
            return resp.json()
        except Exception:
            return resp.text
