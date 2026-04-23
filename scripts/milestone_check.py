#!/usr/bin/env python3
"""
milestone_check.py — Milestone health check for project state files.

Reads a project state YAML file, evaluates each milestone's health
(on-track, at-risk, delayed), and calculates the Schedule Performance
Index (SPI).

Usage:
    python milestone_check.py <project_state.yaml>
"""

import sys
from pathlib import Path
from datetime import datetime, date

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

TODAY = date.today()


def parse_date(date_str) -> date:
    """Parse an ISO date string into a date object."""
    if isinstance(date_str, date):
        return date_str
    return datetime.strptime(str(date_str), "%Y-%m-%d").date()


def assess_milestone(ms: dict) -> dict:
    """Assess a single milestone and return its health status."""
    name = ms.get("name", "Unknown")
    status = ms.get("status", "pending").lower()
    completion = ms.get("completion_pct", 0)
    due_str = ms.get("due_date") or ms.get("planned_date")

    result = {"name": name, "status": status, "completion_pct": completion}

    if status == "completed":
        result["health"] = "on-track"
        result["earned_value"] = 1.0
        return result

    if not due_str:
        result["health"] = "unknown"
        result["earned_value"] = completion / 100.0
        result["note"] = "No due date specified"
        return result

    due = parse_date(due_str)
    days_remaining = (due - TODAY).days

    # Calculate expected progress based on timeline
    start_str = ms.get("start_date")
    if start_str:
        start = parse_date(start_str)
        total_days = max((due - start).days, 1)
        elapsed_days = max((TODAY - start).days, 0)
        expected_pct = min((elapsed_days / total_days) * 100, 100)
    else:
        expected_pct = None

    # Determine health
    if days_remaining < 0:
        result["health"] = "delayed"
        result["overdue_days"] = abs(days_remaining)
    elif days_remaining <= 7 and completion < 80:
        result["health"] = "at-risk"
        result["days_remaining"] = days_remaining
    elif expected_pct is not None and completion < (expected_pct - 15):
        result["health"] = "at-risk"
        result["expected_pct"] = round(expected_pct, 1)
        result["gap"] = round(expected_pct - completion, 1)
    else:
        result["health"] = "on-track"

    result["due_date"] = due.isoformat()
    result["earned_value"] = completion / 100.0

    return result


def calculate_spi(milestones: list, results: list) -> float:
    """
    Calculate Schedule Performance Index.
    SPI = Earned Value / Planned Value
    A value < 1.0 indicates behind schedule.
    """
    if not results:
        return 0.0

    total_earned = sum(r.get("earned_value", 0) for r in results)
    # Planned value: milestones that should be completed by now
    total_planned = 0.0
    for ms, result in zip(milestones, results):
        due_str = ms.get("due_date") or ms.get("planned_date")
        if due_str:
            due = parse_date(due_str)
            if due <= TODAY:
                total_planned += 1.0
            else:
                start_str = ms.get("start_date")
                if start_str:
                    start = parse_date(start_str)
                    total_days = max((due - start).days, 1)
                    elapsed = max((TODAY - start).days, 0)
                    total_planned += min(elapsed / total_days, 1.0)
                else:
                    total_planned += 0.5
        else:
            total_planned += 0.5

    return round(total_earned / max(total_planned, 0.01), 2)


def main():
    if len(sys.argv) < 2:
        print("Usage: python milestone_check.py <project_state.yaml>", file=sys.stderr)
        sys.exit(1)

    state_path = Path(sys.argv[1])
    if not state_path.exists():
        print(f"ERROR: File not found: {state_path}", file=sys.stderr)
        sys.exit(1)

    with open(state_path, "r", encoding="utf-8") as f:
        project = yaml.safe_load(f) or {}

    timeline = project.get("timeline", {})
    milestones = timeline.get("milestones", [])

    if not milestones:
        print("No milestones found in project state.")
        sys.exit(0)

    results = [assess_milestone(ms) for ms in milestones]
    spi = calculate_spi(milestones, results)

    # Build summary
    summary = {
        "project_id": project.get("project", {}).get("id", "unknown"),
        "check_date": TODAY.isoformat(),
        "spi": spi,
        "spi_status": "ahead" if spi > 1.05 else ("on-track" if spi >= 0.95 else "behind"),
        "total_milestones": len(results),
        "on_track": sum(1 for r in results if r["health"] == "on-track"),
        "at_risk": sum(1 for r in results if r["health"] == "at-risk"),
        "delayed": sum(1 for r in results if r["health"] == "delayed"),
        "milestones": results,
    }

    print(yaml.dump(summary, allow_unicode=True, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
