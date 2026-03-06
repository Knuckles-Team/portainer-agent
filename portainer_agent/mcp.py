#!/usr/bin/python
# coding: utf-8

from dotenv import load_dotenv, find_dotenv
from agent_utilities.base_utilities import to_boolean
import os
import sys
import logging
from typing import Optional, List, Any

from pydantic import Field
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger
from agent_utilities.mcp_utilities import (
    create_mcp_server,
    config,
)
from portainer_agent.auth import get_client

__version__ = "0.1.2"
print(f"Portainer MCP v{__version__}")

logger = get_logger(name="TokenMiddleware")
logger.setLevel(logging.DEBUG)


def register_prompts(mcp: FastMCP):
    @mcp.prompt(
        name="deploy_stack",
        description="Deploy a new Docker Compose stack to a Portainer environment.",
    )
    def deploy_stack_prompt(stack_name: str, environment: str = "local") -> str:
        """Generate a deploy stack prompt."""
        return f"Deploy a new stack named '{stack_name}' to the '{environment}' environment. Use the Portainer tools to list environments, then create the stack."

    @mcp.prompt(
        name="environment_health",
        description="Check the health and status of all Portainer environments.",
    )
    def environment_health_prompt() -> str:
        """Generate an environment health check prompt."""
        return "Check the health of all Portainer environments. List all endpoints, check their status, and report any issues."


# ══════════════════════════════════════════════════════════════════════════
#  AUTH tools
# ══════════════════════════════════════════════════════════════════════════


def register_auth_tools(mcp: FastMCP):
    @mcp.tool(
        name="authenticate",
        description="Authenticate against Portainer with username and password to get a JWT token.",
        tags={"Auth"},
    )
    def authenticate_tool(
        username: str = Field(description="Username."),
        password: str = Field(description="Password."),
    ) -> Any:
        """Authenticate."""
        return get_client().authenticate(username=username, password=password)

    @mcp.tool(
        name="logout",
        description="Logout and invalidate the current authentication token.",
        tags={"Auth"},
    )
    def logout_tool() -> Any:
        """Logout."""
        return get_client().logout()

    @mcp.tool(
        name="validate_oauth",
        description="Validate an OAuth authorization code.",
        tags={"Auth"},
    )
    def validate_oauth_tool(
        code: str = Field(description="OAuth code."),
    ) -> Any:
        """Validate OAuth."""
        return get_client().validate_oauth(code=code)


# ══════════════════════════════════════════════════════════════════════════
#  ENVIRONMENT tools
# ══════════════════════════════════════════════════════════════════════════


