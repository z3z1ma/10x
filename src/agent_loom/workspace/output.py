from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from agent_loom.core.cli_output import emit_json, normalize_payload
from agent_loom.core.time import now_iso
from agent_loom.workspace.models import ComponentsRefreshIndexResult
from agent_loom.workspace.render import render_services_index_text, render_text


def cmd_name(args: argparse.Namespace) -> str:
    top = getattr(args, "cmd", "") or ""
    if top == "harness":
        cmd = getattr(args, "harness_cmd", "") or ""
        if cmd == "worktree":
            cmd = f"worktree {getattr(args, 'worktree_cmd', '')}".strip()
        elif cmd == "snapshot":
            cmd = f"snapshot {getattr(args, 'snapshot_cmd', '')}".strip()
        elif cmd == "repo":
            cmd = f"repo {getattr(args, 'repo_cmd', '')}".strip()
        elif cmd == "set":
            cmd = f"set {getattr(args, 'set_cmd', '')}".strip()
        elif cmd == "lease":
            cmd = f"lease {getattr(args, 'lease_cmd', '')}".strip()
        elif cmd in {"components", "services"}:
            cmd = f"{cmd} {getattr(args, 'components_cmd', '')}".strip()
        elif cmd == "deps":
            cmd = f"deps {getattr(args, 'deps_cmd', '')}".strip()
        elif cmd == "sandbox":
            cmd = f"sandbox {getattr(args, 'sandbox_cmd', '')}".strip()
        elif cmd == "cleanup":
            cmd = f"cleanup {getattr(args, 'cleanup_cmd', '')}".strip()
        elif cmd == "impact":
            cmd = f"impact {getattr(args, 'impact_cmd', '')}".strip()
        return f"{top} {cmd}".strip()

    cmd = top
    if cmd == "worktree":
        cmd = f"worktree {getattr(args, 'worktree_cmd', '')}".strip()
    elif cmd == "snapshot":
        cmd = f"snapshot {getattr(args, 'snapshot_cmd', '')}".strip()
    elif cmd == "cleanup":
        cmd = f"cleanup {getattr(args, 'cleanup_cmd', '')}".strip()
    elif cmd == "sandbox":
        cmd = f"sandbox {getattr(args, 'sandbox_cmd', '')}".strip()
    elif cmd == "merge":
        cmd = f"merge {getattr(args, 'merge_cmd', '')}".strip()
    return cmd


def emit_ok(args: argparse.Namespace, root: Path, data: Any = None) -> None:
    emit_json(
        {
            "ok": True,
            "cmd": cmd_name(args),
            "root": str(root.resolve()),
            "data": normalize_payload(data),
            "meta": {"generated_at": now_iso()},
        },
        indent=2,
    )


def emit_error(
    args: argparse.Namespace,
    root: Path | None,
    err: BaseException,
) -> None:
    emit_json(
        {
            "ok": False,
            "cmd": cmd_name(args),
            "root": str(root.resolve()) if root else None,
            "error": {"type": type(err).__name__, "message": str(err)},
            "meta": {"generated_at": now_iso()},
        },
        indent=2,
    )


def emit_result(args: argparse.Namespace, root: Path, result: Any) -> None:
    if getattr(args, "json", False):
        emit_ok(args, root, result)
        return

    if isinstance(result, ComponentsRefreshIndexResult) and bool(
        getattr(args, "print", False)
    ):
        sys.stdout.write(render_services_index_text(result.index))
        return

    sys.stdout.write(render_text(result))


__all__ = ["cmd_name", "emit_error", "emit_ok", "emit_result"]
