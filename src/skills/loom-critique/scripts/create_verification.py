#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.cli import (  # noqa: E402
    add_scope_arguments,
    collect_assignments,
    collect_link_assignments,
    resolve_record_scope_args,
)
from _loom_lib.core import find_workspace_root, relative_to_workspace  # noqa: E402
from _loom_lib.records import create_verification_record  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a Loom verification record",
        epilog=(
            "Examples: --link ticket:0005 --link spec:loom-repository-bootstrap "
            "or --link ticket=ticket:0005"
        ),
    )
    parser.add_argument("slug")
    parser.add_argument("--title")
    parser.add_argument("--link", action="append", default=[])
    parser.add_argument("--section", action="append", default=[])
    add_scope_arguments(parser)
    args = parser.parse_args()

    workspace = find_workspace_root()
    sections = {
        heading: "\n".join(values)
        for heading, values in collect_assignments(
            args.section, label="section assignment"
        ).items()
    }
    path = create_verification_record(
        workspace,
        args.slug,
        title=args.title,
        links=collect_link_assignments(args.link, label="link assignment"),
        sections=sections or None,
        repository_scope=resolve_record_scope_args(args, workspace),
    )
    print(relative_to_workspace(path, workspace))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
