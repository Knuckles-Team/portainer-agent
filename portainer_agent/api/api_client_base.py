#!/usr/bin/env python
import logging
from typing import Any

import requests
import urllib3

try:
    from agent_utilities.core.exceptions import AuthError, UnauthorizedError
except ImportError:

    class AuthError(Exception):  # type: ignore[no-redef]
        pass

    class UnauthorizedError(Exception):  # type: ignore[no-redef]
        pass


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


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

    def _url(self, endpoint: str) -> str:
        return f"{self.api_base}/{endpoint.strip('/')}"

    def _get(
        self, endpoint: str, params: dict | None = None, timeout: int | None = None
    ) -> Any:
        resp = self.session.get(
            self._url(endpoint), params=params, timeout=timeout or self.timeout
        )
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _post(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        resp = self.session.post(
            self._url(endpoint),
            json=data,
            params=params,
            timeout=timeout or self.timeout,
        )
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _put(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        resp = self.session.put(
            self._url(endpoint),
            json=data,
            params=params,
            timeout=timeout or self.timeout,
        )
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _patch(
        self,
        endpoint: str,
        data: dict | list | None = None,
        params: dict | None = None,
        timeout: int | None = None,
    ) -> Any:
        resp = self.session.patch(
            self._url(endpoint),
            json=data,
            params=params,
            timeout=timeout or self.timeout,
        )
        resp.raise_for_status()
        try:
            return resp.json()
        except Exception:
            return resp.text

    def _delete(
        self, endpoint: str, params: dict | None = None, timeout: int | None = None
    ) -> bool:
        resp = self.session.delete(
            self._url(endpoint), params=params, timeout=timeout or self.timeout
        )
        resp.raise_for_status()
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
