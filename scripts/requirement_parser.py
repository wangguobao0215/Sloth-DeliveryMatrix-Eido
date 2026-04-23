#!/usr/bin/env python3
"""
requirement_parser.py — Parse requirement documents and extract structured requirements.

Reads raw requirement text (from documents, emails, meeting notes, etc.),
extracts individual requirements with IDs, descriptions, priorities, and
categories, and outputs a structured requirement list.

Usage:
    python requirement_parser.py <input_file> [--format yaml|json|csv] [--id-prefix REQ]

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
        description="Parse requirement documents and extract structured requirements."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input requirement document (text, markdown, or YAML)",
    )
    parser.add_argument(
        "--format",
        choices=["yaml", "json", "csv"],
        default="yaml",
        help="Output format (default: yaml)",
    )
    parser.add_argument(
        "--id-prefix",
        type=str,
        default="REQ",
        help="Prefix for auto-generated requirement IDs (default: REQ)",
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        help="Default category for requirements without explicit categorization",
    )
    return parser.parse_args()


def parse_requirements(input_path: Path, output_format: str, id_prefix: str, default_category: str):
    """
    Parse a requirement document and extract structured requirements.

    TODO: Planned implementation steps:
      1. Read the input file content
      2. Detect input format (plain text, markdown, structured YAML)
      3. Apply parsing heuristics based on format:
         - Numbered lists -> individual requirements
         - Headings -> category/module grouping
         - "shall/must/should" keywords -> requirement sentences
         - Priority markers (P0/P1/P2, high/medium/low)
         - Acceptance criteria following requirements
      4. For each extracted requirement, generate:
         - id: auto-incremented with id_prefix (e.g., REQ-001)
         - description: the requirement statement
         - priority: high/medium/low (inferred or default medium)
         - category: functional/non-functional/constraint (inferred or default)
         - source: line number or section reference in original document
         - acceptance_criteria: extracted if present, null otherwise
      5. Deduplicate similar requirements and flag potential overlaps
      6. Output in the requested format:
         - yaml: structured list suitable for state file integration
         - json: JSON array for API/tool consumption
         - csv: tabular format for spreadsheet import
    """
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        return False

    print(f"[STUB] requirement_parser is not yet implemented.")
    print(f"  Input    : {input_path}")
    print(f"  Format   : {output_format}")
    print(f"  ID prefix: {id_prefix}")
    print(f"  Category : {default_category or '(auto-detect)'}")
    print()
    print("Planned functionality:")
    print("  - Detect input format (text, markdown, YAML)")
    print("  - Extract requirements using NL heuristics (shall/must/should)")
    print("  - Auto-assign IDs, priorities, and categories")
    print("  - Extract acceptance criteria where present")
    print("  - Deduplicate and flag overlapping requirements")
    print("  - Output structured requirement list in yaml/json/csv")
    return False


def main():
    args = parse_args()
    input_path = Path(args.input_file)

    success = parse_requirements(input_path, args.format, args.id_prefix, args.category)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
