# Portainer Agent - A2A | AG-UI | MCP

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

*Version: 0.1.1*

## Overview

**Portainer Agent MCP Server + A2A Agent**

Agent package for Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices.

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `PORTAINER_URL`: The URL of the target Portainer service.
*   `PORTAINER_TOKEN`: The API token or access token.
*   `PORTAINER_VERIFY`: Verify SSL certificate (default: True).

#### Run in stdio mode (default):
```bash
export PORTAINER_URL="http://localhost:9000"
export PORTAINER_TOKEN="your_token"
portainer-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export PORTAINER_URL="http://localhost:9000"
export PORTAINER_TOKEN="your_token"
portainer-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export PORTAINER_URL="http://localhost:9000"
export PORTAINER_TOKEN="your_token"
portainer-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Docker

### Build

```bash
docker build -t portainer-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name portainer-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e PORTAINER_URL="http://your-service:9000" \
  -e PORTAINER_TOKEN="your_token" \
  knucklessg1/portainer-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  portainer-agent:
    image: knucklessg1/portainer-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - PORTAINER_URL=http://your-service:9000
      - PORTAINER_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "portainer": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "portainer-agent",
        "portainer-mcp"
      ],
      "env": {
        "PORTAINER_URL": "http://your-service:9000",
        "PORTAINER_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install portainer-agent
```
```bash
uv pip install portainer-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
