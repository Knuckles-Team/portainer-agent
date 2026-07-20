import os

os.environ["PORTAINER_URL"] = "http://portainer.example"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="


from agent_utilities.core.model_factory import create_model

if __name__ == "__main__":
    try:
        model = create_model(
            provider="openai",
            model_id="nvidia/nemotron-3-super",
            base_url="http://vllm.example/v1",
            api_key="llama",
        )
        print(f"Model created successfully: {model}")
        print(f"Model type: {type(model)}")
    except Exception as e:
        print(f"Operation failed: {type(e).__name__}")
        import traceback

        traceback.print_exc()
