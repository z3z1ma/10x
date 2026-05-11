---
name: loom-git-workspace-isolation
description: "Use when implementation needs workspace isolation or provenance because unrelated changes, worker write scopes, baseline ambiguity, branch/worktree setup, or later cleanup/finish decisions could affect safety."
---

# loom-git-workspace-isolation

Git workspace isolation is a safety playbook for code-facing Loom work.

It detects the current Git/workspace state, chooses the least surprising isolation
mechanism, verifies a clean baseline, and records provenance for later finish or
cleanup.

## Core Dependency

Use `loom-core` first. This playbook composes `loom-tickets`, `loom-plans`,
`loom-ralph`, `loom-evidence`, and `loom-audit`.

It does not replace ticket scope, branch policy, evidence, or operator approval.

## Use This Playbook When

Use this playbook when:

- starting non-trivial implementation work
- executing a plan with multiple tickets or worker packets
- the current branch contains unrelated work
- a worker needs an isolated write scope
- baseline tests or setup need to distinguish pre-existing failure from new failure
- cleanup or branch finish later depends on knowing who owns the workspace

Skip it when the operator explicitly wants in-place editing and the ticket scope is
small enough that isolation would not reduce risk.

## Route

Use this route:

```text
detect -> decide -> isolate -> setup -> baseline -> record -> proceed
```

## Detect

Before creating anything, inspect the current workspace state.

Check:

- current branch or detached state
- uncommitted changes and whether they are related to the ticket
- whether the workspace is already a linked worktree or harness-managed workspace
- whether the repository is a submodule
- available native harness worktree or workspace tools
- project-local worktree conventions such as `.worktrees/` or `worktrees/`

Do not create nested worktrees or overwrite a harness-managed isolation model.

If unrelated user changes exist, leave them alone and choose a path that does not
mix them with the ticket.

## Decide

Choose the isolation mechanism in this order:

- existing isolated workspace when it already matches the ticket
- native harness workspace or worktree tool when available
- Git worktree fallback when the operator approves and local policy allows it
- in-place execution when isolation is unnecessary, unavailable, or declined

Ask before creating a new worktree unless the operator or project instructions
already authorize it.

## Isolate

When using a Git worktree fallback:

- choose a branch name tied to the ticket or plan unit
- prefer the project's existing worktree directory convention
- verify project-local worktree directories are ignored before placing work there
- avoid creating worktrees inside other worktrees
- record the path and branch in the ticket or packet

If sandbox permissions block worktree creation, state the limitation and continue
only if in-place work is acceptable for the ticket risk.

## Setup

Run setup proportional to the project and ticket:

- dependency install or download when the workspace is new
- generated setup only when the project normally requires it
- environment checks needed by the ticket
- branch or upstream fetches needed to establish the base

Do not add setup churn to the ticket unless setup files are intentionally in scope.

## Baseline

Run the smallest honest baseline check before changing code.

Useful baselines:

- focused tests for the area in scope
- existing lint/type/build commands when the ticket will rely on them
- smoke checks for plan execution
- current failure reproduction for bug work

If baseline fails, record the failure as evidence or ticket state before deciding
whether to proceed. Do not treat pre-existing failure as caused by the current
ticket.

## Record

Record enough provenance for recovery:

- branch name and base branch or base commit
- workspace path when it matters for continuation
- whether the workspace is harness-owned, manually created, or in-place
- baseline command and result
- unrelated changes intentionally left out
- cleanup expectation after merge, PR, discard, or handoff

Use `loom-evidence` when baseline output will support later closure or audit.

## Proceed

After isolation and baseline, continue through the appropriate route:

- `loom-incremental-implementation` for local execution
- `loom-ralph` for one bounded worker packet
- `loom-parallel-worker-coordination` for independent packets
- `loom-debugging-and-error-recovery` when baseline or setup fails
- `loom-branch-finish` if the only remaining work is integration or cleanup

## Done Means

The isolation pass is done when:

- the workspace state is known
- isolation choice matches the ticket risk and operator constraints
- baseline state is recorded when it affects later claims
- branch/workspace provenance is recoverable
- implementation can start without mixing unrelated work
