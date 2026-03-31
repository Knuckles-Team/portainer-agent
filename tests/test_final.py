import os
os.environ['PORTAINER_URL'] = 'http://portainer.arpa'
os.environ['PORTAINER_TOKEN'] = 'ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg='
os.environ['PORTAINER_SSL_VERIFY'] = 'False'

                                   
from portainer_agent.agent_server import agent_template
from agent_utilities.graph_orchestration import run_graph
import asyncio
import json

async def test_graph():
    try:
        print("=== STACKS QUERY TEST ===")
        graph_bundle = agent_template(
            provider='openai',
            agent_model='nvidia/nemotron-3-super',
            base_url='http://10.0.0.18:1234/v1',
            api_key='llama'
        )
        
        graph, config = graph_bundle
        
        print('Executing: List stacks in portainer')
        result = await run_graph(
            graph=graph,
            config=config,
            query='List stacks in portainer'
        )
        
        print("\n=== EXECUTION COMPLETED ===")
        print(f"Success: {result.get('error') is None}")
        print(f"Domain: {result.get('domain')}")
        print(f"Run ID: {result.get('run_id')}")
        
        if 'results' in result and isinstance(result['results'], dict):
            print("\n=== RESULTS BY DOMAIN ===")
            for domain, domain_result in result['results'].items():
                print(f"\n{domain.upper()} RESULT:")
                print(f"Type: {type(domain_result)}")
                if isinstance(domain_result, str):
                                                             
                    try:
                        parsed = json.loads(domain_result)
                        if isinstance(parsed, list):
                            print(f"Found {len(parsed)} items:")
                            for i, item in enumerate(parsed[:5]):                      
                                print(f"  {i+1}. {json.dumps(item, indent=2)}")
                            if len(parsed) > 5:
                                print(f"  ... and {len(parsed) - 5} more items")
                        else:
                            print(f"{json.dumps(parsed, indent=2)}")
                    except json.JSONDecodeError:
                                                
                        print(domain_result[:500] + ('...' if len(domain_result) > 500 else ''))
                else:
                    print(str(domain_result)[:500] + ('...' if len(str(domain_result)) > 500 else ''))
        
        if result.get('mermaid'):
            print("\n=== MERMAID DIAGRAM ===")
            print(result['mermaid'])
            
        print("\n=== TEST COMPLETED ===")
        
    except Exception as e:
        print(f"\n=== ERROR ===")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(test_graph())
