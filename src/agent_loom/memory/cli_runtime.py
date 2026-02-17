from __future__ import annotations

import argparse
import json
import select
import sys
from dataclasses import asdict, dataclass, is_dataclass
from pathlib import Path
from typing import Any, Optional, Sequence

from agent_loom.memory.cli_parser import (
    _effective_format,
    _infer_error_format,
    _normalize_argv,
    _parse_args,
)
from agent_loom.memory.core import (
    add,
    around,
    edit,
    forget,
    grep,
    init,
    janitor,
    link,
    list_recent,
    open_note,
    prime,
    recall,
    reindex,
    show,
    timeline,
)
from agent_loom.memory.errors import MemoryError
from agent_loom.memory.models import (
    AddResult,
    EditResult,
    JanitorFixResult,
    JanitorReportResult,
    LinkBacklinksResult,
    LinkGraphResult,
    LinkNeighborsResult,
    LinkSuggestResult,
    LinkValidateResult,
    PrimeResult,
    RecallResult,
)
from agent_loom.memory.recall import print_index_warnings
from agent_loom.memory.utils import emit_error, format_json, read_all_stdin_text
from agent_loom.memory.vault import resolve_vault_root, vault_paths


def _stdin_is_ready() -> bool:
    if sys.stdin.isatty():
        return False
    try:
        r, _w, _x = select.select([sys.stdin], [], [], 0)
        return bool(r)
    except Exception:
        # In-memory streams used in tests support getvalue(); non-readable capture
        # wrappers should not be treated as ready.
        return bool(hasattr(sys.stdin, "getvalue"))


def emit(payload: Any, fmt: str) -> None:
    if fmt == "json":
        print(format_json(payload))
        return
    if fmt == "jsonl":
        if isinstance(payload, list):
            for it in payload:
                print(json.dumps(it, ensure_ascii=False, sort_keys=True))
        else:
            print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        return
    if isinstance(payload, str):
        print(payload)
        return
    print(format_json(payload))


def render_link_validate(rows: list[dict[str, Any]], *, fmt: str) -> str:
    if fmt == "md":
        lines = []
        for r in rows:
            lines.append(
                f"- {r.get('src_id')} -> {r.get('dst_raw')} ({r.get('resolution')}, {r.get('style')})"
            )
        return "\n".join(lines).rstrip() + "\n"
    if fmt == "prompt":
        lines = ["Broken/ambiguous memo links:", ""]
        for r in rows:
            lines.append(
                f"- {r.get('src_id')} -> {r.get('dst_raw')} ({r.get('resolution')}, {r.get('style')})"
            )
        return "\n".join(lines).rstrip() + "\n"

    lines2: list[str] = []
    for r in rows:
        lines2.append(
            f"{r.get('src_id')}\t{r.get('dst_raw')}\t{r.get('resolution')}\t{r.get('style')}"
        )
    return "\n".join(lines2).rstrip() + "\n"


def render_recall_results(results: list[dict[str, Any]], *, fmt: str) -> str:
    if fmt == "md":
        lines: list[str] = []
        for r in results:
            nid = r.get("id")
            title = (r.get("title") or "").strip()
            preview = (r.get("preview") or "").strip()
            lines.append(f"- [[{nid}]] {title} - {preview}")
        return "\n".join(lines).rstrip() + "\n"
    if fmt == "prompt":
        lines = ["Relevant memory notes:", ""]
        for r in results:
            title = (r.get("title") or "").strip()
            snippet = None
            why = r.get("why")
            if isinstance(why, dict):
                snippet = (why.get("fts_snippet") or "").strip() or None
            preview = (r.get("preview") or "").strip()
            lines.append(f"- {title} (`{r.get('id')}`)")
            lines.append(f"  {snippet or preview}")
        return "\n".join(lines).rstrip() + "\n"

    lines2: list[str] = []
    for r in results:
        nid = r.get("id")
        title = (r.get("title") or "").strip()
        updated_at = (r.get("updated_at") or "").strip()
        preview = (r.get("preview") or "").strip()
        lines2.append(f"{nid}\t{updated_at}\t{title}\t{preview}")
    return "\n".join(lines2).rstrip() + "\n"


