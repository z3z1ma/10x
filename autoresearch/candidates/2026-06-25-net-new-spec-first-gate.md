# Candidate: Net-New Spec First Gate

Candidate ID: `candidate-net-new-spec-first-gate-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

Prevent ratified net-new behavior from collapsing directly into one executable
ticket or direct implementation. Once a new product/app/API/CLI/UI/workflow
behavior contract is concrete enough to execute, the agent should first create
or update an active specification that owns the behavior, then derive
implementation tickets from that spec. The parent/child ticket graph owns
execution and sequencing, not the durable behavioral contract.

## Proposed Instruction Overlay

Add near the Outer Loop exit condition and the specification/ticket boundary:

```text
Net-new or important behavior needs a specification before executable tickets.
When clarified work creates or materially changes user-visible product behavior,
domain workflow, durable data semantics, UI/API/CLI behavior, permissions,
lifecycle states, notification behavior, money, security/privacy posture,
operational ownership, or any behavior multiple tickets, subagents, reviews, or
future sessions must agree on, the next durable record after ratification is an
active specification or an update to an existing active specification.

The specification owns the behavioral contract: purpose and scope, explicit
exclusions, behavior, acceptance criteria, constraints, and verification
scenarios. Implementation tickets derive from that specification and reference
it; they own bounded execution slices, not the canonical behavior contract.

For greenfield apps, tools, CLIs, APIs, user workflows, persisted behavior, or
other net-new surfaces, do not open a single all-purpose executable ticket as a
substitute for the specification. If implementation has multiple independent
surfaces, create a parent plan and one or more child tickets after the
governing specification exists. If implementation is one coherent slice, one
child ticket may be enough, but it must reference the active specification.

Do not implement in the same turn as authoring or materially updating the
governing specification and opening the first executable ticket for non-trivial
net-new behavior. Stop after the spec/ticket structure unless the work is
trivial enough to need no ticket.

A separate specification is not required for exact mechanical edits, typo
fixes, formatting-only changes, record-only maintenance, no-code/reuse answers,
or implementation work that is already fully governed by one active
specification and does not change its behavior.
```

## Expected Score Movement

- S001/S003 should improve on ratified greenfield continuations by preventing
  direct implementation after ambiguity resolution.
- S002 should improve by creating the correct durable record type for behavior.
- S006 should improve later because closure has a spec to compare evidence and
  reviews against.
- S005 should hold on exact trivial edit, exact formatting edit, and no-code
  controls.

## Scenario Coverage

Primary:

- SCN-001 continuation from a shaped greenfield to-do app after the user
  ratifies behavior.

Regressions:

- Exact one-line source edit should remain record-free.
- Exact formatting edit should remain record-free.
- Already spec-backed executable ticket should not create duplicate specs.
- No-code answer where source/records already satisfy the goal should not
  create a spec.

## Expected Failure Modes

- Agent creates a spec and then still implements in the same turn.
- Agent treats one implementation ticket with many acceptance criteria as a
  substitute for the spec.
- Agent over-applies the rule to exact mechanical edits.
- Agent creates duplicate specs when an active governing spec already exists.
- Agent writes a weak spec after the ticket as a retrospective artifact rather
  than using it as the ticket source.

## Promotion Boundary

Promote only if the candidate blocks direct implementation and produces an
active governing spec before executable tickets on the primary continuation,
while preserving exact mechanical edit controls. If the primary still
implements in the same turn, revise the candidate before promotion.

## Result

Promoted after:

- `EXP-20260625-737-net-new-spec-first-gate-candidate-batch-live-micro`
- `EXP-20260625-738-net-new-spec-first-corrected-formatting-regression-live-micro`
- `EXP-20260625-739-post-promotion-net-new-spec-first-sanity-live-micro`

Current canonical had reproduced the failure in
`EXP-20260625-736-greenfield-spec-before-ticket-continuation-live-micro`.
The candidate created an active governing spec plus parent/child ticket
structure, avoided app files in the same turn, preserved exact one-line source
edits, and preserved corrected exact formatting edits. Post-promotion canonical
matched the candidate behavior.
