from __future__ import annotations

from pathlib import Path

from .core import (
    build_record_index,
    create_record,
    flatten_link_values,
    merge_repository_scopes,
    normalize_links,
    read_record,
    render_with_frontmatter,
    relative_to_workspace,
    scan_records,
    utc_now,
)


def resolve_record_path(
    workspace: Path, target: str, *, include_runs: bool = True
) -> Path:
    candidate = Path(target)
    if candidate.is_absolute() and candidate.exists():
        return candidate
    workspace_candidate = (workspace / target).resolve()
    if workspace_candidate.exists():
        return workspace_candidate
    index, issues = build_record_index(workspace)
    if issues:
        raise SystemExit("Fix record parse issues before mutating records")
    if target not in index:
        area = "record graph including runs" if include_runs else "canonical records"
        raise SystemExit(f"Unknown target in {area}: {target}")
    return index[target]


def write_record(path: Path, frontmatter: dict, body: str) -> None:
    path.write_text(render_with_frontmatter(frontmatter, body))


def _parse_sections(body: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("# "):
            if current_heading is not None:
                sections.append((current_heading, current_lines))
            current_heading = line[2:].strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((current_heading, current_lines))
    return sections


def _render_sections(sections: list[tuple[str, list[str]]]) -> str:
    chunks: list[str] = []
    for heading, lines in sections:
        content = "\n".join(lines).strip()
        if content:
            chunks.append(f"# {heading}\n\n{content}\n")
        else:
            chunks.append(f"# {heading}\n")
    return "\n".join(chunks).rstrip()


def _load_record(workspace: Path, target: str) -> tuple[Path, dict, str]:
    path = resolve_record_path(workspace, target)
    frontmatter, body = read_record(path)
    return path, frontmatter, body


def set_sections(workspace: Path, target: str, updates: dict[str, str]) -> Path:
    path, frontmatter, body = _load_record(workspace, target)
    sections = _parse_sections(body)
    section_map = {heading: index for index, (heading, _lines) in enumerate(sections)}
    missing = [heading for heading in updates if heading not in section_map]
    if missing:
        raise SystemExit(
            f"Unknown section(s) in {relative_to_workspace(path, workspace)}: {', '.join(missing)}"
        )
    for heading, content in updates.items():
        sections[section_map[heading]] = (heading, content.rstrip().splitlines())
    frontmatter["updated_at"] = utc_now()
    write_record(path, frontmatter, _render_sections(sections))
    return path


def mutate_links(
    workspace: Path,
    target: str,
    *,
    additions: dict[str, list[str]] | None = None,
    removals: dict[str, list[str]] | None = None,
) -> Path:
    path, frontmatter, body = _load_record(workspace, target)
    record_id = frontmatter.get("id")
    links: dict[str, list[str]] = normalize_links(frontmatter.get("links", {}))
    if record_id == "constitution:main" and flatten_link_values(additions or {}):
        raise SystemExit(
            "constitution:main must not declare frontmatter links; remove links from other records instead"
        )
    for key, values in (additions or {}).items():
        links.setdefault(key, [])
        for value in values:
            if value not in links[key]:
                links[key].append(value)
    for key, values in (removals or {}).items():
        if key not in links:
            continue
        links[key] = [value for value in links[key] if value not in values]
        if not links[key]:
            links.pop(key)
    if record_id == "constitution:main" and flatten_link_values(links):
        raise SystemExit(
            "constitution:main must not declare frontmatter links; remove every existing link instead"
        )
    frontmatter["links"] = links
    frontmatter["updated_at"] = utc_now()
    write_record(path, frontmatter, body)
    return path


def create_verification_record(
    workspace: Path,
    slug: str,
    *,
    title: str | None = None,
    links: dict[str, list[str]] | None = None,
    sections: dict[str, str] | None = None,
    repository_scope: dict | None = None,
) -> Path:
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
        initial_links=links,
        repository_scope=inferred_scope,
    )
    if sections:
        set_sections(workspace, str(path), sections)
    return path


def list_records(
    workspace: Path,
    *,
    kind: str | None = None,
    status: str | None = None,
    include_runs: bool = False,
) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for path in scan_records(workspace, include_runs=include_runs):
        frontmatter, _body = read_record(path)
        record_kind = frontmatter.get("kind")
        record_status = frontmatter.get("status")
        if kind and record_kind != kind:
            continue
        if status and record_status != status:
            continue
        results.append(
            {
                "id": frontmatter.get("id", "unknown"),
                "kind": record_kind or "unknown",
                "status": record_status or "unknown",
                "path": relative_to_workspace(path, workspace),
            }
        )
    return results
