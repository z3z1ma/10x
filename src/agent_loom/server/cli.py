from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional, Sequence

from agent_loom.core.git import git_repo_root
from agent_loom.server.app import create_app
from agent_loom.server.config import ServerConfig


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="server", description="Loom HTTP server")
    sub = p.add_subparsers(dest="cmd", required=True)

    start = sub.add_parser("start", help="Start the server")
    start.add_argument("--host", default="127.0.0.1", help="Bind address")
    start.add_argument("--port", type=int, default=8764, help="Bind port")
    start.add_argument(
        "--repo-root",
        default=".",
        help="Repo root (default: .; if inside git, resolves to git root)",
    )
    start.add_argument(
        "--workspace-mode",
        default="auto",
        choices=["auto", "repo", "poly"],
        help="Workspace mode for workspace endpoints (default: auto)",
    )
    start.add_argument(
        "--workspace-root",
        default="",
        help="Workspace root for poly mode (optional; auto-detected when possible)",
    )
    start.add_argument(
        "--enable-writes",
        action="store_true",
        help="Enable write endpoints (disabled by default)",
    )
    start.add_argument(
        "--token",
        default=os.environ.get("LOOM_SERVER_TOKEN", ""),
        help="Auth token for write endpoints (or set LOOM_SERVER_TOKEN)",
    )
    start.add_argument(
        "--require-token",
        action="store_true",
        help="Require a token even when bound to loopback",
    )
    return p


def _resolve_repo_root(arg: str) -> Path:
    p = Path(arg or ".").expanduser().resolve()
    gr = git_repo_root(p)
    return gr if gr is not None else p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)

    if args.cmd == "start":
        repo_root = _resolve_repo_root(str(args.repo_root))
        ws_root: Path | None = None
        if str(args.workspace_root or "").strip():
            ws_root = Path(str(args.workspace_root)).expanduser().resolve()

        cfg = ServerConfig(
            repo_root=repo_root,
            workspace_mode=str(args.workspace_mode or "auto"),
            workspace_root=ws_root,
            enable_writes=bool(args.enable_writes),
            token=str(args.token or ""),
            require_token=bool(args.require_token),
        )
        app = create_app(cfg=cfg)
        app.run(host=str(args.host), port=int(args.port), debug=False)
        return 0

    raise SystemExit(2)


__all__ = ["build_parser", "main"]
