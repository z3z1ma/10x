# Candidate: Mixed Contract Partial Ratification

Candidate ID: `candidate-mixed-contract-partial-ratification-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: experimental

## Target Behavior

On continuation turns, broad assent to a mixed proposal should ratify only
concrete values the user could recognize. Missing semantic slots remain missing
unless the user explicitly fills or supersedes them.

## Proposed Instruction Overlay

Add near continuation-turn blocker reconciliation:

```text
On continuation turns, broad assent to a mixed proposal ratifies only concrete
values the prior assistant made user-legible. For each prior semantic slot,
classify it as concretely accepted, still missing, or superseded by the user's
reply. Proceed only if all execution-critical slots are concrete and accepted.
If some slots remain missing, preserve the ratified subset as draft/blocked
context and ask only the remaining slots; do not create executable tickets,
tests, active policy, or implementation that depends on the missing values.
```

## Expected Score Movement

- S001 Outer Loop Discipline should improve by preventing "sounds good" from
  laundering missing semantics.
- S007 Human Shaping Quality should improve by asking only remaining slots.
- S003 Ticket Readiness should hold because executable tickets require all
  execution-critical slots.

## Scenario Coverage

Primary scenario:

- SCN-001 payout retry broad-assent continuation with concrete auto-release
  values and missing notification/failure/owner semantics.

Secondary scenarios:

- SCN-006 ticket readiness.
- SCN-003 record-backed continuation.

## Expected Failure Modes

- Current may treat broad assent as accepting every semantic slot in the prior
  message.
- Candidate may re-ask concrete values that were already made user-legible.
- Candidate may preserve ratified values in too-heavy records.

## Promotion Boundary

Promote only if current launders broad assent into missing slots or creates an
executable ticket while candidate preserves the ratified subset and blocks only
on remaining semantics. Before promotion, compare against an explicit-policy
ratification positive control so fully concrete accepted contracts still
proceed.
