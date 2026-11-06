#!/usr/bin/python
"""Portainer native knowledge-graph ingestion tools.

The per-operation tools are derived from the client methods by the connector; only the
ingestion tools are written by hand.
"""

import warnings

from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

from typing import Any

from scion_sdk.mcp.concurrency import run_blocking

from portainer_agent.auth import get_client


def register_ingest_tools(mcp: FastMCP):
    """Register the Portainer native-ingestion tools."""

    @mcp.tool(tags={"System"})
    async def portainer_system_raw_request(
        http_method: str = Field(
            description="HTTP method: GET, POST, PUT, PATCH or DELETE."
        ),
        api_path: str = Field(
            description="API path relative to /api, for example 'users/3/gitcredentials'."
        ),
        query_json: str | None = Field(
            default=None, description="JSON-encoded query parameters."
        ),
        body_json: str | None = Field(
            default=None, description="JSON-encoded request body."
        ),
        client=Depends(get_client),
    ) -> Any:
        """Send an authenticated request to any Portainer API endpoint.

        Covers REST operations that have no dedicated typed tool. Prefer the typed
        tool when one exists; a non-GET call changes state.
        """
        import json as _json

        return await run_blocking(
            client.request,
            method=http_method,
            path=api_path,
            params=_json.loads(query_json) if query_json else None,
            data=_json.loads(body_json) if body_json else None,
        )

    @mcp.tool(tags={"System", "kg"})
    async def portainer_ingest_environments(
        include_stacks: bool = Field(
            default=True,
            description="Also list and ingest all stacks and link them to their environments.",
        ),
        client=Depends(get_client),
    ) -> dict:
        """Natively ingest Portainer environments (+ stacks) into epistemic-graph.

        Lists endpoints via the Portainer API and pushes them as typed ``:Environment``
        nodes (with ``:EndpointGroup`` + ``:partOfEndpointGroup`` links); when
        ``include_stacks`` is set, also pushes ``:Stack`` nodes linked ``:inEnvironment``.
        Best-effort: ``ingested`` is ``None`` when no engine is reachable.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        from portainer_agent.kg_ingest import ingest_environments, ingest_stacks

        def _records(res: Any) -> list[dict]:
            data = res.get("data", res) if isinstance(res, dict) else res
            data = data if isinstance(data, list) else [data]
            return [
                r.model_dump() if hasattr(r, "model_dump") else r
                for r in data
                if isinstance(r, dict) or hasattr(r, "model_dump")
            ]

        endpoints = _records(await run_blocking(client.get_endpoints))
        env_result = await ingest_environments(endpoints)
        out: dict[str, Any] = {
            "environments_listed": len(endpoints),
            "environments_ingested": env_result,
        }
        if include_stacks:
            stacks = _records(await run_blocking(client.get_stacks))
            out["stacks_listed"] = len(stacks)
            out["stacks_ingested"] = await ingest_stacks(stacks)
        return out

    @mcp.tool(tags={"System", "kg"})
    async def portainer_ingest_containers(
        environment_id: int = Field(
            description="Environment (endpoint) id to list containers in."
        ),
        client=Depends(get_client),
    ) -> dict:
        """Natively ingest an environment's Docker containers into epistemic-graph.

        Lists containers in ``environment_id`` and pushes them as typed ``:Container``
        nodes linked ``:inEnvironment`` (and ``:deployedByStack`` where a compose/stack
        label is present). Best-effort: ``ingested`` is ``None`` with no reachable engine.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        from portainer_agent.kg_ingest import ingest_containers

        res = await run_blocking(client.list_containers, endpoint_id=environment_id)
        data = res.get("data", res) if isinstance(res, dict) else res
        records = data if isinstance(data, list) else [data]
        containers = [
            r.model_dump() if hasattr(r, "model_dump") else r
            for r in records
            if isinstance(r, dict) or hasattr(r, "model_dump")
        ]
        result = await ingest_containers(containers, environment_id)
        return {"listed": len(containers), "ingested": result}
