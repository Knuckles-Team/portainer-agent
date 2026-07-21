# Backing Platform — Portainer

`portainer-agent` is a **client** of a Portainer instance. This page provides a Docker
recipe for deploying one locally to serve as the target of `PORTAINER_URL`. For
production topologies, follow the upstream
[Portainer documentation](https://docs.portainer.io/).

!!! note "Backing-system recipe"
    Each connector in the ecosystem follows the same convention — a
    `docs/platform.md` recipe for the system it integrates with, accompanied by a
    sample Compose stack that mirrors [`services/`](https://github.com/Knuckles-Team).
    Systems offered only as a managed service have no local recipe.

## Single-node deployment (Compose)

Portainer publishes the `portainer/portainer-ce` Community Edition image. The following
stack runs one Portainer instance on `:9000` (HTTP) with persistent data:

```yaml
# docker/portainer.compose.yml
services:
  portainer:
    image: docker.io/portainer/portainer-ce@sha256:<digest>
    container_name: portainer
    hostname: portainer
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    ports:
      - "9000:9000"            # web UI + REST API
      - "9443:9443"            # web UI + REST API (HTTPS, self-signed)
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - portainer:/data
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:9000/api/status"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 20s

volumes:
  portainer:
```

```bash
docker compose -f docker/portainer.compose.yml up -d

# Wait for the API status endpoint to answer
curl -s http://localhost:9000/api/status
```

Open `http://localhost:9000`, create the admin account, then mint an **API access
token** (User settings → Access tokens) for `PORTAINER_TOKEN`.

## Connect portainer-agent

```bash
export PORTAINER_URL=http://localhost:9000
export PORTAINER_TOKEN=your_api_token
# TLS policy is resolved from the XDG AgentConfig profile.
export SSL_CERT_FILE=/run/secrets/private-ca-bundle.pem

portainer-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

## Combined deployment

A combined stack places Portainer and the MCP server on one Docker network, so the
server reaches Portainer by container name:

```yaml
# docker/stack.compose.yml
services:
  portainer:
    image: docker.io/portainer/portainer-ce@sha256:<digest>
    hostname: portainer
    ports: ["9000:9000"]
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - portainer:/data

  portainer-agent-mcp:
    image: example/portainer-agent@sha256:<digest>
    depends_on: [portainer]
    environment:
      - PORTAINER_URL=http://portainer:9000
      - PORTAINER_TOKEN=your_api_token
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8000
    ports: ["8000:8000"]

volumes:
  portainer:
```

```bash
docker compose -f docker/stack.compose.yml up -d
```

## Manage Portainer from an agent

With both services running, the [MCP tools](usage.md#as-an-mcp-server) and the A2A
[agent server](deployment.md#a2a-agent-server) can list environments, deploy and
control stacks, inspect Kubernetes clusters, and report system health through one typed
interface.
