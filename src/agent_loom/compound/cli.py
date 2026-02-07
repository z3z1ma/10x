from __future__ import annotations

import argparse
import contextlib
import dataclasses
import json
import os
import sys
from pathlib import Path
from typing import Literal, Optional, Sequence, cast

from agent_loom.compound.install import install_opencode
from agent_loom.compound.mirror import sync_claude_skills_mirror
from agent_loom.compound.observations import count_observations, read_observations_tail
from agent_loom.compound.paths import compound_paths
from agent_loom.compound.prime import prime_rules
from agent_loom.compound.roadmap import append_changelog
from agent_loom.compound.scaffold import (
    check_scaffold_installed,
    require_scaffold_installed,
)
from agent_loom.compound.skills import write_or_update_skill
from agent_loom.compound.sync import sync as compound_sync


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


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="compound", description="Loom compound integration"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    init = sub.add_parser(
        "init",
        help="Install/upgrade the .opencode compound plugin template into a repo",
    )
    init.add_argument(
        "--dest",
        default=".",
        help="Destination project directory (default: .)",
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
        default=".",
        help="Repo root (default: .)",
    )
    sync.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    refresh = sub.add_parser(
        "refresh",
        help="Refresh derived compound docs (LOOM_CONTEXT/ROADMAP/INSTINCTS index) and mirrors",
    )
    refresh.add_argument(
        "--repo",
        default=".",
        help="Repo root (default: .)",
    )
    refresh.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    update = sub.add_parser(
        "update",
        help="Update derived compound artifacts (docs + rules + mirrors)",
    )
    update.add_argument(
        "--repo",
        default=".",
        help="Repo root (default: .)",
    )
    update.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    prime = sub.add_parser(
        "prime",
        help="Write subsystem cookbooks into .opencode/rules/*.md",
    )
    prime.add_argument(
        "--repo",
        default=".",
        help="Repo root (default: .)",
    )
    prime.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    status = sub.add_parser(
        "status",
        help="Show compound status (skills/instincts/observations + config)",
    )
    status.add_argument(
        "--repo",
        default=".",
        help="Repo root (default: .)",
    )
    status.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )

    obs = sub.add_parser(
        "observations",
        help="Observations utilities (read-only)",
    )
    obs_sub = obs.add_subparsers(dest="obs_cmd", required=True)

    obs_tail = obs_sub.add_parser("tail", help="Show the last N observation records")
    obs_tail.add_argument("--repo", default=".", help="Repo root (default: .)")
    obs_tail.add_argument("--n", type=int, default=30, help="Number of records")
    obs_tail.add_argument("--json", action="store_true", help="Emit JSON")

    skill = sub.add_parser("skill", help="Skill operations")
    skill_sub = skill.add_subparsers(dest="skill_cmd", required=True)

    skill_upsert = skill_sub.add_parser("upsert", help="Create/update a skill")
    skill_upsert.add_argument("name")
    skill_upsert.add_argument("--repo", default=".", help="Repo root (default: .)")
    skill_upsert.add_argument("--description", default="", help="Skill description")
    skill_upsert.add_argument(
        "--body",
        default=None,
        help="Full managed body. If omitted: read stdin.",
    )
    skill_upsert.add_argument("--json", action="store_true", help="Emit JSON")

    instinct = sub.add_parser("instinct", help="Instinct operations")
    instinct_sub = instinct.add_subparsers(dest="instinct_cmd", required=True)

    instinct_upsert = instinct_sub.add_parser(
        "upsert", help="Create/update an instinct"
    )
    instinct_upsert.add_argument("operation", choices=["create", "update"])
    instinct_upsert.add_argument("id")
    instinct_upsert.add_argument("--repo", default=".", help="Repo root (default: .)")
    instinct_upsert.add_argument("--title", default=None)
    instinct_upsert.add_argument("--trigger", default=None)
    instinct_upsert.add_argument("--action", default=None)
    instinct_upsert.add_argument("--confidence", type=float, default=None)
    instinct_upsert.add_argument("--confidence-delta", type=float, default=None)
    instinct_upsert.add_argument("--evidence-note", default=None)
    instinct_upsert.add_argument("--session-id", default=None)
    instinct_upsert.add_argument("--json", action="store_true", help="Emit JSON")

    instinct_list = instinct_sub.add_parser(
        "list", help="List instincts (top by confidence)"
    )
    instinct_list.add_argument("--repo", default=".", help="Repo root (default: .)")
    instinct_list.add_argument("--n", type=int, default=30)
    instinct_list.add_argument("--json", action="store_true", help="Emit JSON")

    docblock = sub.add_parser("docblock", help="Doc-block operations")
    docblock_sub = docblock.add_subparsers(dest="docblock_cmd", required=True)
    docblock_upsert = docblock_sub.add_parser(
        "upsert", help="Upsert an allowed AI-managed doc block"
    )
    docblock_upsert.add_argument("--repo", default=".", help="Repo root (default: .)")
    docblock_upsert.add_argument("--file", required=True)
    docblock_upsert.add_argument("--id", required=True)
    docblock_upsert.add_argument(
        "--content",
        default=None,
        help="Block content. If omitted: read stdin.",
    )
    docblock_upsert.add_argument("--json", action="store_true", help="Emit JSON")

    changelog = sub.add_parser("changelog", help="Changelog operations")
    changelog_sub = changelog.add_subparsers(dest="changelog_cmd", required=True)
    changelog_append = changelog_sub.add_parser(
        "append", help="Append a short entry to LOOM_ROADMAP.md"
    )
    changelog_append.add_argument("--repo", default=".", help="Repo root (default: .)")
    changelog_append.add_argument(
        "--note", default=None, help="Note text. If omitted: read stdin."
    )
    changelog_append.add_argument("--json", action="store_true", help="Emit JSON")

    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)

    if args.cmd == "init":
        res = install_opencode(
            dest=Path(args.dest),
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
        return 0

    if args.cmd == "sync":
        try:
            res = compound_sync(
                repo=Path(args.repo).resolve(), message=str(args.message or "")
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
        repo = Path(args.repo).resolve()
        try:
            require_scaffold_installed(repo)
            from agent_loom.compound.docs import sync_docs

            with _chdir(repo):
                sync_docs(root=repo)
                mirror = sync_claude_skills_mirror(
                    root=repo,
                    enabled=(str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0"),
                )
            payload = {"ok": True, "mirror": dataclasses.asdict(mirror)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write("compound refresh: ok\n")
            return 0
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "update":
        repo = Path(args.repo).resolve()
        try:
            require_scaffold_installed(repo)
            from agent_loom.compound.docs import sync_docs

            with _chdir(repo):
                sync_docs(root=repo)
                prime = prime_rules(root=repo)
                mirror = sync_claude_skills_mirror(
                    root=repo,
                    enabled=(str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0"),
                )
            payload = {
                "ok": bool(prime.ok),
                "prime": dataclasses.asdict(prime),
                "mirror": dataclasses.asdict(mirror),
            }
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write(
                    f"compound update: wrote {len(prime.wrote)} rules file(s)\n"
                )
            return 0 if prime.ok else 1
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "prime":
        repo = Path(args.repo).resolve()
        try:
            with _chdir(repo):
                res = prime_rules(root=repo)
            payload = {"ok": bool(res.ok), **dataclasses.asdict(res)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stdout.write(f"compound prime: wrote {len(res.wrote)} file(s)\n")
                for w in res.warnings:
                    sys.stdout.write(f"warning: {w}\n")
            return 0 if res.ok else 1
        except Exception as e:
            payload = {"ok": False, "error": str(e)}
            if bool(getattr(args, "json", False)):
                _emit_json(payload)
            else:
                sys.stderr.write(f"Error: {e}\n")
            return 1

    if args.cmd == "status":
        repo = Path(args.repo).resolve()
        paths = compound_paths(repo)
        scaffold = check_scaffold_installed(repo)
        obs = count_observations(paths.observations_file)

        # count skills
        skills = 0
        if paths.skills_dir.exists() and paths.skills_dir.is_dir():
            for p in sorted(paths.skills_dir.iterdir()):
                if not p.is_dir():
                    continue
                if (p / "SKILL.md").exists():
                    skills += 1

        from agent_loom.compound.instincts import load_instincts

        instincts = load_instincts(paths.instincts_file)

        payload = {
            "ok": True,
            "repo": str(repo),
            "scaffold_ok": bool(scaffold.ok),
            "scaffold_missing": scaffold.missing,
            "skills": skills,
            "instincts": len(instincts.instincts),
            "observations": obs.count,
            "observations_tail_sha256": obs.tail_sha256,
            "mirror_claude": (
                str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0"
            ),
        }
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
        return 0

    if args.cmd == "observations" and args.obs_cmd == "tail":
        repo = Path(args.repo).resolve()
        paths = compound_paths(repo)
        tail = read_observations_tail(paths.observations_file, max_lines=int(args.n))
        if bool(getattr(args, "json", False)):
            _emit_json(tail)
        else:
            sys.stdout.write(json.dumps(tail, indent=2) + "\n")
        return 0

    if args.cmd == "skill" and args.skill_cmd == "upsert":
        repo = Path(args.repo).resolve()
        require_scaffold_installed(repo)

        body = getattr(args, "body", None)
        if body is None:
            body = (
                sys.stdin.read()
                if sys.stdin is not None and not sys.stdin.isatty()
                else ""
            )
        action, path = write_or_update_skill(
            skills_dir=(repo / ".opencode" / "skills"),
            name=str(args.name),
            description=str(args.description or ""),
            body=str(body or ""),
            mirror_claude_dir=(repo / ".claude" / "skills")
            if (str(os.environ.get("COMPOUND_MIRROR_CLAUDE", "1")) != "0")
            else None,
        )
        payload = {"ok": True, "action": action, "path": str(path)}
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(f"compound skill upsert: {action} {path}\n")
        return 0

    if args.cmd == "instinct" and args.instinct_cmd == "upsert":
        repo = Path(args.repo).resolve()
        require_scaffold_installed(repo)
        from agent_loom.compound.instincts import (
            instinct_upsert,
            load_instincts,
            save_instincts,
        )

        store = load_instincts(repo / ".opencode" / "memory" / "instincts.json")
        delta = instinct_upsert(
            store,
            operation=cast(Literal["create", "update"], args.operation),
            ident=str(args.id),
            title=args.title,
            trigger=args.trigger,
            action=args.action,
            confidence=args.confidence,
            confidence_delta=getattr(args, "confidence_delta", None),
            evidence_note=getattr(args, "evidence_note", None),
            session_id=getattr(args, "session_id", None),
        )
        if delta.created or delta.updated:
            save_instincts(repo / ".opencode" / "memory" / "instincts.json", store)
            # keep derived index in sync
            from agent_loom.compound.docs import sync_instincts_markdown

            sync_instincts_markdown(root=repo, store=store)
        payload = {"ok": True, **dataclasses.asdict(delta)}
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
        return 0

    if args.cmd == "instinct" and args.instinct_cmd == "list":
        repo = Path(args.repo).resolve()
        from agent_loom.compound.instincts import load_instincts

        store = load_instincts(repo / ".opencode" / "memory" / "instincts.json")
        active = [i for i in store.instincts if i.status == "active"]
        active.sort(key=lambda x: float(x.confidence or 0.0), reverse=True)
        active = active[: int(args.n)]
        payload = [dataclasses.asdict(i) for i in active]
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
        return 0

    if args.cmd == "docblock" and args.docblock_cmd == "upsert":
        repo = Path(args.repo).resolve()
        require_scaffold_installed(repo)
        from agent_loom.compound.docblocks import docblock_upsert

        content = getattr(args, "content", None)
        if content is None:
            content = (
                sys.stdin.read()
                if sys.stdin is not None and not sys.stdin.isatty()
                else ""
            )
        res = docblock_upsert(
            root=repo, file=str(args.file), block_id=str(args.id), content=str(content)
        )
        payload = {"ok": bool(res.ok), "changed": bool(res.changed)}
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
        return 0

    if args.cmd == "changelog" and args.changelog_cmd == "append":
        repo = Path(args.repo).resolve()
        require_scaffold_installed(repo)
        note = getattr(args, "note", None)
        if note is None:
            note = (
                sys.stdin.read()
                if sys.stdin is not None and not sys.stdin.isatty()
                else ""
            )
        changed = append_changelog(
            roadmap_path=(repo / "LOOM_ROADMAP.md"), note=str(note)
        )
        payload = {"ok": True, "changed": bool(changed)}
        if bool(getattr(args, "json", False)):
            _emit_json(payload)
        else:
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
        return 0

    raise SystemExit(2)


__all__ = [
    "build_parser",
    "main",
]
