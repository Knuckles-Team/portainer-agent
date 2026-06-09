# portainer-agent

Portainer container-management **MCP Server + A2A Agent** for the agent-utilities
ecosystem — Docker environments, stacks, Kubernetes clusters, registries, users, and
edge devices through one typed tool surface.

!!! info "Official documentation"
    This site is the canonical reference for `portainer-agent`, maintained alongside
    every release.

[![PyPI](https://img.shields.io/pypi/v/portainer-agent)](https://pypi.org/project/portainer-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/portainer-agent)](https://github.com/Knuckles-Team/portainer-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/portainer-agent)

## Overview

`portainer-agent` wraps the [Portainer](https://www.portainer.io/) REST API with
typed, deterministic MCP tools and ships an optional A2A agent server. It provides:

- **`PortainerApi`** — a composed REST client covering authentication, environments,
  Docker, stacks, Kubernetes, edge devices, templates, users, registries, and system.
- **Ten action-dispatch MCP tools** — one per management domain
  (`portainer_auth`, `portainer_docker`, `portainer_stack`, `portainer_kubernetes`,
  `portainer_edge`, `portainer_template`, `portainer_user`, `portainer_registry`,
  `portainer_environment`, `portainer_system`), each gated by a `*TOOL` toggle.
- **An A2A agent server** (`portainer-agent` console script) that routes natural-language
  requests to the relevant domain through a confidence-gated graph orchestrator.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP server and the A2A agent, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `PortainerApi` client, and the CLI.
- :material-database-cog: **[Backing Platform](platform.md)** — deploy Portainer with Docker.
- :material-sitemap: **[Overview](overview.md)** — modes, environment variables, graph routing.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:PORT-*` registry.

</div>

## Quick start

```bash
pip install portainer-agent
portainer-mcp                    # stdio MCP server (default transport)
```

Connect it to a Portainer instance:

```bash
export PORTAINER_URL=http://your-portainer:9000
export PORTAINER_TOKEN=your_api_token
portainer-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
