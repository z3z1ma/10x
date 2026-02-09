from __future__ import annotations

import argparse
import contextlib
import dataclasses
import json
import os
import sys
from importlib import resources
from pathlib import Path
from typing import Optional, Sequence

from agent_loom.compound.install import install_opencode
from agent_loom.compound.install import COMPOUND_PACK_ID
from agent_loom.compound.mirror import sync_claude_skills_mirror
from agent_loom.compound.scaffold import require_scaffold_installed
from agent_loom.compound.sync import sync as compound_sync
from agent_loom.core.git import git_repo_root
from agent_loom.pack.diff import any_pack_diffs, diff_pack_files


class ArgParseError(RuntimeError):
    pass


class CompoundArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # noqa: D401
        raise ArgParseError(message)


def _emit_json(obj: object) -> None:
    sys.stdout.write(json.dumps(obj, sort_keys=True) + "\n")


@contextlib.contextmanager
def _chdir(p: Path):
    prev = Path.cwd()
    os.chdir(p)
    try:
        yield
    finally:
        os.chdir(prev)


def _resolve_repo_root(repo: Optional[str]) -> Path:
    cr = str(os.environ.get("COMPOUND_ROOT") or "").strip()
    if cr:
        p = Path(cr).expanduser().resolve()
        if p.exists() and p.is_dir():
            return p

    start = Path(repo).expanduser().resolve() if repo else Path.cwd().resolve()
    return (git_repo_root(start) or start).resolve()


def _resolve_init_dest(dest: Optional[str]) -> Path:
    # Make `loom compound init` safe from any subdirectory.
    # If dest is '.' (default) and we're inside a git repo, install into repo root.
    d = str(dest or ".").strip() or "."
    if d == ".":
        gr = git_repo_root(Path.cwd().resolve())
        if gr is not None:
            return gr.resolve()
    return Path(d).expanduser().resolve()


def _infer_json(argv: Sequence[str]) -> bool:
    return any(str(tok) == "--json" or str(tok).startswith("--json=") for tok in argv)


