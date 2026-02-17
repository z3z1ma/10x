from __future__ import annotations

import argparse
from typing import Any

from agent_loom.workspace.commands.core import (
    cmd_add,
    cmd_branch,
    cmd_context,
    cmd_deepen,
    cmd_list,
    cmd_remove,
    cmd_snapshot_capture,
    cmd_snapshot_diff,
    cmd_snapshot_restore,
    cmd_status,
    cmd_sync,
)
from agent_loom.workspace.commands.deps import (
    cmd_components_refresh_index,
    cmd_deps_closure,
    cmd_deps_impacted,
    cmd_deps_show,
    cmd_deps_who_uses,
    cmd_services_refresh_index,
)
from agent_loom.workspace.commands.harness import (
    cmd_harness_cleanup_apply,
    cmd_harness_cleanup_suggest,
    cmd_harness_exec,
    cmd_harness_impact_repos,
    cmd_harness_impact_snapshot,
    cmd_harness_init,
    cmd_harness_repo_edit,
    cmd_harness_sandbox_create,
    cmd_harness_sandbox_gc,
    cmd_harness_sandbox_promote,
    cmd_harness_set_ls,
    cmd_harness_set_rm,
    cmd_harness_set_show,
    cmd_harness_set_upsert,
)
from agent_loom.workspace.commands.lease import (
    cmd_lease_acquire,
    cmd_lease_ls,
    cmd_lease_release,
    cmd_lease_renew,
    cmd_lease_show,
)
from agent_loom.workspace.commands.worktree import (
    cmd_worktree_add,
    cmd_worktree_gc,
    cmd_worktree_group_annotate,
    cmd_worktree_group_check_clean,
    cmd_worktree_group_check_divergence,
    cmd_worktree_group_diff,
    cmd_worktree_group_status,
    cmd_worktree_ls,
    cmd_worktree_prune,
    cmd_worktree_push,
    cmd_worktree_rebase,
    cmd_worktree_rm,
)


def _add_selection_flags(
    parser: argparse.ArgumentParser,
    *,
    include_all: bool,
    repos_help: str,
) -> None:
    if include_all:
        parser.add_argument(
            "--all",
            action="store_true",
            help="Confirm operating on multiple repos when no selection is provided",
        )
    parser.add_argument("--repos", nargs="*", help=repos_help)
    parser.add_argument(
        "--set", dest="sets", action="append", help="Select repos by set"
    )
    parser.add_argument(
        "--tag", dest="tags", action="append", help="Select repos by tag"
    )


def _add_repo_parsers(sub: Any) -> None:
    sp = sub.add_parser("repo", help="Edit workspace repo metadata")
    sub_repo = sp.add_subparsers(dest="repo_cmd", required=True)

    spe = sub_repo.add_parser("edit", help="Edit a repo entry in workspace.json")
    spe.add_argument("name")
    spe.add_argument("--remote", default=None)
    spe.add_argument("--default-branch", dest="default_branch", default=None)
    spe.add_argument("--description", default=None)
    spe.add_argument("--add-tag", action="append", default=[])
    spe.add_argument("--rm-tag", action="append", default=[])
    sh = spe.add_mutually_exclusive_group()
    sh.add_argument("--shallow", action="store_true")
    sh.add_argument("--no-shallow", dest="no_shallow", action="store_true")
    spe.add_argument("--depth", type=int, default=None)
    spe.set_defaults(func=cmd_harness_repo_edit)


def _add_set_parsers(sub: Any) -> None:
    sp = sub.add_parser("set", help="Manage repo sets (workspace.json repo_sets)")
    sub_set = sp.add_subparsers(dest="set_cmd", required=True)

    sps = sub_set.add_parser("upsert", help="Create/update a repo set")
    sps.add_argument("name")
    sps.add_argument("items", nargs="*")
    sps.set_defaults(func=cmd_harness_set_upsert)

    sps = sub_set.add_parser("rm", help="Remove a repo set")
    sps.add_argument("name")
    sps.set_defaults(func=cmd_harness_set_rm)

    sps = sub_set.add_parser("show", help="Show a repo set")
    sps.add_argument("name")
    sps.set_defaults(func=cmd_harness_set_show)

    sps = sub_set.add_parser("ls", help="List repo sets")
    sps.set_defaults(func=cmd_harness_set_ls)


