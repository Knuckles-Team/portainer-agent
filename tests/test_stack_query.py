import os
os.environ['PORTAINER_URL'] = 'http://portainer.arpa'
os.environ['PORTAINER_TOKEN'] = 'ptr_P444Nokxd9Tn4yr47e26yc5PmGGaR3zVcfvaPUPxmZg='
os.environ['PORTAINER_SSL_VERIFY'] = 'False'

                                                        
from portainer_agent.agent_server import agent_template
from agent_utilities.graph_orchestration import run_graph
import asyncio

async def test_query():
    try:
        graph_bundle = agent_template(
            provider='openai',
            agent_model='nvidia/nemotron-3-super',
            base_url='http://10.0.0.18:1234/v1',
            api_key='llama'
        )
        
        graph, config = graph_bundle
        
        print('Testing query: List stacks in portainer')
        result = await run_graph(
            graph=graph,
            config=config,
            query='List stacks in portainer'
        )
        print(f'Result: {result}')
        return result
        
    except Exception as e:
        print(f'Error running query: {e}')
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    result = asyncio.run(test_query())
    if result:
        print('SUCCESS: Query completed')
    else:
        print('FAILED: Query failed')
