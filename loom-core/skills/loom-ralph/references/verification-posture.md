# Verification Posture

Verification posture is the evidence contract for Ralph runs that change behavior,
implementation, validation, or other checkable state.

Use one label when needed:

- `test-first`: automated or executable check can exercise the target
- `observation-first`: useful state is observable but automated testing is not
  practical for this run
- `none`: no implementation or validation evidence obligation beyond output

Review and synthesis runs may instead name review lenses or explicit evidence
expectations.

## test-first

Use when behavior can be exercised. The worker should create or identify a check,
confirm the expected failure before implementation, make the smallest scoped
change, record red/green evidence, and run broader checks when risk or the run asks
for them. If the check already passes, tighten it, explain existing behavior, or
escalate.

## observation-first

Use when observation is the right proof. Capture before state, make the scoped
change, capture after state, and preserve observations in evidence when another
surface will rely on them. Observations can be command output, screenshots, logs,
manual reproductions, generated artifacts, diffs, or structured inspections.

## none

Use when the run has no validation evidence obligation: non-semantic record
cleanup, read-only review, narrow prose cleanup that does not change behavior or
authority, or a refactor already covered by named checks.

## Evidence And Audit

Verification is not audit. Verification produces observations for the run; audit
challenges claims, evidence, findings, risks, and implementation shape before
another surface relies on them.
