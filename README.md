# Portainer Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/portainer-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/portainer-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/portainer-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/portainer-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/portainer-agent)
![PyPI - License](https://img.shields.io/pypi/l/portainer-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/portainer-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/portainer-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/portainer-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/portainer-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/portainer-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/portainer-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/portainer-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/portainer-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/portainer-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/portainer-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/portainer-agent)

*Version: 1.0.0*

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and guidance for provisioning the Portainer platform are maintained in
> the [official documentation](https://knuckles-team.github.io/portainer-agent/).

---

## Overview

**Portainer Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Portainer container management — Docker environments, stacks, Kubernetes clusters, registries, users, and edge devices. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools

This table is auto-generated from the live server — do not edit by hand.

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `portainer_auth` | `AUTHTOOL` | Manage auth operations. |
| `portainer_docker` | `DOCKERTOOL` | Manage docker operations. |
| `portainer_edge` | `EDGETOOL` | Manage edge operations. |
| `portainer_environment` | `ENVIRONMENTTOOL` | Manage environment operations. |
| `portainer_kubernetes` | `KUBERNETESTOOL` | Manage kubernetes operations. |
| `portainer_registry` | `REGISTRYTOOL` | Manage registry operations. |
| `portainer_stack` | `STACKTOOL` |  |
| `portainer_system` | `SYSTEMTOOL` | Manage system operations. |
| `portainer_template` | `TEMPLATETOOL` | Manage template operations. |
| `portainer_user` | `USERTOOL` | Manage user operations (incl. per-user Git credentials for binding to |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>228 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `portainer_add_endpoint_to_group` | `APITOOL` | Add an environment to a group. |
| `portainer_associate_stack` | `APITOOL` | Associate an orphaned stack. |
| `portainer_authenticate` | `APITOOL` | Authenticate and get a JWT token. |
| `portainer_backup` | `APITOOL` | Create a backup of Portainer data. |
| `portainer_change_user_password` | `APITOOL` | Change a user's password. |
| `portainer_check_admin_init` | `APITOOL` | Check if admin user has been initialized. |
| `portainer_check_ldap` | `APITOOL` | Check LDAP connectivity. |
| `portainer_configure_registry` | `APITOOL` | Configure registry access for an environment. |
| `portainer_create_container` | `APITOOL` | Create a container. |
| `portainer_create_custom_template_from_repository` | `APITOOL` | Create a custom template from a Git repository. |
| `portainer_create_custom_template_from_string` | `APITOOL` | Create a custom template from a string. Types: 1=swarm, 2=compose, 3=kubernetes. |
| `portainer_create_edge_group` | `APITOOL` | Create an edge group. |
| `portainer_create_edge_job_from_string` | `APITOOL` | Create an edge job from a string. |
| `portainer_create_edge_stack_from_repository` | `APITOOL` | Create an edge stack from a Git repository. |
| `portainer_create_edge_stack_from_string` | `APITOOL` | Create an edge stack from a string. |
| `portainer_create_endpoint` | `APITOOL` | Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes. |
| `portainer_create_endpoint_group` | `APITOOL` | Create an endpoint group. |
| `portainer_create_exec` | `APITOOL` | Create an exec instance. |
| `portainer_create_kubernetes_namespace` | `APITOOL` | Create a Kubernetes namespace. |
| `portainer_create_kubernetes_stack_from_repository` | `APITOOL` | Create a Kubernetes stack from a Git repository. |
| `portainer_create_kubernetes_stack_from_string` | `APITOOL` | Create a Kubernetes stack from a string. |
| `portainer_create_network` | `APITOOL` | Create a network. |
| `portainer_create_registry` | `APITOOL` | Create a registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub. |
| `portainer_create_resource_control` | `APITOOL` | Create a resource control. |
| `portainer_create_standalone_stack_from_repository` | `APITOOL` | Create a standalone stack from a Git repository. |
| `portainer_create_standalone_stack_from_string` | `APITOOL` | Create a standalone Docker Compose stack from a string. |
| `portainer_create_swarm_stack_from_repository` | `APITOOL` | Create a Swarm stack from a Git repository. |
| `portainer_create_swarm_stack_from_string` | `APITOOL` | Create a Swarm stack from a string. |
| `portainer_create_tag` | `APITOOL` | Create a tag. |
| `portainer_create_team` | `APITOOL` | Create a team. |
| `portainer_create_team_membership` | `APITOOL` | Create a team membership. Roles: 1=leader, 2=member. |
| `portainer_create_user` | `APITOOL` | Create a user. Roles: 1=admin, 2=standard. |
| `portainer_create_user_git_credential` | `APITOOL` | Store a reusable Git credential for a user. |
| `portainer_create_user_helm_repository` | `APITOOL` | Add a Helm repository for a user. |
| `portainer_create_user_token` | `APITOOL` | Create an API token for a user. |
| `portainer_create_volume` | `APITOOL` | Create a volume. |
| `portainer_create_webhook` | `APITOOL` | Create a webhook. |
| `portainer_delete_custom_template` | `APITOOL` | Delete a custom template. |
| `portainer_delete_edge_group` | `APITOOL` | Delete an edge group. |
| `portainer_delete_edge_job` | `APITOOL` | Delete an edge job. |
| `portainer_delete_edge_stack` | `APITOOL` | Delete an edge stack. |
| `portainer_delete_endpoint` | `APITOOL` | Delete a single environment. |
| `portainer_delete_endpoint_group` | `APITOOL` | Delete an endpoint group. |
| `portainer_delete_endpoints` | `APITOOL` | Delete multiple environments. |
| `portainer_delete_helm_release` | `APITOOL` | Delete a Helm release. |
| `portainer_delete_kubernetes_ingresses` | `APITOOL` | Delete Kubernetes ingresses. |
| `portainer_delete_kubernetes_namespace` | `APITOOL` | Delete a Kubernetes namespace. |
| `portainer_delete_kubernetes_services` | `APITOOL` | Delete Kubernetes services. |
| `portainer_delete_kubernetes_volume` | `APITOOL` | Delete a Kubernetes volume. |
| `portainer_delete_registry` | `APITOOL` | Delete a registry. |
| `portainer_delete_resource_control` | `APITOOL` | Delete a resource control. |
| `portainer_delete_stack` | `APITOOL` | Delete a stack. |
| `portainer_delete_tag` | `APITOOL` | Delete a tag. |
| `portainer_delete_team` | `APITOOL` | Delete a team. |
| `portainer_delete_team_membership` | `APITOOL` | Delete a team membership. |
| `portainer_delete_user` | `APITOOL` | Delete a user. |
| `portainer_delete_user_git_credential` | `APITOOL` | Remove a saved Git credential for a user. |
| `portainer_delete_user_helm_repository` | `APITOOL` | Remove a Helm repository for a user. |
| `portainer_delete_user_token` | `APITOOL` | Delete an API token. |
| `portainer_delete_webhook` | `APITOOL` | Delete a webhook. |
| `portainer_describe_kubernetes_resource` | `APITOOL` | Describe a Kubernetes resource. |
| `portainer_drain_kubernetes_node` | `APITOOL` | Drain a Kubernetes node. |
| `portainer_export_all_stacks` | `APITOOL` | Export all stacks' compose definitions to a target directory. |
| `portainer_get_container_gpus` | `APITOOL` | Get GPU info for a container. |
| `portainer_get_container_logs` | `APITOOL` | Get container logs. |
| `portainer_get_container_stats` | `APITOOL` | Get container stats. |
| `portainer_get_current_user` | `APITOOL` | Get the currently authenticated user. |
| `portainer_get_custom_template` | `APITOOL` | Get a specific custom template. |
| `portainer_get_custom_template_file` | `APITOOL` | Get custom template compose file content. |
| `portainer_get_custom_templates` | `APITOOL` | List custom templates. |
| `portainer_get_docker_dashboard` | `APITOOL` | Get Docker dashboard data for an environment. |
| `portainer_get_docker_df` | `APITOOL` | Get Docker data usage information. |
| `portainer_get_docker_events` | `APITOOL` | Get Docker events. |
| `portainer_get_docker_images` | `APITOOL` | List Docker images in an environment. |
| `portainer_get_docker_info` | `APITOOL` | Get Docker system information. |
| `portainer_get_docker_version` | `APITOOL` | Get Docker version information. |
| `portainer_get_edge_group` | `APITOOL` | Get a specific edge group. |
| `portainer_get_edge_groups` | `APITOOL` | List edge groups. |
| `portainer_get_edge_job` | `APITOOL` | Get a specific edge job. |
| `portainer_get_edge_job_file` | `APITOOL` | Get the script file content for an edge job. |
| `portainer_get_edge_job_task_logs` | `APITOOL` | Get logs for an edge job task. |
| `portainer_get_edge_job_tasks` | `APITOOL` | List tasks for an edge job. |
| `portainer_get_edge_jobs` | `APITOOL` | List edge jobs. |
| `portainer_get_edge_stack` | `APITOOL` | Get a specific edge stack. |
| `portainer_get_edge_stack_file` | `APITOOL` | Get the compose file content for an edge stack. |
| `portainer_get_edge_stack_status` | `APITOOL` | Get edge stack deployment status. |
| `portainer_get_edge_stacks` | `APITOOL` | List edge stacks. |
| `portainer_get_endpoint` | `APITOOL` | Get a specific environment by ID. |
| `portainer_get_endpoint_group` | `APITOOL` | Get a specific endpoint group. |
| `portainer_get_endpoint_groups` | `APITOOL` | List all endpoint groups. |
| `portainer_get_endpoint_registries` | `APITOOL` | List registries for an environment. |
| `portainer_get_endpoint_relations` | `APITOOL` | Get environment relations. |
| `portainer_get_endpoint_settings` | `APITOOL` | Get environment settings. |
| `portainer_get_endpoints` | `APITOOL` | List all environments (endpoints). |
| `portainer_get_helm_release_history` | `APITOOL` | Get Helm release history. |
| `portainer_get_helm_releases` | `APITOOL` | List Helm releases for an environment. |
| `portainer_get_helm_templates` | `APITOOL` | List Helm chart templates. |
| `portainer_get_image_history` | `APITOOL` | Get image history. |
| `portainer_get_kubernetes_application_count` | `APITOOL` | Get application count. |
| `portainer_get_kubernetes_applications` | `APITOOL` | List Kubernetes applications (deployments, statefulsets, daemonsets). |
| `portainer_get_kubernetes_cluster_role_bindings` | `APITOOL` | List Kubernetes cluster role bindings. |
| `portainer_get_kubernetes_cluster_roles` | `APITOOL` | List Kubernetes cluster roles. |
| `portainer_get_kubernetes_config` | `APITOOL` | Get Kubernetes global configuration. |
| `portainer_get_kubernetes_configmap_count` | `APITOOL` | Get configmap count. |
| `portainer_get_kubernetes_configmaps` | `APITOOL` | List Kubernetes configmaps. |
| `portainer_get_kubernetes_cron_jobs` | `APITOOL` | List Kubernetes cron jobs. |
| `portainer_get_kubernetes_dashboard` | `APITOOL` | Get Kubernetes dashboard data. |
| `portainer_get_kubernetes_events` | `APITOOL` | List Kubernetes events. |
| `portainer_get_kubernetes_ingress_controllers` | `APITOOL` | List Kubernetes ingress controllers. |
| `portainer_get_kubernetes_ingress_count` | `APITOOL` | Get ingress count. |
| `portainer_get_kubernetes_ingresses` | `APITOOL` | List Kubernetes ingresses. |
| `portainer_get_kubernetes_jobs` | `APITOOL` | List Kubernetes jobs. |
| `portainer_get_kubernetes_max_resource_limits` | `APITOOL` | Get max resource limits for the cluster. |
| `portainer_get_kubernetes_metrics_applications` | `APITOOL` | Get application resource metrics. |
| `portainer_get_kubernetes_metrics_node` | `APITOOL` | Get metrics for a specific node. |
| `portainer_get_kubernetes_metrics_nodes` | `APITOOL` | Get metrics for Kubernetes nodes. |
| `portainer_get_kubernetes_namespace` | `APITOOL` | Get a specific Kubernetes namespace. |
| `portainer_get_kubernetes_namespace_count` | `APITOOL` | Get namespace count. |
| `portainer_get_kubernetes_namespace_events` | `APITOOL` | List events in a specific namespace. |
| `portainer_get_kubernetes_namespace_services` | `APITOOL` | List services in a specific namespace. |
| `portainer_get_kubernetes_namespaces` | `APITOOL` | List Kubernetes namespaces. |
| `portainer_get_kubernetes_nodes_limits` | `APITOOL` | Get Kubernetes node resource limits. |
| `portainer_get_kubernetes_rbac_enabled` | `APITOOL` | Check if RBAC is enabled on the cluster. |
| `portainer_get_kubernetes_role_bindings` | `APITOOL` | List Kubernetes role bindings. |
| `portainer_get_kubernetes_roles` | `APITOOL` | List Kubernetes roles. |
| `portainer_get_kubernetes_secret_count` | `APITOOL` | Get secret count. |
| `portainer_get_kubernetes_secrets` | `APITOOL` | List Kubernetes secrets. |
| `portainer_get_kubernetes_service_accounts` | `APITOOL` | List Kubernetes service accounts. |
| `portainer_get_kubernetes_service_count` | `APITOOL` | Get service count. |
| `portainer_get_kubernetes_services` | `APITOOL` | List Kubernetes services. |
| `portainer_get_kubernetes_volume_count` | `APITOOL` | Get volume count. |
| `portainer_get_kubernetes_volumes` | `APITOOL` | List Kubernetes persistent volume claims. |
| `portainer_get_motd` | `APITOOL` | Get the message of the day. |
| `portainer_get_public_settings` | `APITOOL` | Get public (unauthenticated) settings. |
| `portainer_get_registries` | `APITOOL` | List all Docker registries. |
| `portainer_get_registry` | `APITOOL` | Get a specific registry. |
| `portainer_get_resource_controls` | `APITOOL` | List all resource controls. |
| `portainer_get_roles` | `APITOOL` | List all roles. |
| `portainer_get_service_logs` | `APITOOL` | Get Swarm service logs. |
| `portainer_get_settings` | `APITOOL` | Get Portainer settings. |
| `portainer_get_ssl_settings` | `APITOOL` | Get SSL settings. |
| `portainer_get_stack` | `APITOOL` | Get a specific stack. |
| `portainer_get_stack_by_name` | `APITOOL` | Get a stack by name. |
| `portainer_get_stack_file` | `APITOOL` | Get the compose file content for a stack. |
| `portainer_get_stack_logs` | `APITOOL` | Get logs for all containers/services in a stack. |
| `portainer_get_stacks` | `APITOOL` | List all stacks. |
| `portainer_get_status` | `APITOOL` | Get Portainer instance status. |
| `portainer_get_system_info` | `APITOOL` | Get system information. |
| `portainer_get_system_nodes` | `APITOOL` | Get system nodes. |
| `portainer_get_system_status` | `APITOOL` | Get detailed system status. |
| `portainer_get_system_version` | `APITOOL` | Get Portainer version information. |
| `portainer_get_tags` | `APITOOL` | List all tags. |
| `portainer_get_team` | `APITOOL` | Get a specific team. |
| `portainer_get_team_memberships` | `APITOOL` | List all team memberships. |
| `portainer_get_team_memberships_by_team` | `APITOOL` | List memberships for a team. |
| `portainer_get_teams` | `APITOOL` | List all teams. |
| `portainer_get_template_file` | `APITOOL` | Get template compose file. |
| `portainer_get_templates` | `APITOOL` | List app templates. |
| `portainer_get_user` | `APITOOL` | Get a specific user. |
| `portainer_get_user_git_credential` | `APITOOL` | Get one saved Git credential for a user. |
| `portainer_get_user_git_credentials` | `APITOOL` | List a user's saved Git credentials (passwords are never returned). |
| `portainer_get_user_helm_repositories` | `APITOOL` | List Helm repositories for a user. |
| `portainer_get_user_memberships` | `APITOOL` | Get team memberships for a user. |
| `portainer_get_user_tokens` | `APITOOL` | List API tokens for a user. |
| `portainer_get_users` | `APITOOL` | List all users. |
| `portainer_get_webhooks` | `APITOOL` | List all webhooks. |
| `portainer_git_fetch_custom_template` | `APITOOL` | Fetch latest version of a custom template from Git. |
| `portainer_init_admin` | `APITOOL` | Initialize the admin user (first-time setup). |
| `portainer_inspect_container` | `APITOOL` | Inspect a container. |
| `portainer_inspect_exec` | `APITOOL` | Inspect an exec instance. |
| `portainer_inspect_image` | `APITOOL` | Inspect an image. |
| `portainer_inspect_network` | `APITOOL` | Inspect a network. |
| `portainer_inspect_service` | `APITOOL` | Inspect a Swarm service. |
| `portainer_inspect_volume` | `APITOOL` | Inspect a volume. |
| `portainer_install_helm_chart` | `APITOOL` | Install a Helm chart. |
| `portainer_list_containers` | `APITOOL` | List containers in an environment. |
| `portainer_list_images` | `APITOOL` | List images in an environment. |
| `portainer_list_networks` | `APITOOL` | List networks. |
| `portainer_list_services` | `APITOOL` | List Swarm services. |
| `portainer_list_volumes` | `APITOOL` | List volumes. |
| `portainer_logout` | `APITOOL` | Logout and invalidate the current token. |
| `portainer_migrate_stack` | `APITOOL` | Migrate a stack to another environment. |
| `portainer_ping_registry` | `APITOOL` | Test registry connectivity. |
| `portainer_preview_git_file` | `APITOOL` | Preview a file from a Git repository. |
| `portainer_prune_containers` | `APITOOL` | Delete unused containers. |
| `portainer_prune_images` | `APITOOL` | Delete unused images. |
| `portainer_prune_networks` | `APITOOL` | Delete unused networks. |
| `portainer_prune_volumes` | `APITOOL` | Delete unused volumes. |
| `portainer_redeploy_stack_git` | `APITOOL` | Redeploy a stack from its Git config. |
| `portainer_remove_container` | `APITOOL` | Remove a container. |
| `portainer_remove_endpoint_association` | `APITOOL` | Remove edge environment association. |
| `portainer_remove_endpoint_from_group` | `APITOOL` | Remove an environment from a group. |
| `portainer_remove_image` | `APITOOL` | Remove an image. |
| `portainer_remove_network` | `APITOOL` | Remove a network. |
| `portainer_remove_service` | `APITOOL` | Remove a Swarm service. |
| `portainer_remove_volume` | `APITOOL` | Remove a volume. |
| `portainer_request` | `BASE_API_CLIENTTOOL` | Generic authenticated passthrough to ANY Portainer API endpoint. |
| `portainer_restart_container` | `APITOOL` | Restart a container. |
| `portainer_restore` | `APITOOL` | Restore Portainer data from a backup. |
| `portainer_rollback_helm_release` | `APITOOL` | Rollback a Helm release to a specific revision. |
| `portainer_snapshot_all_endpoints` | `APITOOL` | Take a snapshot of all environments. |
| `portainer_snapshot_endpoint` | `APITOOL` | Take a snapshot of a specific environment. |
| `portainer_start_container` | `APITOOL` | Start a container. |
| `portainer_start_exec` | `APITOOL` | Start an exec instance. |
| `portainer_start_stack` | `APITOOL` | Start a stopped stack. |
| `portainer_stop_container` | `APITOOL` | Stop a container. |
| `portainer_stop_stack` | `APITOOL` | Stop a running stack. |
| `portainer_update_custom_template` | `APITOOL` | Update a custom template. |
| `portainer_update_edge_group` | `APITOOL` | Update an edge group. |
| `portainer_update_edge_job` | `APITOOL` | Update an edge job. |
| `portainer_update_edge_stack` | `APITOOL` | Update an edge stack. |
| `portainer_update_endpoint` | `APITOOL` | Update an environment. |
| `portainer_update_endpoint_group` | `APITOOL` | Update an endpoint group. |
| `portainer_update_endpoint_settings` | `APITOOL` | Update environment settings. |
| `portainer_update_kubernetes_namespace` | `APITOOL` | Update a Kubernetes namespace. |
| `portainer_update_registry` | `APITOOL` | Update a registry. |
| `portainer_update_resource_control` | `APITOOL` | Update a resource control. |
| `portainer_update_settings` | `APITOOL` | Update Portainer settings. |
| `portainer_update_ssl_settings` | `APITOOL` | Update SSL settings. |
| `portainer_update_stack` | `APITOOL` | Update a stack. |
| `portainer_update_stack_git` | `APITOOL` | Update a stack's Git settings (auto-attaches configured git auth). |
| `portainer_update_team` | `APITOOL` | Update a team. |
| `portainer_update_team_membership` | `APITOOL` | Update a team membership. |
| `portainer_update_user` | `APITOOL` | Update a user. |
| `portainer_update_user_git_credential` | `APITOOL` | Update a saved Git credential (e.g. rotate the password/PAT). |
| `portainer_update_webhook` | `APITOOL` | Update a webhook. |
| `portainer_upgrade_system` | `APITOOL` | Trigger a system upgrade. |
| `portainer_validate_oauth` | `APITOOL` | Validate an OAuth code. |

</details>

_10 action-routed tool(s) (default) · 228 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

> **Install the slim `[mcp]` extra.** All examples below install
> `portainer-agent[mcp]` — the MCP-server extra that pulls only the FastMCP /
> FastAPI tooling (`agent-utilities[mcp]`). It deliberately **excludes** the heavy
> agent runtime (the epistemic-graph engine, `pydantic-ai`, `dspy`, `llama-index`,
> `tree-sitter`), so `uvx`/container installs are dramatically smaller and faster.
> Use the full `[agent]` extra only when you need the integrated Pydantic AI agent
> (see [Installation](#installation)).

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "portainer-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "portainer-agent[mcp]",
        "portainer-mcp"
      ],
      "env": {
        "PORTAINER_ENDPOINT": "your_portainer_endpoint_here",
        "PORTAINER_USERNAME": "your_portainer_username_here",
        "PORTAINER_PASSWORD": "your_portainer_password_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "portainer-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "portainer-agent[mcp]",
        "portainer-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "PORTAINER_ENDPOINT": "your_portainer_endpoint_here",
        "PORTAINER_USERNAME": "your_portainer_username_here",
        "PORTAINER_PASSWORD": "your_portainer_password_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "portainer-agent": {
      "url": "http://localhost:8000/portainer-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name portainer-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e PORTAINER_ENDPOINT="your_value" \
  -e PORTAINER_USERNAME="your_value" \
  -e PORTAINER_PASSWORD="your_value" \
  knucklessg1/portainer-agent:mcp
```

> The `:mcp` tag is the **slim MCP-server image** (built from
> `docker/Dockerfile --target mcp`, installing `portainer-agent[mcp]`). The default
> `:latest` tag is the **full agent image** (`--target agent`, `portainer-agent[agent]`)
> which also bundles the Pydantic AI agent and the epistemic-graph engine — use it
> when you run `portainer-agent` (the agent), not just the MCP server. See
> [Container images](#container-images-mcp-vs-agent).

---

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`portainer-agent` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/portainer-agent/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://portainer-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export PORTAINER_ENDPOINT="your_value"
export PORTAINER_USERNAME="your_value"
export PORTAINER_PASSWORD="your_value"

# Run the agent server
portainer-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  portainer-agent-mcp:
    image: knucklessg1/portainer-agent:mcp
    container_name: portainer-agent-mcp
    hostname: portainer-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  portainer-agent-agent:
    image: knucklessg1/portainer-agent:latest
    container_name: portainer-agent-agent
    hostname: portainer-agent-agent
    restart: always
    depends_on:
      - portainer-agent-mcp
    env_file:
      - ../.env
    command: [ "portainer-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://portainer-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `PORTAINER_URL` | `http://localhost:9000` |  |
| `PORTAINER_PASSWORD` | `your_portainer_password_here` |  |
| `PORTAINER_TOKEN` | `your_portainer_api_token_here` |  |
| `PORTAINER_SSL_VERIFY` | `True` |  |
| `PORTAINER_GIT_USERNAME` | `oauth2` | username for git-backed stack auth (default: oauth2) |
| `PORTAINER_GIT_TOKEN` | — | token for private git repos used by stacks |
| `GITLAB_TOKEN` | — | fallback token when PORTAINER_GIT_TOKEN is unset |
| `PORTAINER_VERIFY` | `True` | TLS verify for the portainer-sync-agent stack helper script |
| `AUTHTOOL` | `True` |  |
| `ENVIRONMENTTOOL` | `True` |  |
| `DOCKERTOOL` | `True` |  |
| `STACKTOOL` | `True` |  |
| `KUBERNETESTOOL` | `True` |  |
| `EDGETOOL` | `True` |  |
| `TEMPLATETOOL` | `True` |  |
| `USERTOOL` | `True` |  |
| `REGISTRYTOOL` | `True` |  |
| `SYSTEMTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_29 package + 14 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads, grouped by purpose.

### Connection & Credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `PORTAINER_URL` | Base HTTP/HTTPS URL of your Portainer instance. | `http://localhost:9000` |
| `PORTAINER_ENDPOINT` | Alternative Portainer socket / connection endpoint path. | `unix:///var/run/portainer/events.sock` |
| `PORTAINER_USERNAME` | Username for basic authentication. | `admin` |
| `PORTAINER_PASSWORD` | Password for basic authentication. | — |
| `PORTAINER_TOKEN` | API token (alternative to username/password). | — |
| `PORTAINER_SSL_VERIFY` | Verify TLS certificates on outbound requests. | `True` |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse`. | `stdio` |
| `HOST` | Bind host (HTTP transports). | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports). | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both`. | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list. | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list. | — |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers). | `1` |

### Tool toggles
Each action-routed tool can be disabled individually by setting its toggle env var to `false`.
The names match the authoritative "Toggle Env Var" column in the
[Available MCP Tools](#available-mcp-tools) table above.

| Variable | Tool | Default |
|----------|------|---------|
| `AUTHTOOL` | `portainer_auth` | `True` |
| `ENVIRONMENTTOOL` | `portainer_environment` | `True` |
| `DOCKERTOOL` | `portainer_docker` | `True` |
| `STACKTOOL` | `portainer_stack` | `True` |
| `KUBERNETESTOOL` | `portainer_kubernetes` | `True` |
| `EDGETOOL` | `portainer_edge` | `True` |
| `TEMPLATETOOL` | `portainer_template` | `True` |
| `USERTOOL` | `portainer_user` | `True` |
| `REGISTRYTOOL` | `portainer_registry` | `True` |
| `SYSTEMTOOL` | `portainer_system` | `True` |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export. | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint. | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys. | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`). | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote`. | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file. | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL. | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to. | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`). | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`). | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface. | `True` |

See [`.env.example`](.env.example) for a copy-paste starting point.

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `portainer-agent[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `portainer-agent[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `portainer-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "portainer-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "portainer-agent[agent]"

# Everything (development)
uv pip install "portainer-agent[all]"      # or: python -m pip install "portainer-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/portainer-agent:mcp` | `--target mcp` | `portainer-agent[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `portainer-mcp` |
| `knucklessg1/portainer-agent:latest` | `--target agent` (default) | `portainer-agent[agent]` — **full** agent runtime + epistemic-graph engine | `portainer-agent` |

```bash
docker build --target mcp   -t knucklessg1/portainer-agent:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/portainer-agent:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/portainer-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/portainer-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/portainer-agent/deployment/) | run the MCP server and A2A agent, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/portainer-agent/usage/) | the MCP tools, the `PortainerApi` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/portainer-agent/platform/) | deploy Portainer with Docker |
| [Overview](https://knuckles-team.github.io/portainer-agent/overview/) | modes, environment variables, graph routing |
| [Concepts](https://knuckles-team.github.io/portainer-agent/concepts/) | concept registry (`CONCEPT:PORT-*`) |

`AGENTS.md` is the canonical contributor/agent guidance.

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `portainer-agent` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx portainer-mcp` · or `uv tool install portainer-agent` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/portainer-agent:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
