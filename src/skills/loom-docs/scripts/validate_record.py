#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.core import (
    find_workspace_root,
    issue,
    relative_to_workspace,
    scan_records,
    validate_record_path,
    validate_records,
)  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Loom records")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    workspace = find_workspace_root()
    if args.path:
        target = (
            (workspace / args.path).resolve()
            if not Path(args.path).is_absolute()
            else Path(args.path)
        )
        problems = (
            validate_record_path(target, workspace)
            if target.exists()
            else [issue(None, workspace, f"missing path: {args.path}")]
        )
    else:
        problems = validate_records(
            scan_records(workspace, include_runs=True), workspace
        )

    if args.json:
        print(json.dumps({"issues": problems}, indent=2))
    elif problems:
        for problem in problems:
            print(f"ERROR {problem['path']}: {problem['message']}")
    else:
        print("All checked records are structurally valid")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
