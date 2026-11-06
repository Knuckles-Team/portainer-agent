# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.12] - 2026-11-06

### Changed
- Connector surface: agent-definition prompts (operator, release deployer, container operator, access administrator), task skills, tool-use contracts for all tools, data locations and roles; ontology classes extend core classes.
- Require `scion-sdk>=0.9.0`; `uv.lock` relocked.
- The unregistered condensed action-routed `portainer_{auth,docker,edge,environment,kubernetes,registry,stack,system,template,user}` modules and their characterization tests are removed; the typed per-operation tools are the surface. `portainer_system_raw_request` is a typed tool.

## [2.3.9] - 2026-10-30

### Changed
- Require `scion-sdk>=0.6.4,<0.7.0`; `uv.lock` relocked.

## [2.3.7] - 2026-10-26

### Added
- Adopt the canonical spec-delivery Pages dashboard and package the portainer-agent development skill.

## [2.3.6] - 2026-10-24

### Changed
- Central connector migration: requires `agent-connector-sdk>=0.5.4`; server bootstrap, version, containers, ontology artifacts, security scaffold and pre-commit config are provided centrally.

## [Unreleased]

### Added
- Per-user git credentials (typed, 1:1): get/get-one/create/update/remove via
  `/users/{id}/gitcredentials`, exposed as `port__user` actions. Provision a
  reusable credential once and bind it to git-backed stacks via
  `RepositoryGitCredentialID` so Portainer redeploys them unattended.
- Generic API passthrough: `BaseApiClient.request(method, path, params, data)`
  plus a `port__system` `raw_request` action, making the entire Portainer REST
  API reachable via MCP (any method/path) without hand-written wrappers for the
  long tail of operations.

### Fixed
- Inject git auth on GitOps stack creation (swarm/standalone/kubernetes
  `*_from_repository`), not just redeploy, so private-repo stacks authenticate
  via `PORTAINER_GIT_TOKEN`/`GITLAB_TOKEN` without callers passing secrets.

### Added
- Action-Routed dynamic metaprogramming to drastically reduce tool limits while preserving 1:1 endpoint parity

### Changed
- Replaced 108 independent tools with 10 tag-grouped dynamic routers
- Standardized tool schemas and removed any underscored parameters
- `BaseApiClient` internals strangled onto the shared
  `agent_utilities.http.BaseApiClient` fleet base: same public surface
  (`session`, `_url`, `_get/_post/_put/_patch/_delete/_list` and their
  return shapes), now with typed error mapping, rate-limit capture, bounded
  429 backoff, and log redaction. The transport remains the client's
  `requests.Session` via an adapter, so raw-session call sites
  (`backup`/`restore`) and existing test fixtures are unaffected.
- Bumped `agent-utilities` pin to `>=0.47.2` — **requires unreleased
  agent-utilities (`agent_utilities.http` ships in the next release) — do
  not push until that release is on PyPI**; until then, run tests with the
  dev tree on `PYTHONPATH` and expect `uv lock` against the public index to
  fail to resolve.

### Fixed
- Pydantic V2 validations and Pytest failures related to missing parameters or schema conflicts

## [0.1.29] - 2026-04-29

### Added
- Initial release
