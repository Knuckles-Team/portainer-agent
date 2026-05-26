"""MCP tool registration modules for portainer-agent.

Auto-generated during ecosystem standardization.
Each domain has its own module with a register_*_tools function.
"""

from portainer_agent.mcp.mcp_auth import register_auth_tools
from portainer_agent.mcp.mcp_docker import register_docker_tools
from portainer_agent.mcp.mcp_edge import register_edge_tools
from portainer_agent.mcp.mcp_environment import register_environment_tools
from portainer_agent.mcp.mcp_kubernetes import register_kubernetes_tools
from portainer_agent.mcp.mcp_registry import register_registry_tools
from portainer_agent.mcp.mcp_stack import register_stack_tools
from portainer_agent.mcp.mcp_system import register_system_tools
from portainer_agent.mcp.mcp_template import register_template_tools
from portainer_agent.mcp.mcp_user import register_user_tools

__all__ = [
    "register_auth_tools",
    "register_docker_tools",
    "register_edge_tools",
    "register_environment_tools",
    "register_kubernetes_tools",
    "register_registry_tools",
    "register_stack_tools",
    "register_system_tools",
    "register_template_tools",
    "register_user_tools",
]
