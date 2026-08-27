#!/usr/bin/env python3

import argparse
import json
import os
import sys
from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Deterministic Portainer stack health and Swarm service update status analyzer."
    )
    parser.add_argument(
        "--stacks-json",
        required=True,
        help="Path to the JSON file containing Portainer stacks data.",
    )
    parser.add_argument(
        "--services-json",
        required=True,
        help="Path to the JSON file containing Docker Swarm services data.",
    )
    parser.add_argument(
        "--output",
        help="Path to write the generated markdown report. If not specified, the report is printed to stdout.",
    )
    return (
        parser.parse_parse_args()
        if hasattr(parser, "parse_parse_args")
        else parser.parse_args()
    )


def load_json_file(filepath):
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
            # Portainer sometimes wraps data inside a dictionary under a 'data' key or lists it directly.
            if isinstance(data, dict) and "data" in data:
                return data["data"]
            return data
    except Exception as exc:
        print(
            f"Error: Failed to load JSON input: {type(exc).__name__}", file=sys.stderr
        )
        sys.exit(1)


def format_timestamp(epoch_or_str):
    if not epoch_or_str:
        return "N/A"
    if isinstance(epoch_or_str, (int, float)):
        try:
            return datetime.fromtimestamp(epoch_or_str).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return "N/A"
    return str(epoch_or_str).replace("T", " ").split(".")[0]


def _build_stacks_index(stacks_data):
    """Build a mapping of stacks by their Name (namespace)."""
    stacks_dict = {}
    for stack in stacks_data:
        name = stack.get("Name")
        if not name:
            continue
        git_conf = stack.get("GitConfig")
        git_repo = git_conf.get("RepositoryURL") if git_conf else None
        git_ref = git_conf.get("RepositoryReferenceName") if git_conf else None

        stacks_dict[name] = {
            "id": stack.get("Id"),
            "name": name,
            "status": "Active" if stack.get("Status") == 1 else "Inactive",
            "created_at": format_timestamp(stack.get("CreationDate")),
            "updated_at": format_timestamp(stack.get("UpdateDate")),
            "updated_by": stack.get("UpdatedBy", "N/A"),
            "git_repo": git_repo,
            "git_ref": git_ref,
            "services": [],
        }
    return stacks_dict


def _resolve_service_namespace(svc, svc_name, labels):
    # 1. Check direct label
    namespace = labels.get("com.docker.stack.namespace")

    # 2. Check PreviousSpec labels
    if not namespace:
        prev_spec = svc.get("PreviousSpec", {})
        prev_labels = prev_spec.get("Labels", {})
        namespace = prev_labels.get("com.docker.stack.namespace")

    # 3. Guess namespace from service name prefix (namespace_servicename)
    if not namespace and "_" in svc_name:
        namespace = svc_name.split("_")[0]

    return namespace


def _resolve_service_replicas(spec):
    replicas = spec.get("Mode", {}).get("Replicated", {}).get("Replicas")
    if replicas is None:
        if spec.get("Mode", {}).get("Global") is not None:
            replicas = "Global"
        else:
            replicas = 1
    return replicas


def _resolve_service_image(spec, labels):
    image = labels.get("com.docker.stack.image")
    if not image:
        container_spec = spec.get("TaskTemplate", {}).get("ContainerSpec", {})
        image = container_spec.get("Image", "N/A")
        # Clean image digest if present
        if "@sha256:" in image:
            image = image.split("@sha256:")[0]
    return image


