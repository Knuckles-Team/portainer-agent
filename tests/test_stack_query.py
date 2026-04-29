import os

os.environ["PORTAINER_URL"] = "http://portainer.arpa"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="
os.environ["PORTAINER_SSL_VERIFY"] = "False"


from agent_utilities import initialize_graph_from_workspace, run_graph
import asyncio


import pytest


@pytest.mark.skip(reason="Requires external model service")
async def test_query():
    try:
        graph_bundle = initialize_graph_from_workspace(
            agent_model="nvidia/nemotron-3-super",
            base_url="http://10.0.0.18:1234/v1",
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
        print(f"Error running query: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_query())
    if result:
        print("SUCCESS: Query completed")
    else:
        print("FAILED: Query failed")
