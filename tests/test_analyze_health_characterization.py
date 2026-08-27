"""Characterization tests for ``analyze_health.main`` (CCN 53).

``portainer_agent/skills/analyze-portainer-health/scripts/analyze_health.py``
is a standalone CLI script (no package ``__init__.py`` along its path, and
no existing test coverage anywhere in the repo before this file), so it is
loaded directly by file path via ``importlib.util``. Pins the pre-refactor
behavior of ``main()`` -- stack/service correlation (direct label, PreviousSpec
label, and name-prefix namespace fallback), replicas resolution (Replicated
count, Global, and the default-1 fallback), image resolution (direct label
vs. TaskTemplate.ContainerSpec.Image, with @sha256 digest stripping),
health classification (Healthy/Degraded/Unhealthy/Healthy (Empty)), the
rendered Markdown report (asserted as an exact golden snapshot captured from
the unmodified script), the JSON-load error path, and the report-write
error path. Part of the CXA-FL-PORTAINERAGENT-01 complexity-reduction
program.
"""

import importlib.util
import json
import sys

import pytest

_SCRIPT_PATH = (
    __file__.rsplit("/tests/", 1)[0]
    + "/portainer_agent/skills/analyze-portainer-health/scripts/analyze_health.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "analyze_health_under_test", _SCRIPT_PATH
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def mod():
    return _load_module()


STACKS_FIXTURE = [
    {
        "Id": 1,
        "Name": "web",
        "Status": 1,
        "CreationDate": 1700000000,
        "UpdateDate": 1700003600,
        "UpdatedBy": "alice",
        "GitConfig": {
            "RepositoryURL": "https://gitlab.example/infra/web.git",
            "RepositoryReferenceName": "refs/heads/main",
        },
    },
    {
        "Id": 2,
        "Name": "db",
        "Status": 1,
        "CreationDate": 1700000000,
        "UpdateDate": 1700003600,
        "UpdatedBy": "bob",
        "GitConfig": None,
    },
    {
        "Id": 3,
        "Name": "cache",
        "Status": 2,
        "CreationDate": 1700000000,
        "UpdateDate": 1700003600,
        "UpdatedBy": "N/A",
        "GitConfig": None,
    },
    {
        "Id": 4,
        "Name": "empty-stack",
        "Status": 1,
        "CreationDate": 1700000000,
        "UpdateDate": 1700003600,
        "UpdatedBy": "carol",
        "GitConfig": {
            "RepositoryURL": "https://gitlab.example/infra/empty.git",
            "RepositoryReferenceName": "refs/heads/main",
        },
    },
]

SERVICES_FIXTURE = [
    {
        "ID": "svc1id",
        "Spec": {
            "Name": "web_frontend",
            "Labels": {
                "com.docker.stack.namespace": "web",
                "com.docker.stack.image": "nginx:1.25",
            },
            "Mode": {"Replicated": {"Replicas": 3}},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "nginx:1.25@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                },
                "Placement": {"Constraints": ["node.role==worker"]},
            },
        },
        "UpdateStatus": {
            "State": "failed",
            "Message": "task failed: no suitable node",
            "StartedAt": 1700004000,
            "CompletedAt": None,
        },
        "CreatedAt": 1699990000,
        "UpdatedAt": 1700004000,
    },
    {
        "ID": "svc2id",
        "Spec": {
            "Name": "web_backend",
            "Labels": {"com.docker.stack.namespace": "web"},
            "Mode": {"Replicated": {"Replicas": 2}},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "myapp:2.0@sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
                },
                "Placement": {},
            },
        },
        "UpdateStatus": {
            "State": "completed",
            "Message": "",
            "StartedAt": None,
            "CompletedAt": 1700004500,
        },
        "CreatedAt": 1699990100,
        "UpdatedAt": 1700004500,
    },
    {
        "ID": "svc3id",
        "Spec": {
            "Name": "db_primary",
            "Labels": {},
            "PreviousSpec": {"Labels": {"com.docker.stack.namespace": "db"}},
            "Mode": {"Global": {}},
            "TaskTemplate": {
                "ContainerSpec": {"Image": "postgres:15"},
                "Placement": {"Constraints": []},
            },
        },
        "UpdateStatus": {
            "State": "updating",
            "Message": "rolling out",
            "StartedAt": 1700005000,
            "CompletedAt": None,
        },
        "CreatedAt": 1699990200,
        "UpdatedAt": 1700005000,
    },
    {
        "ID": "svc4id",
        "Spec": {
            "Name": "standalone_worker",
            "Labels": {},
            "Mode": {"Replicated": {"Replicas": 1}},
            "TaskTemplate": {
                "ContainerSpec": {"Image": "worker:latest"},
                "Placement": {},
            },
        },
        "UpdateStatus": {
            "State": "completed",
            "Message": "",
            "StartedAt": None,
            "CompletedAt": None,
        },
        "CreatedAt": 1699990300,
        "UpdatedAt": 1699990300,
    },
]

