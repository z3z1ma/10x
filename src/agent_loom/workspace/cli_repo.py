from __future__ import annotations

from typing import Any

from agent_loom.workspace.commands.core import cmd_prime
from agent_loom.workspace.commands.repo import (
    cmd_repo_cleanup_apply,
    cmd_repo_cleanup_suggest,
    cmd_repo_init,
    cmd_repo_merge_attempt,
    cmd_repo_sandbox_create,
    cmd_repo_sandbox_gc,
    cmd_repo_sandbox_promote,
    cmd_repo_snapshot_capture,
    cmd_repo_snapshot_diff,
    cmd_repo_snapshot_restore,
    cmd_repo_status,
    cmd_repo_worktree_add,
    cmd_repo_worktree_annotate,
    cmd_repo_worktree_check_clean,
    cmd_repo_worktree_check_divergence,
    cmd_repo_worktree_diff,
    cmd_repo_worktree_ensure,
    cmd_repo_worktree_ensure_detached,
    cmd_repo_worktree_ls,
    cmd_repo_worktree_prune,
    cmd_repo_worktree_rm,
    cmd_repo_worktree_rm_path,
    cmd_repo_worktree_status,
)
from agent_loom.workspace.constants import REPO_INTERNAL_DIR


def add_repo_mode_parsers(sub: Any) -> None:
    sp = sub.add_parser("prime", help="Operating manual + canonical examples")
    sp.set_defaults(func=cmd_prime)

    sp = sub.add_parser("status", help="Show branch/sha/dirty for this repo")
    sp.set_defaults(func=cmd_repo_status)

    sp = sub.add_parser(
        "init",
        help=f"Initialize {REPO_INTERNAL_DIR}/worktrees and ignore bookkeeping",
    )
    sp.set_defaults(func=cmd_repo_init)

    sp = sub.add_parser("worktree", help="Worktree operations (single repo)")
    sub2 = sp.add_subparsers(dest="worktree_cmd", required=True)

    sp2 = sub2.add_parser(
        "add",
        help=f"Add a worktree for a branch under {REPO_INTERNAL_DIR}/worktrees/<branch>",
    )
    sp2.add_argument("branch")
    sp2.add_argument("--base-ref", help="Base ref for new branch")
    sp2.add_argument("--path", help="Override destination path")
    sp2.set_defaults(func=cmd_repo_worktree_add)

    sp2 = sub2.add_parser(
        "ensure",
        help=f"Ensure a branch worktree exists (resumable) under {REPO_INTERNAL_DIR}/worktrees/<branch>",
    )
    sp2.add_argument("branch")
    sp2.add_argument("--path", required=False, help="Destination path (optional)")
    sp2.add_argument("--base-ref", help="Base ref for new branch")
    sp2.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow returning an existing worktree with uncommitted changes",
    )
    sp2.set_defaults(func=cmd_repo_worktree_ensure)

    sp2 = sub2.add_parser("status", help="Show branch/sha/dirty for a worktree")
    sp2.add_argument(
        "--worktree",
        default="",
        help="Branch name or path (default: repo root)",
    )
    sp2.set_defaults(func=cmd_repo_worktree_status)

    sp2 = sub2.add_parser("check-clean", help="Fail if a worktree is dirty")
    sp2.add_argument(
        "--worktree",
        default="",
        help="Branch name or path (default: repo root)",
    )
    sp2.add_argument(
        "--allow-untracked",
        action="store_true",
        help="Ignore untracked files when determining cleanliness",
    )
    sp2.set_defaults(func=cmd_repo_worktree_check_clean)

    sp2 = sub2.add_parser(
        "check-divergence", help="Ahead/behind vs --base for a worktree"
    )
    sp2.add_argument("--base", required=True, help="Base ref-ish")
    sp2.add_argument(
        "--worktree",
        default="",
        help="Branch name or path (default: repo root)",
    )
    sp2.set_defaults(func=cmd_repo_worktree_check_divergence)

    sp2 = sub2.add_parser("diff", help="Print a worktree diff (tracked files)")
    sp2.add_argument(
        "--mode",
        default="dirty",
        choices=["dirty", "cumulative"],
        help="Diff mode: dirty (uncommitted) or cumulative (merge-base)",
    )
    sp2.add_argument(
        "--worktree",
        default="",
        help="Branch name or path (default: repo root)",
    )
    sp2.add_argument(
        "--base",
        default="",
        help="Base ref-ish (default: HEAD when available)",
    )
    sp2.add_argument(
        "--max-bytes",
        dest="max_bytes",
        type=int,
        default=2_000_000,
        help="Max patch bytes to include (default: 2000000)",
    )
    sp2.set_defaults(func=cmd_repo_worktree_diff)

    sp2 = sub2.add_parser(
        "annotate", help="Annotate a branch worktree with purpose/ttl"
    )
    sp2.add_argument("branch")
    sp2.add_argument("--purpose", required=True)
    sp2.add_argument("--ticket", default="")
    sp2.add_argument("--owner", default="")
    sp2.add_argument("--ttl", default="")
    sp2.add_argument("--kind", default="normal", choices=["normal", "sandbox"])
    sp2.set_defaults(func=cmd_repo_worktree_annotate)

    sp2 = sub2.add_parser("rm", help="Remove a worktree for a branch (requires --yes)")
    sp2.add_argument("branch")
    sp2.add_argument("--yes", action="store_true", help="Confirm deletion")
    sp2.add_argument(
        "--force", action="store_true", help="Pass --force to git worktree remove"
    )
    sp2.set_defaults(func=cmd_repo_worktree_rm)

    sp2 = sub2.add_parser("rm-path", help="Remove a worktree by path (requires --yes)")
    sp2.add_argument("path")
    sp2.add_argument("--yes", action="store_true", help="Confirm deletion")
    sp2.add_argument(
        "--force", action="store_true", help="Pass --force to git worktree remove"
    )
    sp2.set_defaults(func=cmd_repo_worktree_rm_path)

    sp2 = sub2.add_parser("prune", help="Prune stale git worktree metadata")
    sp2.set_defaults(func=cmd_repo_worktree_prune)

    sp2 = sub2.add_parser(
        "ensure-detached",
        help="Ensure a detached worktree exists at a path",
    )
    sp2.add_argument("--path", required=True, help="Destination path")
    sp2.add_argument(
        "--ref", required=True, help="Ref-ish (branch, origin/branch, SHA)"
    )
    sp2.set_defaults(func=cmd_repo_worktree_ensure_detached)

    sp2 = sub2.add_parser("ls", help="List worktrees")
    sp2.set_defaults(func=cmd_repo_worktree_ls)

    sp = sub.add_parser("merge", help="Merge helpers (single repo)")
    subm = sp.add_subparsers(dest="merge_cmd", required=True)

    spm = subm.add_parser(
        "attempt",
        help="Attempt a local merge in a dedicated worktree (returns merged=true/false)",
    )
    spm.add_argument("--worktree", required=True, help="Worktree path")
    spm.add_argument("--base", required=True, help="Base ref-ish")
    spm.add_argument("--topic", required=True, help="Topic ref/branch")
    spm.add_argument(
        "--force-clean",
        action="store_true",
        help="Hard reset + clean the worktree before merging",
    )
    spm.set_defaults(func=cmd_repo_merge_attempt)

    sp = sub.add_parser("cleanup", help="Suggest/apply safe worktree cleanup")
    subc = sp.add_subparsers(dest="cleanup_cmd", required=True)

    spc = subc.add_parser("suggest", help="Suggest cleanup candidates")
    spc.set_defaults(func=cmd_repo_cleanup_suggest)

    spa = subc.add_parser("apply", help="Apply cleanup (requires --yes)")
    spa.add_argument(
        "--id", action="append", default=[], help="Candidate id (repeatable)"
    )
    spa.add_argument("--force", action="store_true", help="Force git worktree remove")
    spa.add_argument("--yes", action="store_true")
    spa.set_defaults(func=cmd_repo_cleanup_apply)

    sp = sub.add_parser("sandbox", help="Create/promote/gc sandbox worktrees")
    subs = sp.add_subparsers(dest="sandbox_cmd", required=True)

    spc = subs.add_parser("create", help="Create a sandbox worktree")
    spc.add_argument("--base", required=True, help="Base ref-ish")
    spc.add_argument("--name", default="", help="Optional sandbox name")
    spc.add_argument("--ttl", default="2h")
    spc.add_argument("--purpose", default="sandbox")
    spc.set_defaults(func=cmd_repo_sandbox_create)

    spp = subs.add_parser("promote", help="Promote a sandbox branch")
    spp.add_argument("--from", dest="from_branch", required=True)
    spp.add_argument("--to", dest="to_branch", required=True)
    spp.set_defaults(func=cmd_repo_sandbox_promote)

    spg = subs.add_parser(
        "gc", help="Remove expired sandbox worktrees (requires --yes)"
    )
    spg.add_argument("--force", action="store_true")
    spg.add_argument("--yes", action="store_true")
    spg.set_defaults(func=cmd_repo_sandbox_gc)

    sp = sub.add_parser("snapshot", help="Snapshot/compare/restore repo/worktree state")
    subs = sp.add_subparsers(dest="snapshot_cmd", required=True)

    spc = subs.add_parser("capture", help="Capture a snapshot")
    spc.add_argument("name")
    spc.add_argument(
        "--worktree",
        default="",
        help="Branch name or path (default: repo root)",
    )
    spc.set_defaults(func=cmd_repo_snapshot_capture)

    spd = subs.add_parser("diff", help="Diff current vs snapshot")
    spd.add_argument("name")
    spd.set_defaults(func=cmd_repo_snapshot_diff)

    spr = subs.add_parser("restore", help="Restore snapshot (requires --yes)")
    spr.add_argument("name")
    spr.add_argument("--yes", action="store_true")
    spr.add_argument("--force-clean", action="store_true")
    spr.set_defaults(func=cmd_repo_snapshot_restore)

    return None


__all__ = ["add_repo_mode_parsers"]
