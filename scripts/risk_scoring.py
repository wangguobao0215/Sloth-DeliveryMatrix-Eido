#!/usr/bin/env python3
"""
risk_scoring.py — Automated risk scoring for project state files.

Reads a project state YAML file, auto-detects risk signals from the data
(milestone delays, stale updates, resource gaps), calculates composite
risk scores using probability x impact, and outputs a risk summary.

Usage:
    python risk_scoring.py <project_state.yaml> [--format yaml|json]
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, date

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

SEVERITY_MAP = {"low": 1, "medium": 3, "high": 5}
TODAY = date.today()


def parse_date(date_str: str) -> date:
    """Parse an ISO date string into a date object."""
    if isinstance(date_str, date):
        return date_str
    return datetime.strptime(str(date_str), "%Y-%m-%d").date()


def detect_milestone_risks(project: dict) -> list:
    """Detect risks from milestone delays."""
    risks = []
    timeline = project.get("timeline", {})
    milestones = timeline.get("milestones", [])

    for ms in milestones:
        name = ms.get("name", "Unknown")
        status = ms.get("status", "").lower()
        due_str = ms.get("due_date") or ms.get("planned_date")
        if not due_str:
            continue
        due = parse_date(due_str)
        days_until = (due - TODAY).days

        if status == "delayed" or (status != "completed" and days_until < 0):
            overdue_days = abs(days_until) if days_until < 0 else 0
            probability = "high" if overdue_days > 14 else "medium"
            impact = "high" if ms.get("critical", False) else "medium"
            risks.append({
                "signal": "milestone_delay",
                "description": f"Milestone '{name}' is overdue by {overdue_days} days",
                "probability": probability,
                "impact": impact,
                "source": name,
            })
        elif status != "completed" and 0 <= days_until <= 7:
            risks.append({
                "signal": "milestone_at_risk",
                "description": f"Milestone '{name}' due in {days_until} days, still not completed",
                "probability": "medium",
                "impact": ms.get("impact", "medium"),
                "source": name,
            })
    return risks


def detect_stale_update_risks(project: dict) -> list:
    """Detect risks from stale weekly updates."""
    risks = []
    events = project.get("weekly_events", [])
    last_modified = project.get("_last_modified_at")

    if last_modified:
        try:
            last_date = parse_date(str(last_modified)[:10])
            stale_days = (TODAY - last_date).days
            if stale_days > 14:
                risks.append({
                    "signal": "stale_updates",
                    "description": f"Project state not updated for {stale_days} days",
                    "probability": "high" if stale_days > 30 else "medium",
                    "impact": "medium",
                    "source": "_last_modified_at",
                })
        except (ValueError, TypeError):
            pass

    if not events:
        risks.append({
            "signal": "no_weekly_events",
            "description": "No weekly events recorded in project state",
            "probability": "medium",
            "impact": "low",
            "source": "weekly_events",
        })
    return risks


def detect_resource_risks(project: dict) -> list:
    """Detect risks from resource/team gaps."""
    risks = []
    team = project.get("team", {})
    members = team.get("members", [])

    if not team.get("pm"):
        risks.append({
            "signal": "no_pm_assigned",
            "description": "No project manager assigned",
            "probability": "high",
            "impact": "high",
            "source": "team.pm",
        })

    for member in members:
        allocation = member.get("allocation", 0)
        name = member.get("name", "Unknown")
        if allocation > 1.0:
            risks.append({
                "signal": "resource_overload",
                "description": f"Team member '{name}' over-allocated at {allocation:.0%}",
                "probability": "medium",
                "impact": "medium",
                "source": f"team.members.{name}",
            })
    return risks


def calculate_score(probability: str, impact: str) -> int:
    """Calculate risk score as probability x impact."""
    return SEVERITY_MAP.get(probability, 1) * SEVERITY_MAP.get(impact, 1)


def score_risks(raw_risks: list) -> list:
    """Attach numeric score to each risk."""
    scored = []
    for r in raw_risks:
        score = calculate_score(r["probability"], r["impact"])
        level = "high" if score >= 15 else ("medium" if score >= 6 else "low")
        scored.append({**r, "score": score, "level": level})
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


def main():
    parser = argparse.ArgumentParser(description="Risk scoring for project state YAML")
    parser.add_argument("state_file", type=str, help="Path to project state YAML file")
    parser.add_argument("--format", choices=["yaml", "json"], default="yaml",
                        help="Output format (default: yaml)")
    args = parser.parse_args()

    state_path = Path(args.state_file)
    if not state_path.exists():
        print(f"ERROR: File not found: {state_path}", file=sys.stderr)
        sys.exit(1)

    with open(state_path, "r", encoding="utf-8") as f:
        project = yaml.safe_load(f) or {}

    # Detect risk signals
    all_risks = []
    all_risks.extend(detect_milestone_risks(project))
    all_risks.extend(detect_stale_update_risks(project))
    all_risks.extend(detect_resource_risks(project))

    # Score and rank
    scored = score_risks(all_risks)

    summary = {
        "project_id": project.get("project", {}).get("id", "unknown"),
        "analysis_date": TODAY.isoformat(),
        "total_risks": len(scored),
        "high_risks": sum(1 for r in scored if r["level"] == "high"),
        "medium_risks": sum(1 for r in scored if r["level"] == "medium"),
        "low_risks": sum(1 for r in scored if r["level"] == "low"),
        "risks": scored,
    }

    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, indent=2, default=str))
    else:
        print(yaml.dump(summary, allow_unicode=True, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
