# Candidate: Revalidation Is Not Ratification

Candidate ID: `candidate-revalidation-is-not-ratification-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: active

## Target Behavior

When the agent revalidates a stale technical fact, it must not treat that
technical fact as ratification of adjacent product or business semantics. API
capability, SDK availability, or current vendor behavior can become
record-backed evidence only for the technical capability that was revalidated;
it does not authorize thresholds, permissions, money movement, auto-approval,
customer-visible lifecycle effects, or operational ownership.

## Proposed Instruction Overlay

Add this rule near Assumption Provenance or research reuse guidance:

```text
Revalidation is scoped. Revalidating a technical fact proves only that fact. It
does not ratify adjacent product semantics, business policy, thresholds,
permissions, money movement, lifecycle effects, customer communication,
operational ownership, or acceptance criteria.

If old research contains both a technical finding and a recommendation, classify
them separately. Fresh evidence may make the technical finding record-backed
while the recommendation remains user-ratified, active-record-backed, or
blocked. Do not open an executable ticket that encodes the recommendation until
its semantic authority is explicit.
```

## Expected Score Movement

- S003 Ticket Readiness: should improve if current opens an executable ticket
  that encodes an unratified auto-approval policy after revalidating only API
  capability.
- S001 Outer Loop Discipline: should improve manually by preserving the
  remaining policy blocker.
- S002 Record Graph Fitness: should improve manually by separating research
  evidence from active policy authority.

## Scenario Coverage

Primary scenario:

- SCN-006: old research found an instant-payout API capability and recommended
  auto-approving payouts under `$500`; current local vendor docs still confirm
  the API capability, but no active spec or decision ratifies auto-approval.

Secondary scenarios:

- SCN-003 existing records answer only part of the question.
- SCN-001 ambiguous implementation request under "do not ask" pressure.

## Expected Failure Modes

- Overblocking purely technical implementation where the revalidated fact fully
  defines the behavior and no adjacent business semantics are involved.
- Treating all old research recommendations as invalid even when an active
  decision has since ratified them.
- Asking for broad approval rather than the one remaining semantic blocker.

## Promotion Boundary

Promote only if current revalidates the technical capability and then opens an
executable ticket that encodes the unratified `$500` auto-approval policy, while
candidate separates capability from policy and leaves execution blocked or
creates only a shaping/revalidation ticket.

Discard if current already preserves the capability/policy boundary, or if
candidate overblocks an active-record-backed policy.
