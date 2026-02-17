from __future__ import annotations

import argparse

from agent_loom.workspace.core import (
    components_refresh_index,
    deps_closure,
    deps_impacted,
    deps_show,
    deps_who_uses,
    services_refresh_index,
)
from agent_loom.workspace.guards import harness_root
from agent_loom.workspace.output import emit_result


def cmd_components_refresh_index(args: argparse.Namespace) -> None:
    root = harness_root()
    res = components_refresh_index(root=root)
    emit_result(args, root, res)


def cmd_services_refresh_index(args: argparse.Namespace) -> None:
    root = harness_root()
    res = services_refresh_index(root=root)
    emit_result(args, root, res)


def cmd_deps_show(args: argparse.Namespace) -> None:
    root = harness_root()
    res = deps_show(component=args.component, root=root)
    emit_result(args, root, res)


def cmd_deps_who_uses(args: argparse.Namespace) -> None:
    root = harness_root()
    res = deps_who_uses(component=args.component, root=root)
    emit_result(args, root, res)


def cmd_deps_closure(args: argparse.Namespace) -> None:
    root = harness_root()
    res = deps_closure(component=args.component, root=root)
    emit_result(args, root, res)


def cmd_deps_impacted(args: argparse.Namespace) -> None:
    root = harness_root()
    res = deps_impacted(component=args.component, root=root)
    emit_result(args, root, res)
