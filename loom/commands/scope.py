"""Discover Loom repositories in the workspace."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core import (
    discover_repositories,
    find_workspace_root,
    resolve_repository_for_path,
)


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "scope",
        help="Discover Loom repositories in the workspace",
    )
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--path")
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()
    repos = discover_repositories(workspace)
    if args.path:
        owner = resolve_repository_for_path(workspace, Path(args.path))
        payload = {"repositories": repos, "owner": owner}
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(
                f"owner\t{owner['repository_id']}\t{owner['path']}\t{owner['worktree_id']}"
            )
        return 0
    if args.json:
        print(json.dumps({"repositories": repos}, indent=2))
    else:
        for repo in repos:
            print(f"{repo['repository_id']}\t{repo['path']}\t{repo['worktree_id']}")
    return 0
