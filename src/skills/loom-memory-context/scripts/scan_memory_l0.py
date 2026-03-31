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
from _loom_lib.memory import EXPECTED_DOMAINS, collect_l0_rows  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List L0 summaries from Loom memory files"
    )
    parser.add_argument(
        "--domain",
        choices=["all", *EXPECTED_DOMAINS],
        default="all",
        help="Restrict output to one memory domain",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    workspace = find_workspace_root()
    rows = collect_l0_rows(workspace, domain=args.domain)
    if args.json:
        print(json.dumps(rows, indent=2, sort_keys=True))
    else:
        for row in rows:
            print(f"{row['path']}: {row['summary']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
