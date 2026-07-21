# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`portainer-agent` supports local stdio, a loopback-only development listener, a
least-privilege stdio container, and a remote authenticated HTTPS boundary.
Provider endpoint, credential, selector, identity, and trust material are supplied
at runtime through `AgentConfig`; none is stored in this repository.

### Installed stdio process

```json
{
  "mcpServers": {
    "portainer": {
      "command": "portainer-mcp",
      "args": [],
      "env": {"MCP_TOOL_MODE": "intent"}
    }
  }
}
```

### Loopback development listener

```bash
portainer-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Do not expose this listener beyond loopback. Network deployments require direct TLS
or an explicitly trusted TLS-terminating ingress, configured authentication, exact
`MCP_ALLOWED_HOSTS`, and an exact trusted-proxy CIDR policy.

### Least-privilege local container

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  registry.example.invalid/portainer-agent@sha256:<digest> portainer-mcp
```

The operator projects the selected AgentConfig profile into the process at runtime;
the image remains immutable and contains no environment connection profile.

### Remote authenticated HTTPS endpoint

```json
{
  "mcpServers": {
    "portainer": {"url": "https://service.example.invalid/mcp"}
  }
}
```

Store the real remote URL, outbound identity reference, and TLS-profile reference in
`AgentConfig`, not in MCP client JSON or documentation.
<!-- END GENERATED: deployment-options -->

This page covers running `portainer-agent` as a long-lived service: the MCP
transports, the optional A2A agent server, a Docker Compose stack, putting it behind a
Caddy reverse proxy, and giving it a DNS name with Technitium. To provision the
**Portainer** instance it connects to, see [Backing Platform](platform.md).

> `portainer-agent` ships **two** console scripts: an **MCP server** (`portainer-mcp`)
> that exposes the typed Portainer tool surface, and an **A2A agent server**
> (`portainer-agent`) that routes natural-language requests to those tools through a
> graph orchestrator.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    portainer-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    portainer-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    portainer-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`portainer-agent` is configured entirely from the environment. The **required** set:

| Var | Default | Meaning |
|---|---|---|
| `PORTAINER_URL` | `http://localhost:9000` | Portainer instance URL |
| `PORTAINER_TOKEN` | _(empty)_ | API access token (`X-API-Key`) |
| `PORTAINER_USERNAME` | `admin` | Username for username/password auth |
| `PORTAINER_PASSWORD` | _(empty)_ | Password for username/password auth |
| `HOST` | `0.0.0.0` | Bind address (HTTP transports) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse` |

TLS trust anchors, mTLS material, and proxy policy come from the active XDG
AgentConfig `TLS_PROFILE`/`TLS_PROFILE_REF`; peer and hostname verification are
mandatory.

Each management domain is gated by a `*TOOL` toggle — `AUTHTOOL`, `ENVIRONMENTTOOL`,
`DOCKERTOOL`, `STACKTOOL`, `KUBERNETESTOOL`, `EDGETOOL`, `TEMPLATETOOL`, `USERTOOL`,
`REGISTRYTOOL`, `SYSTEMTOOL` (all `True` by default). The full set, including telemetry
(OTEL) and access-governance (Eunomia) options, is documented in
[`.env.example`](https://github.com/Knuckles-Team/portainer-agent/blob/main/.env.example).
Copy it to `.env` and fill in only what you use.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/portainer-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
services:
  portainer-agent-mcp:
    image: example/portainer-agent@sha256:<digest>
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
```

```bash
cp .env.example .env          # then edit PORTAINER_* values
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## A2A agent server

`portainer-agent` also ships an **A2A agent server** (console script `portainer-agent`).
It connects to the MCP server over HTTP and exposes a natural-language interface with
an optional web UI.

```bash
export PORTAINER_URL=http://your-portainer:9000
export PORTAINER_TOKEN=your_api_token
portainer-agent --provider openai --model-id gpt-4o --api-key sk-...
```

The repo ships [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/portainer-agent/blob/main/docker/agent.compose.yml),
which runs the MCP server and the agent together. The agent listens on `:9004` and
reaches the MCP server by container name via `MCP_URL`:

```yaml
services:
  portainer-agent-mcp:
    image: example/portainer-agent@sha256:<digest>
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

  portainer-agent-agent:
    image: example/portainer-agent@sha256:<digest>
    container_name: portainer-agent-agent
    hostname: portainer-agent-agent
    restart: always
    depends_on:
      - portainer-agent-mcp
    env_file:
      - ../.env
    command: ["portainer-agent"]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://portainer-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
    ports:
      - "9004:9004"
```

```bash
docker compose -f docker/agent.compose.yml up -d
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .example.invalid zone
portainer-agent.example.invalid {
    tls internal
    reverse_proxy portainer-agent-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
portainer-agent.example.com {
    reverse_proxy portainer-agent-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.example.invalid:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=portainer-agent.example.invalid" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=192.0.2.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `portainer-agent.example.invalid → <caddy-host-ip>` in the Technitium web
console (`http://technitium.example.invalid:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json` (multiplexer nickname `pt`):

```json
{
  "mcpServers": {
    "portainer-agent": {
      "command": "uv",
      "args": ["run", "portainer-mcp"],
      "env": {
        "PORTAINER_URL": "http://your-portainer:9000",
        "PORTAINER_TOKEN": "your_api_token"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://portainer-agent.example.invalid/mcp` instead.
