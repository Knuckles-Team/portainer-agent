---
name: portainer-agent-development
skill_type: skill
domain: development
description: >-
  Develop, test, gate, and release the portainer-agent connector. Use this skill
  when changing Portainer API wrappers, action-routed MCP tools, packaged content,
  documentation, or repository gates.
license: MIT
tags: [portainer, development, connector, test, gates]
tier: repository
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# portainer-agent development

This repository owns the Portainer API client, authentication boundary, action-routed
MCP tools, optional A2A agent, packaged skills, prompts, ontology, connectors, and
source declarations. Shared MCP contracts, transports, connector serving, and
credential resolution belong to scion-sdk; admission, serving, and durable
graph state belong to their owning repositories. Read AGENTS.md before changing code.
Keep Portainer URLs, tenant identifiers, credentials, endpoint data, and raw API
responses out of source, logs, fixtures, and packaged skill content.

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver small, reviewable slices and cite the owning
spec row in the commit trailer.

- Find the owning row first with git grep -n "<term>" -- specs; extend the existing
  spec before adding requirement text.
- Reuse the SDK Connector entry point in portainer_agent/__init__.py, the
  PortainerApi client, and the action-routed tools in portainer_agent/mcp_server.py.
  Do not create a second connector entry point, transport, graph-write path, or
  parallel policy.
- Preserve the action names, condensed and verbose MCP_TOOL_MODE behavior, and the
  client/auth boundary. PORTAINER_URL, PORTAINER_TOKEN, PORTAINER_USERNAME,
  PORTAINER_PASSWORD, PORTAINER_GIT_TOKEN, and MCP_URL are runtime inputs, not
  packaged defaults.
- Bind delivered behavior to a focused test. Generated specs/*/status.json files
  come from the shared hooks; never hand-edit them.
- Keep skills/**, prompts/**, ontology/**, connectors/**, and mcp_config.json in the
  package-data contract. Put Spec: <ID> and the assisting-agent trailer on consecutive
  final commit message lines.

## Setup and gates

Use the pinned environment and shared gates from the checkout root:

    uv sync --locked
    uvx pre-commit run --all-files

For focused feedback, use the tests that exercise the actual connector paths:

    uv run --locked --extra test pytest tests/test_publication_workflow.py -q
    uv run --locked --extra test pytest tests/test_action_discovery.py tests/test_init_dynamics.py -q
    uv run --locked --extra test pytest tests/test_api_client_base.py tests/test_stack_git_auth.py -q
    uv run --locked --extra test pytest tests/test_kg_ingest.py tests/test_identity_environment_scoping.py -q

Tests use fakes and local fixtures. Do not call a live Portainer endpoint or require
credentials in local gates. Preserve SDK auth delegation, TLS trust policy, API
error mapping, endpoint scoping, action validation, and ontology/source mappings
when changing client or tool modules.

## Packaging and publication

Build with uv build and inspect the wheel and sdist for
portainer_agent/skills/portainer-agent-development/SKILL.md. Keep the project version
and uv.lock aligned for a genuine content release. The canonical Pages publisher is
.github/workflows/pages.yml, which calls the shared pipelines workflow with
.config/spec-dashboard.json; keep workflow_dispatch and do not add another documentation
publisher. The generated dashboard reads specs/*/status.json and is published at
spec-delivery/.

Before pushing, work in a real Git worktree based on origin/main, inspect the complete
diff, stage only reviewed paths, and verify git status --short after each gate. Do not
use git stash, git add -A, git add ., or force-push. Do not claim Pages publication
until a successful exact-source workflow run and the public dashboard are both observed.