def build_parser() -> argparse.ArgumentParser:
    p = CompoundArgumentParser(prog="compound", description="Loom compound integration")
    sub = p.add_subparsers(dest="cmd", required=True)

    init = sub.add_parser(
        "init",
        help="Install/upgrade the .opencode compound plugin template into a repo",
    )
    init.add_argument(
        "--dest",
        default=".",
        help="Destination project directory (default: repo root if in git, else .)",
    )
    init.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    init.add_argument(
        "--force",
        action="store_true",
        help="Overwrite scaffold files (.opencode plugin/commands/agents/prompts). Never overwrites skills or memory.",
    )
    init.add_argument(
        "--diff",
        action="store_true",
        help="Show diffs for skipped scaffold files (e.g. AGENTS.md)",
    )
    init.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    sync = sub.add_parser(
        "sync",
        help="Stage+commit compound learning changes (skills, memory, agents, LOOM docs)",
    )
    sync.add_argument(
        "-m",
        "--message",
        default="chore: compound",
        help="Commit message (default: chore: compound)",
    )
    sync.add_argument(
        "--repo",
        default=None,
        help="Path inside repo (defaults to CWD; resolves git root)",
    )
    sync.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    refresh = sub.add_parser(
        "refresh",
        help="Regenerate derived compound artifacts (LOOM.md, ROADMAP.md, INSTINCTS.md) and mirrors",
    )
    refresh.add_argument(
        "--repo",
        default=None,
        help="Path inside repo (defaults to CWD; resolves git root)",
    )
    refresh.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    learn = sub.add_parser(
        "learn",
        help="Seal an Episode and apply proposals (records a Decision + blobs for no-loss evidence)",
    )
    learn.add_argument(
        "--repo",
        default=None,
        help="Path inside repo (defaults to CWD; resolves git root)",
    )
    learn.add_argument(
        "--auto",
        action="store_true",
        help="Auto mode (thresholded, quiet-friendly; intended for background use)",
    )
    learn.add_argument(
        "--no-ai",
        action="store_true",
        help="Do not accept proposals; only package an Episode and advance cursors",
    )
    learn.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without writing files",
    )
    learn.add_argument(
        "--proposals",
        default=None,
        help="JSON proposals payload. If omitted and stdin is piped, stdin is used.",
    )
    learn.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    prime = sub.add_parser(
        "prime",
        help="Print the Compound cookbook (module README)",
    )
    prime.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    raw_argv = list(argv) if argv is not None else sys.argv[1:]
    try:
        args = build_parser().parse_args(
            list(raw_argv) if raw_argv is not None else None
        )
    except SystemExit as e:
        return int(e.code or 0)
    except ArgParseError as e:
        payload = {
            "ok": False,
            "code": "ARGPARSE",
            "error": str(e),
            "hint": "Run: loom compound -h",
        }
        if _infer_json(raw_argv):
            _emit_json(payload)
        else:
            sys.stderr.write(f"Error: {e}\n")
            sys.stderr.write("Run: loom compound -h\n")
        return 2

    if args.cmd == "init":
        try:
            res = install_opencode(
                dest=_resolve_init_dest(getattr(args, "dest", None)),
                dry_run=bool(args.dry_run),
                force=bool(getattr(args, "force", False)),
            )
            payload = {
                "ok": True,
                "dest": res.dest,
                "dry_run": res.dry_run,
                "wrote": res.wrote,
                "skipped": res.skipped,
                "warnings": res.warnings,
            }
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write(f"installed into: {res.dest}\n")
                sys.stdout.write(f"pack: {COMPOUND_PACK_ID}\n")
                sys.stdout.write("note: commit .loom/pack/lock.json\n")
                if res.dry_run:
                    sys.stdout.write("(dry-run)\n")
                if res.wrote:
                    sys.stdout.write("wrote:\n")
                    for p in res.wrote:
                        sys.stdout.write(f"- {p}\n")
                if res.skipped:
                    sys.stdout.write("skipped:\n")
                    for p in res.skipped:
                        sys.stdout.write(f"- {p}\n")
                if res.warnings:
                    sys.stdout.write("warnings:\n")
                    for w in res.warnings:
                        sys.stdout.write(f"- {w}\n")

                repo_root = Path(res.dest).resolve()
                diff_targets = ["AGENTS.md"]
                if not bool(getattr(args, "diff", False)) and any_pack_diffs(
                    repo_root=repo_root, pack_id=COMPOUND_PACK_ID, relpaths=diff_targets
                ):
                    sys.stdout.write(
                        "note: AGENTS.md differs from Loom scaffold; rerun with --diff to view\n"
                    )

                if bool(getattr(args, "diff", False)) and not bool(res.dry_run):
                    diffs = diff_pack_files(
                        repo_root=repo_root,
                        pack_id=COMPOUND_PACK_ID,
                        relpaths=diff_targets,
                        max_lines=400,
                    )
                    for d in diffs:
                        sys.stdout.write(f"diff (skipped): {d.relpath}\n")
                        sys.stdout.write(d.diff)
            return 0
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "sync":
        try:
            res = compound_sync(
                repo=_resolve_repo_root(getattr(args, "repo", None)),
                message=str(args.message or ""),
            )
            payload = {"ok": True, **dataclasses.asdict(res)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                if not res.committed:
                    sys.stdout.write("compound sync: noop\n")
                else:
                    sys.stdout.write(
                        f"compound sync: committed {res.count} file(s) sha={res.sha[:8]}\n"
                    )
            return 0
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "refresh":
        repo = _resolve_repo_root(getattr(args, "repo", None))
        try:
            require_scaffold_installed(repo)
            from agent_loom.compound.docs import sync_docs

            with _chdir(repo):
                sync_docs(root=repo)
                mirror = sync_claude_skills_mirror(
                    root=repo,
                    enabled=(str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0"),
                )
            payload = {
                "ok": True,
                "mirror": dataclasses.asdict(mirror),
            }
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write("compound refresh: refreshed derived docs\n")
            return 0
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "learn":
        repo = _resolve_repo_root(getattr(args, "repo", None))
        try:
            require_scaffold_installed(repo)
            from agent_loom.compound.engine import run_compound

            proposals = getattr(args, "proposals", None)
            if proposals is None:
                proposals = (
                    sys.stdin.read()
                    if sys.stdin is not None and not sys.stdin.isatty()
                    else None
                )

            res = run_compound(
                root=repo,
                proposals_json=str(proposals) if proposals is not None else None,
                auto=bool(getattr(args, "auto", False)),
                no_ai=bool(getattr(args, "no_ai", False)),
                dry_run=bool(getattr(args, "dry_run", False)),
                mirror_claude=(
                    str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0"
                ),
            )
            payload = dataclasses.asdict(res)
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write(json.dumps(payload, indent=2) + "\n")
            return 0
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "prime":
        traversable = resources.files("agent_loom.compound").joinpath("README.md")
        with resources.as_file(traversable) as p:
            md = p.read_text(encoding="utf-8", errors="replace")
        payload = {"ok": True, "markdown": md}
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(str(md).rstrip() + "\n")
        return 0

    return 2


__all__ = [
    "build_parser",
    "main",
]
