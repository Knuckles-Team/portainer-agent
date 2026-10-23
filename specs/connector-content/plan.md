# CONN-PORTAINER-AGENT-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `portainer-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `portainer_agent` from it.