def _add_lease_parsers(sub: Any) -> None:
    sp = sub.add_parser(
        "lease",
        help="Coordination leases (optional in-use marker + exclusive coordination lock)",
    )
    sub_lease = sp.add_subparsers(dest="lease_cmd", required=True)

    spl = sub_lease.add_parser(
        "acquire",
        help="Acquire a lease key (marks resource in-use; can prevent cleanup/GC)",
    )
    spl.add_argument("key")
    spl.add_argument(
        "--ttl",
        default="",
        help="Lease TTL (default 8h; use 'none' for no expiry)",
    )
    spl.add_argument(
        "--force",
        action="store_true",
        help="Steal an existing lease (override another owner)",
    )
    spl.set_defaults(func=cmd_lease_acquire)

    spl = sub_lease.add_parser("release", help="Release a lease key")
    spl.add_argument("key")
    spl.set_defaults(func=cmd_lease_release)

    spl = sub_lease.add_parser(
        "renew",
        help="Renew a lease (bump updated_at; optionally change TTL)",
    )
    spl.add_argument("key")
    spl.add_argument(
        "--ttl",
        default="",
        help="Lease TTL (default 8h; use 'none' for no expiry)",
    )
    spl.set_defaults(func=cmd_lease_renew)

    spl = sub_lease.add_parser("show", help="Show a lease (prunes if expired)")
    spl.add_argument("key")
    spl.set_defaults(func=cmd_lease_show)

    spl = sub_lease.add_parser("ls", help="List leases")
    spl.set_defaults(func=cmd_lease_ls)


