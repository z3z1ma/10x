# Verification Posture

Verification posture is an evidence contract for Ralph runs that change behavior,
implementation, validation, or other checkable state.

Use one of these labels when a run needs this contract:

- `test-first`
- `observation-first`
- `none`

Review and synthesis runs may instead use mode-specific labels such as review lens
or explicit evidence expectations in the ticket, target record, or launch body.

## test-first

Use `test-first` when the target names behavior that can be exercised by an
automated or executable check.

The worker should:

- create or identify a check that fails before implementation
- confirm it fails for the expected reason
- make the smallest scoped change that drives it green
- record red and green evidence
- run broader regression checks when the run asks for them or the change risk
  calls for them

If the check passes before implementation, tighten the check, explain why the
behavior already exists, or escalate.

## observation-first

Use `observation-first` when behavior or state is observable but a useful automated
test is impractical for this run.

The worker should:

- capture the before state
- make the scoped change
- capture the after state
- preserve the observations in evidence when another surface will rely on them

Useful observations include command output, screenshots, logs, manual
reproductions, generated artifacts, diffs, or structured inspections.

## none

Use `none` when the run has no implementation or validation evidence obligation
beyond its normal output contract.

Examples:

- non-semantic record cleanup
- read-only review where findings, not red/green evidence, are the output
- narrow prose cleanup that does not change behavior, protocol authority,
  acceptance, routing, or operator guidance
- a refactor whose safety is already covered by existing checks named in the run

## Evidence And Audit

Ralph run verification is not audit.

Verification produces observations for this worker run. Audit challenges claims,
evidence, findings, risks, and implementation shape before another surface relies
on them.
