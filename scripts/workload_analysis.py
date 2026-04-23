#!/usr/bin/env python3
"""
workload_analysis.py — Team workload analysis across projects.

Reads all project state YAML files from a directory, aggregates team
member allocations across projects, and flags overloaded (>1.0) and
underutilized (<0.3) members.

Usage:
    python workload_analysis.py <projects_directory>
"""

import sys
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

OVERLOADED_THRESHOLD = 1.0
UNDERUTILIZED_THRESHOLD = 0.3


def load_project_files(directory: Path) -> list:
    """Load all YAML files from the given directory."""
    projects = []
    yaml_files = sorted(directory.glob("*.yaml")) + sorted(directory.glob("*.yml"))
    for fpath in yaml_files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data:
                projects.append((fpath.name, data))
        except (yaml.YAMLError, OSError) as exc:
            print(f"  [WARN] Skipping {fpath.name}: {exc}", file=sys.stderr)
    return projects


def aggregate_workload(projects: list) -> dict:
    """Aggregate team member allocations across all projects."""
    workload = defaultdict(lambda: {"total_allocation": 0.0, "projects": []})

    for filename, project in projects:
        project_name = project.get("project", {}).get("name", filename)
        team = project.get("team", {})
        members = team.get("members", [])

        # Also count PM and tech lead
        for role_key in ("pm", "tech_lead"):
            role_data = team.get(role_key)
            if role_data and isinstance(role_data, dict):
                name = role_data.get("name")
                allocation = role_data.get("allocation", 0.5)
                if name:
                    workload[name]["total_allocation"] += allocation
                    workload[name]["projects"].append({
                        "project": project_name,
                        "role": role_key,
                        "allocation": allocation,
                    })

        for member in members:
            name = member.get("name")
            allocation = member.get("allocation", 0)
            role = member.get("role", "member")
            if name:
                workload[name]["total_allocation"] += allocation
                workload[name]["projects"].append({
                    "project": project_name,
                    "role": role,
                    "allocation": allocation,
                })

    return dict(workload)


def classify_members(workload: dict) -> dict:
    """Classify members as overloaded, normal, or underutilized."""
    overloaded = []
    underutilized = []
    normal = []

    for name, data in sorted(workload.items()):
        total = round(data["total_allocation"], 2)
        entry = {
            "name": name,
            "total_allocation": total,
            "project_count": len(data["projects"]),
            "projects": data["projects"],
        }
        if total > OVERLOADED_THRESHOLD:
            entry["flag"] = "overloaded"
            overloaded.append(entry)
        elif total < UNDERUTILIZED_THRESHOLD:
            entry["flag"] = "underutilized"
            underutilized.append(entry)
        else:
            entry["flag"] = "normal"
            normal.append(entry)

    return {
        "overloaded": sorted(overloaded, key=lambda x: x["total_allocation"], reverse=True),
        "normal": normal,
        "underutilized": sorted(underutilized, key=lambda x: x["total_allocation"]),
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python workload_analysis.py <projects_directory>", file=sys.stderr)
        sys.exit(1)

    projects_dir = Path(sys.argv[1])
    if not projects_dir.is_dir():
        print(f"ERROR: Not a directory: {projects_dir}", file=sys.stderr)
        sys.exit(1)

    projects = load_project_files(projects_dir)
    if not projects:
        print("No project state files found in directory.")
        sys.exit(0)

    workload = aggregate_workload(projects)
    classified = classify_members(workload)

    summary = {
        "analysis_date": __import__("datetime").date.today().isoformat(),
        "projects_scanned": len(projects),
        "total_members": len(workload),
        "overloaded_count": len(classified["overloaded"]),
        "underutilized_count": len(classified["underutilized"]),
        "thresholds": {
            "overloaded": OVERLOADED_THRESHOLD,
            "underutilized": UNDERUTILIZED_THRESHOLD,
        },
        "members": classified,
    }

    print(yaml.dump(summary, allow_unicode=True, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