def _add_worktree_parsers(sub: Any) -> None:
    sp = sub.add_parser("worktree", help="Worktree operations")
    sub2 = sp.add_subparsers(dest="worktree_cmd", required=True)

    _add_worktree_create_parser(
        sub2,
        command="add",
        help_text="Add worktrees under worktrees/<group>/<repo>",
    )
    _add_worktree_create_parser(
        sub2,
        command="ensure",
        help_text="Ensure worktrees exist under worktrees/<group>/<repo> (resumable)",
    )

    sp2 = sub2.add_parser(
        "rm", help="Remove worktrees for a group (optionally subset repos)"
    )
    sp2.add_argument("group")
    sp2.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before deleting worktrees (example: group:<group>)",
    )
    sp2.add_argument(
        "--yes",
        action="store_true",
        help="Confirm deletion (required)",
    )
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.add_argument(
        "--force",
        action="store_true",
        help="Force removal even if worktree has local changes",
    )
    sp2.set_defaults(func=cmd_worktree_rm)

    sp2 = sub2.add_parser(
        "ls", help="List all worktrees with group/repo/branch/sha/status"
    )
    sp2.set_defaults(func=cmd_worktree_ls)

    sp2 = sub2.add_parser("prune", help="Prune stale git worktree metadata in repos")
    _add_selection_flags(
        sp2, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp2.set_defaults(func=cmd_worktree_prune)

    sp2 = sub2.add_parser("status", help="Show status for a worktree group")
    sp2.add_argument("group")
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.set_defaults(func=cmd_worktree_group_status)

    sp2 = sub2.add_parser(
        "diff",
        help="Print per-repo worktree diffs for a group (tracked files; requires explicit intent)",
    )
    sp2.add_argument("group")
    sp2.add_argument(
        "--mode",
        default="dirty",
        choices=["dirty", "cumulative"],
        help="Diff mode: dirty (uncommitted) or cumulative (merge-base)",
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
        help="Max patch bytes per repo (default: 2000000)",
    )
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.set_defaults(func=cmd_worktree_group_diff)

    sp2 = sub2.add_parser("check-clean", help="Fail if any group worktree is dirty")
    sp2.add_argument("group")
    sp2.add_argument(
        "--allow-untracked",
        action="store_true",
        help="Ignore untracked files when determining cleanliness",
    )
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.set_defaults(func=cmd_worktree_group_check_clean)

    sp2 = sub2.add_parser(
        "check-divergence", help="Ahead/behind vs --base for group worktrees"
    )
    sp2.add_argument("group")
    sp2.add_argument("--base", required=True, help="Base ref-ish")
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.set_defaults(func=cmd_worktree_group_check_divergence)

    sp2 = sub2.add_parser("annotate", help="Annotate a group with purpose/ttl")
    sp2.add_argument("group")
    sp2.add_argument("--purpose", required=True)
    sp2.add_argument("--ticket", default="")
    sp2.add_argument("--owner", default="")
    sp2.add_argument("--ttl", default="")
    sp2.add_argument("--kind", default="normal", choices=["normal", "sandbox"])
    sp2.set_defaults(func=cmd_worktree_group_annotate)

    sp2 = sub2.add_parser(
        "rebase", help="Rebase worktrees for a group onto their base branch"
    )
    sp2.add_argument("group")
    sp2.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before rebasing worktrees (example: group:<group>)",
    )
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )
    sp2.add_argument("--base-ref", help="Base ref (default origin/<default_branch>)")
    sp2.set_defaults(func=cmd_worktree_rebase)

    sp2 = sub2.add_parser(
        "push", help="Push worktrees for a group to their remote branch"
    )
    sp2.add_argument("group")
    sp2.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before pushing worktrees (example: group:<group>)",
    )
    _add_selection_flags(
        sp2,
        include_all=True,
        repos_help="Subset of repos (default: all under group)",
    )

    push_mode = sp2.add_mutually_exclusive_group()
    push_mode.add_argument(
        "-u", "--set-upstream", action="store_true", help="Set upstream tracking branch"
    )
    push_mode.add_argument(
        "--force", action="store_true", help="Force push (use with caution)"
    )
    push_mode.add_argument(
        "--force-with-lease", action="store_true", help="Force push with lease (safer)"
    )
    sp2.add_argument(
        "--yes",
        action="store_true",
        help="Confirm destructive operations (required with --force/--force-with-lease)",
    )
    sp2.set_defaults(func=cmd_worktree_push)

    sp2 = sub2.add_parser(
        "gc",
        help="Garbage collect old worktrees (requires --yes; optionally skip leased groups)",
    )
    sp2.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before running GC",
    )
    sp2.add_argument(
        "--older-than",
        type=int,
        default=0,
        help="Only remove groups older than N days (0 = no age filter)",
    )
    sp2.add_argument(
        "--skip-leased",
        action="store_true",
        help="Skip groups that have an active group:<name> lease",
    )
    sp2.add_argument(
        "--force",
        action="store_true",
        help="Force removal even if worktrees have local changes",
    )
    sp2.add_argument("--yes", action="store_true", help="Confirm deletions")
    sp2.set_defaults(func=cmd_worktree_gc)


def _add_worktree_create_parser(sub2: Any, *, command: str, help_text: str) -> None:
    sp2 = sub2.add_parser(command, help=help_text)
    sp2.add_argument("group")
    sp2.add_argument(
        "--path",
        default="",
        help="Override group worktrees base dir (creates worktrees under <path>/<repo>)",
    )
    _add_selection_flags(
        sp2, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp2.add_argument("--base-ref", help="Base ref (default origin/<default_branch>)")
    sp2.add_argument(
        "--clone", action="store_true", help="Clone missing repos automatically"
    )
    sp2.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow checking out a safe branch when local changes exist",
    )
    sp2.set_defaults(func=cmd_worktree_add)


