#!/usr/bin/env python3
"""
normalize.py — Normalize and validate state files against schema.

Reads project state YAML files, validates them against the
project-state.schema.yaml schema, reports any issues, and
optionally auto-fixes common problems (missing fields, type
mismatches, deprecated keys).

Usage:
    python normalize.py <state_file_or_dir> [--fix] [--schema <schema.yaml>]

Dependencies:
    pip install pyyaml
"""

# TODO: Full implementation pending. This is a functional stub.

import sys
import argparse
from pathlib import Path

DEFAULT_SCHEMA = Path(__file__).parent.parent / "schemas" / "project-state.schema.yaml"


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Normalize and validate state files against schema."
    )
    parser.add_argument(
        "target",
        type=str,
        help="Path to a state YAML file or a directory containing state files",
    )
    parser.add_argument(
        "--schema",
        type=str,
        default=str(DEFAULT_SCHEMA),
        help=f"Path to the schema YAML file (default: {DEFAULT_SCHEMA})",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix common issues (add missing fields with defaults, normalize types)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (non-zero exit on any issue)",
    )
    return parser.parse_args()


def normalize_state(target_path: Path, schema_path: Path, auto_fix: bool, strict: bool):
    """
    Validate and optionally normalize state files.

    TODO: Planned implementation steps:
      1. Load the schema YAML defining required fields, types, and constraints
      2. Discover target files:
         - If target is a file, validate that single file
         - If target is a directory, find all *.yaml files recursively
      3. For each state file:
         a. Parse YAML content
         b. Validate _version field exists and is supported
         c. Check all required top-level keys (project, timeline, team, risks, etc.)
         d. Validate field types (string, int, date, list, enum)
         e. Check enum values against allowed lists
         f. Detect deprecated keys and suggest replacements
         g. Validate date formats (ISO 8601)
         h. Check referential integrity (e.g., milestone owners exist in team.members)
      4. Report findings:
         - [ERROR] for missing required fields or invalid types
         - [WARN] for deprecated keys or suspicious values
         - [INFO] for auto-fixable issues
      5. If --fix is set:
         a. Add missing optional fields with default values
         b. Normalize date formats
         c. Remove deprecated keys (after backing up)
         d. Update _last_modified_at timestamp
         e. Write corrected file back
      6. Exit with code 0 if no errors (or only warnings in non-strict mode)
    """
    if not target_path.exists():
        print(f"ERROR: Target not found: {target_path}", file=sys.stderr)
        return False

    print(f"[STUB] normalize is not yet implemented.")
    print(f"  Target : {target_path}")
    print(f"  Schema : {schema_path}")
    print(f"  Auto-fix: {auto_fix}")
    print(f"  Strict : {strict}")
    print()
    print("Planned functionality:")
    print("  - Load schema and discover state files")
    print("  - Validate required fields, types, and enum values")
    print("  - Check date formats and referential integrity")
    print("  - Report errors, warnings, and info messages")
    print("  - Auto-fix mode: add defaults, normalize formats, remove deprecated keys")
    return False


def main():
    args = parse_args()
    target_path = Path(args.target)
    schema_path = Path(args.schema)

    success = normalize_state(target_path, schema_path, args.fix, args.strict)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
