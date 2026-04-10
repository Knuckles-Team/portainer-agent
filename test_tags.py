import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def debug_tags():
    # Use the portainer-agent mcp server
    command = "python"
    args = ["-m", "portainer_agent.mcp_server"]

    server_params = StdioServerParameters(command=command, args=args, env=None)

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            tools = getattr(result, "tools", result)

            for tool in tools:
                print(f"Tool: {tool.name}")
                print(f"  Annotations: {getattr(tool, 'annotations', 'None')}")
                # Check for tags explicitly
                if hasattr(tool, "annotations") and tool.annotations:
                    print(f"  Tags: {tool.annotations.get('tags')}")
                    print(f"  Tag: {tool.annotations.get('tag')}")
                break  # Just one


if __name__ == "__main__":
    asyncio.run(debug_tags())
