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

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and guidance for provisioning the Portainer platform are maintained in
> the [official documentation](https://knuckles-team.github.io/portainer-agent/).

---

## Overview

**Portainer Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Complete support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices. API. The operator can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server use dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools

This table is auto-generated from the live server — do not edit by hand.

<!-- MCP-TOOLS-TABLE:START -->

#### Typed tools (one per operation)

Every Portainer operation is its own typed `portainer_<operation>` tool, derived from the
`PortainerApi` client methods: stacks, Docker workloads, Kubernetes, Helm, edge, templates,
registries, users and teams, resource controls, webhooks, settings and sign-in. The
hand-written tools are `portainer_ingest_environments`, `portainer_ingest_containers` and
`portainer_system_raw_request`. Destructive tools take `confirm=true`.

<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/usage.md](docs/usage.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows the operator to restrict the set of exposed tools to prevent blowing up the LLM's context window.

The operator can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to the operator's transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the connector-focused `[mcp]` extra.** Examples use `portainer-agent[mcp]` to add
> FastMCP / FastAPI through `scion-sdk[mcp]`; the required Meristem core
> still carries `medulla[full]`. The `[agent-runtime]` extra additionally
> enables model orchestration.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "portainer-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "portainer-agent[mcp]",
        "portainer-mcp"
      ],
      "env": {
        "MCP_TOOL_MODE": "intent",
        "AUTHTOOL": "True",
        "DOCKERTOOL": "True",
        "EDGETOOL": "True",
        "ENVIRONMENTTOOL": "True",
        "KUBERNETESTOOL": "True",
        "PORTAINER_GIT_USERNAME": "oauth2",
        "PORTAINER_TOKEN": "your_portainer_api_token_here",
        "PORTAINER_URL": "http://localhost:9000",
        "REGISTRYTOOL": "True",
        "STACKTOOL": "True",
        "SYSTEMTOOL": "True",
        "TEMPLATETOOL": "True",
        "USERTOOL": "True"
      }
    }
  }
}
```

Runtime references require an alias-aware launcher such as Arbora. Other
launchers must omit those entries and inject the resolved values through their
own runtime secret boundary.

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "portainer-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "portainer-agent[mcp]",
        "portainer-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "MCP_TOOL_MODE": "intent",
        "AUTHTOOL": "True",
        "DOCKERTOOL": "True",
        "EDGETOOL": "True",
        "ENVIRONMENTTOOL": "True",
        "KUBERNETESTOOL": "True",
        "PORTAINER_GIT_USERNAME": "oauth2",
        "PORTAINER_TOKEN": "your_portainer_api_token_here",
        "PORTAINER_URL": "http://localhost:9000",
        "REGISTRYTOOL": "True",
        "STACKTOOL": "True",
        "SYSTEMTOOL": "True",
        "TEMPLATETOOL": "True",
        "USERTOOL": "True"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "portainer-mcp": {
      "url": "http://localhost:8000/portainer-mcp/mcp"
    }
  }
}
```

Run a reviewed container image as a least-privilege stdio child (no
listener or published port):

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  -e MCP_TOOL_MODE=intent \
  -e AUTHTOOL=True \
  -e DOCKERTOOL=True \
  -e EDGETOOL=True \
  -e ENVIRONMENTTOOL=True \
  -e KUBERNETESTOOL=True \
  -e PORTAINER_GIT_USERNAME=oauth2 \
  -e PORTAINER_TOKEN=your_portainer_api_token_here \
  -e PORTAINER_URL=http://localhost:9000 \
  -e REGISTRYTOOL=True \
  -e STACKTOOL=True \
  -e SYSTEMTOOL=True \
  -e TEMPLATETOOL=True \
  -e USERTOOL=True \
  registry.example.invalid/portainer-agent@sha256:<digest> portainer-mcp
```

For containerized network HTTP, supply an authenticated TLS ingress (or
direct server TLS), exact `MCP_ALLOWED_HOSTS`, and an exact trusted-proxy
CIDR policy through the operator-owned deployment profile. The generator
does not emit an unauthenticated non-loopback listener.

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`portainer-agent` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/portainer-agent/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
<!-- END GENERATED: additional-deployment-options -->

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts smoothly with the **Agent Web UI (AG-UI)** and Terminal interface.

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
    image: example/portainer-agent:mcp
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
    image: example/portainer-agent@sha256:<digest>
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

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/deployment.md](docs/deployment.md).

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `PORTAINER_URL` | `http://localhost:9000` |  |
| `PORTAINER_PASSWORD` | secret-injected |  |
| `PORTAINER_TOKEN` | secret-injected |  |
| `PORTAINER_GIT_USERNAME` | `oauth2` | username for git-backed stack auth (default: oauth2) |
| `PORTAINER_GIT_TOKEN` | secret-injected | token for private git repos used by stacks |
| `GITLAB_TOKEN` | secret-injected | fallback token when PORTAINER_GIT_TOKEN is unset |
| `AUTHTOOL` | `True` |  |
| `ENVIRONMENTTOOL` | `True` |  |
| `DOCKERTOOL` | `True` |  |
| `STACKTOOL` | `True` |  |
| `KUBERNETESTOOL` | `True` |  |
| `EDGETOOL` | `True` |  |
| `TEMPLATETOOL` | `True` |  |
| `USERTOOL` | `True` |  |
| `REGISTRYTOOL` | `True` |  |
| `SYSTEMTOOL` | `True` |  |

