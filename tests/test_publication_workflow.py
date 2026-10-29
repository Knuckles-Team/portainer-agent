"""Keep shared publication and Pages contracts explicit in this connector."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _workflow(name: str):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


def _actions_on(workflow: dict):
    # PyYAML's YAML 1.1 reader represents the Actions on key as True.
    return workflow["on"] if "on" in workflow else workflow[True]


def test_pages_publishes_spec_dashboard_and_supports_manual_refresh():


    config = json.loads((ROOT / ".config/spec-dashboard.json").read_text())
    assert config == {
        "version": 1,
        "sources": [{"glob": "specs/*/status.json", "kind": "spec"}],
    }


def test_legacy_docs_publisher_is_removed_and_release_flags_remain_canonical():
    assert not (ROOT / ".github/workflows/docs.yml").exists()


def test_development_skill_has_real_delivery_contract_and_actual_tests():
    skill = ROOT / "portainer_agent/skills/portainer-agent-development/SKILL.md"
    content = skill.read_text()

    assert "name: portainer-agent-development" in content
    assert "## Rapid delivery: the 5-minute contract" in content
    for test_path in (
        "tests/test_publication_workflow.py",
        "tests/test_action_discovery.py",
        "tests/test_init_dynamics.py",
        "tests/test_api_client_base.py",
        "tests/test_stack_git_auth.py",
    ):
        assert test_path in content
        assert (ROOT / test_path).exists()
    for runtime_name in (
        "PORTAINER_URL",
        "PORTAINER_TOKEN",
        "MCP_TOOL_MODE",
        "PortainerApi",
        "portainer_agent/mcp_server.py",
        "agent-connector-sdk",
        "condensed and verbose",
    ):
        assert runtime_name in content


def test_packaged_skill_and_version_lock_are_coherent():
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
    version = project["version"]
    lock = (ROOT / "uv.lock").read_text()
    assert re.search(
        rf'^name = "portainer-agent"\nversion = "{re.escape(version)}"$',
        lock,
        re.MULTILINE,
    )
    package_data = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"][
        "setuptools"
    ]["package-data"]
    assert "skills/**" in package_data["portainer_agent"]
    assert (
        ROOT / "portainer_agent/skills/portainer-agent-development/SKILL.md"
    ).is_file()
