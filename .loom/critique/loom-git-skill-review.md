---
id: critique:loom-git-skill-review
kind: critique
status: final
created_at: 2026-04-25T07:42:40Z
updated_at: 2026-04-25T07:48:03Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:h5j0wnkz and the `loom-git` product-surface diff
links:
  ticket:
    - ticket:h5j0wnkz
  evidence:
    - evidence:loom-git-skill-validation
external_refs: {}
---

# Summary

Review of the `loom-git` skill and Ralph integration for product-surface quality,
Git topology generality, and Loom truth-boundary discipline.

# Review Target

Reviewed the uncommitted diff adding `skills/loom-git/` and updating Ralph,
`/loom-work`, `README.md`, `PROTOCOL.md`, and `ARCHITECTURE.md`.

The key risk was overfitting Git guidance to one repository convention instead
of teaching a portable method for arbitrary developer machines, remotes,
branches, worktrees, fork/upstream setups, local-only repos, release branches,
stacked diffs, and parallel Ralph workers.

# Verdict

Pass after revisions.

The first draft had material issues. The revised version resolves the findings
and is acceptable as protocol-surface guidance.

# Findings

## FIND-001: Initial draft overfit branch freshness to common `origin`/`main` habits

Severity: high
Confidence: high
Disposition: resolved

Observation:

The initial draft centered examples and procedure around a common hosted-Git
shape rather than starting from a general integration-baseline concept.

Why it matters:

Loom skills are product surface. They must work across arbitrary Git topologies
without assuming remote names, integration branch names, hosted PR workflows, or
this repository's conventions.

Follow-up:

Resolved by making integration-baseline discovery the primary concept in
`skills/loom-git/SKILL.md` and `references/branch-and-remote-hygiene.md`, with
explicit no-assumption guidance for remotes, branch names, and local-only repos.

## FIND-002: Remote provenance was too lossy for fork/upstream and multi-remote repos

Severity: medium
Confidence: high
Disposition: resolved

Observation:

The first packet shape collapsed remote state into `remote_context`, which could
hide the difference between integration remote, push remote, and review target.

Why it matters:

Fork/upstream, stacked-diff, enterprise mirror, and release-branch workflows need
to know which remote/ref provided the baseline and where work is pushed or
reviewed.

Follow-up:

Resolved by adding `source_fingerprint.integration_remote`, preserving
`integration_ref` and `integration_commit`, adding `execution_context.push_remote`,
and requiring packet body details for fork/upstream and multi-repo workflows.

## FIND-003: Parallel worktree guidance missed shared Git metadata contention

Severity: medium
Confidence: high
Disposition: resolved

Observation:

Linked worktrees isolate working directories but can share remote-tracking refs,
config, object storage, hooks, and administrative state. A child fetch or prune
can invalidate sibling packet freshness assumptions.

Why it matters:

Parallel Ralph depends on stable packet fingerprints and non-overlapping write
authority. Shared Git metadata mutation can create invisible contention outside
file write scopes.

Follow-up:

Resolved by requiring the parent to fetch and resolve integration commits before
parallel launch, freezing `integration_commit`, and forbidding child
fetch/prune/config mutations unless the packet explicitly allows them.

## FIND-004: Parent-only setup notes could become shadow execution truth

Severity: medium
Confidence: high
Disposition: resolved

Observation:

The parallel setup table could initially live in vague parent notes after launch.

Why it matters:

Branch, worktree, baseline, and child write-scope assignments are launch and
reconciliation context. Once workers launch, they must be visible in plan,
ticket, or packet surfaces rather than hidden in transcript scratch.

Follow-up:

Resolved by allowing scratch notes only while designing the wave and requiring
launched-wave setup to live in the plan, ticket journal, or packet working notes.

## FIND-005: `integration_commit` needed an operational resolution recipe

Severity: low
Confidence: high
Disposition: resolved

Observation:

The first draft required `integration_commit` but did not show how to resolve a
movable ref or tag to a commit.

Why it matters:

Packet freshness needs an immutable commit, not only a branch or tag name.

Follow-up:

Resolved by adding `git rev-parse --verify HEAD^{commit}` and
`git rev-parse --verify <integration-ref-or-commit>^{commit}` guidance, including
annotated tag handling.

## FIND-006: Package framing and `/loom-work` needed consistency fixes

Severity: low
Confidence: high
Disposition: resolved

Observation:

`README.md` did not list Git-backed isolation where `PROTOCOL.md` and
`ARCHITECTURE.md` did, and `/loom-work` listed fetch without enough conditional
wording.

Why it matters:

Top-level docs and optional wrappers should not quietly teach a weaker or more
remote-assumptive workflow than the skill.

Follow-up:

Resolved by adding Git-backed isolation to `README.md` workflow framing and
qualifying fetch as relevant only when the resolved baseline is remote-backed.

# Evidence Reviewed

- `skills/loom-git/SKILL.md`
- `skills/loom-git/references/branch-and-remote-hygiene.md`
- `skills/loom-git/references/worktree-discipline.md`
- `skills/loom-git/references/parallel-ralph-with-git.md`
- `skills/loom-git/references/diff-commit-and-merge-hygiene.md`
- `skills/loom-ralph/SKILL.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-ralph/references/work-driver.md`
- `skills/loom-ralph/references/parent-child-handshake.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `commands/loom-work.md`
- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `git diff --check`
- targeted grep checks recorded in evidence:loom-git-skill-validation

# Residual Risks

- The guidance is intentionally generic and cannot encode every organization's
  Git policy; it must fail closed to local repository policy and operator input.
- No golden example was added for a parallel multi-repo Git wave in this ticket.

# Required Follow-up

None required before this ticket can move to `complete_pending_acceptance`.

A future example could demonstrate a parallel Ralph wave using separate
worktrees, but that is not necessary for this skill to be useful.

# Acceptance Recommendation

Move ticket:h5j0wnkz to `complete_pending_acceptance` after final structural
validation and ticket reconciliation.
