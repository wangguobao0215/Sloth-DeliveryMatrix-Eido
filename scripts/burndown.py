#!/usr/bin/env python3
"""
burndown.py — Generate burndown/burnup chart data.

Reads sprint or iteration data from a project state YAML file,
calculates ideal vs actual burndown curves, and outputs chart data
for progress visualization.

Usage:
    python burndown.py <project_state.yaml> [--sprint <sprint_name>] [--format text|csv|json]

Dependencies:
    pip install pyyaml
"""

# TODO: Full implementation pending. This is a functional stub.

import sys
import argparse
from pathlib import Path


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate burndown/burnup chart data from project state."
    )
    parser.add_argument(
        "state_file",
        type=str,
        help="Path to the project state YAML file",
    )
    parser.add_argument(
        "--sprint",
        type=str,
        default=None,
        help="Name or ID of the sprint/iteration to chart (default: current sprint)",
    )
    parser.add_argument(
        "--mode",
        choices=["burndown", "burnup"],
        default="burndown",
        help="Chart mode: burndown (remaining work) or burnup (completed work). Default: burndown",
    )
    parser.add_argument(
        "--format",
        choices=["text", "csv", "json"],
        default="text",
        help="Output format (default: text)",
    )
    return parser.parse_args()


def generate_burndown(state_path: Path, sprint_name: str, mode: str, output_format: str):
    """
    Generate burndown or burnup chart data.

    TODO: Planned implementation steps:
      1. Read and parse the project state YAML file
      2. Locate the target sprint/iteration data:
         - If sprint_name provided, find matching sprint
         - Otherwise, identify the current active sprint by date range
      3. Extract data points:
         - Total story points / work items at sprint start
         - Daily completion records from weekly_events[]
         - Scope changes (items added/removed mid-sprint)
      4. Calculate ideal burndown line:
         - Linear from total_points on day 1 to 0 on last day
      5. Calculate actual burndown curve:
         - Remaining = total - completed_cumulative (for burndown)
         - Completed = completed_cumulative (for burnup)
      6. For text format: ASCII chart with ideal (---) and actual (===) lines
      7. For csv format: date, ideal_remaining, actual_remaining, scope_change
      8. For json format: structured data for web charting libraries
    """
    if not state_path.exists():
        print(f"ERROR: State file not found: {state_path}", file=sys.stderr)
        return False

    print(f"[STUB] burndown is not yet implemented.")
    print(f"  State file: {state_path}")
    print(f"  Sprint    : {sprint_name or '(current)'}")
    print(f"  Mode      : {mode}")
    print(f"  Format    : {output_format}")
    print()
    print("Planned functionality:")
    print("  - Identify target sprint from project state")
    print("  - Calculate ideal linear burndown curve")
    print("  - Calculate actual progress from daily completion data")
    print("  - Track scope changes and their impact on the chart")
    print("  - Output in text/csv/json for visualization")
    return False


def main():
    args = parse_args()
    state_path = Path(args.state_file)

    success = generate_burndown(state_path, args.sprint, args.mode, args.format)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
