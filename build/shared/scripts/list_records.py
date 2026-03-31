#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.core import find_workspace_root  # noqa: E402
from _loom_lib.records import list_records  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="List Loom records")
    parser.add_argument("--kind")
    parser.add_argument("--status")
    parser.add_argument("--include-runs", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

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


if __name__ == "__main__":
    raise SystemExit(main())
