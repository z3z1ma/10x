"""Loom CLI entrypoint."""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="loom",
        description="Loom workspace CLI — Markdown-first project management",
    )
    subparsers = parser.add_subparsers(dest="command")

    # Import and register all subcommands
    from loom.commands import (
        check_links,
        create,
        diagnose,
        link,
        list as list_cmd,
        memory,
        packet,
        scope,
        status,
        verify,
    )

    create.register(subparsers)
    diagnose.register(subparsers)
    check_links.register(subparsers)
    link.register(subparsers)
    list_cmd.register(subparsers)
    status.register(subparsers)
    scope.register(subparsers)
    verify.register(subparsers)
    packet.register(subparsers)
    memory.register(subparsers)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
