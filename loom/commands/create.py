"""Create and validate Loom records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..cli import (
    add_scope_arguments,
    collect_assignments,
    collect_link_assignments,
    resolve_record_scope_args,
)
from ..core import (
    create_record,
    extract_headings,
    find_workspace_root,
    issue,
    read_record,
    relative_to_workspace,
    scan_records,
    set_sections,
    slugify,
)
from ..schema import SCHEMAS


def validate(workspace: Path, kind: str | None = None) -> list[dict]:
    """Validate records. If *kind* is given, validate only that kind."""
    problems: list[dict] = []
    kinds = [kind] if kind else sorted(SCHEMAS)
    for path in scan_records(workspace):
        try:
            frontmatter, body = read_record(path)
        except Exception as exc:
            problems.append(issue(path, workspace, str(exc)))
            continue
        record_kind = frontmatter.get("kind")
        if record_kind not in kinds:
            continue
        schema = SCHEMAS.get(record_kind)
        if schema is None:
            continue
        record_status = frontmatter.get("status")
        if record_status not in schema["statuses"]:
            problems.append(
                issue(
                    path,
                    workspace,
                    f"invalid status for {record_kind}: {record_status}",
                )
            )
        headings = extract_headings(body)
        for section in schema["sections"]:
            if section not in headings:
                problems.append(issue(path, workspace, f"missing section: {section}"))
    return problems


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "create",
        help="Create or validate Loom records",
        description=(
            "Create or validate Loom records. "
            "Run with just a kind to validate existing records of that kind. "
            "Run with no arguments to validate all record kinds."
        ),
    )
    parser.add_argument(
        "kind",
        nargs="?",
        choices=sorted(SCHEMAS),
        help="Record kind",
    )
    parser.add_argument(
        "slug", nargs="?", help="Slug for a new record (omit to validate)"
    )
    parser.add_argument("--title")
    parser.add_argument("--status")
    parser.add_argument("--link", action="append", default=[])
    parser.add_argument("--section", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    add_scope_arguments(parser)
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()

    # Validate mode: no slug (or no kind at all)
    if not args.slug:
        problems = validate(workspace, kind=args.kind)
        if args.json:
            print(json.dumps({"issues": problems}, indent=2))
        elif problems:
            for p in problems:
                print(f"ERROR {p['path']}: {p['message']}")
        else:
            label = args.kind or "all"
            print(f"All {label} records are valid")
        return 1 if problems else 0

    if not args.kind:
        raise SystemExit("Provide a record kind when creating a record")

    kind = args.kind
    schema = SCHEMAS[kind]

    # Build extra kwargs for special kinds
    extra: dict[str, Any] = {}
    if schema.get("file_slug_prefix"):
        suffix = slugify(args.title or args.slug)
        extra["file_slug"] = f"{schema['file_slug_prefix']}-{suffix}"
    if schema.get("id_from_slug"):
        record_slug = slugify(args.slug)
        extra["record_id"] = f"{kind}:{record_slug}"
        extra["file_slug"] = record_slug

    path = create_record(
        kind,
        args.slug,
        workspace,
        title=args.title,
        status=args.status or schema["default_status"],
        sections=schema["sections"],
        initial_links=collect_link_assignments(args.link, label="link assignment"),
        repository_scope=resolve_record_scope_args(args, workspace),
        output_directory=schema["output_directory"],
        **extra,
    )
    if args.section:
        set_sections(
            workspace,
            str(path),
            {
                heading: "\n".join(values)
                for heading, values in collect_assignments(
                    args.section, label="section assignment"
                ).items()
            },
        )
    print(relative_to_workspace(path, workspace))
    return 0
