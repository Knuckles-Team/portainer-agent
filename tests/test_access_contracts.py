"""Each competency recording is certified against its access contract."""

import asyncio
import json
from pathlib import Path
from unittest.mock import patch

import pytest
from fastmcp import Client
from scion_sdk.access_contract import parse_access_contracts
from scion_sdk.connector import build_server

from portainer_agent.api.api_client_stacks import Api

ROOT = Path(__file__).resolve().parents[1]


def _field(row, path):
    for part in path.split("."):
        row = row[part]
    return row


@pytest.mark.spec("CONN-PORTAINER-AGENT-CONNECTOR-CONTENT-R002")
def test_competency_contracts_certified():
    contracts = parse_access_contracts(
        (ROOT / "portainer_agent/ontology/access_contracts.ttl").read_text()
    )
    (contract,) = contracts
    assert contract.entity == "stack"
    assert contract.access_kind == "mcp_tool"
    recording = json.loads((ROOT / "tests/recordings/stack.json").read_text())

    async def call():
        mcp = build_server("portainer_agent", command_args=[])[1]
        with patch.object(Api, "get_stacks", return_value=recording):
            async with Client(mcp) as client:
                return await client.call_tool(
                    contract.operation, {}, raise_on_error=False
                )

    result = asyncio.run(call())
    assert not result.is_error
    rows = json.loads(result.content[0].text)
    assert rows == recording
    assert contract.key_field in rows[0]
    for _, field in contract.predicates:
        assert _field(rows[0], field) is not None
    ontology = (ROOT / "portainer_agent/ontology/portainer.ttl").read_text()
    for prop, _ in contract.predicates:
        assert f":{prop.rsplit('#', 1)[-1]} a owl:DatatypeProperty" in ontology