def render_mutation_result(result: dict[str, Any], *, fmt: str) -> str:
    rid = str(result.get("id") or "")
    path = str(result.get("path") or "")
    action = "updated" if bool(result.get("updated")) else "created"
    lines = [f"Memory note {action}: {rid}"]
    if path:
        lines.append(f"path: {path}")

    hs = result.get("hydration_summary") or {}
    if isinstance(hs, dict):
        rewrites = int(hs.get("rewrites") or 0)
        created = int(hs.get("created_notes") or 0)
        seeded = int(hs.get("seeded_notes") or 0)
        ambiguous = int(hs.get("ambiguous") or 0)
        lines.append(
            "hydration: "
            f"rewrites={rewrites} created={created} seeded={seeded} ambiguous={ambiguous}"
        )

    actions = result.get("next_actions") or []
    if isinstance(actions, list) and actions:
        lines.append("next:")
        for item in actions[:5]:
            s = str(item or "").strip()
            if s:
                lines.append(f"- {s}")

    if fmt == "md":
        if len(lines) > 1 and lines[1].startswith("path: "):
            lines[1] = f"- {lines[1]}"
        out: list[str] = [f"- {lines[0]}"]
        for ln in lines[1:]:
            out.append(ln if ln.startswith("-") else f"- {ln}")
        return "\n".join(out).rstrip() + "\n"

    if fmt == "prompt":
        return "\n".join(lines).rstrip() + "\n"

    return "\n".join(lines).rstrip() + "\n"


def payload_for(obj: Any, *, fmt: str) -> Any:
    if isinstance(obj, (AddResult, EditResult)):
        payload = asdict(obj)
        if fmt in ("text", "md", "prompt"):
            return render_mutation_result(payload, fmt=fmt)
        return payload
    if isinstance(obj, PrimeResult):
        if fmt in ("json", "jsonl"):
            return obj.payload
        text = str(obj.payload.get("markdown") or "")
        if text:
            return text.rstrip() + "\n"
        return ""
    if isinstance(obj, RecallResult):
        if obj.context_text:
            return obj.context_text
        items = [asdict(it) for it in obj.items]
        if fmt in ("text", "md", "prompt"):
            return render_recall_results(items, fmt=fmt)
        return items
    if isinstance(obj, LinkValidateResult):
        rows = [asdict(r) for r in obj.rows]
        if fmt in ("text", "md", "prompt"):
            return render_link_validate(rows, fmt=fmt)
        return rows
    if isinstance(obj, LinkBacklinksResult):
        return [asdict(b) for b in obj.backlinks]
    if isinstance(obj, LinkGraphResult):
        return [asdict(e) for e in obj.edges]
    if isinstance(obj, LinkNeighborsResult):
        if obj.nodes is not None:
            return {"id": obj.id, "k": obj.k, "nodes": obj.nodes}
        if obj.neighbors is not None:
            return obj.neighbors
        return {}
    if isinstance(obj, LinkSuggestResult):
        items = [asdict(it) for it in obj.suggestions]
        if fmt == "md":
            lines = [
                f"- [[{it['id']}]] ({it.get('score')}) {it.get('title')}"
                for it in items
            ]
            return "\n".join(lines).rstrip() + "\n" if lines else ""
        if fmt == "prompt":
            lines = ["Suggested related notes:", ""]
            for it in items:
                lines.append(f"- [[{it['id']}]] ({it.get('score')}) {it.get('title')}")
            return "\n".join(lines).rstrip() + "\n" if items else ""
        if fmt == "text":
            lines2: list[str] = []
            for it in items:
                lines2.append(
                    f"{it.get('id')}\t{it.get('score')}\t{it.get('updated_at')}\t{(it.get('title') or '').strip()}"
                )
            return "\n".join(lines2).rstrip() + "\n" if items else ""
        return items
    if isinstance(obj, (JanitorReportResult, JanitorFixResult)):
        return asdict(obj)
    if is_dataclass(obj) and not isinstance(obj, type):
        return asdict(obj)
    return obj


@dataclass(frozen=True)
class _EditRunOptions:
    note_id: str
    title: str | None
    visibility: str | None
    status: str | None
    tag: list[str]
    remove_tag: list[str]
    clear_tags: bool
    alias: list[str]
    remove_alias: list[str]
    clear_aliases: bool
    link: list[str]
    remove_link: list[str]
    clear_links: bool
    related: list[str]
    scope: list[str]
    command: str | None
    remove_scope: list[str]
    clear_scopes: bool
    allow_missing_scopes: bool
    body: str | None
    append: str | None
    interactive: bool


