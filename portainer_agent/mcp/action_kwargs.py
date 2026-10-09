"""Declarative action-kwargs dispatch for the ``portainer_agent.mcp`` tool modules.

Every ``register_*_tools`` module in this package exposes one MCP tool whose
``action`` argument selects among several Portainer API calls. In each of
these tools ``action`` is exactly the client method name (they were
generated from ``PortainerApi``'s own surface), so dispatch reduces to: look
up which of the tool's named parameters that action forwards, drop the ones
left at their default (``None``), and call ``getattr(client, action)`` with
what remains. Expressing that lookup as a table instead of a long if/elif
chain keeps each tool function at a single, low-complexity table lookup.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from agent_connector_sdk.mcp.concurrency import run_blocking

#: One parameter to forward: either a plain name (used as both the target
#: keyword and the lookup key in `values`) or a `(target_keyword, source_key)`
#: pair when the client expects a differently-named/-cased argument.
ActionParam = str | tuple[str, str]


@dataclass(frozen=True)
class ActionCall:
    """One dispatchable action: which of the tool's values to forward, and how."""

    params: tuple[ActionParam, ...] = ()
    #: Wrap a list result as ``{"data": result}`` (list-returning "get all" calls).
    wrap_list_as_data: bool = False


def _action_kwargs(call: ActionCall, values: Mapping[str, Any]) -> dict[str, Any]:
    kwargs: dict[str, Any] = {}
    for param in call.params:
        target, source = param if isinstance(param, tuple) else (param, param)
        value = values.get(source)
        if value is not None:
            kwargs[target] = value
    return kwargs


async def dispatch_client_action(
    *,
    action: str,
    client: Any,
    values: Mapping[str, Any],
    actions: Mapping[str, ActionCall],
) -> Any:
    """Call ``client.<action>`` with the parameters ``actions[action]`` forwards.

    Caller is expected to have already validated ``action in actions`` (and
    raised its own "unknown action" error otherwise), since each tool keeps
    its own historical error text.
    """
    call = actions[action]
    result = await run_blocking(getattr(client, action), **_action_kwargs(call, values))
    if call.wrap_list_as_data and isinstance(result, list):
        return {"data": result}
    return result