def register_environment_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_endpoints",
        description="List all Portainer environments (endpoints). Each environment represents a Docker host, Swarm cluster, or Kubernetes cluster.",
        tags={"Environment"},
    )
    def get_endpoints_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        offset: Optional[int] = Field(
            default=None, description="Offset for pagination."
        ),
    ) -> Any:
        """List environments."""
        return get_client().get_endpoints(limit=limit, offset=offset)

    @mcp.tool(
        name="get_endpoint",
        description="Get details of a specific environment (endpoint) by ID.",
        tags={"Environment"},
    )
    def get_endpoint_tool(
        endpoint_id: int = Field(description="Environment/endpoint ID."),
    ) -> Any:
        """Get environment."""
        return get_client().get_endpoint(endpoint_id)

    @mcp.tool(
        name="create_endpoint",
        description="Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes.",
        tags={"Environment"},
    )
    def create_endpoint_tool(
        name: str = Field(description="Environment name."),
        endpoint_type: int = Field(description="Environment type (1-7)."),
        url: str = Field(default="", description="URL of the Docker/Kubernetes host."),
    ) -> Any:
        """Create environment."""
        return get_client().create_endpoint(
            name=name, endpoint_type=endpoint_type, url=url
        )

    @mcp.tool(
        name="update_endpoint",
        description="Update an existing environment's configuration.",
        tags={"Environment"},
    )
    def update_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID."),
        name: Optional[str] = Field(default=None, description="New name."),
        url: Optional[str] = Field(default=None, description="New URL."),
        public_url: Optional[str] = Field(default=None, description="Public URL."),
        group_id: Optional[int] = Field(default=None, description="Group ID."),
    ) -> Any:
        """Update environment."""
        kwargs = {}
        if name:
            kwargs["Name"] = name
        if url:
            kwargs["URL"] = url
        if public_url:
            kwargs["PublicURL"] = public_url
        if group_id is not None:
            kwargs["GroupID"] = group_id
        return get_client().update_endpoint(endpoint_id, **kwargs)

    @mcp.tool(
        name="delete_endpoint",
        description="Delete an environment (endpoint).",
        tags={"Environment"},
    )
    def delete_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID to delete."),
    ) -> Any:
        """Delete environment."""
        return get_client().delete_endpoint(endpoint_id)

    @mcp.tool(
        name="snapshot_endpoint",
        description="Take a snapshot of an environment to refresh its state.",
        tags={"Environment"},
    )
    def snapshot_endpoint_tool(
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Snapshot environment."""
        return get_client().snapshot_endpoint(endpoint_id)

    @mcp.tool(
        name="snapshot_all_endpoints",
        description="Take a snapshot of all environments.",
        tags={"Environment"},
    )
    def snapshot_all_endpoints_tool() -> Any:
        """Snapshot all environments."""
        return get_client().snapshot_all_endpoints()

    @mcp.tool(
        name="get_endpoint_groups",
        description="List all environment groups.",
        tags={"Environment"},
    )
    def get_endpoint_groups_tool() -> Any:
        """List groups."""
        return get_client().get_endpoint_groups()

    @mcp.tool(
        name="create_endpoint_group",
        description="Create a new environment group.",
        tags={"Environment"},
    )
    def create_endpoint_group_tool(
        name: str = Field(description="Group name."),
        description: str = Field(default="", description="Group description."),
    ) -> Any:
        """Create group."""
        return get_client().create_endpoint_group(name=name, description=description)

    @mcp.tool(
        name="delete_endpoint_group",
        description="Delete an environment group.",
        tags={"Environment"},
    )
    def delete_endpoint_group_tool(
        group_id: int = Field(description="Group ID."),
    ) -> Any:
        """Delete group."""
        return get_client().delete_endpoint_group(group_id)


# ══════════════════════════════════════════════════════════════════════════
#  DOCKER tools
# ══════════════════════════════════════════════════════════════════════════


def register_docker_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_docker_dashboard",
        description="Get Docker dashboard data (containers, images, volumes, networks summary) for an environment.",
        tags={"Docker"},
    )
    def get_docker_dashboard_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Get Docker dashboard."""
        return get_client().get_docker_dashboard(environment_id)

    @mcp.tool(
        name="get_docker_images",
        description="List Docker images in an environment.",
        tags={"Docker"},
    )
    def get_docker_images_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List Docker images."""
        return get_client().get_docker_images(environment_id)

    @mcp.tool(
        name="get_container_gpus",
        description="Get GPU information for a Docker container.",
        tags={"Docker"},
    )
    def get_container_gpus_tool(
        environment_id: int = Field(description="Environment ID."),
        container_id: str = Field(description="Container ID."),
    ) -> Any:
        """Get container GPUs."""
        return get_client().get_container_gpus(environment_id, container_id)


# ══════════════════════════════════════════════════════════════════════════
#  STACK tools
# ══════════════════════════════════════════════════════════════════════════


def register_stack_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_stacks",
        description="List all stacks across all environments.",
        tags={"Stack"},
    )
    def get_stacks_tool() -> Any:
        """List stacks."""
        return get_client().get_stacks()

    @mcp.tool(
        name="get_stack",
        description="Get details of a specific stack by ID.",
        tags={"Stack"},
    )
    def get_stack_tool(
        stack_id: int = Field(description="Stack ID."),
    ) -> Any:
        """Get stack."""
        return get_client().get_stack(stack_id)

    @mcp.tool(
        name="get_stack_file",
        description="Get the Docker Compose/manifest file content for a stack.",
        tags={"Stack"},
    )
    def get_stack_file_tool(
        stack_id: int = Field(description="Stack ID."),
    ) -> Any:
        """Get stack file."""
        return get_client().get_stack_file(stack_id)

    @mcp.tool(
        name="create_standalone_stack",
        description="Create a standalone Docker Compose stack from compose file content.",
        tags={"Stack"},
    )
    def create_standalone_stack_tool(
        name: str = Field(description="Stack name."),
        file_content: str = Field(description="Docker Compose YAML content."),
        endpoint_id: int = Field(description="Target environment ID."),
    ) -> Any:
        """Create standalone stack."""
        return get_client().create_standalone_stack_from_string(
            name=name, file_content=file_content, endpoint_id=endpoint_id
        )

    @mcp.tool(
        name="create_standalone_stack_from_repo",
        description="Create a standalone Docker Compose stack from a Git repository.",
        tags={"Stack"},
    )
    def create_standalone_stack_from_repo_tool(
        name: str = Field(description="Stack name."),
        repo_url: str = Field(description="Git repository URL."),
        endpoint_id: int = Field(description="Target environment ID."),
        compose_file: str = Field(
            default="docker-compose.yml", description="Path to compose file in repo."
        ),
    ) -> Any:
        """Create stack from repo."""
        return get_client().create_standalone_stack_from_repository(
            name=name,
            repo_url=repo_url,
            endpoint_id=endpoint_id,
            ComposeFilePathInRepository=compose_file,
        )

    @mcp.tool(
        name="update_stack",
        description="Update a stack's configuration.",
        tags={"Stack"},
    )
    def update_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
        file_content: Optional[str] = Field(
            default=None, description="Updated compose file content."
        ),
    ) -> Any:
        """Update stack."""
        kwargs = {}
        if file_content:
            kwargs["StackFileContent"] = file_content
        return get_client().update_stack(stack_id, endpoint_id, **kwargs)

    @mcp.tool(
        name="delete_stack",
        description="Delete a stack.",
        tags={"Stack"},
    )
    def delete_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Delete stack."""
        return get_client().delete_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="start_stack",
        description="Start a stopped stack.",
        tags={"Stack"},
    )
    def start_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Start stack."""
        return get_client().start_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="stop_stack",
        description="Stop a running stack.",
        tags={"Stack"},
    )
    def stop_stack_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Stop stack."""
        return get_client().stop_stack(stack_id, endpoint_id)

    @mcp.tool(
        name="redeploy_stack_git",
        description="Redeploy a stack from its Git repository (pull latest and redeploy).",
        tags={"Stack"},
    )
    def redeploy_stack_git_tool(
        stack_id: int = Field(description="Stack ID."),
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Redeploy from Git."""
        return get_client().redeploy_stack_git(stack_id, endpoint_id)


# ══════════════════════════════════════════════════════════════════════════
#  KUBERNETES tools
# ══════════════════════════════════════════════════════════════════════════


def register_kubernetes_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_kubernetes_dashboard",
        description="Get Kubernetes dashboard data for an environment (pods, services, deployments summary).",
        tags={"Kubernetes"},
    )
    def get_k8s_dashboard_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Get K8s dashboard."""
        return get_client().get_kubernetes_dashboard(environment_id)

    @mcp.tool(
        name="get_kubernetes_namespaces",
        description="List Kubernetes namespaces in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_namespaces_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List namespaces."""
        return get_client().get_kubernetes_namespaces(environment_id)

    @mcp.tool(
        name="get_kubernetes_applications",
        description="List Kubernetes applications (deployments, statefulsets, daemonsets) in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_applications_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List applications."""
        return get_client().get_kubernetes_applications(environment_id)

    @mcp.tool(
        name="get_kubernetes_services",
        description="List Kubernetes services in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_services_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List services."""
        return get_client().get_kubernetes_services(environment_id)

    @mcp.tool(
        name="get_kubernetes_ingresses",
        description="List Kubernetes ingresses in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_ingresses_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List ingresses."""
        return get_client().get_kubernetes_ingresses(environment_id)

    @mcp.tool(
        name="get_kubernetes_configmaps",
        description="List Kubernetes configmaps in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_configmaps_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List configmaps."""
        return get_client().get_kubernetes_configmaps(environment_id)

    @mcp.tool(
        name="get_kubernetes_secrets",
        description="List Kubernetes secrets in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_secrets_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List secrets."""
        return get_client().get_kubernetes_secrets(environment_id)

    @mcp.tool(
        name="get_kubernetes_volumes",
        description="List Kubernetes persistent volume claims in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_volumes_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List volumes."""
        return get_client().get_kubernetes_volumes(environment_id)

    @mcp.tool(
        name="get_kubernetes_events",
        description="List Kubernetes events in an environment.",
        tags={"Kubernetes"},
    )
    def get_k8s_events_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List events."""
        return get_client().get_kubernetes_events(environment_id)

    @mcp.tool(
        name="get_kubernetes_nodes_limits",
        description="Get Kubernetes node resource limits for capacity planning.",
        tags={"Kubernetes"},
    )
    def get_k8s_nodes_limits_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Get node limits."""
        return get_client().get_kubernetes_nodes_limits(environment_id)

    @mcp.tool(
        name="get_kubernetes_metrics_nodes",
        description="Get resource metrics for Kubernetes nodes.",
        tags={"Kubernetes"},
    )
    def get_k8s_metrics_nodes_tool(
        environment_id: int = Field(description="Environment ID."),
    ) -> Any:
        """Get node metrics."""
        return get_client().get_kubernetes_metrics_nodes(environment_id)

    @mcp.tool(
        name="get_helm_releases",
        description="List Helm releases installed in an environment.",
        tags={"Kubernetes"},
    )
    def get_helm_releases_tool(
        endpoint_id: int = Field(description="Environment ID."),
    ) -> Any:
        """List Helm releases."""
        return get_client().get_helm_releases(endpoint_id)

    @mcp.tool(
        name="install_helm_chart",
        description="Install a Helm chart in an environment.",
        tags={"Kubernetes"},
    )
    def install_helm_chart_tool(
        endpoint_id: int = Field(description="Environment ID."),
        chart_name: str = Field(description="Helm chart name."),
        release_name: str = Field(default="", description="Name for the Helm release."),
        namespace: str = Field(default="default", description="Target namespace."),
    ) -> Any:
        """Install Helm chart."""
        return get_client().install_helm_chart(
            endpoint_id, chart_name, ReleaseName=release_name, Namespace=namespace
        )

    @mcp.tool(
        name="delete_helm_release",
        description="Delete (uninstall) a Helm release.",
        tags={"Kubernetes"},
    )
    def delete_helm_release_tool(
        endpoint_id: int = Field(description="Environment ID."),
        release_name: str = Field(description="Helm release name."),
    ) -> Any:
        """Delete Helm release."""
        return get_client().delete_helm_release(endpoint_id, release_name)


# ══════════════════════════════════════════════════════════════════════════
#  EDGE tools
# ══════════════════════════════════════════════════════════════════════════


def register_edge_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_edge_groups",
        description="List all edge groups.",
        tags={"Edge"},
    )
    def get_edge_groups_tool() -> Any:
        """List edge groups."""
        return get_client().get_edge_groups()

    @mcp.tool(
        name="create_edge_group",
        description="Create an edge group for organizing edge devices.",
        tags={"Edge"},
    )
    def create_edge_group_tool(
        name: str = Field(description="Edge group name."),
    ) -> Any:
        """Create edge group."""
        return get_client().create_edge_group(name=name)

    @mcp.tool(
        name="delete_edge_group",
        description="Delete an edge group.",
        tags={"Edge"},
    )
    def delete_edge_group_tool(
        group_id: int = Field(description="Edge group ID."),
    ) -> Any:
        """Delete edge group."""
        return get_client().delete_edge_group(group_id)

    @mcp.tool(
        name="get_edge_stacks",
        description="List all edge stacks deployed to edge groups.",
        tags={"Edge"},
    )
    def get_edge_stacks_tool() -> Any:
        """List edge stacks."""
        return get_client().get_edge_stacks()

    @mcp.tool(
        name="get_edge_stack",
        description="Get details of a specific edge stack.",
        tags={"Edge"},
    )
    def get_edge_stack_tool(
        stack_id: int = Field(description="Edge stack ID."),
    ) -> Any:
        """Get edge stack."""
        return get_client().get_edge_stack(stack_id)

    @mcp.tool(
        name="create_edge_stack",
        description="Create an edge stack from compose file content.",
        tags={"Edge"},
    )
    def create_edge_stack_tool(
        name: str = Field(description="Stack name."),
        file_content: str = Field(description="Docker Compose YAML content."),
        edge_groups: List[int] = Field(
            description="List of edge group IDs to deploy to."
        ),
    ) -> Any:
        """Create edge stack."""
        return get_client().create_edge_stack_from_string(
            name=name, file_content=file_content, edge_groups=edge_groups
        )

    @mcp.tool(
        name="delete_edge_stack",
        description="Delete an edge stack.",
        tags={"Edge"},
    )
    def delete_edge_stack_tool(
        stack_id: int = Field(description="Edge stack ID."),
    ) -> Any:
        """Delete edge stack."""
        return get_client().delete_edge_stack(stack_id)

    @mcp.tool(
        name="get_edge_jobs",
        description="List all edge jobs.",
        tags={"Edge"},
    )
    def get_edge_jobs_tool() -> Any:
        """List edge jobs."""
        return get_client().get_edge_jobs()

    @mcp.tool(
        name="get_edge_job",
        description="Get details of a specific edge job.",
        tags={"Edge"},
    )
    def get_edge_job_tool(
        job_id: int = Field(description="Edge job ID."),
    ) -> Any:
        """Get edge job."""
        return get_client().get_edge_job(job_id)

    @mcp.tool(
        name="create_edge_job",
        description="Create an edge job to execute scripts on edge devices.",
        tags={"Edge"},
    )
    def create_edge_job_tool(
        name: str = Field(description="Job name."),
        file_content: str = Field(description="Script content."),
    ) -> Any:
        """Create edge job."""
        return get_client().create_edge_job_from_string(
            name=name, file_content=file_content
        )

    @mcp.tool(
        name="delete_edge_job",
        description="Delete an edge job.",
        tags={"Edge"},
    )
    def delete_edge_job_tool(
        job_id: int = Field(description="Edge job ID."),
    ) -> Any:
        """Delete edge job."""
        return get_client().delete_edge_job(job_id)


# ══════════════════════════════════════════════════════════════════════════
#  TEMPLATE tools
# ══════════════════════════════════════════════════════════════════════════


def register_template_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_templates",
        description="List available app templates.",
        tags={"Template"},
    )
    def get_templates_tool() -> Any:
        """List templates."""
        return get_client().get_templates()

    @mcp.tool(
        name="get_custom_templates",
        description="List custom templates created by users.",
        tags={"Template"},
    )
    def get_custom_templates_tool() -> Any:
        """List custom templates."""
        return get_client().get_custom_templates()

    @mcp.tool(
        name="get_custom_template",
        description="Get details of a specific custom template.",
        tags={"Template"},
    )
    def get_custom_template_tool(
        template_id: int = Field(description="Template ID."),
    ) -> Any:
        """Get custom template."""
        return get_client().get_custom_template(template_id)

    @mcp.tool(
        name="create_custom_template",
        description="Create a custom template from compose file content. Types: 1=swarm, 2=compose, 3=kubernetes.",
        tags={"Template"},
    )
    def create_custom_template_tool(
        title: str = Field(description="Template title."),
        description: str = Field(description="Template description."),
        file_content: str = Field(description="Compose/manifest file content."),
        template_type: int = Field(
            default=2, description="Type: 1=swarm, 2=compose, 3=kubernetes."
        ),
    ) -> Any:
        """Create custom template."""
        return get_client().create_custom_template_from_string(
            title=title,
            description=description,
            file_content=file_content,
            template_type=template_type,
        )

    @mcp.tool(
        name="delete_custom_template",
        description="Delete a custom template.",
        tags={"Template"},
    )
    def delete_custom_template_tool(
        template_id: int = Field(description="Template ID."),
    ) -> Any:
        """Delete custom template."""
        return get_client().delete_custom_template(template_id)

    @mcp.tool(
        name="get_custom_template_file",
        description="Get the compose file content of a custom template.",
        tags={"Template"},
    )
    def get_custom_template_file_tool(
        template_id: int = Field(description="Template ID."),
    ) -> Any:
        """Get template file."""
        return get_client().get_custom_template_file(template_id)

    @mcp.tool(
        name="get_helm_templates",
        description="List available Helm chart templates.",
        tags={"Template"},
    )
    def get_helm_templates_tool() -> Any:
        """List Helm templates."""
        return get_client().get_helm_templates()


# ══════════════════════════════════════════════════════════════════════════
#  USER tools
# ══════════════════════════════════════════════════════════════════════════


def register_user_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_users",
        description="List all Portainer users.",
        tags={"User"},
    )
    def get_users_tool() -> Any:
        """List users."""
        return get_client().get_users()

    @mcp.tool(
        name="get_user",
        description="Get details of a specific user.",
        tags={"User"},
    )
    def get_user_tool(
        user_id: int = Field(description="User ID."),
    ) -> Any:
        """Get user."""
        return get_client().get_user(user_id)

    @mcp.tool(
        name="get_current_user",
        description="Get the currently authenticated user's profile.",
        tags={"User"},
    )
    def get_current_user_tool() -> Any:
        """Get current user."""
        return get_client().get_current_user()

    @mcp.tool(
        name="create_user",
        description="Create a new Portainer user. Roles: 1=admin, 2=standard.",
        tags={"User"},
    )
    def create_user_tool(
        username: str = Field(description="Username."),
        password: str = Field(description="Password."),
        role: int = Field(default=2, description="Role: 1=admin, 2=standard."),
    ) -> Any:
        """Create user."""
        return get_client().create_user(username=username, password=password, role=role)

    @mcp.tool(
        name="delete_user",
        description="Delete a Portainer user.",
        tags={"User"},
    )
    def delete_user_tool(
        user_id: int = Field(description="User ID."),
    ) -> Any:
        """Delete user."""
        return get_client().delete_user(user_id)

    @mcp.tool(
        name="get_teams",
        description="List all teams.",
        tags={"User"},
    )
    def get_teams_tool() -> Any:
        """List teams."""
        return get_client().get_teams()

    @mcp.tool(
        name="create_team",
        description="Create a new team.",
        tags={"User"},
    )
    def create_team_tool(
        name: str = Field(description="Team name."),
    ) -> Any:
        """Create team."""
        return get_client().create_team(name=name)

    @mcp.tool(
        name="delete_team",
        description="Delete a team.",
        tags={"User"},
    )
    def delete_team_tool(
        team_id: int = Field(description="Team ID."),
    ) -> Any:
        """Delete team."""
        return get_client().delete_team(team_id)

    @mcp.tool(
        name="get_roles",
        description="List all available roles.",
        tags={"User"},
    )
    def get_roles_tool() -> Any:
        """List roles."""
        return get_client().get_roles()

    @mcp.tool(
        name="get_user_tokens",
        description="List API tokens for a user.",
        tags={"User"},
    )
    def get_user_tokens_tool(
        user_id: int = Field(description="User ID."),
    ) -> Any:
        """List user tokens."""
        return get_client().get_user_tokens(user_id)


# ══════════════════════════════════════════════════════════════════════════
#  REGISTRY tools
# ══════════════════════════════════════════════════════════════════════════


def register_registry_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_registries",
        description="List all configured Docker registries.",
        tags={"Registry"},
    )
    def get_registries_tool() -> Any:
        """List registries."""
        return get_client().get_registries()

    @mcp.tool(
        name="get_registry",
        description="Get details of a specific registry.",
        tags={"Registry"},
    )
    def get_registry_tool(
        registry_id: int = Field(description="Registry ID."),
    ) -> Any:
        """Get registry."""
        return get_client().get_registry(registry_id)

    @mcp.tool(
        name="create_registry",
        description="Add a Docker registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub.",
        tags={"Registry"},
    )
    def create_registry_tool(
        name: str = Field(description="Registry name."),
        registry_type: int = Field(description="Registry type (1-8)."),
        url: str = Field(description="Registry URL."),
        username: str = Field(default="", description="Username for authentication."),
        password: str = Field(default="", description="Password for authentication."),
    ) -> Any:
        """Create registry."""
        kwargs = {}
        if username:
            kwargs["Username"] = username
        if password:
            kwargs["Password"] = password
        return get_client().create_registry(
            name=name, registry_type=registry_type, url=url, **kwargs
        )

    @mcp.tool(
        name="delete_registry",
        description="Delete a Docker registry.",
        tags={"Registry"},
    )
    def delete_registry_tool(
        registry_id: int = Field(description="Registry ID."),
    ) -> Any:
        """Delete registry."""
        return get_client().delete_registry(registry_id)


# ══════════════════════════════════════════════════════════════════════════
#  SYSTEM tools
# ══════════════════════════════════════════════════════════════════════════


def register_system_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_status",
        description="Get Portainer instance status (version, uptime, etc.).",
        tags={"System"},
    )
    def get_status_tool() -> Any:
        """Get status."""
        return get_client().get_status()

    @mcp.tool(
        name="get_system_info",
        description="Get detailed system information (build info, dependencies, runtime).",
        tags={"System"},
    )
    def get_system_info_tool() -> Any:
        """Get system info."""
        return get_client().get_system_info()

    @mcp.tool(
        name="get_system_version",
        description="Get Portainer version information.",
        tags={"System"},
    )
    def get_system_version_tool() -> Any:
        """Get version."""
        return get_client().get_system_version()

    @mcp.tool(
        name="get_settings",
        description="Get Portainer settings (authentication, templates URL, edge agent, etc.).",
        tags={"System"},
    )
    def get_settings_tool() -> Any:
        """Get settings."""
        return get_client().get_settings()

    @mcp.tool(
        name="update_settings",
        description="Update Portainer settings.",
        tags={"System"},
    )
    def update_settings_tool(
        authentication_method: Optional[int] = Field(
            default=None, description="Auth method: 1=internal, 2=LDAP, 3=OAuth."
        ),
        enable_telemetry: Optional[bool] = Field(
            default=None, description="Enable telemetry."
        ),
    ) -> Any:
        """Update settings."""
        kwargs = {}
        if authentication_method is not None:
            kwargs["AuthenticationMethod"] = authentication_method
        if enable_telemetry is not None:
            kwargs["EnableTelemetry"] = enable_telemetry
        return get_client().update_settings(**kwargs)

    @mcp.tool(
        name="get_tags",
        description="List all tags used for organizing environments.",
        tags={"System"},
    )
    def get_tags_tool() -> Any:
        """List tags."""
        return get_client().get_tags()

    @mcp.tool(
        name="create_tag",
        description="Create a tag for organizing environments.",
        tags={"System"},
    )
    def create_tag_tool(
        name: str = Field(description="Tag name."),
    ) -> Any:
        """Create tag."""
        return get_client().create_tag(name=name)

    @mcp.tool(
        name="delete_tag",
        description="Delete a tag.",
        tags={"System"},
    )
    def delete_tag_tool(
        tag_id: int = Field(description="Tag ID."),
    ) -> Any:
        """Delete tag."""
        return get_client().delete_tag(tag_id)

    @mcp.tool(
        name="get_motd",
        description="Get the Portainer message of the day.",
        tags={"System"},
    )
    def get_motd_tool() -> Any:
        """Get MOTD."""
        return get_client().get_motd()

    @mcp.tool(
        name="backup_portainer",
        description="Create a backup of all Portainer data.",
        tags={"System"},
    )
    def backup_portainer_tool(
        password: str = Field(
            default="", description="Password to encrypt the backup."
        ),
    ) -> Any:
        """Create backup."""
        return get_client().backup(password=password)


# ══════════════════════════════════════════════════════════════════════════
#  MCP Server entry point
# ══════════════════════════════════════════════════════════════════════════


def mcp_server():
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="Portainer MCP",
        version=__version__,
        instructions="Portainer MCP Server — Manage Docker environments, stacks, Kubernetes clusters, registries, users, edge devices, and system settings.",
    )

    # Register tool groups with env-var toggles
    if to_boolean(os.getenv("AUTHTOOL", "True")):
        register_auth_tools(mcp)
    if to_boolean(os.getenv("ENVIRONMENTTOOL", "True")):
        register_environment_tools(mcp)
    if to_boolean(os.getenv("DOCKERTOOL", "True")):
        register_docker_tools(mcp)
    if to_boolean(os.getenv("STACKTOOL", "True")):
        register_stack_tools(mcp)
    if to_boolean(os.getenv("KUBERNETESTOOL", "True")):
        register_kubernetes_tools(mcp)
    if to_boolean(os.getenv("EDGETOOL", "True")):
        register_edge_tools(mcp)
    if to_boolean(os.getenv("TEMPLATETOOL", "True")):
        register_template_tools(mcp)
    if to_boolean(os.getenv("USERTOOL", "True")):
        register_user_tools(mcp)
    if to_boolean(os.getenv("REGISTRYTOOL", "True")):
        register_registry_tools(mcp)
    if to_boolean(os.getenv("SYSTEMTOOL", "True")):
        register_system_tools(mcp)

    register_prompts(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)

    print("\nStarting Portainer MCP Server")
    print(f"  Transport: {args.transport.upper()}")
    print(f"  Auth: {args.auth_type}")
    print(f"  Delegation: {'ON' if config['enable_delegation'] else 'OFF'}")
    print(f"  Eunomia: {args.eunomia_type}")

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
