from __future__ import annotations

import json
from typing import Any

from agent_loom.core.cli_output import normalize_payload
from agent_loom.workspace.models import (
    AddRepoResult,
    BranchResult,
    ComponentsRefreshIndexResult,
    ContextResult,
    DeepenResult,
    DepsShowResult,
    DepsWhoUsesResult,
    HarnessExecResult,
    HarnessInitResult,
    ImpactResult,
    LeaseAcquireResult,
    LeaseListResult,
    LeaseReleaseResult,
    LeaseRenewResult,
    LeaseShowResult,
    ListReposResult,
    MergeAttemptResult,
    PrimeResult,
    RemoveRepoResult,
    RepoInitResult,
    RepoStatusResult,
    RepoWorktreeAddResult,
    RepoWorktreeEnsureDetachedResult,
    RepoWorktreeListResult,
    RepoWorktreePruneResult,
    RepoWorktreeRemoveResult,
    SnapshotDiffResult,
    SnapshotRestoreResult,
    SnapshotResult,
    StatusResult,
    SyncResult,
    WorktreeAddResult,
    WorktreeDiffResult,
    WorktreeEnsureResult,
    WorktreeGcResult,
    WorktreeGroupDiffResult,
    WorktreeGroupRemoveResult,
    WorktreeListResult,
    WorktreePushResult,
    WorktreeRebaseResult,
)


def render_prime_text(payload: dict[str, Any]) -> str:
    text = str(payload.get("markdown") or "")
    if text:
        return text.rstrip() + "\n"
    return ""


def render_services_index_text(index: dict[str, Any]) -> str:
    components = {}
    if isinstance(index, dict):
        components = index.get("components", {}) or index.get("services", {}) or {}
    lines = [f"Components ({len(components)})"]
    for name in sorted(components.keys()):
        entry = components.get(name) or {}
        deps = ", ".join(entry.get("depends_on", []) or []) or "-"
        ext = ", ".join(entry.get("depends_on_external", []) or []) or "-"
        used_by = ", ".join(entry.get("used_by", []) or []) or "-"
        lines.append(f"- {name} deps: {deps} external: {ext} used_by: {used_by}")
    return "\n".join(lines).rstrip() + "\n"


def _bool(value: bool) -> str:
    return "yes" if value else "no"


