# Concept Registry — portainer-agent

> **Prefix**: `CONCEPT:PORT-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:ECO-4.0`](../../agent-utilities/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:PORT-001` | Authentication & Session Management | MCP tool domain `auth` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-002` | Docker Container Management | MCP tool domain `docker` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-003` | Edge Computing & Deployment | MCP tool domain `edge` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-004` | Environment Configuration | MCP tool domain `environment` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-005` | Kubernetes Orchestration | MCP tool domain `kubernetes` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-006` | Container Registry Management | MCP tool domain `registry` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-007` | Stack Deployment & Management | MCP tool domain `stack` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-008` | System Information & Health | MCP tool domain `system` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-009` | Template Management | MCP tool domain `template` — Action-routed dynamic tool registration |
| `CONCEPT:PORT-010` | User & Identity Management | MCP tool domain `user` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:ECO-4.0` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:ORCH-1.2` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:OS-5.1` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:OS-5.2` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:OS-5.3` | Guardrail Engine | agent-utilities |
| `CONCEPT:OS-5.4` | Audit Logging | agent-utilities |
| `CONCEPT:KG-2.0` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:ECO-4.0` (Unified Toolkit Ingestion). The `portainer_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all PORT-* concepts.