def _add_snapshot_parsers(sub: Any) -> None:
    sp = sub.add_parser(
        "snapshot", help="Snapshot/compare/restore repo or worktree state"
    )
    sub_snap = sp.add_subparsers(dest="snapshot_cmd", required=True)

    spc = sub_snap.add_parser(
        "capture",
        help="Write states/<name>.json with branch/sha/dirty per repo (or per worktree group)",
    )
    spc.add_argument("name")
    spc.add_argument(
        "--group",
        default=None,
        help="Capture from worktrees/<group>/<repo> instead of repos/<repo>",
    )
    _add_selection_flags(
        spc, include_all=True, repos_help="Subset of repos (default all)"
    )
    spc.set_defaults(func=cmd_snapshot_capture)

    spd = sub_snap.add_parser("diff", help="Compare current state to a snapshot")
    spd.add_argument("name")
    spd.set_defaults(func=cmd_snapshot_diff)

    spr = sub_snap.add_parser(
        "restore",
        help="Restore repos/worktrees to a snapshot (requires --yes)",
    )
    spr.add_argument("name")
    spr.add_argument("--yes", action="store_true", help="Confirm restore")
    spr.add_argument(
        "--force-clean",
        action="store_true",
        help="Abort merges, hard reset, and clean before restoring",
    )
    spr.set_defaults(func=cmd_snapshot_restore)


def _add_deps_parsers(sub: Any) -> None:
    sp = sub.add_parser("deps", help="Dependency queries (from components/index.json)")
    sub4 = sp.add_subparsers(dest="deps_cmd", required=True)

    sp4 = sub4.add_parser("show", help="Show deps + reverse deps for a component")
    sp4.add_argument("component")
    sp4.set_defaults(func=cmd_deps_show)

    sp4 = sub4.add_parser("who-uses", help="List components that depend on a component")
    sp4.add_argument("component")
    sp4.set_defaults(func=cmd_deps_who_uses)

    sp4 = sub4.add_parser(
        "closure", help="Transitive deps + reverse deps for a component"
    )
    sp4.add_argument("component")
    sp4.set_defaults(func=cmd_deps_closure)

    sp4 = sub4.add_parser(
        "impacted", help="Transitive reverse deps (who is impacted by changes)"
    )
    sp4.add_argument("component")
    sp4.set_defaults(func=cmd_deps_impacted)


def _add_impact_parsers(sub: Any) -> None:
    sp = sub.add_parser(
        "impact",
        help="Impact analysis: changed repos -> impacted components (from components/index.json)",
    )
    subi = sp.add_subparsers(dest="impact_cmd", required=True)

    spi = subi.add_parser("repos", help="Report impacted components from changed repos")
    spi.add_argument("changed", nargs="+", help="Changed repo/component names")
    spi.set_defaults(func=cmd_harness_impact_repos)

    spi = subi.add_parser(
        "snapshot", help="Report impacted components from snapshot diff"
    )
    spi.add_argument("name", help="Snapshot name")
    spi.add_argument(
        "--no-missing",
        action="store_true",
        help="Do not treat missing repos/worktrees as changed",
    )
    spi.set_defaults(func=cmd_harness_impact_snapshot)


def _add_init_parser(sub: Any) -> None:
    sp = sub.add_parser(
        "init",
        help="Initialize harness manifest + dirs + baseline .gitignore",
    )
    sp.add_argument(
        "--root",
        default="",
        help="Initialize the harness at a specific root (default: current directory)",
    )
    sp.add_argument(
        "--symlinks",
        action="store_true",
        help="Create root-level symlinks (repos/, worktrees/, states/, components/) into .loom/workspaces",
    )
    sp.set_defaults(func=cmd_harness_init)


