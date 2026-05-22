# Portainer Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/portainer-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/portainer-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/portainer-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/portainer-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/portainer-agent)
![PyPI - License](https://img.shields.io/pypi/l/portainer-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/portainer-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/portainer-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/portainer-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/portainer-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/portainer-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/portainer-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/portainer-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/portainer-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/portainer-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/portainer-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/portainer-agent)

*Version: 0.11.1*

---

## Overview

**Portainer Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](file:///home/apps/workspace/agent-packages/agents/portainer-agent/docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Auth** | `AUTHTOOL` | `True` | Manage auth operations. Action-routed methods: `authenticate`, `logout`, `validate_oauth`. |
| **Environment** | `ENVIRONMENTTOOL` | `True` | Manage environment operations. Action-routed methods: `get_endpoints`, `get_endpoint`, `create_endpoint`, `update_endpoint`, `delete_endpoint`, `snapshot_endpoint`, `snapshot_all_endpoints`, `get_endpoint_groups`, `create_endpoint_group`, `delete_endpoint_group`. |
| **Docker** | `DOCKERTOOL` | `True` | Manage docker operations. Action-routed methods: `get_docker_dashboard`, `get_container_gpus`, `docker_list_containers`, `docker_inspect_container`, `docker_get_container_logs`, `docker_get_container_stats`, `docker_start_container`, `docker_stop_container`, `docker_restart_container`, `docker_remove_container`, `docker_list_services`, `docker_inspect_service`, `docker_get_service_logs`, `docker_list_images`, `docker_inspect_image`, `docker_list_networks`, `docker_inspect_network`, `docker_list_volumes`, `docker_inspect_volume`, `docker_get_info`, `docker_get_version`, `docker_get_system_df`, `docker_create_container`, `docker_create_network`, `docker_create_volume`, `docker_create_exec`, `docker_start_exec`, `docker_inspect_exec`, `docker_get_stack_logs`. |
| **Stack** | `STACKTOOL` | `True` | Manage stack operations. Action-routed methods: `get_stacks`, `get_stack`, `get_stack_file`, `create_standalone_stack`, `create_standalone_stack_from_repo`, `update_stack`, `delete_stack`, `start_stack`, `stop_stack`, `redeploy_stack_git`. |
| **Kubernetes** | `KUBERNETESTOOL` | `True` | Manage kubernetes operations. Action-routed methods: `get_k8s_dashboard`, `get_k8s_namespaces`, `get_k8s_applications`, `get_k8s_services`, `get_k8s_ingresses`, `get_k8s_configmaps`, `get_k8s_secrets`, `get_k8s_volumes`, `get_k8s_events`, `get_k8s_nodes_limits`, `get_k8s_metrics_nodes`, `get_helm_releases`, `install_helm_chart`, `delete_helm_release`. |
| **Edge** | `EDGETOOL` | `True` | Manage edge operations. Action-routed methods: `get_edge_groups`, `create_edge_group`, `delete_edge_group`, `get_edge_stacks`, `get_edge_stack`, `create_edge_stack`, `delete_edge_stack`, `get_edge_jobs`, `get_edge_job`, `create_edge_job`, `delete_edge_job`. |
| **Template** | `TEMPLATETOOL` | `True` | Manage template operations. Action-routed methods: `get_templates`, `get_custom_templates`, `get_custom_template`, `create_custom_template`, `delete_custom_template`, `get_custom_template_file`, `get_helm_templates`. |
| **User** | `USERTOOL` | `True` | Manage user operations. Action-routed methods: `get_users`, `get_user`, `get_current_user`, `create_user`, `delete_user`, `get_teams`, `create_team`, `delete_team`, `get_roles`, `get_user_tokens`. |
| **Registry** | `REGISTRYTOOL` | `True` | Manage registry operations. Action-routed methods: `get_registries`, `get_registry`, `create_registry`, `delete_registry`. |
| **System** | `SYSTEMTOOL` | `True` | Manage system operations. Action-routed methods: `get_status`, `get_system_info`, `get_system_version`, `get_settings`, `update_settings`, `get_tags`, `create_tag`, `delete_tag`, `get_motd`, `backup_portainer`. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](file:///home/apps/workspace/agent-packages/agents/portainer-agent/docs/mcp.md).

### MCP Configuration Examples

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "portainer-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "portainer-agent",
        "portainer-mcp"
      ],
      "env": {
        "PORTAINER_ENDPOINT": "your_portainer_endpoint_here",
        "PORTAINER_USERNAME": "your_portainer_username_here",
        "PORTAINER_PASSWORD": "your_portainer_password_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
To run the server as a long-running Streamable-HTTP service:

```json
{
  "mcpServers": {
    "portainer-agent": {
      "url": "http://localhost:8000/portainer-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name portainer-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e PORTAINER_ENDPOINT="your_value" \
  -e PORTAINER_USERNAME="your_value" \
  -e PORTAINER_PASSWORD="your_value" \
  knucklessg1/portainer-agent:latest
```

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export PORTAINER_ENDPOINT="your_value"
export PORTAINER_USERNAME="your_value"
export PORTAINER_PASSWORD="your_value"

# Run the agent server
portainer-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  portainer-agent-mcp:
    image: knucklessg1/portainer-agent:latest
    container_name: portainer-agent-mcp
    hostname: portainer-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  portainer-agent-agent:
    image: knucklessg1/portainer-agent:latest
    container_name: portainer-agent-agent
    hostname: portainer-agent-agent
    restart: always
    depends_on:
      - portainer-agent-mcp
    env_file:
      - ../.env
    command: [ "portainer-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://portainer-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](file:///home/apps/workspace/agent-packages/agents/portainer-agent/docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install portainer-agent[all]

# Using standard pip
python -m pip install portainer-agent[all]
```

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`
