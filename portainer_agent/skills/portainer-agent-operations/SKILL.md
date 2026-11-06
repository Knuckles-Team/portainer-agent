---
name: portainer-agent-operations
skill_type: skill
description: >-
  Operate Docker, Swarm and Kubernetes environments through the portainer-mcp tools: inspect and operate workloads, manage Helm, edge, templates, registries, users and settings. Use for day-to-day platform operation. For stack deployment use portainer-sync-agent.
license: MIT
tags: [portainer, docker, kubernetes]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Portainer operations

Every Docker call is scoped to an environment (endpoint) id; resolve it with portainer_get_endpoints first.

## Rules

- Resolve the environment id before any call.
- Stop, remove, prune, drain and delete take confirm=true; pass it only after the person agrees.
- Never print tokens, registry passwords or stack secrets.

## Task workflows

### inspect-docker-workloads

Read containers, images, networks, volumes, services and system usage of an environment. Contract steps, in order:

1. `portainer_docker_get_system_df`(endpoint_id)
2. `portainer_get_container_gpus`(environment_id, container_id)
3. `portainer_get_container_logs`(endpoint_id, container_id; optional params_json)
4. `portainer_get_container_stats`(endpoint_id, container_id; optional stream)
5. `portainer_get_docker_dashboard`(environment_id)
6. `portainer_get_docker_df`(endpoint_id)
7. `portainer_get_docker_events`(endpoint_id; optional params_json)
8. `portainer_get_docker_images`(environment_id)
9. `portainer_get_docker_info`(endpoint_id)
10. `portainer_get_docker_version`(endpoint_id)
11. `portainer_get_endpoint_registries`(endpoint_id)
12. `portainer_get_image_history`(endpoint_id, image_name)
13. `portainer_get_service_logs`(endpoint_id, service_id; optional params_json)
14. `portainer_inspect_container`(endpoint_id, container_id)
15. `portainer_inspect_image`(endpoint_id, image_name)
16. `portainer_inspect_network`(endpoint_id, network_id)
17. `portainer_inspect_service`(endpoint_id, service_id)
18. `portainer_inspect_volume`(endpoint_id, volume_name)
19. `portainer_list_containers`(endpoint_id; optional params_json)
20. `portainer_list_images`(endpoint_id; optional params_json)
21. `portainer_list_networks`(endpoint_id; optional params_json)
22. `portainer_list_services`(endpoint_id; optional params_json)
23. `portainer_list_volumes`(endpoint_id; optional params_json)

### operate-containers

Create, start, stop, restart, exec into and remove containers. Contract steps, in order:

1. `portainer_create_container`(endpoint_id, config; optional name)
2. `portainer_create_exec`(endpoint_id, container_id, config)
3. `portainer_inspect_exec`(endpoint_id, exec_id)
4. `portainer_remove_container`(endpoint_id, container_id; optional params_json, confirm) (destructive: pass confirm=true only after the person agrees)
5. `portainer_restart_container`(endpoint_id, container_id; optional timeout)
6. `portainer_start_container`(endpoint_id, container_id)
7. `portainer_start_exec`(endpoint_id, exec_id, config)
8. `portainer_stop_container`(endpoint_id, container_id; optional timeout)

### manage-docker-resources

Create, remove and prune images, networks and volumes. Contract steps, in order:

