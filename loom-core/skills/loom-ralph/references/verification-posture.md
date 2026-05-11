# Verification Posture

Verification posture is a packet-level evidence contract for Ralph runs that
change behavior, implementation, validation, or other checkable state.

Use one of these labels when a packet needs this contract:

- `test-first`
- `observation-first`
- `none`

Review and synthesis packets may instead use mode-specific labels such as `Review
Lens:` or explicit evidence expectations in the packet body.

## test-first

Use `test-first` when the target names behavior that can be exercised by an
automated or executable check.

The worker should:

- create or identify a check that fails before implementation
- confirm it fails for the expected reason
- make the smallest scoped change that drives it green
- record red and green evidence
- run broader regression checks when the packet asks for them or the change risk
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

Use `none` when the packet has no implementation or validation evidence obligation
beyond its normal output contract.

Examples:

- packet compilation
- non-semantic record cleanup
- read-only review where findings, not red/green evidence, are the output
- narrow prose cleanup that does not change behavior, protocol authority,
  acceptance, routing, or operator guidance
- a refactor whose safety is already covered by existing checks named in the packet

## Evidence And Audit

Packet verification is not audit.

Verification produces observations for this worker run. Audit challenges claims,
evidence, findings, risks, and implementation shape before another surface relies
on them.
