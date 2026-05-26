#!/usr/bin/env python
from typing import Any

from portainer_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_edge_groups(self) -> Any:
        """List edge groups."""
        return self._get("edge_groups")

    def get_edge_group(self, group_id: int) -> dict:
        """Get a specific edge group."""
        return self._get(f"edge_groups/{group_id}")

    def create_edge_group(self, name: str, **kwargs) -> dict:
        """Create an edge group."""
        data = {"Name": name, **kwargs}
        return self._post("edge_groups", data=data)

    def update_edge_group(self, group_id: int, **kwargs) -> dict:
        """Update an edge group."""
        return self._put(f"edge_groups/{group_id}", data=kwargs)

    def delete_edge_group(self, group_id: int) -> bool:
        """Delete an edge group."""
        return self._delete(f"edge_groups/{group_id}")

    def get_edge_jobs(self) -> Any:
        """List edge jobs."""
        return self._get("edge_jobs")

    def get_edge_job(self, job_id: int) -> dict:
        """Get a specific edge job."""
        return self._get(f"edge_jobs/{job_id}")

    def create_edge_job_from_string(
        self, name: str, file_content: str, **kwargs
    ) -> dict:
        """Create an edge job from a string."""
        data = {"Name": name, "FileContent": file_content, **kwargs}
        return self._post("edge_jobs/create/string", data=data)

    def update_edge_job(self, job_id: int, **kwargs) -> dict:
        """Update an edge job."""
        return self._put(f"edge_jobs/{job_id}", data=kwargs)

    def delete_edge_job(self, job_id: int) -> bool:
        """Delete an edge job."""
        return self._delete(f"edge_jobs/{job_id}")

    def get_edge_job_file(self, job_id: int) -> dict:
        """Get the script file content for an edge job."""
        return self._get(f"edge_jobs/{job_id}/file")

    def get_edge_job_tasks(self, job_id: int) -> Any:
        """List tasks for an edge job."""
        return self._get(f"edge_jobs/{job_id}/tasks")

    def get_edge_job_task_logs(self, job_id: int, task_id: int) -> dict:
        """Get logs for an edge job task."""
        return self._get(f"edge_jobs/{job_id}/tasks/{task_id}/logs")

    def get_edge_stacks(self) -> Any:
        """List edge stacks."""
        return self._get("edge_stacks")

    def get_edge_stack(self, stack_id: int) -> dict:
        """Get a specific edge stack."""
        return self._get(f"edge_stacks/{stack_id}")

    def create_edge_stack_from_string(
        self, name: str, file_content: str, edge_groups: list[int], **kwargs
    ) -> dict:
        """Create an edge stack from a string."""
        data = {
            "Name": name,
            "StackFileContent": file_content,
            "EdgeGroups": edge_groups,
            **kwargs,
        }
        return self._post("edge_stacks/create/string", data=data)

    def create_edge_stack_from_repository(
        self, name: str, repo_url: str, edge_groups: list[int], **kwargs
    ) -> dict:
        """Create an edge stack from a Git repository."""
        data = {
            "Name": name,
            "RepositoryURL": repo_url,
            "EdgeGroups": edge_groups,
            **kwargs,
        }
        return self._post("edge_stacks/create/repository", data=data)

    def update_edge_stack(self, stack_id: int, **kwargs) -> dict:
        """Update an edge stack."""
        return self._put(f"edge_stacks/{stack_id}", data=kwargs)

    def delete_edge_stack(self, stack_id: int) -> bool:
        """Delete an edge stack."""
        return self._delete(f"edge_stacks/{stack_id}")

    def get_edge_stack_file(self, stack_id: int) -> dict:
        """Get the compose file content for an edge stack."""
        return self._get(f"edge_stacks/{stack_id}/file")

    def get_edge_stack_status(self, stack_id: int) -> dict:
        """Get edge stack deployment status."""
        return self._get(f"edge_stacks/{stack_id}/status")