def _add_exec_parser(sub: Any) -> None:
    sp = sub.add_parser(
        "exec", help="Run a command across repos (optionally a worktree group)"
    )
    sp.add_argument(
        "--group",
        default=None,
        help="Run in worktrees/<group>/<repo> instead of repos/<repo>",
    )
    _add_selection_flags(
        sp, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp.add_argument(
        "--jobs",
        type=int,
        default=1,
        help="Parallelism for command execution (default: 1)",
    )
    sp.add_argument(
        "--require-clean",
        action="store_true",
        help="Skip dirty repos/worktrees",
    )
    sp.add_argument(
        "cmd_argv",
        nargs=argparse.REMAINDER,
        help="Command to run (use: exec -- <cmd...>)",
    )
    sp.set_defaults(func=cmd_harness_exec)


def _add_sandbox_parsers(sub: Any) -> None:
    sp = sub.add_parser("sandbox", help="Sandbox worktrees (harness)")
    subs = sp.add_subparsers(dest="sandbox_cmd", required=True)

    spc = subs.add_parser("create", help="Create sandbox worktrees for a group")
    spc.add_argument("group")
    spc.add_argument("--base-ref", required=True, help="Base ref-ish")
    spc.add_argument("--ttl", default="2h")
    spc.add_argument("--purpose", default="sandbox")
    spc.add_argument(
        "--clone", action="store_true", help="Clone missing repos automatically"
    )
    _add_selection_flags(
        spc, include_all=True, repos_help="Subset of repos (default all)"
    )
    spc.set_defaults(func=cmd_harness_sandbox_create)

    spp = subs.add_parser("promote", help="Promote a sandbox group (metadata only)")
    spp.add_argument("group")
    spp.set_defaults(func=cmd_harness_sandbox_promote)

    spg = subs.add_parser("gc", help="Remove expired sandbox groups (requires --yes)")
    spg.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before running sandbox GC",
    )
    spg.add_argument("--force", action="store_true")
    spg.add_argument("--yes", action="store_true")
    spg.set_defaults(func=cmd_harness_sandbox_gc)


def _add_cleanup_parsers(sub: Any) -> None:
    sp = sub.add_parser("cleanup", help="Suggest/apply TTL-based group cleanup")
    subc = sp.add_subparsers(dest="cleanup_cmd", required=True)

    spc = subc.add_parser("suggest", help="Suggest expired groups")
    spc.set_defaults(func=cmd_harness_cleanup_suggest)

    spa = subc.add_parser("apply", help="Apply cleanup (requires --yes)")
    spa.add_argument(
        "--require-lease",
        default="",
        help="Require this lease key before applying cleanup",
    )
    spa.add_argument("--id", action="append", default=[])
    spa.add_argument("--force", action="store_true")
    spa.add_argument("--yes", action="store_true")
    spa.set_defaults(func=cmd_harness_cleanup_apply)


