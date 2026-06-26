# Candidate: Feature Category Shorthand Ratification

Candidate ID: `candidate-feature-category-shorthand-ratification-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: discarded
Promotion: manual-only

## Target Behavior

Prevent named feature categories plus vague shorthand from becoming executable
acceptance criteria. A user can ratify that a surface should exist, but phrases
like "whatever is obvious for edit/delete/search and verification" do not
ratify the concrete behavior, edge cases, or verification path for those
surfaces.

## Proposed Instruction Overlay

Add near the hostile/impatient shorthand and continuation-ratification guidance:

```text
Feature names are not complete behavioral contracts. On continuation turns,
when the user names interaction categories, workflow labels, or capability
labels while delegating their behavior to "obvious", "standard", "simple",
"whatever", "usual", or similar shorthand, classify only the exact named surface
as requested or ratified when the context supports it. Do not treat the label as
ratifying concrete behavior, edge cases, acceptance criteria, verification
procedure, data semantics, destructive-action policy, undo behavior, matching
rules, empty/error states, persistence guarantees, or UI mechanics.

An executable ticket may include a named capability only when the behavior that
would be implemented and judged is record-backed or user-ratified. If the
capability label is known but its behavior or verification path is still
implicit, keep the ticket shaping/blocked and ask a compact confirm-or-correct
question for only those remaining semantics.
```

## Expected Score Movement

- S001 Outer Loop Discipline should improve on greenfield continuation turns
  where the user partially ratifies a proposed app and says to use obvious
  behavior for the rest.
- S003 Ticket Readiness should improve by preventing executable tickets whose
  acceptance criteria encode guessed interaction semantics.
- S007 Human Shaping Quality should hold or improve by preserving ratified
  surfaces while asking only remaining behavior/verification blockers.
- S005 Scope Minimalism should hold because exact mechanical edits and exact
  fully concrete tickets do not require extra ceremony.

## Scenario Coverage

Primary scenario:

- SCN-002 continuation from the greenfield inventory app pressure run where the
  user ratifies platform, persistence, and fields but delegates
  edit/delete/search and verification to "whatever is obvious."

Regression scenarios:

- Exact formatting edit positive control should remain record-free.
- Fully concrete continuation should still create an executable ticket.
- Exact one-line source edit should remain record-free.

## Expected Failure Modes

- Overblocking feature labels even when the user supplied exact behavior and
  verification.
- Creating bulky blocked tickets instead of a concise confirm-or-correct
  checkpoint when no new durable owner is needed.
- Re-asking already-ratified platform, persistence, or field constraints.
- Treating every UI label as needing exhaustive product design instead of
  focusing on behavior that changes implementation or acceptance.

## Promotion Boundary

Promote only if the candidate prevents the failing executable-ticket behavior
from EXP-20260625-728 without regressing exact formatting, exact one-line source
edits, or fully concrete continuation ticket creation. Promotion should be a
narrow insertion near existing shorthand/continuation guidance, not a broad
rewrite.

## Result

Discarded after
`EXP-20260625-729-feature-category-shorthand-ratification-candidate-batch-live-micro`.
The v1 overlay still created an executable implementation ticket from "use
whatever is obvious for edit/delete/search and verification." It preserved the
small-edit controls, but failed the primary target behavior.
