"""Create a Loom verification record."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..cli import (
    add_scope_arguments,
    collect_assignments,
    collect_link_assignments,
    resolve_record_scope_args,
)
from ..core import (
    build_record_index,
    create_record,
    find_workspace_root,
    flatten_link_values,
    merge_repository_scopes,
    read_record,
    relative_to_workspace,
    set_sections,
)
from ..schema import SCHEMAS


def create_verification_record(
    workspace: Path,
    slug: str,
    *,
    title: str | None = None,
    links: dict[str, list[str]] | None = None,
    sections: dict[str, str] | None = None,
    repository_scope: dict | None = None,
) -> Path:
    schema = SCHEMAS["verification"]
    inferred_scope = repository_scope
    if inferred_scope is None and links:
        index, issues = build_record_index(workspace)
        if issues:
            raise SystemExit(
                "Fix record parse issues before inferring verification scope"
            )
        linked_scopes = []
        for ref in flatten_link_values(links):
            path = index.get(ref)
            if path is None:
                continue
            frontmatter, _body = read_record(path)
            linked_scopes.append(frontmatter.get("repository_scope"))
        inferred_scope = merge_repository_scopes(workspace, linked_scopes)
    path = create_record(
        "verification",
        slug,
        workspace,
        title=title,
        status=schema["default_status"],
        sections=schema["sections"],
        initial_links=links,
        repository_scope=inferred_scope,
        output_directory=schema["output_directory"],
    )
    if sections:
        set_sections(workspace, str(path), sections)
    return path


def register(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "verify",
        help="Create a Loom verification record",
        epilog=(
            "Examples: --link ticket:0005 --link spec:loom-repository-bootstrap "
            "or --link ticket=ticket:0005"
        ),
    )
    parser.add_argument("slug")
    parser.add_argument("--title")
    parser.add_argument("--link", action="append", default=[])
    parser.add_argument("--section", action="append", default=[])
    add_scope_arguments(parser)
    parser.set_defaults(func=run)


def run(args: Any) -> int:
    workspace = find_workspace_root()
    sections = {
        heading: "\n".join(values)
        for heading, values in collect_assignments(
            args.section, label="section assignment"
        ).items()
    }
    path = create_verification_record(
        workspace,
        args.slug,
        title=args.title,
        links=collect_link_assignments(args.link, label="link assignment"),
        sections=sections or None,
        repository_scope=resolve_record_scope_args(args, workspace),
    )
    print(relative_to_workspace(path, workspace))
    return 0
