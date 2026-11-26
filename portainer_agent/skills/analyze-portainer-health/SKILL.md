---
name: analyze-portainer-health
skill_type: skill
description: >-
  Analyze Portainer stack and Swarm service health: correlates services to stacks, detects paused or degraded updates and Git drift, and writes a remediation report. Use for a cluster health sweep, to find services with update or deployment issues, or to troubleshoot stacks.
license: MIT
tags:
  - portainer
  - docker-swarm
  - monitoring
  - health-check
  - devops
metadata:
  author: Repository Maintainers
  version: '0.1.21'
---

# Analyze Portainer Health Skill

Scope: Analyze Portainer stack health status and Swarm service status. Correlates Swarm services to Portainer stack namespaces, detects degraded or paused service updates, validates Git-backed source-of-truth status, and generates a visual diagnostic report with actionable remediation recommendations. Use when the user requests a health sweep of the cluster stacks, wants to identify services with update or deployment issues, or needs troubleshooting steps.

The `analyze-portainer-health` skill provides a comprehensive diagnostic sweep of Docker Swarm services and Portainer stacks. It correlates Swarm services with their parent stacks, identifies update states, highlights manual configuration drift, and generates a formatted health report with precise remediation steps.

## Trigger Scenarios

Use this skill when:
- The user requests a status report of Portainer stacks or Swarm services.
- A service is failing to update, rollback, or start up correctly.
- You need to evaluate the alignment between deployed Portainer stacks and their Git repositories.
- You need structured cluster-wide telemetry or a detailed health assessment of Endpoint 3 (Homelab Swarm).

## Resources

This skill includes:

### scripts/analyze_health.py
A deterministic Python 3 utility script that parses JSON extracts of Portainer stacks and Swarm services, correlates them, evaluates individual service health, and writes a detailed markdown diagnostic report.

## Steps

1. Extract stacks by calling `portainer_get_stacks` (via `pt__stack` with action `get_stacks`), saving the JSON to `stacks.json`. Verify the file lists the stacks of the target endpoint.
2. Extract Swarm services with the `pt__docker` tool or the Portainer list-services action, saving the JSON to `services.json`. Verify the file is non-empty and includes `Spec.Labels`.
3. Run the analyzer with `python scripts/analyze_health.py --stacks-json stacks.json --services-json services.json --output stack_health_report.md`. Verify the command exits 0 and writes the report.
4. Read the report with `cat stack_health_report.md`. Verify each stack is classified Unhealthy, Degraded or Healthy under the rules below.
5. Present the Unhealthy and Degraded stacks with their remediation steps, taken from `stack_health_report.md`. Verify every flagged stack in the report appears in your summary.

## Failure recovery

| Failure | Cause | Recovery |
|---------|-------|----------|
| Empty stacks file | Wrong endpoint id, or `PORTAINER_URL` or `PORTAINER_TOKEN` missing | Resolve the endpoint with `portainer_get_endpoints`, set both variables, and extract again with `portainer_get_stacks`. |
| Services not matched to stacks | No `com.docker.stack.namespace` label on the services | Check `Spec.Labels` and `PreviousSpec.Labels` in `services.json`, and confirm service names start with the stack name before running the script again with the corrected extract. |
| Script cannot read input | A path passed to `--stacks-json` or `--services-json` is wrong | Run `ls` on both paths and pass the real file locations. |

## Step-by-Step Diagnostic Workflow

### Step 1: Extract Portainer Stacks and Swarm Services Data
Execute Portainer or Docker Swarm MCP actions to dump live JSON metadata for stacks and services:
- **Stacks**: Call `mcp_mcp-multiplexer_pt__stack` with action `get_stacks` (e.g. for Endpoint 3) and save the JSON result.
- **Services**: Call `mcp_mcp-multiplexer_pt__docker` with action `docker_list_containers` or query the direct service API, or call Portainer's list services action.

### Step 2: Execute the Health Analyzer
Run the packaged script on the saved JSON extracts to correlate services and output the markdown report:

```bash
python scripts/analyze_health.py \
  --stacks-json /path/to/stacks.json \
  --services-json /path/to/services.json \
  --output /path/to/stack_health_report.md
```

### Step 3: Analyze Results and Present to User
Read the generated report at `/path/to/stack_health_report.md` or output to stdout. Highlight any **Unhealthy** or **Degraded** stacks and detail the recommended remediation steps.

## Namespace Correlation Logic Rules

To ensure 100% accurate classification, services are correlated with stacks in `scripts/analyze_health.py` using:
1. **Direct Label Match**: Look for `com.docker.stack.namespace` inside `Spec.Labels`.
2. **Previous Spec Match**: If missing, look for `com.docker.stack.namespace` in `PreviousSpec.Labels`.
3. **Prefix Suffix Match**: If no label is found, parse the service name (split by `_`) and match the first segment to a Portainer stack name.

## Health Classification Rules

- 🔴 **Unhealthy (Action Required)**: Active stack containing one or more services whose updates have `paused` or `failed`.
- 🟡 **Degraded (Warning)**: Active stack containing one or more services whose updates are currently `updating` or `rolling back`.
- 🟢 **Healthy (Operational)**: Active stack with all services successfully updated and running normally.
