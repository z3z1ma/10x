# Candidate: Feature Category Shorthand Ratification v2

Candidate ID: `candidate-feature-category-shorthand-ratification-v2`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

Prevent "yes to these exact slots, use whatever is obvious for the rest" from
becoming an executable ticket. The "whatever/obvious" slots are unresolved for
execution even when the user names the capability categories and even when a
prior assistant recommendation proposed plausible concrete behavior.

## Proposed Instruction Overlay

Add near hostile/impatient shorthand and continuation-turn ratification:

```text
Feature-category shorthand is not execution ratification. On continuation
turns, when the user explicitly accepts some values but says to use "obvious",
"standard", "simple", "whatever", "usual", "your judgment", or similar
shorthand for named capabilities, workflows, interaction labels, or verification
steps, treat the shorthand-covered slots as unresolved for executable work. This
is true even if the prior assistant recommended plausible behavior for those
slots.

The user may have ratified that the capability category is in scope, but not
the concrete behavior that would be implemented or judged. Do not create an
executable ticket, active spec, tests, or implementation from such slots. Keep
or update a shaping/blocked record and ask a compact confirm-or-correct
checkpoint for only the shorthand-covered semantics.

An executable ticket requires the behavior and verification path to be stated in
terms a cold executor and reviewer can apply without inventing semantics:
matching rules, destructive-action policy, undo/confirmation behavior,
empty/error handling when material, persistence expectations, and the exact
verification procedure when those details affect acceptance. The smallest
acceptable answer may be a concise recommended contract for the user to confirm;
it is not executable until confirmed or record-backed.
```

## Expected Score Movement

- S001 should improve on partial greenfield continuations with "obvious" slots.
- S003 should improve by blocking executable tickets with guessed acceptance
  criteria.
- S007 should improve or hold by asking only the remaining shorthand-covered
  slots.
- S005 should hold on exact mechanical edit regressions.

## Scenario Coverage

Primary:

- SCN-002 greenfield inventory continuation from EXP-728/729.

Regressions:

- SCN-010 exact one-line source edit.
- SCN-010 exact formatting edit.
- Fully concrete continuation should remain a later post-promotion sanity check
  before broad confidence.

## Expected Failure Modes

- Still treating named capabilities plus "obvious" as executable.
- Re-asking already confirmed platform/persistence/field choices.
- Overblocking exact mechanical edits or concrete tickets.
- Over-specifying every UI detail rather than only material behavior and
  verification semantics.

## Promotion Boundary

Promote only if v2 blocks the primary executable-ticket failure and preserves
exact edit regressions. If v2 succeeds, run a post-promotion sanity batch with
the promoted canonical text.

## Result

Promoted after
`EXP-20260625-730-feature-category-shorthand-ratification-v2-candidate-batch-live-micro`
and confirmed by
`EXP-20260625-731-post-promotion-feature-category-shorthand-sanity-live-micro`.
The v2 overlay kept shorthand-covered edit/delete/search and verification slots
blocked, preserved already-ratified platform/persistence/field values, and did
not regress exact one-line or formatting edits.
