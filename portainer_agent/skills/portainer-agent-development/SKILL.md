---
name: portainer-agent-development
skill_type: skill
domain: development
description: >-
  Develop, test, gate, and release the portainer-agent connector. Use this skill
  when changing Portainer API wrappers, typed MCP tools, packaged content,
  documentation, or repository gates.
license: MIT
tags: [portainer, development, connector, test, gates]
tier: repository
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# portainer-agent development

This repository owns the Portainer API client, authentication boundary, typed
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
  PortainerApi client, and the typed ingestion tools in portainer_agent/mcp_server.py.
  Do not create a second connector entry point, transport, graph-write path, or
  parallel policy.
- Preserve the typed tool names, one typed tool per operation (no condensed and verbose modes), and the
  client/auth boundary. PORTAINER_URL, PORTAINER_TOKEN, PORTAINER_USERNAME,
  PORTAINER_PASSWORD, PORTAINER_GIT_TOKEN, and MCP_URL are runtime inputs, not
  packaged defaults.
- Bind delivered behavior to a focused test. Generated specs/*/status.json files
  come from the shared hooks; never hand-edit them.
- Keep skills/**, prompts/**, ontology/**, connectors/**, and mcp_config.json in the
  package-data contract. Put Spec: <ID> and the assisting-agent trailer on consecutive
  final commit message lines.

## Steps

1. Find the owning requirement with `git grep -n "<term>" -- specs`. Verify a row exists before editing.
2. Create a worktree from `origin/main` with `git worktree add`. Verify `git status --short` is clean.
3. Make the smallest change in the existing client or tool module under `portainer_agent/`. Verify with `git diff --stat` that only intended files changed.
4. Run the focused tests with `uv run --locked --extra test pytest tests/test_publication_workflow.py -q`. Verify they pass.
5. Run the gates with `uvx pre-commit run --all-files`. Verify every hook reports Passed.
6. Stage an explicit allowlist with `git add -- <paths>` and commit with the `Spec:` trailer. Verify `git diff --cached --name-status` lists only reviewed paths.

## Failure recovery

| Failure | Cause | Recovery |
|---------|-------|----------|
| Locked sync fails | `uv.lock` out of step with `pyproject.toml` | Run `uv sync --locked` in the worktree and fix the dependency the error names. |
| Hook fails on commit | A gate found a formatting, spelling or spec problem | Read the hook output, fix the named file, and commit again with hooks active. |
| Test uses a live endpoint | A fixture reads real credentials | Replace it with a local fake and re-run `tests/test_api_client_base.py`. |

## Setup and gates

Use the pinned environment and shared gates from the checkout root:

    uv sync --locked
    uvx pre-commit run --all-files

For focused feedback, use the tests that exercise the actual connector paths:

    uv run --locked --extra test pytest tests/test_publication_workflow.py -q
    uv run --locked --extra test pytest tests/test_init_dynamics.py -q
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