def _build_service_info(svc):
    """Resolve one Swarm service's namespace + normalized info dict."""
    spec = svc.get("Spec", {})
    svc_name = spec.get("Name", "unnamed-service")
    labels = spec.get("Labels", {})

    namespace = _resolve_service_namespace(svc, svc_name, labels)
    replicas = _resolve_service_replicas(spec)
    image = _resolve_service_image(spec, labels)

    # Get Placement Constraints
    placement = spec.get("TaskTemplate", {}).get("Placement", {})
    constraints = placement.get("Constraints", [])

    # Update Status
    update_status = svc.get("UpdateStatus", {})

    svc_info = {
        "id": svc.get("ID"),
        "name": svc_name,
        "image": image,
        "replicas": replicas,
        "constraints": constraints,
        "update_state": update_status.get("State", "completed"),
        "update_message": update_status.get("Message", ""),
        "update_started": format_timestamp(update_status.get("StartedAt")),
        "update_completed": format_timestamp(update_status.get("CompletedAt")),
        "created_at": format_timestamp(svc.get("CreatedAt")),
        "updated_at": format_timestamp(svc.get("UpdatedAt")),
    }
    return namespace, svc_info


def _correlate_services(services_data, stacks_dict):
    """Process services and correlate them to stacks (mutates stacks_dict in
    place); returns the list of (namespace, svc_info) orphan services."""
    orphan_services = []
    for svc in services_data:
        namespace, svc_info = _build_service_info(svc)
        if namespace in stacks_dict:
            stacks_dict[namespace]["services"].append(svc_info)
        else:
            orphan_services.append((namespace, svc_info))
    return orphan_services


def _classify_stack_health(stacks_dict):
    """Classify each stack's health state; returns (healthy, degraded,
    unhealthy) lists. Mutates each stack dict with a "health" key."""
    healthy_stacks = []
    degraded_stacks = []
    unhealthy_stacks = []

    for _name, stack in stacks_dict.items():
        svcs = stack["services"]
        if not svcs:
            stack["health"] = "Healthy (Empty)"
            healthy_stacks.append(stack)
            continue

        has_error = False
        has_warning = False

        for s in svcs:
            if s["update_state"] in ["paused", "failed"]:
                has_error = True
            elif s["update_state"] in [
                "updating",
                "rollback_started",
                "rollback_paused",
                "rollback_completed",
            ]:
                has_warning = True

        if has_error:
            stack["health"] = "Unhealthy"
            unhealthy_stacks.append(stack)
        elif has_warning:
            stack["health"] = "Degraded"
            degraded_stacks.append(stack)
        else:
            stack["health"] = "Healthy"
            healthy_stacks.append(stack)

    return healthy_stacks, degraded_stacks, unhealthy_stacks


def _render_summary(
    stacks_data,
    services_data,
    healthy_stacks,
    degraded_stacks,
    unhealthy_stacks,
    orphan_services,
):
    md = []
    md.append("# 📋 Homelab Swarm Stack Health Report")
    md.append(
        f"\n> [!IMPORTANT]\n> This report presents a comprehensive health assessment of the **{len(stacks_data)}** Portainer stacks and **{len(services_data)}** Swarm services.\n"
    )

    # Executive Summary Metrics Table
    md.append("## 📊 Executive Summary\n")
    md.append("| Metric | Value | Status |")
    md.append("| :--- | :---: | :--- |")
    md.append(f"| **Total Portainer Stacks** | {len(stacks_data)} | - |")
    md.append(f"| **Total Swarm Services** | {len(services_data)} | - |")
    md.append(f"| **Healthy Stacks** | {len(healthy_stacks)} | 🟢 Operational |")
    md.append(
        f"| **Degraded Stacks** | {len(degraded_stacks)} | 🟡 Warning (Updating/Rollback) |"
    )
    md.append(
        f"| **Unhealthy Stacks** | {len(unhealthy_stacks)} | 🔴 Action Required (Update Paused) |"
    )
    md.append(
        f"| **Standalone Swarm Services** | {len(orphan_services)} | 🌐 Unmanaged by Portainer Stacks |"
    )
    md.append("\n")
    return md


def _render_unhealthy_recommendations(unhealthy_stacks):
    md: list[str] = []
    if not unhealthy_stacks:
        return md
    md.append("### Critical Remediation Actions Required:\n")
    for s in unhealthy_stacks:
        md.append(f"- **Stack `{s['name']}` is Unhealthy**:")
        for svc in s["services"]:
            if svc["update_state"] in ["paused", "failed"]:
                md.append(
                    f"  - Service `{svc['name']}` update state is `{svc['update_state']}`. Error message: *{svc['update_message'] or 'No message available'}*"
                )
        md.append(
            "  - *Action*: Inspect the task exit codes and container logs using `docker service ps` and `docker service logs`."
        )
        md.append("\n")
    return md


