"""Portainer graph configuration — tag prompts and env var mappings.

This is the only file needed to enable graph mode for this agent.
Provides TAG_PROMPTS and TAG_ENV_VARS for create_graph_agent_server().
"""

# ── Tag → System Prompt Mapping ──────────────────────────────────────
TAG_PROMPTS: dict[str, str] = {
    "Auth": (
        "You are a Portainer Auth specialist. Help users manage and interact with Auth functionality using the available tools."
    ),
    "Docker": (
        "You are a Portainer Docker specialist. Help users manage and interact with Docker functionality using the available tools."
    ),
    "Edge": (
        "You are a Portainer Edge specialist. Help users manage and interact with Edge functionality using the available tools."
    ),
    "Environment": (
        "You are a Portainer Environment specialist. Help users manage and interact with Environment functionality using the available tools."
    ),
    "Kubernetes": (
        "You are a Portainer Kubernetes specialist. Help users manage and interact with Kubernetes functionality using the available tools."
    ),
    "Registry": (
        "You are a Portainer Registry specialist. Help users manage and interact with Registry functionality using the available tools."
    ),
    "Stack": (
        "You are a Portainer Stack specialist. Help users manage and interact with Stack functionality using the available tools."
    ),
    "System": (
        "You are a Portainer System specialist. Help users manage and interact with System functionality using the available tools."
    ),
    "Template": (
        "You are a Portainer Template specialist. Help users manage and interact with Template functionality using the available tools."
    ),
    "User": (
        "You are a Portainer User specialist. Help users manage and interact with User functionality using the available tools."
    ),
}


# ── Tag → Environment Variable Mapping ────────────────────────────────
TAG_ENV_VARS: dict[str, str] = {
    "Auth": "AUTHTOOL",
    "Docker": "DOCKERTOOL",
    "Edge": "EDGETOOL",
    "Environment": "ENVIRONMENTTOOL",
    "Kubernetes": "KUBERNETESTOOL",
    "Registry": "REGISTRYTOOL",
    "Stack": "STACKTOOL",
    "System": "SYSTEMTOOL",
    "Template": "TEMPLATETOOL",
    "User": "USERTOOL",
}
