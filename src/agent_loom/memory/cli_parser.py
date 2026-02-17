from __future__ import annotations

import argparse
import os

from agent_loom.core.cli_args import (
    ArgParseError,
    StrictArgumentParser,
    did_you_mean,
    rewrite_flag_aliases,
)
from agent_loom.memory.constants import (
    DEFAULT_VAULT_DIR,
    STATUSES,
    SUBSYSTEM_NAME,
    VISIBILITIES,
)
from agent_loom.memory.utils import emit_error


class MemoryArgumentParser(StrictArgumentParser):
    pass


_FLAG_ALIASES = {
    "--vault-dir": "--vault",
    "--vault_root": "--vault",
    "--stdout-format": "--format",
    "--tags": "--tag",
    "--aliases": "--alias",
    "--scopes": "--scope",
    "--links": "--link",
    "--relateds": "--related",
}


def _normalize_argv(argv: list[str]) -> list[str]:
    argv = rewrite_flag_aliases(argv, _FLAG_ALIASES)
    out: list[str] = []
    i = 0
    while i < len(argv):
        tok = argv[i]

        if tok in {"append-note", "append_note", "add-note", "add_note"}:
            out.append("append")
            i += 1
            continue

        # Common format shorthands.
        if tok == "--json":
            out.extend(["--format", "json"])
            i += 1
            continue
        if tok == "--jsonl":
            out.extend(["--format", "jsonl"])
            i += 1
            continue
        if tok in {"--md", "--markdown"}:
            out.extend(["--format", "md"])
            i += 1
            continue
        if tok == "--prompt":
            out.extend(["--format", "prompt"])
            i += 1
            continue

        out.append(tok)
        i += 1

    # Positional fallbacks:
    # memory add <title>  ->  memory add --title <title>
    # memory add <title> <body>  ->  memory add --title <title> --body <body>
    for add_cmd in ("add", "note", "save"):
        if add_cmd not in out:
            continue
        idx = out.index(add_cmd)
        tail = out[idx:]

        # Gather positional tokens immediately after the subcommand (stop at first flag).
        pos = []
        j = idx + 1
        while j < len(out):
            tok = out[j]
            if not tok or tok.startswith("-"):
                break
            pos.append(tok)
            j += 1

        has_title = "--title" in tail
        has_body = "--body" in tail

        # Only apply the two-positional shortcut when it is unambiguous.
        if not has_title and pos:
            # Rewrite first positional into --title.
            out = out[: idx + 1] + ["--title", pos[0]] + out[idx + 2 :]

            # If the user provided exactly two positional tokens, treat second as body.
            if not has_body and len(pos) == 2:
                # After inserting --title, the second positional shifts by +1.
                body_idx = idx + 3
                if body_idx < len(out) and out[body_idx] == pos[1]:
                    out = (
                        out[:body_idx] + ["--body", out[body_idx]] + out[body_idx + 1 :]
                    )
        break

    # memory edit|update|append <id> <text> -> --append <text>
    for edit_cmd in ("edit", "update", "append"):
        if edit_cmd not in out:
            continue
        idx = out.index(edit_cmd)
        tail = out[idx:]

        pos: list[str] = []
        j = idx + 1
        while j < len(out):
            tok = out[j]
            if not tok or tok.startswith("-"):
                break
            pos.append(tok)
            j += 1

        has_body_mode = any(
            flg in tail
            for flg in (
                "--body",
                "--from-stdin",
                "--append",
                "--append-from-stdin",
                "--interactive",
            )
        )
        if len(pos) >= 2 and not has_body_mode:
            append_text = " ".join(pos[1:]).strip()
            if append_text:
                out = out[: idx + 2] + ["--append", append_text] + out[j:]
        break

    # memory link validate <id>  ->  memory link validate --id <id>
    if len(out) >= 3 and out[0] == "link" and out[1] == "validate":
        if "--id" not in out and out[2] and not out[2].startswith("-"):
            out = ["link", "validate", "--id", out[2]] + out[3:]

    return out