def _render_degraded_recommendations(degraded_stacks):
    md: list[str] = []
    if not degraded_stacks:
        return md
    md.append("### Warning / Active Updates:\n")
    for s in degraded_stacks:
        md.append(f"- **Stack `{s['name']}` is Degraded**:")
        for svc in s["services"]:
            if svc["update_state"] in [
                "updating",
                "rollback_started",
                "rollback_paused",
                "rollback_completed",
            ]:
                md.append(
                    f"  - Service `{svc['name']}` update state is `{svc['update_state']}`."
                )
        md.append(
            "  - *Action*: Monitor the roll-out progression or check if resources are constrained on the active node."
        )
        md.append("\n")
    return md


def _render_git_alignment_warnings(stacks_data):
    md: list[str] = []
    orphan_git_stacks = [s for s in stacks_data if not s.get("GitConfig")]
    if not orphan_git_stacks:
        return md
    md.append("### Git Source of Truth Alignment:\n")
    md.append(
        f"- **{len(orphan_git_stacks)}** stacks are deployed manually/ad-hoc (no associated Git configuration):"
    )
    for s in sorted(orphan_git_stacks, key=lambda x: x.get("Name", "")):
        md.append(f"  - `{s.get('Name')}` (ID: {s.get('Id')})")
    md.append(
        "  - *Action*: Seed GitLab repositories for these orphan stacks to ensure configuration management, change control, and pipeline stability."
    )
    md.append("\n")
    return md


def _render_recommendations(unhealthy_stacks, degraded_stacks, stacks_data):
    md = ["## 💡 Key Diagnostics & Recommendations\n"]
    md.extend(_render_unhealthy_recommendations(unhealthy_stacks))
    md.extend(_render_degraded_recommendations(degraded_stacks))
    md.extend(_render_git_alignment_warnings(stacks_data))
    return md


def _render_unhealthy_section(unhealthy_stacks):
    md = []
    md.append("## 🔴 Unhealthy Stacks (Action Required)\n")
    if not unhealthy_stacks:
        md.append("*No unhealthy stacks found.*\n")
        return md
    for stack in sorted(unhealthy_stacks, key=lambda x: x["name"]):
        md.append(f"### 📦 Stack: `{stack['name']}` (ID: {stack['id']})")
        md.append("| Attribute | Value |")
        md.append("| :--- | :--- |")
        md.append(f"| **Status** | {stack['status']} |")
        md.append(f"| **Created At** | {stack['created_at']} |")
        md.append(
            f"| **Last Updated** | {stack['updated_at']} by `{stack['updated_by']}` |"
        )
        git_status = (
            f"[`{stack['git_repo']}`]({stack['git_repo']}) (ref: `{stack['git_ref']}`)"
            if stack["git_repo"]
            else "None (Manual / Ad-hoc)"
        )
        md.append(f"| **Git Config** | {git_status} |")
        md.append("\n")

        md.append("#### Services Detail:")
        md.append("| Service Name | Image | Replicas | Update State | Status Message |")
        md.append("| :--- | :--- | :---: | :---: | :--- |")
        for s in stack["services"]:
            status_emoji = (
                "🔴 " + s["update_state"]
                if s["update_state"] in ["paused", "failed"]
                else "🟢 healthy"
            )
            msg = s["update_message"] if s["update_message"] else "-"
            md.append(
                f"| `{s['name']}` | `{s['image']}` | {s['replicas']} | {status_emoji} | {msg} |"
            )
        md.append("\n---\n")
    return md


