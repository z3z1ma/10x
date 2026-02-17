from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agent_loom.workspace.core import (
    add_repo,
    branch,
    context,
    deepen,
    list_repos,
    prime,
    remove_repo,
    snapshot,
    snapshot_diff,
    snapshot_restore,
    status,
    sync,
)
from agent_loom.workspace.guards import harness_root
from agent_loom.workspace.output import emit_ok, emit_result


def cmd_add(args: argparse.Namespace) -> None:
    root = harness_root()
    res = add_repo(
        name=args.name,
        remote=args.remote,
        default_branch=args.default_branch,
        shallow=bool(args.shallow),
        depth=int(args.depth),
        clone=bool(args.clone),
        force=bool(args.force),
        root=root,
    )
    emit_result(args, root, res)


def cmd_remove(args: argparse.Namespace) -> None:
    root = harness_root()
    res = remove_repo(
        name=args.name,
        delete_clone=bool(args.delete_clone),
        delete_component_md=bool(getattr(args, "delete_component_md", False)),
        confirm_delete=bool(args.yes_delete),
        root=root,
    )
    emit_result(args, root, res)


def cmd_list(args: argparse.Namespace) -> None:
    root = harness_root()
    res = list_repos(root=root)
    emit_result(args, root, res)


def cmd_sync(args: argparse.Namespace) -> None:
    root = harness_root()
    res = sync(
        repos=args.repos,
        sets=args.sets,
        tags=args.tags,
        clone=bool(args.clone),
        jobs=int(args.jobs),
        allow_all=bool(args.all),
        root=root,
    )
    emit_result(args, root, res)


def cmd_status(args: argparse.Namespace) -> None:
    root = harness_root()
    res = status(
        repos=args.repos,
        sets=args.sets,
        tags=args.tags,
        jobs=int(args.jobs),
        allow_all=bool(args.all),
        root=root,
    )
    emit_result(args, root, res)


def cmd_context(args: argparse.Namespace) -> None:
    root = harness_root()
    res = context(
        repos=args.repos,
        sets=args.sets,
        tags=args.tags,
        jobs=int(args.jobs),
        root=root,
    )
    emit_result(args, root, res)


def cmd_branch(args: argparse.Namespace) -> None:
    root = harness_root()
    res = branch(
        branch=args.branch,
        reset=bool(args.reset),
        allow_dirty=bool(args.allow_dirty),
        clone=bool(args.clone),
        base_ref=args.base_ref,
        refresh_index=bool(args.refresh_index),
        repos=args.repos,
        sets=args.sets,
        tags=args.tags,
        allow_all=bool(args.all),
        confirm_reset=bool(args.yes),
        root=root,
    )
    emit_result(args, root, res)


def cmd_snapshot_capture(args: argparse.Namespace) -> None:
    root = harness_root()
    res = snapshot(
        name=args.name,
        group=args.group,
        repos=args.repos,
        sets=args.sets,
        tags=args.tags,
        allow_all=bool(args.all),
        root=root,
    )
    emit_result(args, root, res)


def cmd_snapshot_diff(args: argparse.Namespace) -> None:
    root = harness_root()
    res = snapshot_diff(name=args.name, root=root)
    emit_result(args, root, res)


def cmd_snapshot_restore(args: argparse.Namespace) -> None:
    root = harness_root()
    res = snapshot_restore(
        name=args.name,
        confirm=bool(args.yes),
        force_clean=bool(args.force_clean),
        root=root,
    )
    emit_result(args, root, res)


def cmd_deepen(args: argparse.Namespace) -> None:
    root = harness_root()
    res = deepen(repo=args.repo, depth=int(args.depth), root=root)
    emit_result(args, root, res)


def cmd_prime(args: argparse.Namespace) -> None:
    res = prime()
    payload = res.payload
    root = Path.cwd().resolve()
    if getattr(args, "json", False):
        emit_ok(args, root, payload)
        return
    from agent_loom.workspace.render import render_prime_text

    sys.stdout.write(render_prime_text(payload))
