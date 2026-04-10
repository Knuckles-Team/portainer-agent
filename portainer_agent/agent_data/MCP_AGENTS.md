# MCP_AGENTS.md - Dynamic Agent Registry

This file tracks the generated agents from MCP servers. You can manually modify the 'Tools' list to customize agent expertise.

## Agent Mapping Table

| Name | Description | System Prompt | Tools | Tag | Source MCP |
|------|-------------|---------------|-------|-----|------------|
| Portainer Auth Specialist | Expert specialist for Auth domain tasks. | You are a Portainer Auth specialist. Help users manage and interact with Auth functionality using the available tools. | portainer-agent_auth_toolset | auth | portainer-agent |
| Portainer User Specialist | Expert specialist for User domain tasks. | You are a Portainer User specialist. Help users manage and interact with User functionality using the available tools. | portainer-agent_user_toolset | user | portainer-agent |
| Portainer Docker Specialist | Expert specialist for docker domain tasks. | You are a Portainer Docker specialist. Help users manage and interact with Docker functionality using the available tools. | portainer-agent_docker_toolset | docker | portainer-agent |
| Portainer System Specialist | Expert specialist for System domain tasks. | You are a Portainer System specialist. Help users manage and interact with System functionality using the available tools. | portainer-agent_system_toolset | system | portainer-agent |
| Portainer Registry Specialist | Expert specialist for Registry domain tasks. | You are a Portainer Registry specialist. Help users manage and interact with Registry functionality using the available tools. | portainer-agent_registry_toolset | registry | portainer-agent |
| Portainer Environment Specialist | Expert specialist for Environment domain tasks. | You are a Portainer Environment specialist. Help users manage and interact with Environment functionality using the available tools. | portainer-agent_environment_toolset | environment | portainer-agent |
| Portainer Kubernetes Specialist | Expert specialist for Kubernetes domain tasks. | You are a Portainer Kubernetes specialist. Help users manage and interact with Kubernetes functionality using the available tools. | portainer-agent_kubernetes_toolset | kubernetes | portainer-agent |
| Portainer Template Specialist | Expert specialist for Template domain tasks. | You are a Portainer Template specialist. Help users manage and interact with Template functionality using the available tools. | portainer-agent_template_toolset | template | portainer-agent |
| Portainer Stack Specialist | Expert specialist for Stack domain tasks. | You are a Portainer Stack specialist. Help users manage and interact with Stack functionality using the available tools. | portainer-agent_stack_toolset | stack | portainer-agent |
| Portainer Edge Specialist | Expert specialist for Edge domain tasks. | You are a Portainer Edge specialist. Help users manage and interact with Edge functionality using the available tools. | portainer-agent_edge_toolset | edge | portainer-agent |

## Tool Inventory Table

| Tool Name | Description | Tag | Source |
|-----------|-------------|-----|--------|
| portainer-agent_auth_toolset | Static hint toolset for auth based on config env. | auth | portainer-agent |
| portainer-agent_user_toolset | Static hint toolset for user based on config env. | user | portainer-agent |
| portainer-agent_docker_toolset | Static hint toolset for docker based on config env. | docker | portainer-agent |
| portainer-agent_system_toolset | Static hint toolset for system based on config env. | system | portainer-agent |
| portainer-agent_registry_toolset | Static hint toolset for registry based on config env. | registry | portainer-agent |
| portainer-agent_environment_toolset | Static hint toolset for environment based on config env. | environment | portainer-agent |
| portainer-agent_kubernetes_toolset | Static hint toolset for kubernetes based on config env. | kubernetes | portainer-agent |
| portainer-agent_template_toolset | Static hint toolset for template based on config env. | template | portainer-agent |
| portainer-agent_stack_toolset | Static hint toolset for stack based on config env. | stack | portainer-agent |
| portainer-agent_edge_toolset | Static hint toolset for edge based on config env. | edge | portainer-agent |