1. `portainer_create_network`(endpoint_id, config)
2. `portainer_create_volume`(endpoint_id, config)
3. `portainer_prune_containers`(endpoint_id; optional filters)
4. `portainer_prune_images`(endpoint_id; optional filters)
5. `portainer_prune_networks`(endpoint_id; optional filters)
6. `portainer_prune_volumes`(endpoint_id; optional filters)
7. `portainer_remove_image`(endpoint_id, image_name; optional params_json, confirm) (destructive: pass confirm=true only after the person agrees)
8. `portainer_remove_network`(endpoint_id, network_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
9. `portainer_remove_service`(endpoint_id, service_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
10. `portainer_remove_volume`(endpoint_id, volume_name; optional force, confirm) (destructive: pass confirm=true only after the person agrees)

### read-kubernetes-cluster

Read Kubernetes applications, workloads, config, RBAC, metrics and events of an environment. Contract steps, in order:

1. `portainer_describe_kubernetes_resource`(environment_id; optional params_json)
2. `portainer_get_kubernetes_application_count`(environment_id)
3. `portainer_get_kubernetes_applications`(environment_id; optional params_json)
4. `portainer_get_kubernetes_cluster_role_bindings`(environment_id)
5. `portainer_get_kubernetes_cluster_roles`(environment_id)
6. `portainer_get_kubernetes_config`(no arguments)
7. `portainer_get_kubernetes_configmap_count`(environment_id)
8. `portainer_get_kubernetes_configmaps`(environment_id; optional params_json)
9. `portainer_get_kubernetes_cron_jobs`(environment_id)
10. `portainer_get_kubernetes_dashboard`(environment_id)
11. `portainer_get_kubernetes_events`(environment_id)
12. `portainer_get_kubernetes_ingress_controllers`(environment_id)
13. `portainer_get_kubernetes_ingress_count`(environment_id)
14. `portainer_get_kubernetes_ingresses`(environment_id; optional params_json)
15. `portainer_get_kubernetes_jobs`(environment_id)
16. `portainer_get_kubernetes_max_resource_limits`(environment_id)
17. `portainer_get_kubernetes_metrics_applications`(environment_id)
18. `portainer_get_kubernetes_metrics_node`(environment_id, node_name)
19. `portainer_get_kubernetes_metrics_nodes`(environment_id)
20. `portainer_get_kubernetes_namespace`(environment_id, namespace)
21. `portainer_get_kubernetes_namespace_count`(environment_id)
22. `portainer_get_kubernetes_namespace_events`(environment_id, namespace)
23. `portainer_get_kubernetes_namespace_services`(environment_id, namespace)
24. `portainer_get_kubernetes_namespaces`(environment_id)
25. `portainer_get_kubernetes_nodes_limits`(environment_id)
26. `portainer_get_kubernetes_rbac_enabled`(environment_id)
27. `portainer_get_kubernetes_role_bindings`(environment_id)
28. `portainer_get_kubernetes_roles`(environment_id)
29. `portainer_get_kubernetes_secret_count`(environment_id)
30. `portainer_get_kubernetes_secrets`(environment_id; optional params_json)
31. `portainer_get_kubernetes_service_accounts`(environment_id)
32. `portainer_get_kubernetes_service_count`(environment_id)
33. `portainer_get_kubernetes_services`(environment_id; optional params_json)
34. `portainer_get_kubernetes_volume_count`(environment_id)
35. `portainer_get_kubernetes_volumes`(environment_id; optional params_json)

### change-kubernetes-cluster

Create, change and delete namespaces, services, ingresses and volumes and drain nodes. Contract steps, in order:

1. `portainer_create_kubernetes_namespace`(environment_id, namespace; optional params_json)
2. `portainer_delete_kubernetes_ingresses`(environment_id, payload; optional confirm) (destructive: pass confirm=true only after the person agrees)
3. `portainer_delete_kubernetes_namespace`(environment_id, namespace; optional confirm) (destructive: pass confirm=true only after the person agrees)
4. `portainer_delete_kubernetes_services`(environment_id, payload; optional confirm) (destructive: pass confirm=true only after the person agrees)
5. `portainer_delete_kubernetes_volume`(environment_id, namespace, volume; optional confirm) (destructive: pass confirm=true only after the person agrees)
6. `portainer_drain_kubernetes_node`(environment_id, node_name)
7. `portainer_update_kubernetes_namespace`(environment_id, namespace; optional params_json)

### manage-helm

Browse Helm templates and install, inspect, roll back and delete releases. Contract steps, in order:

1. `portainer_create_user_helm_repository`(user_id, url)
2. `portainer_delete_helm_release`(endpoint_id, release_name; optional confirm) (destructive: pass confirm=true only after the person agrees)
3. `portainer_delete_user_helm_repository`(user_id, repository_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
4. `portainer_get_helm_release_history`(endpoint_id, release_name)
5. `portainer_get_helm_releases`(endpoint_id)
6. `portainer_get_helm_templates`(repo)
7. `portainer_get_user_helm_repositories`(user_id)
8. `portainer_install_helm_chart`(endpoint_id, chart_name; optional params_json)
9. `portainer_rollback_helm_release`(endpoint_id, release_name, revision)

### manage-edge-deployments

Manage edge groups, edge stacks and edge jobs. Contract steps, in order:

1. `portainer_create_edge_group`(name; optional params_json)
2. `portainer_create_edge_job_from_string`(name, file_content; optional params_json)
3. `portainer_create_edge_stack_from_repository`(name, repo_url, edge_groups; optional params_json)
4. `portainer_create_edge_stack_from_string`(name, file_content, edge_groups; optional params_json)
5. `portainer_delete_edge_group`(group_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
6. `portainer_delete_edge_job`(job_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
7. `portainer_delete_edge_stack`(stack_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
8. `portainer_get_edge_group`(group_id)
9. `portainer_get_edge_groups`(no arguments)
10. `portainer_get_edge_job`(job_id)
11. `portainer_get_edge_job_file`(job_id)
12. `portainer_get_edge_job_task_logs`(job_id, task_id)
13. `portainer_get_edge_job_tasks`(job_id)
14. `portainer_get_edge_jobs`(no arguments)
15. `portainer_get_edge_stack`(stack_id)
16. `portainer_get_edge_stack_file`(stack_id)
17. `portainer_get_edge_stack_status`(stack_id)
18. `portainer_get_edge_stacks`(no arguments)
19. `portainer_update_edge_group`(group_id; optional params_json)
20. `portainer_update_edge_job`(job_id; optional params_json)
21. `portainer_update_edge_stack`(stack_id; optional params_json)

### manage-templates

Create, read, update and delete custom templates and read app templates. Contract steps, in order:

1. `portainer_create_custom_template_from_repository`(title, description, repo_url; optional template_type, params_json)
2. `portainer_create_custom_template_from_string`(title, description, file_content; optional template_type, params_json)
3. `portainer_delete_custom_template`(template_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
4. `portainer_get_custom_template`(template_id)
5. `portainer_get_custom_template_file`(template_id)
6. `portainer_get_custom_templates`(no arguments)
7. `portainer_get_template_file`(template_id)
8. `portainer_get_templates`(no arguments)
9. `portainer_git_fetch_custom_template`(template_id)
10. `portainer_update_custom_template`(template_id; optional params_json)

### manage-registries

Register, change, test and remove container registries. Contract steps, in order:

1. `portainer_configure_registry`(registry_id; optional params_json)
2. `portainer_create_registry`(name, registry_type, url; optional params_json)
3. `portainer_delete_registry`(registry_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
4. `portainer_get_endpoint_registries`(endpoint_id)
5. `portainer_get_registries`(no arguments)
6. `portainer_get_registry`(registry_id)
7. `portainer_ping_registry`(no arguments)
8. `portainer_update_registry`(registry_id; optional params_json)

### manage-users-and-teams

Create, change and remove users, teams, memberships, tokens and git credentials. Contract steps, in order:

1. `portainer_change_user_password`(user_id, password, new_password)
2. `portainer_create_team`(name)
3. `portainer_create_team_membership`(user_id, team_id; optional role)
4. `portainer_create_user`(username, password; optional role)
5. `portainer_create_user_git_credential`(user_id, name, username, password; optional authorization_type)
6. `portainer_create_user_token`(user_id; optional description, params_json)
7. `portainer_delete_team`(team_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
8. `portainer_delete_team_membership`(membership_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
9. `portainer_delete_user`(user_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
10. `portainer_delete_user_git_credential`(user_id, credential_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
11. `portainer_delete_user_token`(user_id, key_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
12. `portainer_get_current_user`(no arguments)
13. `portainer_get_roles`(no arguments)
14. `portainer_get_team`(team_id)
15. `portainer_get_team_memberships`(no arguments)
16. `portainer_get_team_memberships_by_team`(team_id)
17. `portainer_get_teams`(no arguments)
18. `portainer_get_user`(user_id)
19. `portainer_get_user_git_credential`(user_id, credential_id)
20. `portainer_get_user_git_credentials`(user_id)
21. `portainer_get_user_memberships`(user_id)
22. `portainer_get_user_tokens`(user_id)
23. `portainer_get_users`(no arguments)
24. `portainer_update_team`(team_id, name)
25. `portainer_update_team_membership`(membership_id; optional params_json)
26. `portainer_update_user`(user_id; optional params_json)
27. `portainer_update_user_git_credential`(user_id, credential_id; optional params_json)

### control-resource-access

Set ownership and access control on resources and manage webhooks and tags. Contract steps, in order:

1. `portainer_create_resource_control`(resource_id, resource_type; optional params_json)
2. `portainer_create_tag`(name)
3. `portainer_create_webhook`(resource_id, endpoint_id; optional webhook_type, params_json)
4. `portainer_delete_resource_control`(control_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
5. `portainer_delete_tag`(tag_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
6. `portainer_delete_webhook`(webhook_id; optional confirm) (destructive: pass confirm=true only after the person agrees)
7. `portainer_get_resource_controls`(no arguments)
8. `portainer_get_tags`(no arguments)
9. `portainer_get_webhooks`(no arguments)
10. `portainer_update_resource_control`(control_id; optional params_json)
11. `portainer_update_webhook`(webhook_id; optional params_json)

### administer-portainer

Read status and version, change settings, SSL, LDAP and OAuth, back up, restore and upgrade. Contract steps, in order:

1. `portainer_backup`(; optional password)
2. `portainer_backup_portainer`(; optional params_json)
3. `portainer_check_ldap`(settings)
4. `portainer_get_kubernetes_config`(no arguments)
5. `portainer_get_motd`(no arguments)
6. `portainer_get_public_settings`(no arguments)
7. `portainer_get_settings`(no arguments)
8. `portainer_get_ssl_settings`(no arguments)
9. `portainer_get_status`(no arguments)
10. `portainer_get_system_info`(no arguments)
11. `portainer_get_system_nodes`(no arguments)
12. `portainer_get_system_status`(no arguments)
13. `portainer_get_system_version`(no arguments)
14. `portainer_ping_registry`(no arguments)
15. `portainer_restore`(file_content; optional password)
16. `portainer_system_raw_request`(http_method, api_path; optional query_json, body_json)
17. `portainer_update_settings`(settings)
18. `portainer_update_ssl_settings`(; optional cert, key, http_enabled)
19. `portainer_upgrade_system`(no arguments)
20. `portainer_validate_oauth`(code)

### sign-in-and-bootstrap

Initialize the admin account and authenticate. Contract steps, in order:

1. `portainer_authenticate`(username, password)
2. `portainer_check_admin_init`(no arguments)
3. `portainer_init_admin`(username, password)
4. `portainer_logout`(no arguments)
