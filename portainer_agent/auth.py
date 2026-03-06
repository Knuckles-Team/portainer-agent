#!/usr/bin/python
# coding: utf-8

import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from portainer_agent.portainer_api import PortainerApi

_client = None


def get_client() -> PortainerApi:
    """Get or create a singleton PortainerApi client instance."""
    global _client
    if _client is None:
        base_url = os.getenv("PORTAINER_URL", "http://localhost:9000")
        token = os.getenv("PORTAINER_TOKEN", "")
        verify = os.getenv("PORTAINER_VERIFY", "True").lower() in ("true", "1", "yes")

        _client = PortainerApi(
            base_url=base_url,
            token=token,
            verify=verify,
        )

    return _client