# Golden snapshot captured verbatim from `main()` on the UNMODIFIED script,
# run against STACKS_FIXTURE / SERVICES_FIXTURE above. Covers: direct-label
# namespace resolution, PreviousSpec-label namespace fallback, name-prefix
# namespace guess (orphan), Replicated/Global/default-1 replicas, image via
# direct label vs. via ContainerSpec.Image with @sha256 stripped vs. left
# untouched, and all four health buckets (Unhealthy/Degraded/Healthy
# (Empty)/orphan services).
GOLDEN_REPORT = """# 📋 Homelab Swarm Stack Health Report

> [!IMPORTANT]
> This report presents a comprehensive health assessment of the **4** Portainer stacks and **4** Swarm services.

## 📊 Executive Summary

| Metric | Value | Status |
| :--- | :---: | :--- |
| **Total Portainer Stacks** | 4 | - |
| **Total Swarm Services** | 4 | - |
| **Healthy Stacks** | 2 | 🟢 Operational |
| **Degraded Stacks** | 1 | 🟡 Warning (Updating/Rollback) |
| **Unhealthy Stacks** | 1 | 🔴 Action Required (Update Paused) |
| **Standalone Swarm Services** | 1 | 🌐 Unmanaged by Portainer Stacks |


## 💡 Key Diagnostics & Recommendations

### Critical Remediation Actions Required:

- **Stack `web` is Unhealthy**:
  - Service `web_frontend` update state is `failed`. Error message: *task failed: no suitable node*
  - *Action*: Inspect the task exit codes and container logs using `docker service ps` and `docker service logs`.


### Warning / Active Updates:

- **Stack `db` is Degraded**:
  - Service `db_primary` update state is `updating`.
  - *Action*: Monitor the roll-out progression or check if resources are constrained on the active node.


### Git Source of Truth Alignment:

- **2** stacks are deployed manually/ad-hoc (no associated Git configuration):
  - `cache` (ID: 3)
  - `db` (ID: 2)
  - *Action*: Seed GitLab repositories for these orphan stacks to ensure configuration management, change control, and pipeline stability.


---

## 🔴 Unhealthy Stacks (Action Required)

### 📦 Stack: `web` (ID: 1)
| Attribute | Value |
| :--- | :--- |
| **Status** | Active |
| **Created At** | 2023-11-14 16:13:20 |
| **Last Updated** | 2023-11-14 17:13:20 by `alice` |
| **Git Config** | [`https://gitlab.example/infra/web.git`](https://gitlab.example/infra/web.git) (ref: `refs/heads/main`) |


#### Services Detail:
| Service Name | Image | Replicas | Update State | Status Message |
| :--- | :--- | :---: | :---: | :--- |
| `web_frontend` | `nginx:1.25` | 3 | 🔴 failed | task failed: no suitable node |
| `web_backend` | `myapp:2.0` | 2 | 🟢 healthy | - |

---

## 🟡 Degraded Stacks

### 📦 Stack: `db` (ID: 2)
| Attribute | Value |
| :--- | :--- |
| **Created At** | 2023-11-14 16:13:20 |
| **Last Updated** | 2023-11-14 17:13:20 by `bob` |


#### Services Detail:
| Service Name | Image | Replicas | Update State | Status Message |
| :--- | :--- | :---: | :---: | :--- |
| `db_primary` | `postgres:15` | Global | 🟡 updating | rolling out |

---

## 🌐 Standalone Swarm Services

These are active Swarm services that are not currently associated with a Portainer stack namespace.

| Service Name | Image | Replicas | Status |
| :--- | :--- | :---: | :--- |
| `standalone_worker` | `worker:latest` | 1 | 🟢 operational |

---

## 🟢 Healthy Stacks

These stacks are fully operational with all services running normally.

| Stack Name | ID | Services | Git-Backed | Last Updated |
| :--- | :---: | :---: | :---: | :--- |
| `cache` | 3 | 0 | No | 2023-11-14 17:13:20 |
| `empty-stack` | 4 | 0 | Yes | 2023-11-14 17:13:20 |"""


