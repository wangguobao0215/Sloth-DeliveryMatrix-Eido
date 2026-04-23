#!/usr/bin/env python3
"""
init_state.py — Initialize project state directory for Sloth-DeliveryMatrix-Eido.

Creates the persistent state directory structure under
~/.qoderwork/data/Sloth-DeliveryMatrix-Eido/state/
with a global.yaml template and an empty projects/ directory.
"""

import sys
from pathlib import Path
from datetime import datetime

SKILL_NAME = "Sloth-DeliveryMatrix-Eido"
STATE_ROOT = Path.home() / ".qoderwork" / "data" / SKILL_NAME / "state"

GLOBAL_YAML_TEMPLATE = """\
# Sloth-DeliveryMatrix-Eido — Global State
# Auto-generated on {timestamp}

_version: "1.0"
_last_modified_by: "system"
_last_modified_at: "{timestamp}"

settings:
  default_industry: null
  default_project_type: null
  risk_threshold:
    high: 15
    medium: 6
    low: 1
  workload_limits:
    overloaded: 1.0
    underutilized: 0.3

active_projects: []

recent_activity: []
"""

ACTIVE_CONTEXT_YAML_TEMPLATE = """\
# Sloth-DeliveryMatrix-Eido — Active Role Context
# Auto-generated on {timestamp}

_version: 1
_last_modified_by: "system"
_last_modified_at: "{timestamp}"

active_role: "pm"
last_route: null
last_route_at: null
last_output_summary: ""
pending_actions: []
"""


def create_directory(path: Path, label: str) -> bool:
    """Create a directory if it does not exist. Returns True on success."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        print(f"  [OK] {label}: {path}")
        return True
    except OSError as exc:
        print(f"  [ERROR] Failed to create {label}: {exc}", file=sys.stderr)
        return False


def write_template(path: Path, content: str, label: str) -> bool:
    """Write content to a file. Returns True on success."""
    try:
        path.write_text(content, encoding="utf-8")
        print(f"  [OK] {label}: {path}")
        return True
    except OSError as exc:
        print(f"  [ERROR] Failed to write {label}: {exc}", file=sys.stderr)
        return False


def init_state() -> int:
    """
    Initialize the state directory structure.
    Returns 0 on success, 1 on any failure.
    """
    print(f"Initializing state for {SKILL_NAME} ...")
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    ok = True

    # 1. Create root state directory
    ok &= create_directory(STATE_ROOT, "state root")

    # 2. Create projects sub-directory
    projects_dir = STATE_ROOT / "projects"
    ok &= create_directory(projects_dir, "projects directory")

    # 3. Create role-state sub-directory
    role_state_dir = STATE_ROOT / "role-state"
    ok &= create_directory(role_state_dir, "role-state directory")

    # 4. Create _backups sub-directory
    backups_dir = STATE_ROOT / "_backups"
    ok &= create_directory(backups_dir, "_backups directory")

    # 5. Write global.yaml template
    global_yaml_path = STATE_ROOT / "global.yaml"
    if global_yaml_path.exists():
        print(f"  [SKIP] global.yaml already exists: {global_yaml_path}")
    else:
        content = GLOBAL_YAML_TEMPLATE.format(timestamp=timestamp)
        ok &= write_template(global_yaml_path, content, "global.yaml")

    # 6. Write role-state/active-context.yaml template
    active_context_path = role_state_dir / "active-context.yaml"
    if active_context_path.exists():
        print(f"  [SKIP] active-context.yaml already exists: {active_context_path}")
    else:
        content = ACTIVE_CONTEXT_YAML_TEMPLATE.format(timestamp=timestamp)
        ok &= write_template(active_context_path, content, "active-context.yaml")

    if ok:
        print("\nState initialization completed successfully.")
        print(f"  State root      : {STATE_ROOT}")
        print(f"  Projects        : {projects_dir}")
        print(f"  Role state      : {role_state_dir}")
        print(f"  Backups         : {backups_dir}")
        print(f"  Global conf     : {global_yaml_path}")
        print(f"  Active context  : {active_context_path}")
    else:
        print("\nState initialization completed with errors.", file=sys.stderr)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(init_state())
