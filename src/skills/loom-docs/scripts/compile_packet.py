#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

from _loom_lib.core import compile_packet, find_workspace_root, relative_to_workspace  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile a Loom packet")
    parser.add_argument("target_ref")
    parser.add_argument("subsystem", choices=["ralph", "critique", "docs"])
    parser.add_argument(
        "--mode",
        choices=["execution", "review-only", "diagnostic", "reconciliation"],
        default="execution",
    )
    parser.add_argument(
        "--style", choices=["reference-first", "hermetic"], default="reference-first"
    )
    parser.add_argument("--allow-write-ref", action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args()

    workspace = find_workspace_root()
    output = Path(args.output) if args.output else None
    packet_path = compile_packet(
        workspace,
        args.target_ref,
        args.subsystem,
        args.mode,
        args.style,
        args.allow_write_ref,
        output,
    )
    print(relative_to_workspace(packet_path, workspace))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
