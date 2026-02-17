from __future__ import annotations

import argparse

from agent_loom.workspace.core import (
    lease_acquire,
    lease_list,
    lease_release,
    lease_renew,
    lease_show,
)
from agent_loom.workspace.guards import harness_root
from agent_loom.workspace.output import emit_result


def cmd_lease_acquire(args: argparse.Namespace) -> None:
    root = harness_root()
    res = lease_acquire(
        key=args.key,
        ttl=str(getattr(args, "ttl", "") or ""),
        force=bool(args.force),
        root=root,
    )
    emit_result(args, root, res)


def cmd_lease_release(args: argparse.Namespace) -> None:
    root = harness_root()
    res = lease_release(key=args.key, root=root)
    emit_result(args, root, res)


def cmd_lease_ls(args: argparse.Namespace) -> None:
    root = harness_root()
    res = lease_list(root=root)
    emit_result(args, root, res)


def cmd_lease_show(args: argparse.Namespace) -> None:
    root = harness_root()
    res = lease_show(key=args.key, root=root)
    emit_result(args, root, res)


def cmd_lease_renew(args: argparse.Namespace) -> None:
    root = harness_root()
    res = lease_renew(key=args.key, ttl=str(getattr(args, "ttl", "") or ""), root=root)
    emit_result(args, root, res)
