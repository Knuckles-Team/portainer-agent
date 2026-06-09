# Usage — API / CLI / MCP

`portainer-agent` exposes the same capability three ways: as **MCP tools** an agent
calls, as a **Python API** (`PortainerApi`) you import, and as **console scripts** you
run. The complete tool surface and the environment toggles are in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers one action-dispatch tool per
management domain. Each domain is enabled by default and can be toggled off with its
`*TOOL` environment variable.

| Tool | Domain | Toggle |
|---|---|---|
| `portainer_auth` | Authentication & session management | `AUTHTOOL` |
| `portainer_environment` | Environments (endpoints) & groups | `ENVIRONMENTTOOL` |
| `portainer_docker` | Docker containers, images, networks, volumes | `DOCKERTOOL` |
| `portainer_stack` | Stack deployment & lifecycle | `STACKTOOL` |
| `portainer_kubernetes` | Kubernetes orchestration | `KUBERNETESTOOL` |
| `portainer_edge` | Edge devices & deployment | `EDGETOOL` |
| `portainer_template` | Application templates | `TEMPLATETOOL` |
| `portainer_user` | Users, teams & identity | `USERTOOL` |
| `portainer_registry` | Container registries | `REGISTRYTOOL` |
| `portainer_system` | System info, settings & health | `SYSTEMTOOL` |

Example agent prompts that map onto these tools:

- *"List the Docker environments Portainer manages"* → `portainer_environment`
- *"Redeploy the `web` stack on endpoint 1"* → `portainer_stack`
- *"What is the Portainer system version and status?"* → `portainer_system`

## As a Python API

`PortainerApi` is a composed REST client built from one sub-client per management
domain. Construct it directly, or build one from the environment with `get_client()`.

```python
from portainer_agent.api_client import PortainerApi

api = PortainerApi(
    base_url="http://your-portainer:9000",
    token="your_api_token",
    verify=True,
)

# Reads
status = api.get_status()                  # platform status / edition
version = api.get_system_version()         # version + update availability
endpoints = api.get_endpoints()            # managed Docker / Kubernetes environments
stacks = api.get_stacks()                  # deployed stacks
stack = api.get_stack_by_name("web")       # a single stack by name
```

Build a client straight from the environment:

```python
from portainer_agent.auth import get_client

api = get_client()        # reads PORTAINER_URL / PORTAINER_TOKEN / PORTAINER_SSL_VERIFY
nodes = api.get_system_nodes()
```

### Writes

Write operations use the same client — for example, deploying and controlling stacks:

```python
api.create_standalone_stack_from_string(...)   # deploy a Compose stack
api.start_stack(stack_id=3, endpoint_id=1)
api.stop_stack(stack_id=3, endpoint_id=1)
api.redeploy_stack_git(stack_id=3, endpoint_id=1)
```

## As a CLI

Two console scripts are installed:

```bash
# MCP server (stdio / streamable-http / sse)
portainer-mcp --transport streamable-http --host 0.0.0.0 --port 8000

# A2A agent server — natural-language interface over the tools
portainer-agent --provider openai --model-id gpt-4o --api-key sk-...
```

Both honor the `PORTAINER_*` environment variables described in
[Deployment](deployment.md#configuration-environment). The agent reaches the MCP server
via `MCP_URL` (or launches it from `mcp_config.json`) and routes each request to the
relevant domain tool.
