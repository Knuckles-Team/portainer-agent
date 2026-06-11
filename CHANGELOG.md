# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