def _add_repo_lifecycle_parsers(sub: Any) -> None:
    sp = sub.add_parser(
        "add", help="Imperatively add a repo to workspace.json (optionally clone)"
    )
    sp.add_argument("name")
    sp.add_argument("remote")
    sp.add_argument(
        "--default-branch",
        default="",
        help="Default branch (if omitted: infer when --clone, otherwise use main)",
    )
    sp.add_argument(
        "--shallow", action="store_true", help="Use shallow clone/fetch for this repo"
    )
    sp.add_argument(
        "--depth",
        type=int,
        default=1,
        help="History depth for shallow repos (default: 1)",
    )
    sp.add_argument("--clone", action="store_true", help="Clone + fetch immediately")
    sp.add_argument(
        "--force", action="store_true", help="Overwrite existing repo entry"
    )
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser(
        "remove",
        help="Remove a repo from workspace.json (optionally delete clone/metadata)",
    )
    sp.add_argument("name")
    sp.add_argument("--delete-clone", action="store_true")
    sp.add_argument(
        "--delete-component-md",
        dest="delete_component_md",
        action="store_true",
        help="Delete the component metadata markdown (components/<repo>.md)",
    )
    sp.add_argument(
        "--delete-service-md",
        dest="delete_component_md",
        action="store_true",
        help="Alias for --delete-component-md",
    )
    sp.add_argument(
        "--yes-delete",
        dest="yes_delete",
        action="store_true",
        help="Confirm deletions when using --delete-clone",
    )
    sp.set_defaults(func=cmd_remove)

    sp = sub.add_parser("list", help="List configured repos")
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser(
        "sync",
        help="Fetch/prune repos; optionally clone missing; refresh components index",
    )
    sp.add_argument(
        "--clone", action="store_true", help="Clone missing repos before fetching"
    )
    _add_selection_flags(
        sp, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp.add_argument(
        "--jobs",
        type=int,
        default=1,
        help="Parallelism for network/git operations (default: 1)",
    )
    sp.set_defaults(func=cmd_sync)

    sp = sub.add_parser("status", help="Show branch/sha/dirty for repos")
    sp.add_argument(
        "--jobs", type=int, default=1, help="Parallelism for git status (default: 1)"
    )
    _add_selection_flags(
        sp, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp.set_defaults(func=cmd_status)

    sp = sub.add_parser(
        "context", help="Emit a compact workspace context bundle (ideal for AI prompts)"
    )
    _add_selection_flags(
        sp, include_all=False, repos_help="Subset of repos (default all)"
    )
    sp.add_argument(
        "--jobs",
        type=int,
        default=1,
        help="Parallelism for data gathering (default: 1)",
    )
    sp.set_defaults(func=cmd_context)

    sp = sub.add_parser(
        "branch",
        help="Ensure+checkout a branch across repos (use --reset for git checkout -B)",
    )
    sp.add_argument("branch")
    _add_selection_flags(
        sp, include_all=True, repos_help="Subset of repos (default all)"
    )
    sp.add_argument("--base-ref", help="Base ref (default origin/<default_branch>)")
    sp.add_argument(
        "--clone", action="store_true", help="Clone missing repos automatically"
    )
    sp.add_argument(
        "--reset",
        action="store_true",
        help="Reset branch to base_ref (destructive; uses git checkout -B)",
    )
    sp.add_argument(
        "--yes",
        action="store_true",
        help="Confirm destructive operations (required with --reset)",
    )
    sp.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow switching/creating branches when repos have local changes",
    )
    sp.add_argument(
        "--refresh-index",
        action="store_true",
        help="Refresh components index after branching",
    )
    sp.set_defaults(func=cmd_branch)


def _add_refresh_index_parser(
    subcommands: Any, *, help_text: str, handler: Any
) -> None:
    sp = subcommands.add_parser("refresh-index", help=help_text)
    sp.add_argument(
        "--print", action="store_true", help="Print a concise view after refresh"
    )
    sp.set_defaults(func=handler)


def _add_components_parsers(sub: Any) -> None:
    sp = sub.add_parser("components", help="Component metadata cache operations")
    sub3 = sp.add_subparsers(dest="components_cmd", required=True)
    _add_refresh_index_parser(
        sub3,
        help_text="Rebuild components/index.json from components/*.md",
        handler=cmd_components_refresh_index,
    )


def _add_services_parsers(sub: Any) -> None:
    sp = sub.add_parser("services", help="Alias for components (microservice naming)")
    sub3 = sp.add_subparsers(dest="components_cmd", required=True)
    _add_refresh_index_parser(
        sub3,
        help_text="Alias for components refresh-index",
        handler=cmd_services_refresh_index,
    )


def _add_deepen_parser(sub: Any) -> None:
    sp = sub.add_parser("deepen", help="Deepen history of a shallow repo")
    sp.add_argument("repo", help="Repo name")
    sp.add_argument(
        "--depth", type=int, default=50, help="Number of commits to deepen by"
    )
    sp.set_defaults(func=cmd_deepen)


def add_harness_parser(
    root_sub: Any,
    *,
    name: str = "harness",
    help_text: str = "Workspace harness control plane",
    description_text: str = "Workspace harness control plane",
) -> None:
    p = root_sub.add_parser(name, help=help_text, description=description_text)
    sub = p.add_subparsers(dest="harness_cmd", required=True)

    _add_init_parser(sub)
    _add_exec_parser(sub)
    _add_repo_parsers(sub)
    _add_set_parsers(sub)
    _add_lease_parsers(sub)
    _add_sandbox_parsers(sub)
    _add_cleanup_parsers(sub)
    _add_repo_lifecycle_parsers(sub)

    _add_worktree_parsers(sub)
    _add_snapshot_parsers(sub)
    _add_components_parsers(sub)
    _add_services_parsers(sub)
    _add_deps_parsers(sub)
    _add_impact_parsers(sub)
    _add_deepen_parser(sub)

    return None


__all__ = ["add_harness_parser"]
