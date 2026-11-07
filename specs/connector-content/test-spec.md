# CONN-PORTAINER-AGENT-CONNECTOR-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R001` | `tests/test_default_content_surfaces.py::test_default_content_surfaces` (planned) | `resources/list` includes `skill://` and `ontology://`; `prompts/list` includes each packaged prompt. |
| T-002 | `CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R002` | `tests/test_access_contracts.py::test_competency_contracts_certified` (planned) | Test: `tests/test_access_contracts.py::test_competency_contracts_certified` (L2) runs the connector ontology certification and validates each recording against its contract. |

## Negative and boundary cases

Each proving test above includes the refusal or error case that its row names. A vendor outage or an unauthorised call must return the SDK typed error.

## Quality and release proof

Run `uv run pytest tests` and `pre-commit run --all-files` from the repository root. A planned test is added by the code change that lands the row.
| T-003 | `CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R003` | `tests/test_served_dispatch_targets_exist.py` | Every referenced client method exists. |
| T-004 | `CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R004` | `tests/test_kubernetes_rbac_and_helm_routes.py` | RBAC reads use the served routes; the Helm chart listing sends `repo`. |

## Adoption of scion-sdk 0.10.0 (`CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R005`)

| Requirement | Test | Observation |
|---|---|---|
| `CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R005` | `tests/test_scion_sdk_0_10_imports.py::test_every_scion_sdk_import_resolves_on_the_pinned_release` | Every `scion_sdk` import resolves on the pinned release; a removed path fails the test. |
