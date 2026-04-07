---
name: loom-workspace
description: "Parent-side Loom control-plane skill for workspace discovery, status, repository and worktree scope resolution, record discovery, validation routing, and subsystem selection. Use when entering the repo fresh, when `.loom/` is missing or incomplete where Loom expects it, when the user explicitly asks to set up, initialize, bootstrap, or scaffold Loom, when workspace health or scope ownership is unclear, or when you do not yet know which Loom layer owns the next durable action. Not for cases where the owning subsystem is already clear and no control-plane step is needed."
compatibility: Designed for this Markdown-first Loom repository.
metadata:
  author: agent-loom
  version: "0.1"
  loom-layer: control-plane
---

# loom-workspace

Use this skill as the parent-side Loom control plane for workspace discovery, readiness checks, routing, and scope resolution.

## Use This Skill When

- you entered the repository fresh and need orientation
- you need to bootstrap a new Loom workspace (`.loom/` does not exist or is incomplete)
- you do not yet know which Loom layer owns the next durable action
- you need to inspect workspace health before trusting records or packet work
- scope ownership of a path or repository is unclear

## Prefer Another Skill When

- you already know the exact owning subsystem and only need that artifact-layer workflow
- the task is purely local and has no durable Loom consequences

## What This Skill Governs

- workspace initialization and directory bootstrapping
- workspace-level health checks
- repository and worktree scope discovery
- parent-side readiness decisions
- status and health-check guidance

## Default Workspace Posture

- fail closed when repository or worktree ownership is ambiguous
- prefer explicit health checks over silent assumptions
- prefer native file inspection for workspace health checks
- read `constitution:main` before downstream Loom work once the workspace is structurally trustworthy
- prefer reading canonical state before packet launch
- route into the owning subsystem instead of letting one skill absorb unrelated responsibilities
- treat health and validation as decision inputs, not decorative reports

## Execution Playbook

1. resolve the single workspace root that should own the canonical `.loom/` tree
2. inspect the current `.loom/` state before writing anything
3. if the workspace is uninitialized or missing starter files, stop normal work and run the full `loom-setup` procedure at that workspace root
4. if the workspace is already initialized and only one known directory is missing, repair that gap surgically
5. inspect the visible Loom bundle and canonical records directly before trusting downstream records, packets, or operator guidance
6. read `constitution:main` once the workspace is structurally trustworthy enough to continue
7. resolve the owning repository or worktree for the target path with `git rev-parse --show-toplevel` or equivalent path-based inspection
8. keep canonical artifacts in the workspace-root `.loom/` tree even when the target code lives in a nested repository
9. route into the owning subsystem only after workspace trust and repository ownership are explicit

## Decision Rules

If direct workspace inspection or validation reports structural issues, fix those before trusting downstream packet work.

If native repository inspection still cannot assign ownership cleanly, escalate immediately rather than guessing.

If subsystem ownership is unclear, read the relevant canonical record and choose the skill that owns the next durable mutation or review step.

## Failure Conditions

Do not proceed as if the workspace is trustworthy when:

- repository ownership is ambiguous
- validation is failing
- links are broken
- required rule or skill surfaces are missing
- packet-consuming work is being attempted without adequate structural trust

## How To Use Native Tooling

Read `references/queries.md` for native workspace query patterns and example invocations.

- use `find` to enumerate records, directories, and likely owning surfaces
- use `rg` to inspect statuses, IDs, links, and cross-record references directly
- use `mkdir -p` only for surgical repair inside an already initialized workspace
- use `git rev-parse --show-toplevel` from the target path when repository ownership needs confirmation
- switch to the owning skill's script only when you need record-aware scaffolding, validation, or mutation

Prefer native file tools such as `find`, `rg`, `mkdir -p`, and `git` for workspace health checks and repository discovery. Use the full `loom-setup` workflow for bootstrap, and use record-aware commands only in the owning skill.

## What Good Looks Like

- you know whether the workspace is healthy enough to trust
- you know which repository owns the target path or record
- you know which Loom skill should own the next durable action
- you do not need to guess about structure, scope, or routing

## Done Means

- workspace health is explicit enough to trust or explicitly unsafe enough to halt
- ownership is resolved or the ambiguity is surfaced clearly
- the next owning skill is identified without guesswork
- downstream work starts from structural trust instead of optimism

## Read In This Order

1. `references/queries.md`
2. `references/doctor.md`
3. `references/status.md`
4. `references/examples.md`

## References

- `references/queries.md`
- `references/status.md`
- `references/doctor.md`
- `references/examples.md`
