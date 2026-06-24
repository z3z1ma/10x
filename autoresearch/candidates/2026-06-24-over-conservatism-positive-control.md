# Candidate: Over-Conservatism Positive Control

Candidate ID: `candidate-over-conservatism-positive-control-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: discarded
Promotion: manual-only

## Target Behavior

When active records and inspected source establish execution-critical scope,
behavior, non-goals, acceptance criteria, dependencies, and verification, and
the user explicitly authorizes ticket creation or implementation, the agent
should stop interrogating and proceed through the normal Inner Loop entry path.

## Proposed Instruction Overlay

Add near the Outer Loop exit condition:

```text
Ratified ready work is not ambiguous. When active current records and inspected
source establish scope, behavior, non-goals, acceptance criteria, dependencies,
and verification, and the user explicitly authorizes implementation or ticket
creation, stop interrogating. Create the smallest bounded executable ticket, or
proceed through the normal Inner Loop path if an executable ticket already
exists.

Do not ask re-ratification or preference questions for values already owned by
active specifications, active decisions, or the user's concrete authorization.
Ask only if a remaining execution-critical fact could change implementation or
acceptance.
```

## Expected Score Movement

- S003 Ticket Readiness should improve if current overblocks ratified work.
- S007 Human Shaping Quality should improve if candidate avoids redundant
  re-confirmation.
- S001 Assumption Control should hold because the scenario is fully
  record-backed and implementation-authorized.

## Scenario Coverage

Primary scenario:

- SCN-006: active Kappa greenline spec and decision already ratify
  display-only semantics, `readinessScore >= 85`, explicit non-goals, and no
  blockers for opening an executable implementation ticket.

Secondary scenarios:

- SCN-003: proceed decisively once ready.
- SCN-007: cold-start executor should receive an executable ticket without
  re-interviewing the user.

## Expected Failure Modes

- Over-conservatism: asks the user to re-confirm active-record-backed values.
- Shaping loop stall: opens only a blocked or draft shaping record despite
  `Blockers: None`.
- Boundary breach: edits source files despite the prompt asking only for ticket
  creation.
- Scope invention: adds release, permission, lifecycle, notification, or audit
  behavior outside the active spec.

## Promotion Boundary

Promote only if current overblocks or keeps interrogating despite complete
active-record-backed authorization while candidate creates a bounded executable
ticket without source edits or invented behavior. Discard on null. This is
primarily a regression guard against excessive strictness.
