# Concept Registry — portainer-agent

> **Prefix**: `CONCEPT:PORT-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:AU-ECO.messaging.native-backend-abstraction`](https://github.com/Knuckles-Team/agent-utilities/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:PT-OS.governance.port` | Authentication & Session Management | MCP tool domain `auth` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-2` | Docker Container Management | MCP tool domain `docker` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-3` | Edge Computing & Deployment | MCP tool domain `edge` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-4` | Environment Configuration | MCP tool domain `environment` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-5` | Kubernetes Orchestration | MCP tool domain `kubernetes` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-6` | Container Registry Management | MCP tool domain `registry` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-7` | Stack Deployment & Management | MCP tool domain `stack` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-8` | System Information & Health | MCP tool domain `system` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-9` | Template Management | MCP tool domain `template` — Action-routed dynamic tool registration |
| `CONCEPT:PT-OS.governance.port-10` | User & Identity Management | MCP tool domain `user` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:AU-ECO.messaging.native-backend-abstraction` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:AU-ORCH.adapter.hot-cache-invalidation` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:AU-OS.config.secrets-authentication` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:AU-OS.state.cognitive-scheduler-preemption` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:AU-OS.governance.reactive-multi-axis-budget` | Guardrail Engine | agent-utilities |
| `CONCEPT:AU-OS.governance.wasm-micro-agent-sandbox` | Audit Logging | agent-utilities |
| `CONCEPT:AU-KG.query.object-graph-mapper` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:AU-ECO.messaging.native-backend-abstraction` (Unified Toolkit Ingestion). The `portainer_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all PORT-* concepts.
