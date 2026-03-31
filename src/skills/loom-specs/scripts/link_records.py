#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.cli import collect_link_assignments  # noqa: E402
from _loom_lib.core import find_workspace_root, relative_to_workspace  # noqa: E402
from _loom_lib.records import mutate_links  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add or remove Loom record links",
        epilog=(
            "Examples: --add ticket:0004 --add plan:bootstrap-repository "
            "or --add ticket=ticket:0004. constitution:main may only have links removed."
        ),
    )
    parser.add_argument("target")
    parser.add_argument("--add", action="append", default=[])
    parser.add_argument("--remove", action="append", default=[])
    args = parser.parse_args()

    if not args.add and not args.remove:
        raise SystemExit("Provide at least one --add or --remove assignment")

    workspace = find_workspace_root()
    path = mutate_links(
        workspace,
        args.target,
        additions=collect_link_assignments(args.add, label="link assignment"),
        removals=collect_link_assignments(args.remove, label="link assignment"),
    )
    print(relative_to_workspace(path, workspace))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
