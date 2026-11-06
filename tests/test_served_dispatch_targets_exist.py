"""Every client method the served action dispatch references must exist.

The dispatch tables are built eagerly, so one missing method made every action
of that tool raise AttributeError.
"""

import re
from pathlib import Path

from portainer_agent.api_client import PortainerApi

SERVER = Path(__file__).parent.parent / "portainer_agent" / "mcp_server.py"


def test_served_dispatch_targets_exist():
    names = set(re.findall(r"\bclient\.([a-z_][a-z0-9_]*)\b", SERVER.read_text()))
    missing = sorted(n for n in names if not hasattr(PortainerApi, n))
    assert not missing, missing
