"""Summarize Loom workspace state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core import find_workspace_root, read_record, scan_records


def summarize_workspace(workspace: Path) -> dict:
    counts: dict[str, dict[str, int]] = {}
    for path in scan_records(workspace):
        try:
            frontmatter, _ = read_record(path)
        except Exception:
            continue
        kind = frontmatter.get("kind", "unknown")
        status = frontmatter.get("status", "unknown")
        counts.setdefault(kind, {})
        counts[kind][status] = counts[kind].get(status, 0) + 1
    return counts


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "status",
        help="Summarize Loom workspace state",
    )
    parser.add_argument("--json", action="store_true")
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()
    summary = summarize_workspace(workspace)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        for kind in sorted(summary):
            print(kind)
            for status, count in sorted(summary[kind].items()):
                print(f"  {status}: {count}")
    return 0
