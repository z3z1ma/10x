"""Check cross-record link integrity in a Loom workspace."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core import (
    build_record_index,
    find_workspace_root,
    flatten_link_values,
    issue,
    read_record,
    scan_records,
)


def check_links(workspace: Path) -> list[dict]:
    problems: list[dict] = []
    index, duplicate_issues = build_record_index(workspace)
    problems.extend(duplicate_issues)
    for path in scan_records(workspace):
        try:
            frontmatter, _ = read_record(path)
        except Exception as exc:
            problems.append(issue(path, workspace, f"parse error: {exc}"))
            continue
        for ref in flatten_link_values(frontmatter.get("links", {})):
            if ref not in index:
                problems.append(issue(path, workspace, f"missing linked ref: {ref}"))
    return problems


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "check-links",
        help="Check Loom record link integrity",
    )
    parser.add_argument("--json", action="store_true")
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()
    problems = check_links(workspace)
    if args.json:
        print(json.dumps({"issues": problems}, indent=2))
    elif problems:
        for p in problems:
            print(f"ERROR {p['path']}: {p['message']}")
    else:
        print("All checked links resolve")
    return 1 if problems else 0
