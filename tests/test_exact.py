import os

os.environ["PORTAINER_URL"] = "https://portainer.com"
os.environ["PORTAINER_TOKEN"] = "TEST"


import asyncio
import json
from typing import Any

import pytest

# `agent_utilities.graph` transitively imports `agent_utilities.numeric`
# (via `.builder` -> `knowledge_graph.core.engine` -> ... ->
# `agent_utilities.numeric`), which requires the compiled
# `epistemic_graph.numeric` kernel — shipped only behind agent-utilities'
# opt-in `graphos` extra (GOC-73), not installed by this repo's
# `agent-utilities[mcp]` dependency. Left unguarded, this raises a bare
# ModuleNotFoundError/ImportError chain that pytest reports as a COLLECTION
# ERROR, which (a) reads like a regression in THIS repo and (b) aborts
# collection of the entire `tests/` suite, not just this file. This is an
# ENVIRONMENT/packaging gap, not application-code breakage. See
# plans/complex/waves/wD4/WD4-FIX-01.md defect (d).
pytest.importorskip(
    "agent_utilities.numeric",
    exc_type=ImportError,
    reason=(
        "agent_utilities.numeric requires the compiled epistemic_graph.numeric "
        "kernel, shipped only behind agent-utilities' opt-in `graphos` extra "
        "(GOC-73); not installed by this repo's `agent-utilities[mcp]` "
        "dependency — install `agent-utilities[graphos]>=2.27.0` to run this "
        "test (WD4-FIX-01 defect (d))"
    ),
)

from agent_utilities.graph import (
    initialize_graph_from_workspace,
    run_graph,
)


def _as_result_dict(result: Any) -> dict:
    """Normalize a GraphResponse (pydantic model), dict, or other result to a dict."""
    if hasattr(result, "model_dump"):
        return result.model_dump()
    if isinstance(result, dict):
        return result
    return {"results": {"output": str(result)}}


def _print_json_list_or_text(content: str) -> None:
    """Pretty-print a JSON-list preview, a JSON scalar, or raw (possibly truncated) text."""
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        print(content[:500] + ("..." if len(content) > 500 else ""))
        return
    if isinstance(parsed, list):
        print(f"Found {len(parsed)} items:")
        for i, item in enumerate(parsed[:3]):
            print(f"  {i + 1}. {json.dumps(item, indent=2)}")
        if len(parsed) > 3:
            print(f"  ... and {len(parsed) - 3} more items")
    else:
        print(f"{json.dumps(parsed, indent=2)}")


def _print_domain_result(domain: str, content: Any) -> None:
    """Print one domain's result section, formatting dict/JSON-string/other content."""
    print(f"\n{domain.upper()} RESULT:")
    if isinstance(content, dict):
        print(json.dumps(content, indent=2))
        return
    if isinstance(content, str):
        _print_json_list_or_text(content)
        return
    print(str(content)[:500] + ("..." if len(str(content)) > 500 else ""))


@pytest.mark.skip(reason="Requires external model service")
async def test_exact():
    import logging

    logging.basicConfig(level=logging.DEBUG)

    try:
        print("=== EXACT QUERY TEST ===")
        # Use the centralized workspace initialization
        graph, config = initialize_graph_from_workspace(
            base_url="http://vllm.example/v1",
            api_key="llama",
        )

        query = "List the running stacks in portainer"
        print(f"Executing: {query}")
        result = await run_graph(graph=graph, config=config, query=query)

        res_dict = _as_result_dict(result)

        print("\n=== EXECUTION COMPLETED ===")
        print(f"Success: {res_dict.get('error') is None}")
        print(f"Domain: {res_dict.get('domain')}")
        print(
            f"Run ID: {res_dict.get('run_id') or res_dict.get('metadata', {}).get('run_id')}"
        )

        results = res_dict.get("results", {})
        if isinstance(results, dict):
            print("\n=== RESULTS BY DOMAIN ===")
            for domain, domain_result in results.items():
                _print_domain_result(domain, domain_result)

    except Exception as e:
        print("\n=== ERROR ===")
        print(f"Operation failed: {type(e).__name__}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_exact())
