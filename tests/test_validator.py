import os

os.environ["PORTAINER_URL"] = "http://portainer.arpa"
os.environ["PORTAINER_TOKEN"] = "ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg="
os.environ["PORTAINER_SSL_VERIFY"] = "False"


from agent_utilities.model_factory import create_model
from pydantic_ai import Agent
from pydantic import BaseModel


class ValidationResult(BaseModel):
    is_valid: bool
    feedback: str | None = None
    score: float | None = None


try:

    model = create_model(
        provider="openai",
        model_id="nvidia/nemotron-3-super",
        base_url="http://10.0.0.18:1234/v1",
        api_key="llama",
    )
    print("Model created")

    validator_agent_old = Agent(
        output_type=ValidationResult,
        instructions=(
            "You are a quality assurance expert. Evaluate the output of the 'Stack' agent."
            "Original Query: List the running stacks in portainer"
            "Agent Result: Here are the stacks..."
            "Determine if the result accurately and comprehensively addresses the query."
            "If the result is incomplete, hallucinated, or has errors, set is_valid=False and provide feedback."
        ),
    )
    print("Old style agent created")

    validator_agent_new = Agent(
        model=model,
        output_type=ValidationResult,
        instructions=(
            "You are a quality assurance expert. Evaluate the output of the 'Stack' agent."
            "Original Query: List the running stacks in portainer"
            "Agent Result: Here are the stacks..."
            "Determine if the result accurately and comprehensively addresses the query."
            "If the result is incomplete, hallucinated, or has errors, set is_valid=False and provide feedback."
        ),
    )
    print("New style agent created")

    print("\nTesting old style agent...")
    try:

        import asyncio

        async def test_old():
            result = await validator_agent_old.run("Evaluate the result.")
            print("Old style result:", result)

        asyncio.run(test_old())
    except Exception as e:
        print("Old style agent failed: {}".format(e))

    print("\nTesting new style agent...")
    try:
        import asyncio

        async def test_new():
            result = await validator_agent_new.run("Evaluate the result.")
            print("New style result:", result)

        asyncio.run(test_new())
    except Exception as e:
        print("New style agent failed: {}".format(e))
        import traceback

        traceback.print_exc()

except Exception as e:
    print("Error in setup: {}".format(e))
    import traceback

    traceback.print_exc()
