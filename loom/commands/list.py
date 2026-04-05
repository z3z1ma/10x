"""List Loom records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core import (
    find_workspace_root,
    read_record,
    relative_to_workspace,
    scan_records,
)


def list_records(
    workspace: Path,
    *,
    kind: str | None = None,
    status: str | None = None,
    include_runs: bool = False,
) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for path in scan_records(workspace, include_runs=include_runs):
        frontmatter, _body = read_record(path)
        record_kind = frontmatter.get("kind")
        record_status = frontmatter.get("status")
        if kind and record_kind != kind:
            continue
        if status and record_status != status:
            continue
        results.append(
            {
                "id": frontmatter.get("id", "unknown"),
                "kind": record_kind or "unknown",
                "status": record_status or "unknown",
                "path": relative_to_workspace(path, workspace),
            }
        )
    return results


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "list",
        help="List Loom records",
    )
    parser.add_argument("--kind")
    parser.add_argument("--status")
    parser.add_argument("--include-runs", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()
    records = list_records(
        workspace,
        kind=args.kind,
        status=args.status,
        include_runs=args.include_runs,
    )
    if args.json:
        print(json.dumps(records, indent=2, sort_keys=True))
    else:
        for item in records:
            print(f"{item['id']}\t{item['kind']}\t{item['status']}\t{item['path']}")
    return 0
