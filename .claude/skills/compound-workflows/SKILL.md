---
name: compound-workflows
description: Use Plan → Work → Review → Compound to compound skills and maintain project context.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-01-27T17:03:09.731823+00:00"
  updated_at: "2026-01-27T17:03:09.731823+00:00"
  version: "1"
  tags: "workflow,compounding"
---

<!-- BEGIN:compound:skill-managed -->
## Purpose

This repository uses a loop:

1. **Plan**: turn an idea into a ticketed plan (loom ticket), informed by recalled notes (loom memory).
2. **Work**: execute in an isolated git worktree (loom workspace), updating ticket status.
3. **Review**: run a multi-angle review before merging.
4. **Compound**: extract reusable patterns into skills (procedural memory) + store memos for future planning.

The point is not vibes. The point is *reusable procedure*.

## Commands

### `/loom-plan <idea>`

- Recall relevant memos for planning:
  - `loom memory recall "<idea>" --command loom-plan --format prompt`
- Create/organize tickets:
  - `loom ticket init` (if needed)
  - `loom ticket create "..."`
  - `loom ticket dep-add <id> <dep-id>` (optional)
- Output a plan with:
  - ticket IDs
  - sequencing / dependencies
  - acceptance criteria and tests
  - risk list

### `/loom-work <ticket-id>`

- Fetch ticket, set status to `in_progress`.
- Create/ensure a worktree:
  - Branch convention: `ticket-<id>-<slug>`
  - `loom workspace worktree ensure <branch> --base-ref main`
- Do the work in that worktree.
- Update ticket as you go (`add-note`, `update --status`).

### `/loom-review <ticket-id>`

- Run fast checks (lint/tests if applicable).
- Do a review pass with multiple lenses:
  - correctness & maintainability
  - security & foot-guns
  - performance/regressions
  - docs & ergonomics
- Update the ticket with required follow-ups.

### `/loom-compound <ticket-id>`

- Write memory notes (loom memory) that future planning can recall.
- Apply durable learnings using Loom (run via bash):
  - `loom compound skill upsert <name> --description ... --body ...` (or pipe stdin)
  - `loom compound instinct upsert create|update <id> ...`
  - `loom compound docblock upsert --file LOOM.md --id loom-core-context --content ...`
  - `loom compound docblock upsert --file .loom/compound/ROADMAP.md --id roadmap-ai-notes --content ...`
  - `loom compound changelog append --note "..."`
  - `loom memory add --title ... --body ... --scope command:loom-plan` (sparingly)
- Finish with `loom compound refresh`.

## Operational defaults

- Keep skills small, scoped, and action-oriented.
- Prefer updating an existing skill over creating a near-duplicate.
- A skill should be applicable in at least 2 future contexts.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
