# Provider workflow catalog

Load only the workflow relevant to the current request.

- [analyze-portainer-health](../../analyze-portainer-health/WORKFLOW.md): Analyze Portainer stack health status and Swarm service status. Correlates Swarm services to Portainer stack namespaces, detects degraded or paused service updates, validates Git-backed source-of-truth status, and generates a visual diagnostic report with actionable remediation recommendations. Use when the user requests a health sweep of the cluster stacks, wants to identify services with update or deployment issues, or needs troubleshooting steps.
- [portainer-agent-docs](../../portainer-agent-docs/WORKFLOW.md): Documentation and API references for Portainer agent
- [portainer-sync-agent](../../portainer-sync-agent/WORKFLOW.md): Portainer Sync Agent atomic skill. Connects to Portainer API, resolves environment IDs, creates or redeploys stacks, and wires GitOps auto-sync configurations using portainer-mcp.
