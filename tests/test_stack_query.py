import os

os.environ["PORTAINER_URL"] = "http://portainer.example"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="


import asyncio

import pytest

# `agent_utilities.initialize_graph_from_workspace`/`run_graph` are lazy
# `__getattr__` re-exports (agent_utilities/__init__.py) that pull in
# `agent_utilities.graph`, which transitively requires the compiled
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

from agent_utilities import initialize_graph_from_workspace, run_graph


@pytest.mark.skip(reason="Requires external model service")
async def test_query():
    try:
        graph_bundle = initialize_graph_from_workspace(
            agent_model="nvidia/nemotron-3-super",
            base_url="http://vllm.example/v1",
            api_key="llama",
        )

        graph, config = graph_bundle

        print("Testing query: List stacks in portainer")
        result = await run_graph(
            graph=graph, config=config, query="List stacks in portainer"
        )
        print(f"Result: {result}")
        return result

    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_query())
    if result:
        print("SUCCESS: Query completed")
    else:
        print("FAILED: Query failed")
