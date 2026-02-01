---
name: ticket-dependency-hygiene
description: Use when creating/updating multiple Loom tickets and you need deterministic sequencing via dependencies and statuses.
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-01T21:38:42.409Z"
  updated_at: "2026-02-01T21:38:42.409Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
## When to use

- You created/edited several files under `.tickets/`.
- Work spans multiple tasks and you need clear sequencing.

## Goal

Make the ticket graph reflect reality: explicit deps, correct statuses, and short rationale notes.

## Checklist

1. Identify the sequencing
   - List the tickets involved.
   - Decide which tickets are blocked by others.

2. Encode dependencies (graph, not prose)
   - `loom ticket dep <id>`
   - `loom ticket dep-add <id> <dep-id>`
   - `loom ticket dep-rm <id> <dep-id>`

3. Sanity-check status vs deps
   - If a ticket is blocked, keep it out of `in_progress`.
   - Only move a ticket to `in_progress` when you can actively work it.

4. Leave a rationale note for non-obvious edges
   - `loom ticket add-note <id> "Blocked by <dep-id> because ..."`

5. Verify ready queue behavior
   - `loom ticket ready`

## Failure modes

- Hidden sequencing captured only in free-form text.
- Tickets marked `in_progress` while blocked.
- Dependency changes without a short explanation note.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
