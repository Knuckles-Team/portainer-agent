"""Tool-use contracts, surface links, data locations and business roles of portainer-mcp.

The SDK serves this declaration as the connector's surface ontology and checks it
against the served tools, prompts and skills (SCION-CONNECTOR-CONTROL-R916).
"""

# ruff: noqa: E501
from __future__ import annotations

from scion_sdk.surface_contracts import (
    BusinessRole,
    DataLocation,
    Refusal,
    SurfaceLink,
    ToolStep,
    ToolUseContract,
)

CONTRACTS: tuple[ToolUseContract, ...] = (
    ToolUseContract(
        "inspect-a-stack",
        description="Find a stack and read its definition, status and logs",
        steps=(
            ToolStep(
                "portainer_export_all_stacks",
                params=("target_dir",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_get_stack",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_stack_by_name",
                params=("name",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_stack_file",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_stack_logs",
                params=("endpoint_id", "stack_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_stacks",
                params=("limit", "offset", "filters"),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "deploy-a-stack",
        description="Create a stack from a compose string or a git repository and update or redeploy it",
        steps=(
            ToolStep(
                "portainer_associate_stack",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_kubernetes_stack_from_repository",
                params=("name", "repo_url", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_kubernetes_stack_from_string",
                params=("name", "file_content", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_standalone_stack_from_repository",
                params=("name", "repo_url", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_standalone_stack_from_string",
                params=("name", "file_content", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_swarm_stack_from_repository",
                params=("name", "repo_url", "swarm_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_swarm_stack_from_string",
                params=("name", "file_content", "swarm_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_migrate_stack",
                params=("stack_id", "endpoint_id", "target_endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_preview_git_file",
                params=("repo_url",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_redeploy_stack_git",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_update_stack",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_stack_git",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "run-and-stop-a-stack",
        description="Start, stop or delete a stack",
        steps=(
            ToolStep(
                "portainer_delete_stack",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_start_stack",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_stop_stack",
                params=("stack_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "inspect-docker-workloads",
        description="Read containers, images, networks, volumes, services and system usage of an environment",
        steps=(
            ToolStep(
                "portainer_docker_get_system_df",
                params=("endpoint_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_get_container_gpus",
                params=("environment_id", "container_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_container_logs",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_container_stats",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_dashboard",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_df",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_events",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_images",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_info",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_docker_version",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_endpoint_registries",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_image_history",
                params=("endpoint_id", "image_name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_service_logs",
                params=("endpoint_id", "service_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_inspect_container",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_inspect_image",
                params=("endpoint_id", "image_name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_inspect_network",
                params=("endpoint_id", "network_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_inspect_service",
                params=("endpoint_id", "service_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_inspect_volume",
                params=("endpoint_id", "volume_name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_list_containers",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_list_images",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_list_networks",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_list_services",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_list_volumes",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "operate-containers",
        description="Create, start, stop, restart, exec into and remove containers",
        steps=(
            ToolStep(
                "portainer_create_container",
                params=("endpoint_id", "config"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_exec",
                params=("endpoint_id", "container_id", "config"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_inspect_exec",
                params=("endpoint_id", "exec_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_remove_container",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_restart_container",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_start_container",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_start_exec",
                params=("endpoint_id", "exec_id", "config"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_stop_container",
                params=("endpoint_id", "container_id"),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "manage-docker-resources",
        description="Create, remove and prune images, networks and volumes",
        steps=(
            ToolStep(
                "portainer_create_network",
                params=("endpoint_id", "config"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_volume",
                params=("endpoint_id", "config"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_prune_containers",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_prune_images",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_prune_networks",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_prune_volumes",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_remove_image",
                params=("endpoint_id", "image_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_remove_network",
                params=("endpoint_id", "network_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_remove_service",
                params=("endpoint_id", "service_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_remove_volume",
                params=("endpoint_id", "volume_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "manage-environments",
        description="List, add, change, snapshot and remove environments and environment groups",
        steps=(
            ToolStep(
                "portainer_add_endpoint_to_group",
                params=("group_id", "endpoint_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_endpoint",
                params=("name", "endpoint_type"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_endpoint_group",
                params=("name",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_endpoint",
                params=("endpoint_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_endpoint_group",
                params=("group_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_endpoints",
                params=("endpoint_ids",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_endpoint",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_endpoint_group",
                params=("group_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_endpoint_groups",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_endpoint_relations",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_endpoint_settings",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_endpoints",
                params=("limit", "offset", "params_json"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_ingest_containers",
                params=("environment_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_ingest_environments",
                params=("include_stacks",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_remove_endpoint_association",
                params=("endpoint_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_remove_endpoint_from_group",
                params=("group_id", "endpoint_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_snapshot_all_endpoints",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_snapshot_endpoint",
                params=("endpoint_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_update_endpoint",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_endpoint_group",
                params=("group_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_endpoint_settings",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "read-kubernetes-cluster",
        description="Read Kubernetes applications, workloads, config, RBAC, metrics and events of an environment",
        steps=(
            ToolStep(
                "portainer_describe_kubernetes_resource",
                params=("environment_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_kubernetes_application_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_applications",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_cluster_role_bindings",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_cluster_roles",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_config",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_kubernetes_configmap_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_configmaps",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_cron_jobs",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_dashboard",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_events",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_ingress_controllers",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_ingress_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_ingresses",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_jobs",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_max_resource_limits",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_metrics_applications",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_metrics_node",
                params=("environment_id", "node_name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_metrics_nodes",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_namespace",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_namespace_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_namespace_events",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_namespace_services",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_namespaces",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_nodes_limits",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_rbac_enabled",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_role_bindings",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_roles",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_secret_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_secrets",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_service_accounts",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_service_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_services",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_volume_count",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_kubernetes_volumes",
                params=("environment_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "change-kubernetes-cluster",
        description="Create, change and delete namespaces, services, ingresses and volumes and drain nodes",
        steps=(
            ToolStep(
                "portainer_create_kubernetes_namespace",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_delete_kubernetes_ingresses",
                params=("environment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_kubernetes_namespace",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_kubernetes_services",
                params=("environment_id", "payload"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_kubernetes_volume",
                params=("environment_id", "namespace", "volume"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_drain_kubernetes_node",
                params=("environment_id", "node_name"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_update_kubernetes_namespace",
                params=("environment_id", "namespace"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "manage-helm",
        description="Browse Helm templates and install, inspect, roll back and delete releases",
        steps=(
            ToolStep(
                "portainer_create_user_helm_repository",
                params=("user_id", "url"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_delete_helm_release",
                params=("endpoint_id", "release_name"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_user_helm_repository",
                params=("user_id", "repository_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_helm_release_history",
                params=("endpoint_id", "release_name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_helm_releases",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_helm_templates",
                params=("repo",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_user_helm_repositories",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_install_helm_chart",
                params=("endpoint_id", "chart_name"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_rollback_helm_release",
                params=("endpoint_id", "release_name", "revision"),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "manage-edge-deployments",
        description="Manage edge groups, edge stacks and edge jobs",
        steps=(
            ToolStep(
                "portainer_create_edge_group",
                params=("name",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_edge_job_from_string",
                params=("name", "file_content"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_edge_stack_from_repository",
                params=("name", "repo_url", "edge_groups"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_edge_stack_from_string",
                params=("name", "file_content", "edge_groups"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_edge_group",
                params=("group_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_edge_job",
                params=("job_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_edge_stack",
                params=("stack_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_edge_group",
                params=("group_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_groups", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_edge_job",
                params=("job_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_job_file",
                params=("job_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_job_task_logs",
                params=("job_id", "task_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_job_tasks",
                params=("job_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_jobs", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_edge_stack",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_stack_file",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_stack_status",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_edge_stacks", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_update_edge_group",
                params=("group_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_edge_job",
                params=("job_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_edge_stack",
                params=("stack_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "manage-templates",
        description="Create, read, update and delete custom templates and read app templates",
        steps=(
            ToolStep(
                "portainer_create_custom_template_from_repository",
                params=("title", "description", "repo_url"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_custom_template_from_string",
                params=("title", "description", "file_content"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_custom_template",
                params=("template_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_custom_template",
                params=("template_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_custom_template_file",
                params=("template_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_custom_templates",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_template_file",
                params=("template_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_templates", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_git_fetch_custom_template",
                params=("template_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_update_custom_template",
                params=("template_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "manage-registries",
        description="Register, change, test and remove container registries",
        steps=(
            ToolStep(
                "portainer_configure_registry",
                params=("registry_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_registry",
                params=("name", "registry_type", "url"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_registry",
                params=("registry_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_endpoint_registries",
                params=("endpoint_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_registries", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_registry",
                params=("registry_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_ping_registry", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_update_registry",
                params=("registry_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "manage-users-and-teams",
        description="Create, change and remove users, teams, memberships, tokens and git credentials",
        steps=(
            ToolStep(
                "portainer_change_user_password",
                params=("user_id", "password", "new_password"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_team",
                params=("name",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_team_membership",
                params=("user_id", "team_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_user",
                params=("username", "password"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_user_git_credential",
                params=("user_id", "name", "username", "password"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_user_token",
                params=("user_id",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_team",
                params=("team_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_team_membership",
                params=("membership_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_user",
                params=("user_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_user_git_credential",
                params=("user_id", "credential_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_user_token",
                params=("user_id", "key_id"),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_current_user", params=(), result=("result",), refusals=()
            ),
            ToolStep("portainer_get_roles", params=(), result=("result",), refusals=()),
            ToolStep(
                "portainer_get_team",
                params=("team_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_team_memberships",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_team_memberships_by_team",
                params=("team_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep("portainer_get_teams", params=(), result=("result",), refusals=()),
            ToolStep(
                "portainer_get_user",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_user_git_credential",
                params=("user_id", "credential_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_user_git_credentials",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_user_memberships",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_get_user_tokens",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep("portainer_get_users", params=(), result=("result",), refusals=()),
            ToolStep(
                "portainer_update_team",
                params=("team_id", "name"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_team_membership",
                params=("membership_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_user",
                params=("user_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_user_git_credential",
                params=("user_id", "credential_id"),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "control-resource-access",
        description="Set ownership and access control on resources and manage webhooks and tags",
        steps=(
            ToolStep(
                "portainer_create_resource_control",
                params=("resource_id", "resource_type"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_create_tag",
                params=("name",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_create_webhook",
                params=("resource_id", "endpoint_id"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_delete_resource_control",
                params=("control_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_tag",
                params=("tag_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_delete_webhook",
                params=("webhook_id",),
                result=("result",),
                refusals=(
                    Refusal(
                        "confirmation_required",
                        "the destructive call omits confirm=true",
                    ),
                    Refusal("not_found", "the named object does not exist"),
                ),
            ),
            ToolStep(
                "portainer_get_resource_controls",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep("portainer_get_tags", params=(), result=("result",), refusals=()),
            ToolStep(
                "portainer_get_webhooks", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_update_resource_control",
                params=("control_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_webhook",
                params=("webhook_id",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
        ),
    ),
    ToolUseContract(
        "administer-portainer",
        description="Read status and version, change settings, SSL, LDAP and OAuth, back up, restore and upgrade",
        steps=(
            ToolStep(
                "portainer_backup",
                params=("password",),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_backup_portainer",
                params=("params_json",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_check_ldap",
                params=("settings",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_kubernetes_config",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep("portainer_get_motd", params=(), result=("result",), refusals=()),
            ToolStep(
                "portainer_get_public_settings",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_settings", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_ssl_settings", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_status", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_system_info", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_system_nodes", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_get_system_status",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_get_system_version",
                params=(),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_ping_registry", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_restore",
                params=("file_content",),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_system_raw_request",
                params=("http_method", "api_path"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_update_settings",
                params=("settings",),
                result=("result",),
                refusals=(Refusal("not_found", "the named object does not exist"),),
            ),
            ToolStep(
                "portainer_update_ssl_settings",
                params=("cert", "key", "http_enabled"),
                result=("result",),
                refusals=(),
            ),
            ToolStep(
                "portainer_upgrade_system", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_validate_oauth",
                params=("code",),
                result=("result",),
                refusals=(),
            ),
        ),
    ),
    ToolUseContract(
        "sign-in-and-bootstrap",
        description="Initialize the admin account and authenticate",
        steps=(
            ToolStep(
                "portainer_authenticate",
                params=("username", "password"),
                result=("result",),
                refusals=(
                    Refusal(
                        "access_denied", "the credential lacks access to the system"
                    ),
                ),
            ),
            ToolStep(
                "portainer_check_admin_init", params=(), result=("result",), refusals=()
            ),
            ToolStep(
                "portainer_init_admin",
                params=("username", "password"),
                result=("result",),
                refusals=(),
            ),
            ToolStep("portainer_logout", params=(), result=("result",), refusals=()),
        ),
    ),
)

LINKS: tuple[SurfaceLink, ...] = (
    SurfaceLink(
        "inspect-a-stack",
        tools=(
            "portainer_export_all_stacks",
            "portainer_get_stack",
            "portainer_get_stack_by_name",
            "portainer_get_stack_file",
            "portainer_get_stack_logs",
            "portainer_get_stacks",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-release-deployer"),
        skills=("analyze-portainer-health", "portainer-sync-agent"),
    ),
    SurfaceLink(
        "deploy-a-stack",
        tools=(
            "portainer_associate_stack",
            "portainer_create_kubernetes_stack_from_repository",
            "portainer_create_kubernetes_stack_from_string",
            "portainer_create_standalone_stack_from_repository",
            "portainer_create_standalone_stack_from_string",
            "portainer_create_swarm_stack_from_repository",
            "portainer_create_swarm_stack_from_string",
            "portainer_migrate_stack",
            "portainer_preview_git_file",
            "portainer_redeploy_stack_git",
            "portainer_update_stack",
            "portainer_update_stack_git",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-release-deployer"),
        skills=("portainer-sync-agent",),
    ),
    SurfaceLink(
        "run-and-stop-a-stack",
        tools=(
            "portainer_delete_stack",
            "portainer_start_stack",
            "portainer_stop_stack",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-release-deployer"),
        skills=("portainer-sync-agent",),
    ),
    SurfaceLink(
        "inspect-docker-workloads",
        tools=(
            "portainer_docker_get_system_df",
            "portainer_get_container_gpus",
            "portainer_get_container_logs",
            "portainer_get_container_stats",
            "portainer_get_docker_dashboard",
            "portainer_get_docker_df",
            "portainer_get_docker_events",
            "portainer_get_docker_images",
            "portainer_get_docker_info",
            "portainer_get_docker_version",
            "portainer_get_endpoint_registries",
            "portainer_get_image_history",
            "portainer_get_service_logs",
            "portainer_inspect_container",
            "portainer_inspect_image",
            "portainer_inspect_network",
            "portainer_inspect_service",
            "portainer_inspect_volume",
            "portainer_list_containers",
            "portainer_list_images",
            "portainer_list_networks",
            "portainer_list_services",
            "portainer_list_volumes",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("analyze-portainer-health", "portainer-agent-operations"),
    ),
    SurfaceLink(
        "operate-containers",
        tools=(
            "portainer_create_container",
            "portainer_create_exec",
            "portainer_inspect_exec",
            "portainer_remove_container",
            "portainer_restart_container",
            "portainer_start_container",
            "portainer_start_exec",
            "portainer_stop_container",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-docker-resources",
        tools=(
            "portainer_create_network",
            "portainer_create_volume",
            "portainer_prune_containers",
            "portainer_prune_images",
            "portainer_prune_networks",
            "portainer_prune_volumes",
            "portainer_remove_image",
            "portainer_remove_network",
            "portainer_remove_service",
            "portainer_remove_volume",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-environments",
        tools=(
            "portainer_add_endpoint_to_group",
            "portainer_create_endpoint",
            "portainer_create_endpoint_group",
            "portainer_delete_endpoint",
            "portainer_delete_endpoint_group",
            "portainer_delete_endpoints",
            "portainer_get_endpoint",
            "portainer_get_endpoint_group",
            "portainer_get_endpoint_groups",
            "portainer_get_endpoint_relations",
            "portainer_get_endpoint_settings",
            "portainer_get_endpoints",
            "portainer_ingest_containers",
            "portainer_ingest_environments",
            "portainer_remove_endpoint_association",
            "portainer_remove_endpoint_from_group",
            "portainer_snapshot_all_endpoints",
            "portainer_snapshot_endpoint",
            "portainer_update_endpoint",
            "portainer_update_endpoint_group",
            "portainer_update_endpoint_settings",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("portainer-sync-agent",),
    ),
    SurfaceLink(
        "read-kubernetes-cluster",
        tools=(
            "portainer_describe_kubernetes_resource",
            "portainer_get_kubernetes_application_count",
            "portainer_get_kubernetes_applications",
            "portainer_get_kubernetes_cluster_role_bindings",
            "portainer_get_kubernetes_cluster_roles",
            "portainer_get_kubernetes_config",
            "portainer_get_kubernetes_configmap_count",
            "portainer_get_kubernetes_configmaps",
            "portainer_get_kubernetes_cron_jobs",
            "portainer_get_kubernetes_dashboard",
            "portainer_get_kubernetes_events",
            "portainer_get_kubernetes_ingress_controllers",
            "portainer_get_kubernetes_ingress_count",
            "portainer_get_kubernetes_ingresses",
            "portainer_get_kubernetes_jobs",
            "portainer_get_kubernetes_max_resource_limits",
            "portainer_get_kubernetes_metrics_applications",
            "portainer_get_kubernetes_metrics_node",
            "portainer_get_kubernetes_metrics_nodes",
            "portainer_get_kubernetes_namespace",
            "portainer_get_kubernetes_namespace_count",
            "portainer_get_kubernetes_namespace_events",
            "portainer_get_kubernetes_namespace_services",
            "portainer_get_kubernetes_namespaces",
            "portainer_get_kubernetes_nodes_limits",
            "portainer_get_kubernetes_rbac_enabled",
            "portainer_get_kubernetes_role_bindings",
            "portainer_get_kubernetes_roles",
            "portainer_get_kubernetes_secret_count",
            "portainer_get_kubernetes_secrets",
            "portainer_get_kubernetes_service_accounts",
            "portainer_get_kubernetes_service_count",
            "portainer_get_kubernetes_services",
            "portainer_get_kubernetes_volume_count",
            "portainer_get_kubernetes_volumes",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("analyze-portainer-health", "portainer-agent-operations"),
    ),
    SurfaceLink(
        "change-kubernetes-cluster",
        tools=(
            "portainer_create_kubernetes_namespace",
            "portainer_delete_kubernetes_ingresses",
            "portainer_delete_kubernetes_namespace",
            "portainer_delete_kubernetes_services",
            "portainer_delete_kubernetes_volume",
            "portainer_drain_kubernetes_node",
            "portainer_update_kubernetes_namespace",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-helm",
        tools=(
            "portainer_create_user_helm_repository",
            "portainer_delete_helm_release",
            "portainer_delete_user_helm_repository",
            "portainer_get_helm_release_history",
            "portainer_get_helm_releases",
            "portainer_get_helm_templates",
            "portainer_get_user_helm_repositories",
            "portainer_install_helm_chart",
            "portainer_rollback_helm_release",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-release-deployer"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-edge-deployments",
        tools=(
            "portainer_create_edge_group",
            "portainer_create_edge_job_from_string",
            "portainer_create_edge_stack_from_repository",
            "portainer_create_edge_stack_from_string",
            "portainer_delete_edge_group",
            "portainer_delete_edge_job",
            "portainer_delete_edge_stack",
            "portainer_get_edge_group",
            "portainer_get_edge_groups",
            "portainer_get_edge_job",
            "portainer_get_edge_job_file",
            "portainer_get_edge_job_task_logs",
            "portainer_get_edge_job_tasks",
            "portainer_get_edge_jobs",
            "portainer_get_edge_stack",
            "portainer_get_edge_stack_file",
            "portainer_get_edge_stack_status",
            "portainer_get_edge_stacks",
            "portainer_update_edge_group",
            "portainer_update_edge_job",
            "portainer_update_edge_stack",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-container-operator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-templates",
        tools=(
            "portainer_create_custom_template_from_repository",
            "portainer_create_custom_template_from_string",
            "portainer_delete_custom_template",
            "portainer_get_custom_template",
            "portainer_get_custom_template_file",
            "portainer_get_custom_templates",
            "portainer_get_template_file",
            "portainer_get_templates",
            "portainer_git_fetch_custom_template",
            "portainer_update_custom_template",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-release-deployer"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-registries",
        tools=(
            "portainer_configure_registry",
            "portainer_create_registry",
            "portainer_delete_registry",
            "portainer_get_endpoint_registries",
            "portainer_get_registries",
            "portainer_get_registry",
            "portainer_ping_registry",
            "portainer_update_registry",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-access-administrator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "manage-users-and-teams",
        tools=(
            "portainer_change_user_password",
            "portainer_create_team",
            "portainer_create_team_membership",
            "portainer_create_user",
            "portainer_create_user_git_credential",
            "portainer_create_user_token",
            "portainer_delete_team",
            "portainer_delete_team_membership",
            "portainer_delete_user",
            "portainer_delete_user_git_credential",
            "portainer_delete_user_token",
            "portainer_get_current_user",
            "portainer_get_roles",
            "portainer_get_team",
            "portainer_get_team_memberships",
            "portainer_get_team_memberships_by_team",
            "portainer_get_teams",
            "portainer_get_user",
            "portainer_get_user_git_credential",
            "portainer_get_user_git_credentials",
            "portainer_get_user_memberships",
            "portainer_get_user_tokens",
            "portainer_get_users",
            "portainer_update_team",
            "portainer_update_team_membership",
            "portainer_update_user",
            "portainer_update_user_git_credential",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-access-administrator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "control-resource-access",
        tools=(
            "portainer_create_resource_control",
            "portainer_create_tag",
            "portainer_create_webhook",
            "portainer_delete_resource_control",
            "portainer_delete_tag",
            "portainer_delete_webhook",
            "portainer_get_resource_controls",
            "portainer_get_tags",
            "portainer_get_webhooks",
            "portainer_update_resource_control",
            "portainer_update_webhook",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-access-administrator"),
        skills=("portainer-agent-operations",),
    ),
    SurfaceLink(
        "administer-portainer",
        tools=(
            "portainer_backup",
            "portainer_backup_portainer",
            "portainer_check_ldap",
            "portainer_get_kubernetes_config",
            "portainer_get_motd",
            "portainer_get_public_settings",
            "portainer_get_settings",
            "portainer_get_ssl_settings",
            "portainer_get_status",
            "portainer_get_system_info",
            "portainer_get_system_nodes",
            "portainer_get_system_status",
            "portainer_get_system_version",
            "portainer_ping_registry",
            "portainer_restore",
            "portainer_system_raw_request",
            "portainer_update_settings",
            "portainer_update_ssl_settings",
            "portainer_upgrade_system",
            "portainer_validate_oauth",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-access-administrator"),
        skills=("portainer-agent-docs", "portainer-agent-operations"),
    ),
    SurfaceLink(
        "sign-in-and-bootstrap",
        tools=(
            "portainer_authenticate",
            "portainer_check_admin_init",
            "portainer_init_admin",
            "portainer_logout",
        ),
        prompts=("portainer-mcp-operator", "portainer-mcp-access-administrator"),
        skills=("portainer-agent-docs", "portainer-agent-operations"),
    ),
)

LOCATIONS: tuple[DataLocation, ...] = (
    DataLocation(
        "portainer-environments",
        ("Host", "Node"),
        "PORTAINER_URL",
        "portainer_get_endpoints",
        federation_key="endpoint_id",
    ),
    DataLocation(
        "portainer-stacks",
        ("Deployment",),
        "PORTAINER_URL",
        "portainer_get_stacks",
        federation_key="stack_id",
    ),
    DataLocation(
        "portainer-containers",
        ("Container",),
        "PORTAINER_URL",
        "portainer_list_containers",
        federation_key="endpoint_id",
    ),
    DataLocation(
        "portainer-kubernetes",
        ("Application",),
        "PORTAINER_URL",
        "portainer_get_kubernetes_applications",
        federation_key="environment_id",
    ),
    DataLocation(
        "portainer-access",
        ("IdentityUser", "IdentityGroup", "Organization"),
        "PORTAINER_URL",
        "portainer_get_users",
        federation_key="user_id",
    ),
)

ROLES: tuple[BusinessRole, ...] = (
    BusinessRole(
        "release-deployer",
        tasks=(
            "inspect-a-stack",
            "deploy-a-stack",
            "run-and-stop-a-stack",
            "manage-templates",
            "manage-helm",
        ),
    ),
    BusinessRole(
        "container-operator",
        tasks=(
            "inspect-docker-workloads",
            "operate-containers",
            "manage-docker-resources",
            "read-kubernetes-cluster",
            "change-kubernetes-cluster",
            "manage-environments",
            "manage-edge-deployments",
        ),
    ),
    BusinessRole(
        "access-administrator",
        tasks=(
            "manage-users-and-teams",
            "manage-registries",
            "control-resource-access",
            "administer-portainer",
            "sign-in-and-bootstrap",
        ),
    ),
)