def _infer_error_format(argv: list[str]) -> str:
    # Default: memory defaults to JSON success output, so default errors to JSON too.
    fmt = "json"
    for i, tok in enumerate(argv):
        if tok == "--format" and i + 1 < len(argv):
            cand = str(argv[i + 1] or "").strip().lower()
            if cand in {"json", "jsonl", "text", "md", "prompt"}:
                return cand
        if tok.startswith("--format="):
            cand = tok.split("=", 1)[1].strip().lower()
            if cand in {"json", "jsonl", "text", "md", "prompt"}:
                return cand
    return fmt


def build_parser() -> argparse.ArgumentParser:
    p = MemoryArgumentParser(prog=SUBSYSTEM_NAME)

    # Global flags (accepted before the subcommand).
    p.add_argument(
        "--vault",
        default=os.environ.get("MEMORY_VAULT", DEFAULT_VAULT_DIR),
        help="Vault directory (absolute or repo-root-relative when in git). Default: .loom/memory",
    )
    p.add_argument(
        "--format",
        default=None,
        choices=["json", "jsonl", "text", "md", "prompt"],
        help="Output format. Default is json (recall --context defaults to text).",
    )
    p.add_argument(
        "--deterministic",
        action="store_true",
        help="Prefer stable outputs (no recency boost; context pack omits generated_at).",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce stderr diagnostics (still returns structured output).",
    )

    # Same flags accepted after the subcommand too, without overriding when omitted.
    common_sub = MemoryArgumentParser(add_help=False)
    common_sub.add_argument("--vault", default=argparse.SUPPRESS)
    common_sub.add_argument(
        "--format",
        default=argparse.SUPPRESS,
        choices=["json", "jsonl", "text", "md", "prompt"],
    )
    common_sub.add_argument(
        "--deterministic", action="store_true", default=argparse.SUPPRESS
    )
    common_sub.add_argument("--quiet", action="store_true", default=argparse.SUPPRESS)

    sp = p.add_subparsers(dest="cmd", required=True, parser_class=MemoryArgumentParser)

    sp.add_parser(
        "prime",
        parents=[common_sub],
        help="Print memory cookbook",
    )

    sp.add_parser(
        "init",
        parents=[common_sub],
        help="Initialize vault layout, meta.json, gitignore safety, db cache",
    )

    add_p = sp.add_parser(
        "add",
        parents=[common_sub],
        help="Add a note",
        aliases=["note", "save"],
    )
    add_p.add_argument(
        "--title",
        default=None,
        help="Note title (if omitted, derived from first non-empty body line)",
    )
    add_p.add_argument(
        "--id", default=None, help="Explicit note id (advanced; must be link-safe)"
    )
    add_p.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Tag (repeatable; comma-separated ok)",
    )
    add_p.add_argument(
        "--alias",
        action="append",
        default=[],
        help="Alias (repeatable; comma-separated ok)",
    )
    add_p.add_argument(
        "--link",
        action="append",
        default=[],
        help="Add frontmatter links (repeatable; comma-separated ok)",
    )
    add_p.add_argument(
        "--related",
        action="append",
        default=[],
        help="Append a Related: line with [[wikilinks]] (repeatable; comma ok)",
    )
    add_p.add_argument(
        "--scope", action="append", default=[], help="Scope kind:value (repeatable)"
    )
    add_p.add_argument(
        "--command",
        default=None,
        help="Command context shorthand (adds scope command:...)",
    )
    add_p.add_argument(
        "--visibility",
        choices=VISIBILITIES,
        default="shared",
        help="shared|personal|ephemeral",
    )
    add_p.add_argument(
        "--status", choices=STATUSES, default="active", help="active|deprecated"
    )
    add_p.add_argument(
        "--folder",
        default="",
        help="Subfolder under the visibility root (keeps ids path-independent)",
    )
    add_p.add_argument(
        "--body",
        default=None,
        help="Note body text. If omitted: read stdin when piped.",
    )
    add_p.add_argument(
        "--interactive",
        action="store_true",
        help="Open editor to write body (human path; off the beaten path)",
    )
    add_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: scopes that do not exist on disk",
    )

    edit_p = sp.add_parser(
        "edit",
        parents=[common_sub],
        help="Edit a note by id",
        aliases=["update"],
    )
    edit_p.add_argument("id", help="Note reference (id/title/alias)")
    edit_p.add_argument(
        "--body",
        default=None,
        help="Replace note body text (agent path)",
    )
    edit_p.add_argument(
        "--from-stdin",
        action="store_true",
        help="Replace note body from stdin (strict; prevents accidental overwrites)",
    )
    edit_p.add_argument(
        "--append",
        default=None,
        help="Append text to the note body (agent path)",
    )
    edit_p.add_argument(
        "--append-from-stdin",
        action="store_true",
        help="Append text to the note body from stdin (strict)",
    )
    edit_p.add_argument(
        "--interactive",
        action="store_true",
        help="Open editor to edit the note body (human path)",
    )
    edit_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: scopes that do not exist on disk",
    )
    edit_p.add_argument("--title", default=None, help="Set title")
    edit_p.add_argument("--tag", action="append", default=[], help="Add tag(s)")
    edit_p.add_argument(
        "--remove-tag", action="append", default=[], help="Remove tag(s)"
    )
    edit_p.add_argument("--clear-tags", action="store_true", help="Remove all tags")
    edit_p.add_argument("--alias", action="append", default=[], help="Add alias(es)")
    edit_p.add_argument(
        "--remove-alias", action="append", default=[], help="Remove alias(es)"
    )
    edit_p.add_argument(
        "--clear-aliases", action="store_true", help="Remove all aliases"
    )
    edit_p.add_argument(
        "--link",
        action="append",
        default=[],
        help="Add frontmatter links (repeatable; comma-separated ok)",
    )
    edit_p.add_argument(
        "--remove-link",
        action="append",
        default=[],
        help="Remove frontmatter links (repeatable; comma-separated ok)",
    )
    edit_p.add_argument(
        "--clear-links", action="store_true", help="Remove all frontmatter links"
    )
    edit_p.add_argument(
        "--related",
        action="append",
        default=[],
        help="Append a Related: line with [[wikilinks]] (repeatable; comma ok)",
    )
    edit_p.add_argument(
        "--scope", action="append", default=[], help="Add scope(s) kind:value"
    )
    edit_p.add_argument(
        "--command",
        default=None,
        help="Command context shorthand (adds scope command:...)",
    )
    edit_p.add_argument(
        "--remove-scope",
        action="append",
        default=[],
        help="Remove scope(s) kind:value (exact, normalized)",
    )
    edit_p.add_argument("--clear-scopes", action="store_true", help="Remove all scopes")
    edit_p.add_argument(
        "--visibility",
        choices=VISIBILITIES,
        default=None,
        help="Change visibility (also moves file)",
    )
    edit_p.add_argument(
        "--status", choices=STATUSES, default=None, help="Change status"
    )

    append_p = sp.add_parser(
        "append",
        parents=[common_sub],
        help="Append text to a note",
        aliases=["add-note", "append-note"],
    )
    append_p.add_argument("id", help="Note reference (id/title/alias)")
    append_p.add_argument(
        "--append",
        default=None,
        help="Text to append",
    )
    append_p.add_argument(
        "--text",
        default=None,
        help="Alias for --append",
    )
    append_p.add_argument(
        "--body",
        default=None,
        help="Alias for --append",
    )
    append_p.add_argument(
        "--from-stdin",
        action="store_true",
        help="Append text from stdin (strict)",
    )
    append_p.add_argument(
        "--related",
        action="append",
        default=[],
        help="Append a Related: line with [[wikilinks]] (repeatable; comma ok)",
    )

    recall_p = sp.add_parser(
        "recall",
        parents=[common_sub],
        help="Recall notes (FTS + filters), default JSON output",
        aliases=["get", "remember"],
    )
    recall_p.add_argument(
        "query", nargs="?", default="", help="Full-text query (FTS5 if available)"
    )
    recall_p.add_argument(
        "--limit", type=int, default=8, help="Max results (default 8)"
    )
    recall_p.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Filter by note tag (repeatable; comma ok)",
    )
    recall_p.add_argument(
        "--not-tag",
        action="append",
        default=[],
        help="Exclude by note tag (repeatable)",
    )
    recall_p.add_argument(
        "--scope",
        action="append",
        default=[],
        help="Context scope kind:value (repeatable)",
    )
    recall_p.add_argument(
        "--not-scope",
        action="append",
        default=[],
        help="Exclude notes matching these context scopes",
    )
    recall_p.add_argument(
        "--command",
        default=None,
        help="Command context (shorthand for --scope command:...)",
    )
    recall_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    recall_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )
    recall_p.add_argument(
        "--until",
        default=None,
        help="Only notes updated_at <= until (RFC3339 or YYYY-MM-DD)",
    )
    recall_p.add_argument(
        "--or",
        dest="or_mode",
        action="store_true",
        help="Use OR semantics between query tokens (default: AND)",
    )
    recall_p.add_argument(
        "--fts-raw",
        action="store_true",
        help="Treat the query as a raw SQLite FTS expression (advanced)",
    )
    recall_p.add_argument(
        "--since",
        default=None,
        help="Only notes updated_at >= since (RFC3339 or YYYY-MM-DD)",
    )
    recall_p.add_argument(
        "--and",
        dest="and_mode",
        action="store_true",
        help="AND semantics for multiple --tag/--scope",
    )
    recall_p.add_argument(
        "--scoped-only",
        action="store_true",
        help="When context scopes are provided, drop unscoped notes",
    )
    recall_p.add_argument(
        "--full",
        action="store_true",
        help="Include note body (bounded by --max-body-chars)",
    )
    recall_p.add_argument(
        "--max-body-chars",
        type=int,
        default=None,
        help="Max chars of body when included (default 800; default 4000 for --context)",
    )
    recall_p.add_argument(
        "--context",
        action="store_true",
        help="Emit a bounded context pack (string output; requires query or context)",
    )
    recall_p.add_argument(
        "--max-chars",
        type=int,
        default=12000,
        help="Max output chars for --context (default 12000)",
    )
    recall_p.add_argument(
        "--expand",
        type=int,
        default=0,
        help="k-hop graph expansion around hits (adds role=neighbor notes)",
    )
    recall_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: context scopes that do not exist on disk",
    )

    grep_p = sp.add_parser(
        "grep",
        parents=[common_sub],
        help="Regex search notes (literal regex; no ranking)",
    )
    grep_p.add_argument("pattern", help="Python regex pattern")
    grep_p.add_argument("--limit", type=int, default=20, help="Max results")
    grep_p.add_argument(
        "--ignore-case",
        action="store_true",
        help="Case-insensitive regex matching",
    )
    grep_p.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Filter by note tag (repeatable; comma ok)",
    )
    grep_p.add_argument(
        "--not-tag",
        action="append",
        default=[],
        help="Exclude by note tag (repeatable)",
    )
    grep_p.add_argument(
        "--scope",
        action="append",
        default=[],
        help="Context scope kind:value (repeatable)",
    )
    grep_p.add_argument(
        "--not-scope",
        action="append",
        default=[],
        help="Exclude notes matching these context scopes",
    )
    grep_p.add_argument(
        "--command",
        default=None,
        help="Command context (shorthand for --scope command:...)",
    )
    grep_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    grep_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )
    grep_p.add_argument(
        "--since",
        default=None,
        help="Only notes updated_at >= since (RFC3339 or YYYY-MM-DD)",
    )
    grep_p.add_argument(
        "--until",
        default=None,
        help="Only notes updated_at <= until (RFC3339 or YYYY-MM-DD)",
    )
    grep_p.add_argument(
        "--and",
        dest="and_mode",
        action="store_true",
        help="AND semantics for multiple --tag/--scope",
    )
    grep_p.add_argument(
        "--scoped-only",
        action="store_true",
        help="When context scopes are provided, drop unscoped notes",
    )
    grep_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: context scopes that do not exist on disk",
    )

    list_p = sp.add_parser(
        "list",
        parents=[common_sub],
        help="List recent notes (no query required)",
        aliases=["ls", "recent"],
    )
    list_p.add_argument("--limit", type=int, default=20, help="Max results")
    list_p.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Filter by note tag (repeatable; comma ok)",
    )
    list_p.add_argument(
        "--not-tag",
        action="append",
        default=[],
        help="Exclude by note tag (repeatable)",
    )
    list_p.add_argument(
        "--scope",
        action="append",
        default=[],
        help="Context scope kind:value (repeatable)",
    )
    list_p.add_argument(
        "--not-scope",
        action="append",
        default=[],
        help="Exclude notes matching these context scopes",
    )
    list_p.add_argument(
        "--command",
        default=None,
        help="Command context (shorthand for --scope command:...)",
    )
    list_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    list_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )
    list_p.add_argument(
        "--since",
        default=None,
        help="Only notes updated_at >= since (RFC3339 or YYYY-MM-DD)",
    )
    list_p.add_argument(
        "--until",
        default=None,
        help="Only notes updated_at <= until (RFC3339 or YYYY-MM-DD)",
    )
    list_p.add_argument(
        "--sort",
        choices=["updated", "created"],
        default="updated",
        help="Sort key (default updated)",
    )
    list_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: context scopes that do not exist on disk",
    )

    show_p = sp.add_parser("show", parents=[common_sub], help="Show a note by id")
    show_p.add_argument("id", help="Note reference (id/title/alias)")
    show_p.add_argument("--meta", action="store_true", help="Show frontmatter only")

    open_p = sp.add_parser("open", parents=[common_sub], help="Open a note in editor")
    open_p.add_argument("id", help="Note reference (id/title/alias)")

    forget_p = sp.add_parser(
        "forget",
        parents=[common_sub],
        help="Forget notes (soft by default; hard delete with --hard)",
        aliases=["archive"],
    )
    forget_p.add_argument(
        "query",
        nargs="?",
        default="",
        help="Optional full-text query (FTS5 if available)",
    )
    forget_p.add_argument("--limit", type=int, default=50, help="Max candidates")
    forget_p.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Filter by note tag (repeatable; comma ok)",
    )
    forget_p.add_argument(
        "--not-tag",
        action="append",
        default=[],
        help="Exclude by note tag (repeatable)",
    )
    forget_p.add_argument(
        "--scope",
        action="append",
        default=[],
        help="Context scope kind:value (repeatable)",
    )
    forget_p.add_argument(
        "--not-scope",
        action="append",
        default=[],
        help="Exclude notes matching these context scopes",
    )
    forget_p.add_argument(
        "--command",
        default=None,
        help="Command context (shorthand for --scope command:...)",
    )
    forget_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    forget_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )
    forget_p.add_argument(
        "--since",
        default=None,
        help="Only notes updated_at >= since (RFC3339 or YYYY-MM-DD)",
    )
    forget_p.add_argument(
        "--until",
        default=None,
        help="Only notes updated_at <= until (RFC3339 or YYYY-MM-DD)",
    )
    forget_p.add_argument(
        "--or",
        dest="or_mode",
        action="store_true",
        help="Use OR semantics between query tokens (default: AND)",
    )
    forget_p.add_argument(
        "--fts-raw",
        action="store_true",
        help="Treat the query as a raw SQLite FTS expression (advanced)",
    )
    forget_p.add_argument(
        "--apply", action="store_true", help="Apply changes (default is dry-run)"
    )
    forget_p.add_argument(
        "--hard",
        action="store_true",
        help="Hard delete matching notes (requires --apply)",
    )
    forget_p.add_argument(
        "--allow-missing-scopes",
        action="store_true",
        help="Allow file: context scopes that do not exist on disk",
    )

    around_p = sp.add_parser(
        "around",
        parents=[common_sub],
        help="Show notes temporally near a note",
    )
    around_p.add_argument("id", help="Note reference (id/title/alias)")
    around_p.add_argument("--k", type=int, default=12, help="Number of neighbors")
    around_p.add_argument(
        "--by",
        choices=["updated", "created"],
        default="updated",
        help="Which timestamp to use",
    )
    around_p.add_argument(
        "--window-days",
        type=int,
        default=14,
        help="Search window in days around the target timestamp",
    )
    around_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    around_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )

    timeline_p = sp.add_parser(
        "timeline",
        parents=[common_sub],
        help="Temporal browse of recent notes grouped by day",
    )
    timeline_p.add_argument(
        "--days", type=int, default=30, help="How many days back to include"
    )
    timeline_p.add_argument(
        "--by",
        choices=["updated", "created"],
        default="updated",
        help="Which timestamp to group by",
    )
    timeline_p.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    timeline_p.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )

    link_p = sp.add_parser(
        "link",
        parents=[common_sub],
        help="Link graph utilities (backlinks/neighbors/validate/graph)",
    )
    lsp = link_p.add_subparsers(
        dest="link_cmd", required=True, parser_class=MemoryArgumentParser
    )

    lb = lsp.add_parser(
        "backlinks",
        parents=[common_sub],
        help="Show backlinks (notes that link to <id>)",
    )
    lb.add_argument("id", help="Note reference (id/title/alias)")
    lb.add_argument("--limit", type=int, default=50)

    ln = lsp.add_parser(
        "neighbors",
        parents=[common_sub],
        help="Show neighbors (inbound+outbound), optionally k-hop expansion",
    )
    ln.add_argument("id", help="Note reference (id/title/alias)")
    ln.add_argument(
        "--k", type=int, default=0, help="k-hop expansion (0 => only 1-hop lists)"
    )

    lv = lsp.add_parser(
        "validate", parents=[common_sub], help="List broken links (missing/ambiguous)"
    )
    lv.add_argument(
        "--id",
        default=None,
        help="Only validate links originating from this note reference (id/title/alias)",
    )
    lv.add_argument("--limit", type=int, default=200)

    lg = lsp.add_parser("graph", parents=[common_sub], help="Export link edge list")
    lg.add_argument(
        "--include-unresolved",
        action="store_true",
        help="Include missing/ambiguous links too",
    )

    ls = lsp.add_parser(
        "suggest",
        parents=[common_sub],
        help="Suggest likely related notes for <id> (non-mutating)",
    )
    ls.add_argument("id", help="Note reference (id/title/alias)")
    ls.add_argument("--limit", type=int, default=12)
    ls.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared+personal)",
    )
    ls.add_argument(
        "--include-deprecated", action="store_true", help="Include status=deprecated"
    )

    sp.add_parser(
        "reindex",
        parents=[common_sub],
        help="Rebuild derived sqlite index from scratch (safe, deterministic)",
    )

    janitor_p = sp.add_parser(
        "janitor",
        parents=[common_sub],
        help="Clean up stale scopes after files move/delete",
    )
    jsp = janitor_p.add_subparsers(
        dest="janitor_cmd", required=True, parser_class=MemoryArgumentParser
    )

    jr = jsp.add_parser(
        "report",
        parents=[common_sub],
        help="Report file: scopes whose files do not exist",
    )
    jr.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared)",
    )
    jr.add_argument("--limit", type=int, default=200)

    jf = jsp.add_parser(
        "fix",
        parents=[common_sub],
        help="Remove stale file: scopes (requires --apply)",
    )
    jf.add_argument(
        "--visibility",
        action="append",
        choices=VISIBILITIES,
        default=None,
        help="Visibility filter (default: shared)",
    )
    jf.add_argument("--limit", type=int, default=200)
    jf.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes (otherwise dry-run)",
    )

    return p