def _emit_and_ok(payload: Any, *, fmt: str) -> int:
    emit(payload, fmt)
    return 0


def _ensure_vault_ready(args: argparse.Namespace) -> None:
    vp = vault_paths(resolve_vault_root(str(args.vault), cwd=Path.cwd()))
    if not vp.root.exists():
        raise MemoryError(
            f"Vault not found at {vp.root}",
            code="NOT_FOUND",
            exit_code=2,
            hint="Initialize a vault or point --vault to an existing one.",
            suggestions=[
                f"loom memory init --vault {vp.root}",
                "export MEMORY_VAULT=.loom/memory",
            ],
            details={"vault": str(vp.root)},
        )
    if not vp.meta_path.exists():
        init(vault=str(args.vault))


def _build_edit_options(args: argparse.Namespace) -> _EditRunOptions:
    cmd = str(getattr(args, "cmd", "") or "")
    is_append_cmd = cmd in {"append", "add-note", "append-note"}

    body_override = getattr(args, "body", None)
    body_append = getattr(args, "append", None)
    from_stdin = bool(getattr(args, "from_stdin", False))
    append_from_stdin = bool(getattr(args, "append_from_stdin", False))
    interactive = bool(getattr(args, "interactive", False))

    title = getattr(args, "title", None)
    visibility = getattr(args, "visibility", None)
    status = getattr(args, "status", None)
    tag = list(getattr(args, "tag", []) or [])
    remove_tag = list(getattr(args, "remove_tag", []) or [])
    clear_tags = bool(getattr(args, "clear_tags", False))
    alias = list(getattr(args, "alias", []) or [])
    remove_alias = list(getattr(args, "remove_alias", []) or [])
    clear_aliases = bool(getattr(args, "clear_aliases", False))
    link_values = list(getattr(args, "link", []) or [])
    remove_link = list(getattr(args, "remove_link", []) or [])
    clear_links = bool(getattr(args, "clear_links", False))
    related = list(getattr(args, "related", []) or [])
    scope = list(getattr(args, "scope", []) or [])
    command = getattr(args, "command", None)
    remove_scope = list(getattr(args, "remove_scope", []) or [])
    clear_scopes = bool(getattr(args, "clear_scopes", False))
    allow_missing_scopes = bool(getattr(args, "allow_missing_scopes", False))

    if is_append_cmd:
        append_from_stdin = bool(getattr(args, "from_stdin", False))
        from_stdin = False
        if body_append is None:
            body_append = getattr(args, "text", None)
        if body_append is None:
            body_append = body_override
        body_override = None
        interactive = False
        title = None
        visibility = None
        status = None
        tag = []
        remove_tag = []
        clear_tags = False
        alias = []
        remove_alias = []
        clear_aliases = False
        link_values = []
        remove_link = []
        clear_links = False
        scope = []
        command = None
        remove_scope = []
        clear_scopes = False
        allow_missing_scopes = False

    if from_stdin and append_from_stdin:
        raise MemoryError(
            "edit: cannot combine --from-stdin and --append-from-stdin",
            code="ARG",
            exit_code=2,
            hint="Pick exactly one stdin mode.",
            suggestions=[
                "cat file.md | loom memory edit <id> --from-stdin",
                "cat file.md | loom memory edit <id> --append-from-stdin",
            ],
        )

    stdin_ready = _stdin_is_ready()
    uses_stdin = from_stdin or append_from_stdin
    if (
        stdin_ready
        and not uses_stdin
        and body_override is None
        and body_append is None
        and not interactive
    ):
        raise MemoryError(
            "stdin is piped but no body mode was selected",
            code="ARG",
            exit_code=2,
            hint="Choose whether stdin should replace or append to the note body.",
            suggestions=[
                "cat file.md | loom memory edit <id> --from-stdin",
                "cat file.md | loom memory edit <id> --append-from-stdin",
            ],
        )

    if body_override == "-":
        if not _stdin_is_ready():
            raise MemoryError(
                "--body - requires piped stdin",
                code="ARG",
                exit_code=2,
                hint="Pipe body text into stdin.",
            )
        body_override = read_all_stdin_text()
    if from_stdin:
        if sys.stdin.isatty():
            raise MemoryError(
                "edit --from-stdin requires piped stdin",
                code="ARG",
                exit_code=2,
                hint="Pipe content: cat file.md | loom memory edit <id> --from-stdin",
            )
        body_override = read_all_stdin_text()

    if body_append == "-":
        if not _stdin_is_ready():
            raise MemoryError(
                "--append - requires piped stdin",
                code="ARG",
                exit_code=2,
                hint="Pipe append text into stdin.",
            )
        body_append = read_all_stdin_text()
    if append_from_stdin:
        if sys.stdin.isatty():
            raise MemoryError(
                "edit --append-from-stdin requires piped stdin",
                code="ARG",
                exit_code=2,
                hint="Pipe content: cat file.md | loom memory edit <id> --append-from-stdin",
            )
        body_append = read_all_stdin_text()

    if is_append_cmd and body_append is None and not related:
        raise MemoryError(
            "append requires text (--append/--text/--body) or piped stdin",
            code="ARG",
            exit_code=2,
            hint="Provide append text directly or pipe it on stdin.",
            suggestions=[
                "loom memory append <id> --append 'New findings'",
                "cat update.md | loom memory append <id> --from-stdin",
            ],
        )

    return _EditRunOptions(
        note_id=str(getattr(args, "id", "") or ""),
        title=(str(title) if title is not None else None),
        visibility=(str(visibility).strip().lower() if visibility is not None else None),
        status=(str(status).strip().lower() if status is not None else None),
        tag=tag,
        remove_tag=remove_tag,
        clear_tags=clear_tags,
        alias=alias,
        remove_alias=remove_alias,
        clear_aliases=clear_aliases,
        link=link_values,
        remove_link=remove_link,
        clear_links=clear_links,
        related=related,
        scope=scope,
        command=(str(command) if command is not None else None),
        remove_scope=remove_scope,
        clear_scopes=clear_scopes,
        allow_missing_scopes=allow_missing_scopes,
        body=(str(body_override) if body_override is not None else None),
        append=(str(body_append) if body_append is not None else None),
        interactive=interactive,
    )