def render_text(result: Any) -> str:
    if isinstance(result, WorktreeDiffResult):
        # Raw patch only; keep pipe-friendly.
        chunks: list[str] = []
        for f in result.files:
            p = str((f or {}).get("patch") or "")
            if p:
                chunks.append(p.rstrip("\n") + "\n")
        if not chunks:
            return ""
        return "".join(chunks)

    if isinstance(result, WorktreeGroupDiffResult):
        # Deterministic, repo-separated output.
        lines: list[str] = []
        for row in sorted(
            result.results, key=lambda x: str((x or {}).get("repo") or "")
        ):
            if str((row or {}).get("status") or "") != "ok":
                continue
            repo = str((row or {}).get("repo") or "")
            wt = str((row or {}).get("worktree") or "")
            files = row.get("files") if isinstance(row, dict) else None
            patches: list[str] = []
            if isinstance(files, list):
                for f in files:
                    p = str((f or {}).get("patch") or "")
                    if p:
                        patches.append(p.rstrip("\n") + "\n")
            if not patches:
                continue
            lines.append(f"===== {repo} ({wt}) =====\n")
            lines.extend(patches)
        return "".join(lines)

    if isinstance(result, RepoStatusResult):
        return (
            "\n".join(
                [
                    f"repo: {result.repo_root}",
                    f"branch: {result.branch}",
                    f"commit: {result.commit}",
                    f"dirty: {_bool(result.dirty)}",
                    f"default_branch: {result.default_branch}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, RepoWorktreeAddResult):
        return (
            "\n".join(
                [
                    f"branch: {result.branch}",
                    f"path: {result.path}",
                    f"existed: {_bool(result.existed)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, WorktreeEnsureResult):
        return (
            "\n".join(
                [
                    f"branch: {result.branch}",
                    f"path: {result.path}",
                    f"existed: {_bool(result.existed)}",
                    f"reused: {_bool(result.reused)}",
                    f"base_ref: {result.base_ref}",
                    f"base_branch: {result.base_branch}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, RepoWorktreeRemoveResult):
        lines = [f"removed: {result.removed}"]
        if result.branch:
            lines.append(f"branch: {result.branch}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, RepoWorktreePruneResult):
        return f"pruned: {_bool(result.pruned)}\n"

    if isinstance(result, RepoWorktreeEnsureDetachedResult):
        return (
            "\n".join(
                [
                    f"path: {result.path}",
                    f"ref: {result.ref}",
                    f"commit: {result.commit}",
                    f"existed: {_bool(result.existed)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, RepoWorktreeListResult):
        lines = ["worktrees:"]
        for row in result.worktrees:
            path = row.get("path", "")
            branch = row.get("branch") or "(detached)"
            head = row.get("head", "")
            flags: list[str] = []
            if row.get("detached"):
                flags.append("detached")
            if row.get("locked"):
                flags.append("locked")
            tail = f" ({', '.join(flags)})" if flags else ""
            lines.append(f"- {path} {branch} {head}{tail}".rstrip())
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, MergeAttemptResult):
        lines = [
            f"merged: {_bool(result.merged)}",
            f"worktree: {result.worktree}",
            f"base: {result.base}",
            f"base_commit: {result.base_commit}",
            f"topic: {result.topic}",
        ]
        if result.merge_commit:
            lines.append(f"merge_commit: {result.merge_commit}")
        if result.error:
            lines.append(f"error: {result.error}")
        if result.hint:
            lines.append(f"hint: {result.hint}")
        if result.stdout:
            lines.append(f"stdout: {result.stdout}")
        if result.stderr:
            lines.append(f"stderr: {result.stderr}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, HarnessInitResult):
        return (
            "\n".join(
                [
                    f"workspace_file: {result.workspace_file}",
                    f"repos_dir: {result.repos_dir}",
                    f"worktrees_dir: {result.worktrees_dir}",
                    f"states_dir: {result.states_dir}",
                    f"components_dir: {result.components_dir}",
                    f"gitignore_path: {result.gitignore_path}",
                    f"updated_gitignore: {_bool(bool(result.updated_gitignore))}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, RepoInitResult):
        return (
            "\n".join(
                [
                    f"repo_root: {result.repo_root}",
                    f"internal_dir: {result.internal_dir}",
                    f"worktrees_dir: {result.worktrees_dir}",
                    f"git_exclude_path: {result.git_exclude_path}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, HarnessExecResult):
        s = result.summary or {}
        return (
            "\n".join(
                [
                    f"repos: {s.get('repos')}",
                    f"success: {s.get('success')}",
                    f"fail: {s.get('fail')}",
                    f"skip: {s.get('skip')}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, LeaseAcquireResult):
        return (
            "\n".join(
                [
                    f"key: {result.key}",
                    f"lease_path: {result.lease_path}",
                    f"existed: {_bool(result.existed)}",
                    f"forced: {_bool(result.forced)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, LeaseReleaseResult):
        return (
            "\n".join(
                [
                    f"key: {result.key}",
                    f"lease_path: {result.lease_path}",
                    f"released: {_bool(result.released)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, LeaseListResult):
        keys: list[str] = []
        for row in result.leases or []:
            if not isinstance(row, dict):
                continue
            data = row.get("data")
            if not isinstance(data, dict):
                continue
            k = str(data.get("key") or "").strip()
            if k:
                keys.append(k)
        keys = sorted(set(keys))

        lines = [
            f"leases_dir: {result.leases_dir}",
            f"leases: {len(keys)}",
        ]
        if int(getattr(result, "pruned_expired", 0)):
            lines.append(f"pruned_expired: {int(getattr(result, 'pruned_expired', 0))}")
        for k in keys:
            lines.append(f"- {k}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, LeaseShowResult):
        lines = [
            f"key: {result.key}",
            f"lease_path: {result.lease_path}",
            f"exists: {_bool(result.exists)}",
            f"active: {_bool(result.active)}",
        ]
        ttl = (result.data or {}).get("ttl_seconds")
        if ttl is not None:
            lines.append(f"ttl_seconds: {ttl}")
        owner = (result.data or {}).get("owner")
        if isinstance(owner, dict):
            u = str(owner.get("user") or "").strip()
            h = str(owner.get("host") or "").strip()
            if u or h:
                lines.append(f"owner: {u}@{h}".rstrip("@"))
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, LeaseRenewResult):
        ttl = (result.data or {}).get("ttl_seconds")
        lines = [
            f"key: {result.key}",
            f"lease_path: {result.lease_path}",
            f"renewed: {_bool(result.renewed)}",
        ]
        if ttl is not None:
            lines.append(f"ttl_seconds: {ttl}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreeGcResult):
        return (
            "\n".join(
                [
                    f"removed: {len(result.removed)}",
                    f"skipped: {len(result.skipped)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, AddRepoResult):
        lines = [f"repo: {result.repo}", f"cloned: {_bool(result.cloned)}"]
        entry = result.entry or {}
        for key in ("remote", "default_branch", "shallow", "depth"):
            if key in entry:
                lines.append(f"{key}: {entry.get(key)}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, RemoveRepoResult):
        return (
            "\n".join(
                [
                    f"repo: {result.repo}",
                    f"deleted_clone: {_bool(result.deleted_clone)}",
                    f"deleted_component_md: {_bool(result.deleted_component_md)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, ListReposResult):
        lines = [f"repos: {len(result.repos)}"]
        for row in result.repos:
            name = row.get("name")
            remote = row.get("remote")
            default_branch = row.get("default_branch")
            tags = ",".join(row.get("tags") or []) or "-"
            desc = row.get("description") or ""
            bits = [str(name), f"({default_branch})", str(remote), f"tags:{tags}"]
            if desc:
                bits.append(f"desc:{desc}")
            lines.append("- " + " ".join(bits))
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, SyncResult):
        lines = [f"repos: {len(result.results)}"]
        for row in result.results:
            name = row.get("repo")
            actions = ",".join(row.get("actions") or [])
            warnings = "; ".join(row.get("warnings") or [])
            parts = [f"- {name}"]
            if actions:
                parts.append(f"actions:{actions}")
            if warnings:
                parts.append(f"warnings:{warnings}")
            if row.get("error"):
                parts.append(f"error:{row.get('error')}")
            lines.append(" ".join(parts))
        if result.components_index is not None:
            lines.append("components_index: refreshed")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, StatusResult):
        lines = [f"repos: {len(result.repos)}"]
        for row in result.repos:
            lines.append(
                f"- {row.get('repo')} {row.get('branch')} {row.get('sha')} {row.get('status')}"
            )
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, BranchResult):
        lines = [f"branch: {result.branch}"]
        for row in result.repos:
            lines.append(f"- {row.get('repo')} {row.get('branch')}")
        if result.components_index is not None:
            lines.append("components_index: refreshed")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreeAddResult):
        lines = [f"group: {result.group}"]
        for row in result.worktrees:
            lines.append(
                f"- {row.get('repo')} {row.get('path')} existed:{_bool(bool(row.get('existed')))}"
            )
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreeGroupRemoveResult):
        lines = [f"group: {result.group}", f"removed: {len(result.removed)}"]
        for path in result.removed:
            lines.append(f"- {path}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreeListResult):
        lines = [f"worktrees: {len(result.worktrees)}"]
        for row in result.worktrees:
            lines.append(
                f"- {row.get('group')} {row.get('repo')} {row.get('branch')} {row.get('sha')} {row.get('status')}"
            )
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreeRebaseResult):
        lines = [f"group: {result.group}"]
        for row in result.results:
            parts = [f"- {row.get('repo')}", str(row.get("status"))]
            if row.get("onto"):
                parts.append(f"onto:{row.get('onto')}")
            if row.get("reason"):
                parts.append(f"reason:{row.get('reason')}")
            lines.append(" ".join(parts))
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, WorktreePushResult):
        lines = [f"group: {result.group}"]
        for row in result.results:
            parts = [f"- {row.get('repo')}", str(row.get("status"))]
            if row.get("reason"):
                parts.append(f"reason:{row.get('reason')}")
            if row.get("branch"):
                parts.append(f"branch:{row.get('branch')}")
            lines.append(" ".join(parts))
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, SnapshotResult):
        repo_count = len(result.snapshot.get("repos", {}))
        return (
            "\n".join(
                [
                    f"snapshot_path: {result.snapshot_path}",
                    f"repos: {repo_count}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, SnapshotDiffResult):
        s = result.summary or {}
        return (
            "\n".join(
                [
                    f"snapshot_path: {result.snapshot_path}",
                    f"repos: {s.get('repos')}",
                    f"match: {s.get('match')}",
                    f"changed: {s.get('changed')}",
                    f"missing: {s.get('missing')}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, SnapshotRestoreResult):
        s = result.summary or {}
        return (
            "\n".join(
                [
                    f"snapshot_path: {result.snapshot_path}",
                    f"repos: {s.get('repos')}",
                    f"success: {s.get('success')}",
                    f"skipped: {s.get('skipped')}",
                    f"failed: {s.get('failed')}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, ComponentsRefreshIndexResult):
        components = (
            result.index.get("components", {}) if isinstance(result.index, dict) else {}
        )
        return (
            "\n".join(
                [
                    f"components_index_path: {result.components_index_path}",
                    f"components: {len(components)}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, DepsShowResult):
        data = result.data or {}
        deps = ", ".join(data.get("depends_on", []) or []) or "-"
        ext = ", ".join(data.get("depends_on_external", []) or []) or "-"
        used_by = ", ".join(data.get("used_by", []) or []) or "-"
        return (
            "\n".join(
                [
                    f"component: {result.component}",
                    f"depends_on: {deps}",
                    f"depends_on_external: {ext}",
                    f"used_by: {used_by}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, DepsWhoUsesResult):
        used_by = ", ".join(result.used_by or []) or "-"
        return (
            "\n".join(
                [
                    f"component: {result.component}",
                    f"used_by: {used_by}",
                ]
            ).rstrip()
            + "\n"
        )

    if isinstance(result, ImpactResult):
        src = result.source or {}
        out_lines: list[str] = []
        kind = str(src.get("kind") or "").strip()
        if kind:
            out_lines.append(f"source: {kind}")
        if kind == "snapshot":
            name = str(src.get("name") or "").strip()
            if name:
                out_lines.append(f"snapshot: {name}")

        out_lines.append(f"changed: {len(result.changed)}")
        for s in result.changed:
            out_lines.append(f"- {s}")
        if result.unknown:
            out_lines.append(f"unknown: {len(result.unknown)}")
            for s in result.unknown:
                out_lines.append(f"- {s}")
        out_lines.append(f"impacted: {len(result.impacted)}")
        for s in result.impacted:
            out_lines.append(f"- {s}")
        out_lines.append(f"all: {len(result.all)}")
        return "\n".join(out_lines).rstrip() + "\n"

    if isinstance(result, DeepenResult):
        lines = [f"repo: {result.repo}"]
        if result.skipped:
            lines.append("skipped: yes")
            if result.reason:
                lines.append(f"reason: {result.reason}")
        else:
            lines.append(f"depth: {result.depth}")
        return "\n".join(lines).rstrip() + "\n"

    if isinstance(result, PrimeResult):
        return render_prime_text(result.payload)

    if isinstance(result, ContextResult):
        payload = normalize_payload(result)
        return json.dumps(payload, indent=2, sort_keys=True) + "\n"

    payload = normalize_payload(result)
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"



__all__ = ['render_prime_text', 'render_services_index_text', 'render_text']
