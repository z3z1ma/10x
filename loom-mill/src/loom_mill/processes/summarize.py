from __future__ import annotations

import asyncio
import json
from dataclasses import asdict, dataclass
from pathlib import Path


TRACKED_LABELS = {
    "ID": "id",
    "Type": "type",
    "Status": "status",
    "Created": "created",
    "Updated": "updated",
    "Risk": "risk",
    "Priority": "priority",
    "Depends On": "depends_on",
}


@dataclass(frozen=True)
class FileChangeSummary:
    count: int
    paths: list[str]
    stat: str


@dataclass(frozen=True)
class ChangedRecord:
    path: str
    record_id: str | None
    changed_fields: list[str]


@dataclass(frozen=True)
class IterationSummary:
    label: str
    ticket_slug: str
    iteration: int
    exit_code: int | None
    duration_seconds: float
    files_changed: FileChangeSummary
    records_changed: list[ChangedRecord]
    storage_path: str


async def summarize_iteration(
    *,
    workspace_root: Path,
    worktree_path: Path,
    ticket_slug: str,
    iteration: int,
    exit_code: int | None,
    duration_seconds: float,
) -> IterationSummary:
    changed_paths = await _changed_paths(worktree_path)
    files_changed = FileChangeSummary(
        count=len(changed_paths),
        paths=changed_paths,
        stat=await _git_output(worktree_path, "diff", "--stat", "HEAD"),
    )
    records_changed = [
        await _record_change(worktree_path, path)
        for path in changed_paths
        if path.startswith(".loom/") and path.endswith(".md")
    ]

    storage_path = workspace_root / ".mill" / "summaries" / ticket_slug / f"iteration-{iteration}.json"
    summary = IterationSummary(
        label="iteration summary (visibility output, not evidence, audit, or acceptance)",
        ticket_slug=ticket_slug,
        iteration=iteration,
        exit_code=exit_code,
        duration_seconds=round(duration_seconds, 3),
        files_changed=files_changed,
        records_changed=records_changed,
        storage_path=str(storage_path),
    )
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    storage_path.write_text(json.dumps(asdict(summary), indent=2) + "\n", encoding="utf-8")
    return summary


async def _changed_paths(worktree_path: Path) -> list[str]:
    tracked = await _git_lines(worktree_path, "diff", "--name-only", "HEAD")
    untracked = await _git_lines(worktree_path, "ls-files", "--others", "--exclude-standard")
    return sorted(dict.fromkeys([*tracked, *untracked]))


async def _record_change(worktree_path: Path, path: str) -> ChangedRecord:
    current_path = worktree_path / path
    previous = await _git_output(worktree_path, "show", f"HEAD:{path}", check=False)
    current = current_path.read_text(encoding="utf-8") if current_path.exists() else ""
    previous_labels = _labels(previous) if previous else {}
    current_labels = _labels(current) if current else {}

    record_id = current_labels.get("id") or previous_labels.get("id")
    if not previous:
        changed_fields = ["created"]
    elif not current:
        changed_fields = ["removed"]
    else:
        changed_fields = sorted(
            field
            for field in set(previous_labels) | set(current_labels)
            if previous_labels.get(field) != current_labels.get(field)
        )
        if not changed_fields and previous != current:
            changed_fields = ["body"]

    return ChangedRecord(path=path, record_id=record_id, changed_fields=changed_fields)


def _labels(text: str) -> dict[str, str]:
    labels: dict[str, str] = {}
    for line in text.splitlines():
        for prefix, field in TRACKED_LABELS.items():
            marker = f"{prefix}:"
            if line.startswith(marker):
                labels[field] = line[len(marker) :].strip()
                break
    return labels


async def _git_lines(worktree_path: Path, *args: str) -> list[str]:
    output = await _git_output(worktree_path, *args)
    return [line for line in output.splitlines() if line]


async def _git_output(worktree_path: Path, *args: str, check: bool = True) -> str:
    process = await asyncio.create_subprocess_exec(
        "git",
        *args,
        cwd=worktree_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if check and process.returncode != 0:
        message = stderr.decode(errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {message}")
    if process.returncode != 0:
        return ""
    return stdout.decode(errors="replace").strip()