def _render_degraded_section(degraded_stacks):
    md = []
    md.append("## 🟡 Degraded Stacks\n")
    if not degraded_stacks:
        md.append("*No degraded stacks found.*\n")
        return md
    for stack in sorted(degraded_stacks, key=lambda x: x["name"]):
        md.append(f"### 📦 Stack: `{stack['name']}` (ID: {stack['id']})")
        md.append("| Attribute | Value |")
        md.append("| :--- | :--- |")
        md.append(f"| **Created At** | {stack['created_at']} |")
        md.append(
            f"| **Last Updated** | {stack['updated_at']} by `{stack['updated_by']}` |"
        )
        md.append("\n")

        md.append("#### Services Detail:")
        md.append("| Service Name | Image | Replicas | Update State | Status Message |")
        md.append("| :--- | :--- | :---: | :---: | :--- |")
        for s in stack["services"]:
            status_emoji = (
                "🟡 " + s["update_state"]
                if s["update_state"]
                in [
                    "updating",
                    "rollback_started",
                    "rollback_paused",
                    "rollback_completed",
                ]
                else "🟢 completed"
            )
            msg = s["update_message"] if s["update_message"] else "-"
            md.append(
                f"| `{s['name']}` | `{s['image']}` | {s['replicas']} | {status_emoji} | {msg} |"
            )
        md.append("\n---\n")
    return md


def _render_orphan_services_section(orphan_services):
    md: list[str] = []
    if not orphan_services:
        return md
    md.append("## 🌐 Standalone Swarm Services\n")
    md.append(
        "These are active Swarm services that are not currently associated with a Portainer stack namespace.\n"
    )
    md.append("| Service Name | Image | Replicas | Status |")
    md.append("| :--- | :--- | :---: | :--- |")
    for _namespace, s in sorted(orphan_services, key=lambda x: x[1]["name"]):
        status_str = (
            f"🔴 {s['update_state']}"
            if s["update_state"] in ["paused", "failed"]
            else "🟢 operational"
        )
        md.append(
            f"| `{s['name']}` | `{s['image']}` | {s['replicas']} | {status_str} |"
        )
    md.append("\n---\n")
    return md


def _render_healthy_section(healthy_stacks):
    md = []
    md.append("## 🟢 Healthy Stacks\n")
    md.append(
        "These stacks are fully operational with all services running normally.\n"
    )
    md.append("| Stack Name | ID | Services | Git-Backed | Last Updated |")
    md.append("| :--- | :---: | :---: | :---: | :--- |")
    for stack in sorted(healthy_stacks, key=lambda x: x["name"]):
        git_backed = "Yes" if stack["git_repo"] else "No"
        svc_count = len(stack["services"])
        md.append(
            f"| `{stack['name']}` | {stack['id']} | {svc_count} | {git_backed} | {stack['updated_at']} |"
        )
    return md


def _write_or_print_report(report_content, output_path):
    if output_path:
        try:
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report_content)
            print("Diagnostics report written successfully")
        except Exception as exc:
            print(
                f"Error: Failed to write report: {type(exc).__name__}",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        print(report_content)


def main():
    args = parse_arguments()

    stacks_data = load_json_file(args.stacks_json)
    services_data = load_json_file(args.services_json)

    stacks_dict = _build_stacks_index(stacks_data)
    orphan_services = _correlate_services(services_data, stacks_dict)
    healthy_stacks, degraded_stacks, unhealthy_stacks = _classify_stack_health(
        stacks_dict
    )

    md = []
    md.extend(
        _render_summary(
            stacks_data,
            services_data,
            healthy_stacks,
            degraded_stacks,
            unhealthy_stacks,
            orphan_services,
        )
    )
    md.extend(_render_recommendations(unhealthy_stacks, degraded_stacks, stacks_data))
    md.append("---\n")

    # Unhealthy Stacks Section
    md.extend(_render_unhealthy_section(unhealthy_stacks))

    # Degraded Stacks Section
    md.extend(_render_degraded_section(degraded_stacks))

    # Standalone/Orphan Services Section
    md.extend(_render_orphan_services_section(orphan_services))

    # Healthy Stacks Section
    md.extend(_render_healthy_section(healthy_stacks))

    # Write or Print Report
    report_content = "\n".join(md)
    _write_or_print_report(report_content, args.output)


if __name__ == "__main__":
    main()