def _run_prime(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del args, quiet
    res = prime()
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_init(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del quiet
    res = init(vault=str(args.vault))
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_add(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del quiet
    body = args.body
    if body == "-":
        if not _stdin_is_ready():
            raise MemoryError(
                "--body - requires piped stdin",
                code="ARG",
                exit_code=2,
                hint="Pipe body text into stdin.",
                suggestions=[
                    "cat file.md | loom memory add --title 'Title' --body -",
                ],
            )
        body = read_all_stdin_text()
    if body is None and not sys.stdin.isatty():
        body = read_all_stdin_text()
    res = add(
        vault=str(args.vault),
        title=args.title,
        visibility=str(args.visibility or "shared").strip().lower(),
        status=str(args.status or "active").strip().lower(),
        tag=args.tag,
        alias=args.alias,
        link=getattr(args, "link", None),
        related=getattr(args, "related", None),
        scope=args.scope,
        command=args.command,
        allow_missing_scopes=bool(getattr(args, "allow_missing_scopes", False)),
        body=body,
        interactive=bool(args.interactive),
        note_id=args.id,
        folder=args.folder or "",
    )
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_edit(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del quiet
    options = _build_edit_options(args)
    res = edit(
        vault=str(args.vault),
        note_id=options.note_id,
        title=options.title,
        visibility=options.visibility,
        status=options.status,
        tag=options.tag,
        remove_tag=options.remove_tag,
        clear_tags=options.clear_tags,
        alias=options.alias,
        remove_alias=options.remove_alias,
        clear_aliases=options.clear_aliases,
        link=options.link,
        remove_link=options.remove_link,
        clear_links=options.clear_links,
        related=options.related,
        scope=options.scope,
        command=options.command,
        remove_scope=options.remove_scope,
        clear_scopes=options.clear_scopes,
        allow_missing_scopes=options.allow_missing_scopes,
        body=options.body,
        append=options.append,
        interactive=options.interactive,
    )
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_recall(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    res = recall(
        vault=str(args.vault),
        query=args.query or "",
        limit=int(args.limit),
        tag=args.tag,
        not_tag=args.not_tag,
        scope=args.scope,
        not_scope=args.not_scope,
        command=args.command or "",
        visibility=args.visibility,
        include_deprecated=bool(args.include_deprecated),
        since=args.since,
        until=getattr(args, "until", None),
        and_mode=bool(args.and_mode),
        scoped_only=bool(args.scoped_only),
        full=bool(args.full),
        max_body_chars=args.max_body_chars,
        expand=int(args.expand or 0),
        max_chars=int(args.max_chars),
        context=bool(args.context),
        deterministic=bool(getattr(args, "deterministic", False)),
        quiet=quiet,
        allow_missing_scopes=bool(getattr(args, "allow_missing_scopes", False)),
        format=fmt,
        or_mode=bool(getattr(args, "or_mode", False)),
        fts_raw=bool(getattr(args, "fts_raw", False)),
    )
    if not quiet and res.warnings:
        print_index_warnings(list(res.warnings))
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_list(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    res = list_recent(
        vault=str(args.vault),
        limit=int(args.limit),
        tag=args.tag,
        not_tag=args.not_tag,
        scope=args.scope,
        not_scope=args.not_scope,
        command=args.command or "",
        visibility=args.visibility,
        include_deprecated=bool(args.include_deprecated),
        since=args.since,
        until=getattr(args, "until", None),
        and_mode=False,
        scoped_only=False,
        deterministic=bool(getattr(args, "deterministic", False)),
        quiet=quiet,
        allow_missing_scopes=bool(getattr(args, "allow_missing_scopes", False)),
        sort=str(getattr(args, "sort", "updated") or "updated"),
    )
    if not quiet and res.warnings:
        print_index_warnings(list(res.warnings))
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_grep(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    payload = grep(
        vault=str(args.vault),
        pattern=str(args.pattern),
        limit=int(args.limit),
        tag=args.tag,
        not_tag=args.not_tag,
        scope=args.scope,
        not_scope=args.not_scope,
        command=args.command or "",
        visibility=args.visibility,
        include_deprecated=bool(args.include_deprecated),
        since=args.since,
        until=getattr(args, "until", None),
        and_mode=bool(getattr(args, "and_mode", False)),
        scoped_only=bool(getattr(args, "scoped_only", False)),
        quiet=quiet,
        allow_missing_scopes=bool(getattr(args, "allow_missing_scopes", False)),
        ignore_case=bool(getattr(args, "ignore_case", False)),
    )
    return _emit_and_ok(payload, fmt=fmt)


def _run_show(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del quiet
    text = show(vault=str(args.vault), note_id=str(args.id), meta_only=bool(args.meta))
    return _emit_and_ok(text, fmt=fmt)


def _run_open(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    del quiet
    rel = open_note(vault=str(args.vault), note_id=str(args.id))
    return _emit_and_ok(rel, fmt=fmt)


def _run_forget(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    payload = forget(
        vault=str(args.vault),
        query=args.query or "",
        limit=int(args.limit),
        tag=args.tag,
        not_tag=args.not_tag,
        scope=args.scope,
        not_scope=args.not_scope,
        command=args.command or "",
        visibility=args.visibility,
        include_deprecated=bool(args.include_deprecated),
        since=args.since,
        until=getattr(args, "until", None),
        and_mode=False,
        scoped_only=False,
        deterministic=bool(getattr(args, "deterministic", False)),
        quiet=quiet,
        allow_missing_scopes=bool(getattr(args, "allow_missing_scopes", False)),
        or_mode=bool(getattr(args, "or_mode", False)),
        fts_raw=bool(getattr(args, "fts_raw", False)),
        apply=bool(getattr(args, "apply", False)),
        hard=bool(getattr(args, "hard", False)),
    )
    return _emit_and_ok(payload, fmt=fmt)


def _run_around(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    payload = around(
        vault=str(args.vault),
        note_id=str(args.id),
        k=int(getattr(args, "k", 12) or 12),
        by=str(getattr(args, "by", "updated") or "updated"),
        window_days=int(getattr(args, "window_days", 14) or 14),
        visibility=args.visibility,
        include_deprecated=bool(getattr(args, "include_deprecated", False)),
        quiet=quiet,
    )
    return _emit_and_ok(payload, fmt=fmt)


def _run_timeline(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    payload = timeline(
        vault=str(args.vault),
        days=int(getattr(args, "days", 30) or 30),
        by=str(getattr(args, "by", "updated") or "updated"),
        visibility=args.visibility,
        include_deprecated=bool(getattr(args, "include_deprecated", False)),
        quiet=quiet,
    )
    return _emit_and_ok(payload, fmt=fmt)


def _run_reindex(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    res = reindex(vault=str(args.vault), quiet=quiet)
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_janitor(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    res = janitor(
        vault=str(args.vault),
        cmd=args.janitor_cmd,
        visibility=args.visibility,
        limit=int(args.limit),
        apply=bool(getattr(args, "apply", False)),
        quiet=quiet,
    )
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


def _run_link(args: argparse.Namespace, *, fmt: str, quiet: bool) -> int:
    res = link(
        vault=str(args.vault),
        cmd=args.link_cmd,
        note_id=getattr(args, "id", ""),
        limit=int(getattr(args, "limit", 200) or 200),
        k=int(getattr(args, "k", 1) or 1),
        include_unresolved=bool(getattr(args, "include_unresolved", False)),
        visibility=getattr(args, "visibility", None),
        include_deprecated=bool(getattr(args, "include_deprecated", False)),
        quiet=quiet,
    )
    if not quiet and res.warnings:
        print_index_warnings(list(res.warnings))
    return _emit_and_ok(payload_for(res, fmt=fmt), fmt=fmt)


_RUN_HANDLERS: dict[str, Any] = {
    "prime": _run_prime,
    "init": _run_init,
    "add": _run_add,
    "note": _run_add,
    "save": _run_add,
    "edit": _run_edit,
    "update": _run_edit,
    "append": _run_edit,
    "add-note": _run_edit,
    "append-note": _run_edit,
    "recall": _run_recall,
    "get": _run_recall,
    "remember": _run_recall,
    "list": _run_list,
    "ls": _run_list,
    "recent": _run_list,
    "grep": _run_grep,
    "show": _run_show,
    "open": _run_open,
    "forget": _run_forget,
    "archive": _run_forget,
    "around": _run_around,
    "timeline": _run_timeline,
    "reindex": _run_reindex,
    "janitor": _run_janitor,
    "link": _run_link,
}


def _run_with_args(args: argparse.Namespace, *, fmt: str) -> int:
    quiet = bool(getattr(args, "quiet", False))
    cmd = str(getattr(args, "cmd", "") or "")
    handler = _RUN_HANDLERS.get(cmd)
    if handler is None:
        raise MemoryError(
            f"Unknown command: {args.cmd}",
            code="ARG",
            exit_code=2,
            hint="Run `loom memory -h` to see commands.",
            suggestions=["loom memory -h"],
            details={"cmd": cmd},
        )

    if cmd not in {"prime", "init"}:
        _ensure_vault_ready(args)

    return int(handler(args, fmt=fmt, quiet=quiet))


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv_list = list(argv) if argv is not None else sys.argv[1:]
    argv_list = _normalize_argv(argv_list)
    fmt_for_parse_errors = _infer_error_format(argv_list)

    args = _parse_args(argv_list, fmt_for_parse_errors=fmt_for_parse_errors)
    if args is None:
        return 2

    fmt = _effective_format(args)
    if args.format is None:
        args.format = fmt

    try:
        return _run_with_args(args, fmt=fmt)
    except MemoryError as e:
        hint = str(getattr(e, "hint", "") or "")
        if not hint and str(getattr(e, "code", "")) in {"ARG", "ARGPARSE"}:
            hint = "Run `loom memory -h` or `loom memory <command> -h`."
        emit_error(
            code=str(getattr(e, "code", "ERROR")),
            error=str(e),
            fmt=fmt,
            hint=hint,
            suggestions=list(getattr(e, "suggestions", []) or []),
            details=getattr(e, "details", None),
        )
        return int(getattr(e, "exit_code", 1) or 1)
    except FileExistsError as e:
        emit_error(
            code="CONFLICT",
            error=str(e),
            fmt=fmt,
            hint="Choose a different id/folder or remove the existing file.",
        )
        return 2
    except FileNotFoundError as e:
        emit_error(
            code="NOT_FOUND",
            error=str(e),
            fmt=fmt,
            hint="Confirm the id/path, or search with `loom memory recall <query>`.",
        )
        return 2
    except ValueError as e:
        emit_error(
            code="ARG",
            error=str(e),
            fmt=fmt,
            hint="Run `loom memory -h` or `loom memory <command> -h`.",
        )
        return 2
    except Exception as e:
        emit_error(code="ERROR", error=str(e), fmt=fmt)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
