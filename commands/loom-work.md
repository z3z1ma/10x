---
name: loom-work
description: "Execute a bounded ticket through Ralph iterations, keep the ticket as the sole live execution ledger, and stop honestly when scope, evidence, or review says to stop."
arguments: "<ticket id preferred | bounded execution request>"
category: core
suggested_skills:
  - loom-workspace
  - loom-records
  - loom-tickets
  - loom-ralph
  - loom-git
  - loom-specs
  - loom-research
  - loom-plans
  - loom-critique
  - loom-wiki
---

# /loom-work

You are running **Loom Work**.

Ticket or bounded execution request:
`$ARGUMENTS`

This command is the high-level execution driver.
Its job is not to “just code.”
Its job is to move one truthful ticket forward through bounded Ralph iterations and reconcile the results back into the execution ledger.

Hydrate only what you need from:
- `loom-workspace`
- `loom-records`
- `loom-tickets`
- `loom-ralph`
- `loom-git`
- `loom-specs`
- `loom-research`
- `loom-plans`
- `loom-critique`
- `loom-wiki`

## Goals

- ensure the work is owned by a ticket
- prepare Git branch/worktree isolation when repository files will change
- compile a bounded Ralph packet
- execute through one or more fresh-context iterations
- reconcile each iteration back into ticket truth
- stop at the right status instead of forcing closure

## Canonical Procedure

Use `skills/loom-ralph/references/work-driver.md` and
`skills/loom-ralph/SKILL.md` as the procedure. Use
`skills/loom-git/SKILL.md` when repository files will change or Git isolation
matters.

In short:

1. anchor to one ticket
2. confirm readiness
3. use `loom-git` for branch/worktree setup when Git isolation matters
4. compile a bounded Ralph packet
5. run one bounded iteration
6. reconcile as parent
7. route to the next owner

## Native tools to prefer

- `rg -n 'ticket:[a-z0-9]+' .loom --glob '*.md'`
- `git status --short`
- `git remote -v`
- `git fetch --prune <remote>` when the resolved baseline is remote-backed
- `git worktree list`
- `git diff --stat`
- `git diff`
- `find .loom/packets/ralph -type f -name '*.md' | sort | tail`
- `date -u +"%Y-%m-%dT%H:%M:%SZ"`

## Guardrails

- Do not work without a ticket owning live state.
- Do not let the packet outrank the ticket or other canonical records.
- Do not widen scope because another nearby fix looks easy.
- Do not close the ticket on vibes.

## Required output

- what changed
- Ralph packets created or updated
- iteration outcomes and why they stopped
- evidence gathered
- ticket status after reconciliation
- recommended next command