def _parse_args(
    argv_list: list[str], *, fmt_for_parse_errors: str
) -> argparse.Namespace | None:
    parser = build_parser()
    try:
        return parser.parse_args(argv_list)
    except ArgParseError as e:
        first = ""
        for tok in argv_list:
            if not tok.startswith("-"):
                first = tok
                break

        cmds: list[str] = []
        try:
            sub = next(
                a
                for a in parser._actions
                if isinstance(a, argparse._SubParsersAction)  # type: ignore[attr-defined]
            )
            cmds = sorted(list(sub.choices.keys()))
        except Exception:
            cmds = []

        suggestions = [f"loom memory {c} -h" for c in did_you_mean(first, cmds)]
        emit_error(
            code="ARGPARSE",
            error=str(e),
            fmt=fmt_for_parse_errors,
            hint="Run `loom memory -h` or `loom memory <command> -h`.",
            suggestions=suggestions or ["loom memory -h"],
            details={"argv": argv_list},
        )
        return None


def _effective_format(args: argparse.Namespace) -> str:
    if (
        args.format is None
        and args.cmd in {"recall", "get", "remember"}
        and bool(getattr(args, "context", False))
    ):
        return "text"
    if args.format is None and args.cmd in {"list", "ls", "recent"}:
        return "text"
    if args.format is None and args.cmd in {"show", "open"}:
        return "text"
    return args.format or "json"
