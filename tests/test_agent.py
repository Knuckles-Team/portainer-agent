import os

os.environ["PORTAINER_URL"] = "http://portainer.arpa"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="
os.environ["PORTAINER_SSL_VERIFY"] = "False"


from agent_utilities.core.model_factory import create_model
from pydantic_ai import Agent

if __name__ == "__main__":
    try:
        model = create_model(
            provider="openai",
            model_id="nvidia/nemotron-3-super",
            base_url="http://vllm.arpa/v1",
            api_key="llama",
        )
        print("Model created successfully")

        agent = Agent(
            model=model, output_type=bool, instructions="You are a helpful assistant."
        )
        print("Agent created successfully")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
