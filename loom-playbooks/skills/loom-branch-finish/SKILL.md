---
name: loom-branch-finish
description: "Use when code work on an isolated branch or worktree appears complete and the next decision is branch disposition: local merge, PR, keep, discard, cleanup, or follow-up routing."
---

# loom-branch-finish

Branch finish is a Git integration and cleanup playbook.

It verifies the work, detects whether the workspace is normal, worktree-based, or
harness-managed, presents bounded finish options, and records the chosen
disposition in Loom records.

## Core Dependency

Use `loom-core` first. This playbook composes `loom-tickets`, `loom-evidence`,
`loom-audit`, `loom-retrospective`, and optionally `loom-shipping-and-launch`.

It does not replace ticket acceptance, PR review, release readiness, or operator
approval for destructive cleanup.

## Use This Playbook When

Use this playbook when:

- implementation work on a branch or isolated workspace appears complete
- all planned tickets or packets for a branch have returned
- the operator needs a clear merge, PR, keep, or discard choice
- a worktree may need cleanup after local integration
- branch provenance and ticket closure need to agree

Skip it when the work is still active, evidence is missing, audit is unresolved, or
the next move is release rollout rather than branch disposition.

## Route

Use this route:

```text
verify -> detect -> summarize -> present -> execute choice -> record -> cleanup
```

## Verify

Before presenting finish options, check that the branch is actually finishable.

Confirm:

- ticket acceptance is satisfied or explicitly not ready
- required evidence exists and reflects the latest source state
- audit findings are resolved, accepted as risk, or routed
- relevant focused checks passed after the last material change
- broader checks required by the ticket or branch risk passed or have stated limits

If verification fails, stop and route to debugging, evidence, audit, or ticket work
instead of offering merge or PR choices.

## Detect

Inspect the Git/workspace environment:

- current branch or detached state
- base branch or likely merge target
- whether the workspace is a linked worktree
- whether the worktree is project-created, manually created, or harness-owned
- uncommitted changes and whether they are in scope
- remote tracking status if PR is an option

Do not remove or modify workspaces owned by the harness unless the operator and
harness provide an explicit safe path.

## Summarize

Prepare a concise finish summary from Core records and source state:

- tickets completed or still open
- evidence and checks that support completion
- audit status and residual risk
- changed files or high-level diff shape
- branch name, base branch, and workspace path when relevant
- follow-up tickets or cleanup still needed

Do not claim more than tickets, evidence, and audit support.

## Present

Offer bounded options that match the environment.

Common options:

- merge locally into the base branch
- push and create a pull request
- keep the branch or worktree for later
- discard the branch and workspace
- stop because ticket acceptance or evidence is not ready

Detached or harness-managed workspaces may not support every option. Present only
safe options.

Discard or destructive cleanup requires explicit operator confirmation naming what
will be deleted.

## Execute Choice

Execute only the selected path.

Guidelines:

- for local merge, verify the merged result before cleanup
- for PR creation, preserve the worktree unless the operator explicitly says
  otherwise
- for keep, report branch/workspace provenance and next command or record to read
- for discard, require explicit confirmation and never remove unrelated changes
- for stop, update the ticket with the missing acceptance, evidence, or audit item

Never force-push, rewrite published history, or delete work without explicit
operator approval.

## Record

Update Loom records after the selected path:

- ticket state, closure notes, or blocked/review state
- evidence for final verification, merge check, PR creation, or cleanup observation
- audit disposition when review was part of the finish claim
- retrospective follow-up when the branch revealed a reusable procedure or trap
- knowledge when an accepted finish procedure should be easy to find later

## Cleanup

Clean up only what this workflow owns.

Safe cleanup depends on provenance:

- normal repository: no worktree cleanup is needed
- project-created worktree: remove only after merge/discard is confirmed and safe
- PR path: usually preserve workspace for review iteration
- harness-owned workspace: use native harness exit/cleanup if available, otherwise
  leave it in place

Run worktree pruning only when using Git worktree cleanup and the operator approved
the cleanup path.

## Done Means

The branch finish pass is done when:

- finishability was verified before integration options were offered
- environment and cleanup provenance were detected
- the operator selected a bounded finish path
- selected actions were performed without touching unrelated work
- Loom ticket, evidence, audit, and follow-up records match the final branch state
