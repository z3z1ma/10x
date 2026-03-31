#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.core import find_workspace_root, summarize_workspace  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize Loom workspace state")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

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


if __name__ == "__main__":
    raise SystemExit(main())
