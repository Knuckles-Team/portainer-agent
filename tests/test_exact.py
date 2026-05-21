import os

os.environ["PORTAINER_URL"] = "https://portainer.com"
os.environ["PORTAINER_TOKEN"] = "TEST"
os.environ["PORTAINER_SSL_VERIFY"] = "False"


import asyncio

import pytest
from agent_utilities.graph_orchestration import (
    initialize_graph_from_workspace,
    run_graph,
)


@pytest.mark.skip(reason="Requires external model service")
async def test_exact():
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    try:
        print("=== EXACT QUERY TEST ===")
        # Use the centralized workspace initialization
        graph, config = initialize_graph_from_workspace(
            base_url="http://10.0.0.18:1234/v1",
            api_key="llama",
        )

        query = "List the running stacks in portainer"
        print(f"Executing: {query}")
        result = await run_graph(graph=graph, config=config, query=query)

        # Handle GraphResponse object (Pydantic model) or dict
        if hasattr(result, "model_dump"):
            res_dict = result.model_dump()
        elif isinstance(result, dict):
            res_dict = result
        else:
            # Fallback for unexpected types
            res_dict = {"results": {"output": str(result)}}

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
                print(f"\n{domain.upper()} RESULT:")

                content = domain_result
                if isinstance(content, dict):
                    import json

                    print(json.dumps(content, indent=2))
                    continue

                if isinstance(content, str):
                    import json

                    try:
                        parsed = json.loads(content)
                        if isinstance(parsed, list):
                            print(f"Found {len(parsed)} items:")
                            for i, item in enumerate(parsed[:3]):
                                print(f"  {i + 1}. {json.dumps(item, indent=2)}")
                            if len(parsed) > 3:
                                print(f"  ... and {len(parsed) - 3} more items")
                        else:
                            print(f"{json.dumps(parsed, indent=2)}")
                    except json.JSONDecodeError:
                        print(content[:500] + ("..." if len(content) > 500 else ""))
                else:
                    print(
                        str(content)[:500] + ("..." if len(str(content)) > 500 else "")
                    )

    except Exception as e:
        print("\n=== ERROR ===")
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_exact())
