"""Loom memory module operations: scan, validate, rebuild indexes."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..core import find_workspace_root, parse_frontmatter

MEMORY_ROOT = Path(".loom/memories")
MANIFEST_PATH = MEMORY_ROOT / "manifest.json"
EXPECTED_DOMAINS = ("system", "user")
DOMAIN_REQUIRED_FILES = {
    "system": [
        "hot-memory.md",
        "patterns.md",
        "self-observations.md",
        "improvements.md",
    ],
    "user": ["hot-memory.md", "observations.md", "entities.md", "action-items.md"],
}
L0_PATTERN = re.compile(r"^<!-- L0: .+ -->$")
WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def memory_root(workspace: Path) -> Path:
    return workspace / MEMORY_ROOT


def load_memory_manifest(workspace: Path) -> dict:
    manifest_path = workspace / MANIFEST_PATH
    if not manifest_path.exists():
        raise SystemExit(f"Missing memory manifest: {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid memory manifest JSON: {exc}") from exc
    if not isinstance(manifest, dict):
        raise SystemExit("Memory manifest must be a JSON object")
    return manifest


def list_memory_markdown_files(workspace: Path) -> list[Path]:
    root = memory_root(workspace)
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def read_l0_summary(path: Path) -> str | None:
    try:
        first_line = path.read_text().splitlines()[0].strip()
    except IndexError:
        return None
    if not L0_PATTERN.match(first_line):
        return None
    return first_line.removeprefix("<!-- L0: ").removesuffix(" -->")


def collect_archive_rows(workspace: Path) -> list[dict[str, str | int]]:
    glacier_root = memory_root(workspace) / "glacier"
    if not glacier_root.exists():
        return []
    rows: list[dict[str, str | int]] = []
    for path in sorted(glacier_root.rglob("*.md")):
        if path.name == "index.md":
            continue
        frontmatter, _ = parse_frontmatter(path.read_text())
        rows.append(
            {
                "path": str(path.relative_to(memory_root(workspace))),
                "domain": str(frontmatter.get("domain", "")),
                "type": str(frontmatter.get("type", "")),
                "tags": ", ".join(frontmatter.get("tags", [])),
                "date_range": str(frontmatter.get("date_range", "")),
                "entries": int(frontmatter.get("entries", 0)),
                "summary": str(frontmatter.get("summary", "")),
            }
        )
    return rows


def validate_memory_structure(workspace: Path) -> dict:
    manifest = load_memory_manifest(workspace)
    if manifest.get("schema_version") != 1:
        raise SystemExit("Memory manifest schema_version must be 1")
    domains = manifest.get("domains")
    if not isinstance(domains, dict):
        raise SystemExit("Memory manifest domains must be a JSON object")
    actual_domains = tuple(sorted(domains))
    if actual_domains != EXPECTED_DOMAINS:
        expected = ", ".join(EXPECTED_DOMAINS)
        actual = ", ".join(actual_domains) or "<none>"
        raise SystemExit(
            f"Memory manifest domains must be exactly {expected}; got {actual}"
        )
    root = memory_root(workspace)
    if not root.exists():
        raise SystemExit(f"Missing memory root: {root}")
    required_paths = [
        root / "hot-memory.md",
        root / "link-index.md",
        root / "glacier/index.md",
    ]
    for domain_name, expected_files in DOMAIN_REQUIRED_FILES.items():
        domain = domains.get(domain_name)
        if not isinstance(domain, dict):
            raise SystemExit(f"Memory domain {domain_name} must be a JSON object")
        if domain.get("path") != domain_name:
            raise SystemExit(
                f"Memory domain {domain_name} must use path '{domain_name}'"
            )
        files = domain.get("files")
        if files != expected_files:
            raise SystemExit(
                f"Memory domain {domain_name} files must be {expected_files}; got {files}"
            )
        required_paths.extend(
            root / domain_name / file_name for file_name in expected_files
        )
    missing = [
        str(path.relative_to(workspace)) for path in required_paths if not path.exists()
    ]
    if missing:
        raise SystemExit(f"Missing required memory files: {', '.join(missing)}")
    regular_files = []
    for path in list_memory_markdown_files(workspace):
        relative_path = path.relative_to(root)
        if relative_path.parts[:1] == ("glacier",) and relative_path.name != "index.md":
            continue
        regular_files.append(path)
    missing_l0 = [
        str(path.relative_to(workspace))
        for path in regular_files
        if read_l0_summary(path) is None
    ]
    if missing_l0:
        raise SystemExit(f"Missing L0 headers in memory files: {', '.join(missing_l0)}")
    return {
        "memory_root": str(root.relative_to(workspace)),
        "domain_count": len(domains),
        "domains": list(EXPECTED_DOMAINS),
        "markdown_file_count": len(list_memory_markdown_files(workspace)),
        "archive_file_count": len(collect_archive_rows(workspace)),
    }


def utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Scan: L0 summaries
# ---------------------------------------------------------------------------


def collect_l0_rows(workspace: Path, domain: str | None = None) -> list[dict[str, str]]:
    root = memory_root(workspace)
    rows = []
    for path in list_memory_markdown_files(workspace):
        relative_path = path.relative_to(root)
        if relative_path.parts[:1] == ("glacier",) and relative_path.name != "index.md":
            continue
        if domain and domain != "all":
            if relative_path.parts[:1] == (domain,):
                pass
            elif relative_path.as_posix() != "hot-memory.md":
                continue
        summary = read_l0_summary(path)
        if summary is None:
            continue
        rows.append({"path": str(relative_path), "summary": summary})
    return rows


def run_scan(args: Any) -> int:
    workspace = find_workspace_root()
    rows = collect_l0_rows(workspace, domain=args.domain)
    if args.json:
        print(json.dumps(rows, indent=2, sort_keys=True))
    else:
        for row in rows:
            print(f"{row['path']}: {row['summary']}")
    return 0


# ---------------------------------------------------------------------------
# Validate
# ---------------------------------------------------------------------------


def run_validate(args: Any) -> int:
    workspace = find_workspace_root()
    summary = validate_memory_structure(workspace)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        for key, value in summary.items():
            print(f"{key}: {value}")
    return 0


# ---------------------------------------------------------------------------
# Rebuild glacier index
# ---------------------------------------------------------------------------


def render_glacier_index(rows: list[dict[str, str | int]]) -> str:
    lines = [
        "<!-- L0: Archive catalog for stored memory snapshots -->",
        "# Memory Glacier Index",
        "",
        "<!-- Auto-generated by loom memory rebuild-glacier. Do not edit manually. -->",
        f"<!-- Last updated: {utc_today()} -->",
        "",
        "| File | Domain | Type | Tags | Date Range | Entries | Summary |",
        "|------|--------|------|------|------------|---------|---------|",
    ]
    if rows:
        for row in rows:
            lines.append(
                "| `{path}` | {domain} | {type} | {tags} | {date_range} "
                "| {entries} | {summary} |".format(
                    path=row["path"],
                    domain=row["domain"] or "-",
                    type=row["type"] or "-",
                    tags=row["tags"] or "-",
                    date_range=row["date_range"] or "-",
                    entries=row["entries"],
                    summary=row["summary"] or "-",
                )
            )
    else:
        lines.append("| - | - | - | - | - | 0 | No archived memory files yet. |")
    lines.append("")
    return "\n".join(lines)


def run_rebuild_glacier(args: Any) -> int:
    workspace = find_workspace_root()
    validate_memory_structure(workspace)
    output = memory_root(workspace) / "glacier/index.md"
    rows = collect_archive_rows(workspace)
    output.write_text(render_glacier_index(rows))
    print(output.relative_to(workspace))
    return 0


# ---------------------------------------------------------------------------
# Rebuild link index
# ---------------------------------------------------------------------------


def source_ref_from_path(root: Path, path: Path) -> str:
    relative = path.relative_to(root).as_posix()
    if relative.endswith(".md"):
        relative = relative[:-3]
    return relative


def collect_link_index_rows(workspace: Path) -> list[dict[str, str]]:
    root = memory_root(workspace)
    inbound: dict[str, set[str]] = {}
    for path in list_memory_markdown_files(workspace):
        relative = path.relative_to(root).as_posix()
        if relative.startswith("glacier/"):
            continue
        if relative == "link-index.md":
            continue
        text = path.read_text()
        source = source_ref_from_path(root, path)
        for target in WIKI_LINK_PATTERN.findall(text):
            inbound.setdefault(target, set()).add(source)
    rows = []
    for target in sorted(inbound):
        rows.append(
            {"target": target, "linked_from": ", ".join(sorted(inbound[target]))}
        )
    return rows


def render_link_index(rows: list[dict[str, str]]) -> str:
    lines = [
        "<!-- L0: Backlink map showing which memory files point to which topics -->",
        "# Memory Link Index",
        "",
        "<!-- Auto-generated by loom memory rebuild-links. Do not edit manually. -->",
        f"<!-- Last updated: {utc_today()} -->",
        "",
        "| Target | Linked from |",
        "|--------|-------------|",
    ]
    if rows:
        for row in rows:
            lines.append(f"| `{row['target']}` | `{row['linked_from']}` |")
    else:
        lines.append("| - | No inbound wiki-links yet. |")
    lines.append("")
    return "\n".join(lines)


def run_rebuild_links(args: Any) -> int:
    workspace = find_workspace_root()
    validate_memory_structure(workspace)
    output = memory_root(workspace) / "link-index.md"
    rows = collect_link_index_rows(workspace)
    output.write_text(render_link_index(rows))
    print(output.relative_to(workspace))
    return 0


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------


def register(subparsers: Any) -> None:
    memory_parser = subparsers.add_parser(
        "memory",
        help="Loom memory module operations",
    )
    memory_sub = memory_parser.add_subparsers(dest="memory_command")

    scan = memory_sub.add_parser("scan", help="List L0 summaries from memory files")
    scan.add_argument(
        "--domain",
        choices=["all", *EXPECTED_DOMAINS],
        default="all",
        help="Restrict output to one memory domain",
    )
    scan.add_argument("--json", action="store_true")
    scan.set_defaults(func=run_scan)

    validate = memory_sub.add_parser(
        "validate", help="Validate memory module structure"
    )
    validate.add_argument("--json", action="store_true")
    validate.set_defaults(func=run_validate)

    rebuild_glacier = memory_sub.add_parser(
        "rebuild-glacier", help="Rebuild glacier archive index"
    )
    rebuild_glacier.set_defaults(func=run_rebuild_glacier)

    rebuild_links = memory_sub.add_parser(
        "rebuild-links", help="Rebuild wiki-link backlink index"
    )
    rebuild_links.set_defaults(func=run_rebuild_links)
