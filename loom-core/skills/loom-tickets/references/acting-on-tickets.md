# Acting On Tickets

Use this detail card when resuming, updating, blocking, reviewing, closing, or
cancelling a ticket.

## First Move

Read the whole ticket before editing code or records. Read or already know every
material `## Related Records` entry. If a related record is unavailable, stale, or
contradicts the ticket, stop and surface that instead of guessing.

For source changes, inspect workspace state first:

```bash
git status --short
```

## Preflight

Before execution, check:

- `Status:` is `open` or `active`, unless the task is inspection, review,
  unblock, cancellation, or closure
- `Risk:` still fits
- scope is narrow and write boundaries are clear
- `ACC-*` criteria are observable
- Current State does not name a blocker for this step
- related records needed for execution have been read
- evidence and audit expectations are understood
- the next Ralph run can be bounded from ticket context

Set `Status: active` and update `Updated:` before launching or consuming the
first worker run if work materially begins.

## During Work

Stay inside the ticket boundary. Use `loom-ralph` for each bounded implementation,
inspection, review, or audit slice. If this session performs the work directly, it
still operates inside the ticket-owned Ralph boundary.

Do not batch unrelated cleanup, nearby fixes, record edits, refactors, or features.
Propose or create a separate ticket for valuable adjacent work.

Update the ticket when continuation would otherwise be misleading: material
progress, changes, blockers, changed assumptions, scope pressure, acceptance
changes, evidence, audit/review, status change, or closure.

## Ambiguity And Changes

Do not silently invent scope. Route behavior ambiguity to specs, sequencing to
plans, feasibility or tradeoffs to research, durable rules to constitution,
observations to evidence, adversarial findings to audit, reusable understanding to
knowledge, and operator-owned decisions to the operator.

Change scope or acceptance only to make the ticket more truthful. Update
`Updated:`, Current State, and Journal; preserve old context when audit would need
it. Split if the ticket has become multiple work units.

Use `Status: blocked` only for a concrete blocker. Record what is blocked, why
progress is unsafe, what unblocks it, and who or what owns the next move.

## Evidence, Review, Closure

Gather evidence proportional to the claim: tests, commands, manual checks, files
inspected, diffs reviewed, acceptance checks, or why verification was not possible
or appropriate. Do not claim verification that did not happen.

Use `Status: review` when implementation or record work appears complete but
audit, verification, acceptance review, or risk review is next.

Close only when every `ACC-*` is satisfied or revised with authority, unsatisfied
acceptance is handled outside closure, named evidence exists or its absence is
justified, audit has happened or is explicitly not useful, Current State is final,
Journal records the material path, and residual risk is named.

Set `Status: cancelled` when work should not proceed. Record why, who or what made
that decision, and what related work remains.
