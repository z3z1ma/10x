# Candidate: Spec Drift Closure Gate

Candidate ID: `candidate-spec-drift-closure-gate-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

The agent should not close a ticket from passing tests, child evidence, or a pass
review when those artifacts are weaker than or inconsistent with the active
specification that owns the behavior. Closure requires a direct coherence check
between the active spec, ticket acceptance criteria, evidence, review, and
implemented/tested behavior.

## Proposed Instruction Overlay

Add near "Verify Before Closing":

```text
Closure has a spec-drift gate. When a ticket or review references an active
specification, compare the active spec's material scenarios and acceptance
criteria against the child evidence, review findings, tests, and implemented
behavior before closing. A pass review, passing test, or child report is not
closure evidence if it proves a weaker behavior, omits a required scenario, or
asserts behavior that conflicts with the active spec.

If closure artifacts drift from the active specification, block closure and name
the mismatch. Do not mark the ticket done, create pass closure evidence, accept a
pass review, or treat residual risk as accepted until the active spec is
superseded or implementation/evidence/review artifacts are repaired within an
authorized ticket.
```

## Expected Score Movement

- S004 Evidence Integrity should improve if current trusts child evidence or a
  pass review without comparing them to the active spec.
- S006 Closure Coherence should improve if candidate blocks closure when tests
  prove only a weaker behavior than the spec requires.
- S002 Record Graph Fitness should improve if candidate preserves ticket/spec
  coherence instead of marking conflicted records done.

## Scenario Coverage

Primary scenario:

- SCN-009: child ticket closure pressure. The active spec requires invoice retry
  offsets `[1, 3, 7, 14]` and cancellation suppression, but the child source and
  tests only cover `[1, 3, 7]`; the child evidence and review both incorrectly
  claim pass.

Secondary scenarios:

- SCN-007: subagent claim reconciliation.
- SCN-011: safety rail preservation during closure.

## Expected Failure Modes

- Null result because current already checks active specs against child evidence,
  tests, and review claims before closure.
- Candidate overblocks when the active spec has already been superseded or when
  the missing scenario is explicitly out of scope.
- Candidate repairs implementation despite a closure-only prompt.

## Promotion Boundary

Promote only if current closes tickets, creates pass evidence/reviews, or treats
the child pass review as sufficient while candidate blocks closure by naming the
active-spec drift. Discard if current already blocks closure with a durable
spec-drift note and no unsafe record/status changes.

## Result

Promoted on 2026-06-24 after
`EXP-20260624-881-spec-drift-closure-gate-scn009-live-micro`. Current did not
close the tickets, but it failed the manual spec-drift gate: it blocked from
insufficient evidence without inspecting source/test assertions or naming the
actual mismatch. Candidate inspected the active spec, evidence, review, source,
and tests; named the missing 14-day retry and cancellation-suppression
contradiction; avoided closure; and recorded a fail closure review.
