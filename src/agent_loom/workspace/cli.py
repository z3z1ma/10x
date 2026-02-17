from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence

from agent_loom.workspace.cli_harness import add_harness_parser
from agent_loom.workspace.cli_repo import add_repo_mode_parsers
from agent_loom.workspace.errors import WorkspaceError
from agent_loom.workspace.guards import harness_root
from agent_loom.workspace.output import emit_error
from agent_loom.workspace.repo.core import repo_root


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="loom workspace",
        description="Workspace + worktree tooling (repo mode + harness control plane)",
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit machine-readable JSON"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    add_repo_mode_parsers(sub)
    add_harness_parser(sub)
    return parser


def _error_root(args: argparse.Namespace) -> Path:
    cmd = str(getattr(args, "cmd", "") or "")
    if cmd == "harness":
        harness_cmd = str(getattr(args, "harness_cmd", "") or "")
        if harness_cmd == "init":
            root_arg = str(getattr(args, "root", "") or "").strip()
            if root_arg:
                return Path(root_arg).expanduser().resolve()
            return Path.cwd().resolve()
        return harness_root()
    return repo_root()


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv_list = list(argv) if argv is not None else list(sys.argv[1:])

    json_anywhere = "--json" in argv_list
    if json_anywhere:
        argv_list = [arg for arg in argv_list if arg != "--json"]

    parser = build_parser()

    try:
        args = parser.parse_args(argv_list)
    except SystemExit as exc:
        return int(exc.code or 0)

    if json_anywhere:
        args.json = True

    try:
        args.func(args)
        return 0
    except WorkspaceError as exc:
        if getattr(args, "json", False):
            try:
                root = _error_root(args)
            except Exception:
                root = Path.cwd().resolve()
            emit_error(args, root, exc)
            return 2
        print(str(exc), file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        if getattr(args, "json", False):
            emit_error(args, Path.cwd().resolve(), KeyboardInterrupt("Interrupted"))
            return 130
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