#### Inherited scion-sdk variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `intent` | Tool surface: `intent` \| `condensed` \| `verbose` \| `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_27 package + 16 inherited variable(s). Auto-generated from `.env.example` + the shared scion-sdk set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads, grouped by purpose.

### Connection & Credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `PORTAINER_URL` | Base HTTP/HTTPS URL of the operator's Portainer instance. | `http://localhost:9000` |
| `PORTAINER_ENDPOINT` | Alternative Portainer socket / connection endpoint path. | `unix:///var/run/portainer/events.sock` |
| `PORTAINER_USERNAME` | Username for basic authentication. | `admin` |
| `PORTAINER_PASSWORD` | Password for basic authentication. | — |
| `PORTAINER_TOKEN` | API token (alternative to username/password). | — |

TLS trust anchors, mTLS material, and proxy policy are resolved from the active XDG
AgentConfig `TLS_PROFILE`/`TLS_PROFILE_REF`. Certificate and hostname verification
cannot be disabled.

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse`. | `stdio` |
| `HOST` | Bind host (HTTP transports). | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports). | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both`. | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list. | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list. | — |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers). | `1` |

### Tool toggles
The tool surface is the typed per-operation tools; there are no per-domain toggles.

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export. | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint. | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys. | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`). | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote`. | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file. | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL. | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to. | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`). | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`). | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface. | `True` |

See [`.env.example`](.env.example) for a copy-paste starting point.

---

## Security & Governance

Built directly upon the enterprise-ready [`scion-sdk`](https://github.com/Knuckles-Team/scion-sdk) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Feature | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Pick the extra that matches what the operator want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `portainer-agent[mcp]` | Connector-focused MCP server (`scion-sdk[mcp]` — FastMCP/FastAPI + `medulla[full]`) | The operator only run the **MCP server** (smallest install / image) |
| `portainer-agent[agent]` | Agent runtime (`scion-sdk[agent-runtime,logfire]` — model orchestration + `medulla[full]`) | The operator run the **integrated agent** |
| `portainer-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# Connector-focused MCP server (includes the shared graph engine)
uv pip install "portainer-agent[mcp]"

# Agent runtime (adds model orchestration to the shared graph engine)
uv pip install "portainer-agent[agent]"

# Everything (development)
uv pip install "portainer-agent[all]"      # or: python -m pip install "portainer-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `example/portainer-agent:mcp` | `--target mcp` | `portainer-agent[mcp]` — **connector-focused**, includes `medulla[full]`; no model-orchestration stack | `portainer-mcp` |
| `example/portainer-agent@sha256:<digest>` | `--target agent` (default) | `portainer-agent[agent]` — **agent runtime**, model orchestration + `medulla[full]` | `portainer-agent` |

```bash
docker build --target mcp   -t example/portainer-agent:mcp    docker/   # connector-focused MCP server
docker build --target agent -t example/portainer-agent:agent-local docker/   # agent runtime
```

`docker/mcp.compose.yml` runs the connector-focused `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`medulla`)

Both `[mcp]` and `[agent]` carry the **medulla** engine through the required
Meristem core dependency (`medulla[full]`). The `[mcp]` extra keeps
the server connector-focused; `[agent]` also enables model orchestration. Local
deployments can use the bundled engine. For production or shared state, run
**medulla as a dedicated database service** and configure the runtime to use it.
Deployment recipes (single-node + Raft HA), connection configuration, and architecture
diagrams are documented in the
[medulla deployment guide](https://knuckles-team.github.io/medulla/deployment/).

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/portainer-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/portainer-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/portainer-agent/deployment/) | run the MCP server and A2A agent, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/portainer-agent/usage/) | the MCP tools, the `PortainerApi` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/portainer-agent/platform/) | deploy Portainer with Docker |
| [Overview](https://knuckles-team.github.io/portainer-agent/overview/) | modes, environment variables, graph routing |
| [Concepts](https://knuckles-team.github.io/portainer-agent/concepts/) | concept registry (`CONCEPT:PORT-*`) |

`AGENTS.md` is the canonical contributor/agent guidance.

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=example&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/example)
![GitHub User's stars](https://img.shields.io/github/stars/example)

---

## Contribute

Contributions are welcome! Please ensure code quality by running local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Ran test suites using `pytest`


<!-- BEGIN scion-sdk-deployment (generated; do not edit between markers) -->

## Deploy with `scion-sdk-deployment`

Provision this package with the consolidated **`scion-sdk-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `portainer-agent` with scion-sdk-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "portainer-agent[mcp]"`, then run `portainer-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `portainer-mcp` |
| Immutable container | deploy `registry.example.invalid/portainer-agent@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END scion-sdk-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, Arbora delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
