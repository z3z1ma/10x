# Candidate: Honest Subagent Handoff

Candidate ID: `candidate-honest-subagent-handoff-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: experimental
Promotion: manual-only

## Target Behavior

When 10x requires child-ticket execution by a subagent, the agent should use an
actual delegation primitive when one exists and should not fake delegation when
one does not. It should keep parent-agent ownership of orchestration, evidence,
review, and promotion decisions.

This is an instruction overlay candidate. It is not a canonical change to
`SKILL.md`.

## Proposed Instruction Overlay

Add this Inner Loop delegation rule:

```text
When an executable child ticket exists and implementation is requested, first
determine whether this harness exposes an actual subagent/delegation primitive
and whether delegation is authorized.

If an actual subagent primitive is available, delegate the child ticket with:

- the ticket path and scope;
- relevant specs, decisions, research, knowledge, and evidence;
- explicit file/work ownership;
- forbidden scope expansion;
- required verification and changed-file reporting.

If no actual subagent primitive is available, do not pretend delegation
happened. State the harness limitation, keep the parent from editing
implementation files, and ask for either a real executor/handoff or explicit
authorization to run the current agent as the child-ticket executor.

If the user explicitly authorizes the current agent to act as the child-ticket
executor in a no-subagent harness, record that role switch in the ticket, execute
only that ticket's scope, and return to parent-agent review/closure discipline
after implementation.
```

## Expected Score Movement

- S003 Ticket Readiness: should improve by preserving parent/child boundaries
  instead of silently collapsing them.
- S006 Closure Coherence: should improve because subagent output remains a claim
  for parent review rather than becoming self-certified truth.
- S007 Human Shaping Quality: may improve by naming the real harness limitation
  instead of producing fake "assigned to subagent" claims.

## Scenario Coverage

Primary scenario:

- SCN-007 parent-agent-implementation-trap

Secondary scenarios:

- SCN-006 ticket-boundary
- SCN-009 closure-trap

## Expected Failure Modes

- Paralysis: the agent may refuse to execute even when the user and harness
  clearly authorize single-agent execution.
- Boundary weakening: the role-switch clause may be overused and collapse the
  parent/child invariant.
- Tool hallucination: the agent may claim a subagent exists without invoking a
  real mechanism.

## Promotion Boundary

This candidate cannot be promoted without live evidence in a harness where
subagent availability is explicit, manual inspection, review, and explicit
human promotion. It must not directly edit `SKILL.md`.
