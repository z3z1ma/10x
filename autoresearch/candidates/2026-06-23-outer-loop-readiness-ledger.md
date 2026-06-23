# Candidate: Outer Loop Readiness Ledger

Candidate ID: `candidate-outer-loop-readiness-ledger-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: experimental
Promotion: manual-only

## Target Behavior

When shaping work with multiple material unknowns, the agent should make the
state of ambiguity legible without turning the response into a process ritual.
It should show what is already known from inspection, which unknowns still block
execution, and what next safe action each answer unlocks.

This is an instruction overlay candidate. It is not a canonical change to
`SKILL.md`.

## Proposed Instruction Overlay

Add this Outer Loop readiness rule:

```text
For non-trivial Outer Loop work with more than one material unknown, use a
compact readiness pass before asking or ticketing:

- Known from inspection: <one concise line>.
- Blocking unknowns: <only current blockers, in dependency order>.
- Next safe action: <what can happen after the blocker is answered>.

Keep the readiness pass compact. Do not use it for trivial work. Do not convert
it into a durable record unless it has independent record force.

Before creating an executable ticket or entering implementation, verify the exit
gate in substance, not as a pasted checklist:

- intended behavior is known;
- scope and non-goals are known;
- acceptance criteria are known;
- constraints and safety rails are known;
- relevant records/code/artifacts were inspected;
- implementation authorization is explicit.

If any exit-gate item is missing, stay in the Outer Loop and ask the blocker
question that would change the next safe action.
```

## Expected Score Movement

- S001 Outer Loop Discipline: should improve on multi-unknown ambiguity by
  preserving what is known, what blocks execution, and what answer changes.
- S003 Ticket Readiness: should improve by reducing premature executable ticket
  creation before the exit gate is satisfied.
- S007 Human Shaping Quality: should improve if the readiness pass makes
  repeated questioning feel useful instead of evasive.

## Scenario Coverage

Primary scenarios:

- SCN-001 ambiguous-implementation-request
- SCN-002 missing-acceptance-criteria-under-pressure
- SCN-006 ticket-boundary

## Expected Failure Modes

- Ledger theater: the agent may print a table without improving judgment.
- Verbosity regression: the readiness pass may make simple blockers too long.
- Over-blocking: the agent may classify downstream details as execution
  blockers.

## Promotion Boundary

This candidate cannot be promoted without live evidence, manual inspection,
held-out checks, review, and explicit human promotion. It must not directly edit
`SKILL.md`.
