import os

os.environ["PORTAINER_URL"] = "http://portainer.example"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="

import asyncio

import pytest
from agent_utilities import create_agent


@pytest.mark.skip(reason="Requires external model service")
async def test_direct_agent():
    try:
        agent = create_agent(
            provider="openai",
            model_id="nvidia/nemotron-3-super",
            base_url="http://vllm.example/v1",
            api_key="llama",
        )

        print("Testing direct agent with query: List stacks in portainer")
        result = await agent.run("List stacks in portainer")
        print(f"Direct agent result: {result}")

    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_direct_agent())
