import os

os.environ["PORTAINER_URL"] = "http://portainer.arpa"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="
os.environ["PORTAINER_SSL_VERIFY"] = "False"

from agent_utilities import create_agent
import asyncio


async def test_direct_agent():
    try:
        agent = create_agent(
            provider="openai",
            model_id="google/gemma-4-31b",
            base_url="http://10.0.0.18:1234/v1",
            api_key="llama",
        )

        print("Testing direct agent with query: List stacks in portainer")
        result = await agent.run("List stacks in portainer")
        print(f"Direct agent result: {result}")

    except Exception as e:
        print(f"Error running direct agent: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_direct_agent())