def test_main_prints_golden_report_to_stdout(mod, tmp_path, monkeypatch, capsys):
    stacks_path = tmp_path / "stacks.json"
    services_path = tmp_path / "services.json"
    stacks_path.write_text(json.dumps(STACKS_FIXTURE))
    services_path.write_text(json.dumps(SERVICES_FIXTURE))

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "analyze_health.py",
            "--stacks-json",
            str(stacks_path),
            "--services-json",
            str(services_path),
        ],
    )
    mod.main()
    out = capsys.readouterr().out
    assert out.rstrip("\n") == GOLDEN_REPORT


def test_main_accepts_data_wrapped_json(mod, tmp_path, monkeypatch, capsys):
    """load_json_file unwraps a top-level {"data": [...]} envelope."""
    stacks_path = tmp_path / "stacks.json"
    services_path = tmp_path / "services.json"
    stacks_path.write_text(json.dumps({"data": STACKS_FIXTURE}))
    services_path.write_text(json.dumps({"data": SERVICES_FIXTURE}))

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "analyze_health.py",
            "--stacks-json",
            str(stacks_path),
            "--services-json",
            str(services_path),
        ],
    )
    mod.main()
    out = capsys.readouterr().out
    assert out.rstrip("\n") == GOLDEN_REPORT


def test_main_writes_report_to_output_file(mod, tmp_path, monkeypatch, capsys):
    stacks_path = tmp_path / "stacks.json"
    services_path = tmp_path / "services.json"
    output_path = tmp_path / "nested" / "report.md"
    stacks_path.write_text(json.dumps(STACKS_FIXTURE))
    services_path.write_text(json.dumps(SERVICES_FIXTURE))

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "analyze_health.py",
            "--stacks-json",
            str(stacks_path),
            "--services-json",
            str(services_path),
            "--output",
            str(output_path),
        ],
    )
    mod.main()
    captured = capsys.readouterr()
    assert "Diagnostics report written successfully" in captured.out
    assert output_path.read_text() == GOLDEN_REPORT


def test_main_exits_1_on_invalid_stacks_json(mod, tmp_path, monkeypatch, capsys):
    stacks_path = tmp_path / "stacks.json"
    services_path = tmp_path / "services.json"
    stacks_path.write_text("{not valid json")
    services_path.write_text(json.dumps(SERVICES_FIXTURE))

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "analyze_health.py",
            "--stacks-json",
            str(stacks_path),
            "--services-json",
            str(services_path),
        ],
    )
    with pytest.raises(SystemExit) as excinfo:
        mod.main()
    assert excinfo.value.code == 1
    assert "Failed to load JSON input" in capsys.readouterr().err


def test_main_exits_1_when_output_write_fails(mod, tmp_path, monkeypatch, capsys):
    stacks_path = tmp_path / "stacks.json"
    services_path = tmp_path / "services.json"
    stacks_path.write_text(json.dumps(STACKS_FIXTURE))
    services_path.write_text(json.dumps(SERVICES_FIXTURE))

    # A regular file where main() will try to os.makedirs() a parent
    # directory forces the write path's except branch.
    blocking_file = tmp_path / "blocking"
    blocking_file.write_text("not a directory")
    bad_output = blocking_file / "sub" / "report.md"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "analyze_health.py",
            "--stacks-json",
            str(stacks_path),
            "--services-json",
            str(services_path),
            "--output",
            str(bad_output),
        ],
    )
    with pytest.raises(SystemExit) as excinfo:
        mod.main()
    assert excinfo.value.code == 1
    assert "Failed to write report" in capsys.readouterr().err


def test_format_timestamp_epoch_and_string_and_missing(mod):
    assert mod.format_timestamp(None) == "N/A"
    assert mod.format_timestamp(0) == "N/A"
    assert mod.format_timestamp(1700000000) == "2023-11-14 16:13:20"
    assert mod.format_timestamp("2023-11-14T16:13:20.123Z") == "2023-11-14 16:13:20"


def test_load_json_file_exits_1_on_missing_file(mod, tmp_path, capsys):
    with pytest.raises(SystemExit) as excinfo:
        mod.load_json_file(str(tmp_path / "does-not-exist.json"))
    assert excinfo.value.code == 1
    assert "Failed to load JSON input" in capsys.readouterr().err
