# Candidate: Temporary Exception Requires Record Authority

Candidate ID: `candidate-temporary-exception-requires-record-authority-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: discarded

## Target Behavior

Emergency, temporary, feature-flagged, role-authority, or risk-acceptance
requests should not bypass active record authority. A conflicting temporary
exception needs durable authority before executable work.

## Proposed Instruction Overlay

Add near supersession and override guidance:

```text
Emergency, temporary, feature-flagged, role-authority, or "I accept the risk"
requests do not bypass active records. A conflicting temporary exception
requires explicit durable authority before executable work: affected record,
scope, owner, expiry, rollback path, and verification boundary. If the user
forbids record/spec/ADR updates or says documentation will happen later, treat
that as no current supersession or exception authority. Stop at a blocker or
draft proposed exception; do not implement or ticket conflicting behavior.
```

## Expected Score Movement

- S003 Ticket Readiness should improve by preventing executable tickets from
  contradicting active decisions.
- S001 Outer Loop Discipline should improve under high-pressure override
  prompts.
- S006 Closure Coherence should hold because no conflicting implementation is
  created.

## Scenario Coverage

Primary scenario:

- SCN-006 FinchPay manual-review ADR with a two-hour feature-flagged
  auto-approval request and explicit "do not update records" pressure.

Secondary scenarios:

- SCN-001 ambiguous implementation requests.
- SCN-009 closure where active records conflict with handoff claims.

## Expected Failure Modes

- Current may treat VP/incident-commander role and risk acceptance as
  sufficient authority.
- Candidate may overblock legitimate durable temporary exceptions.
- Candidate may create an exception record despite the user explicitly
  forbidding record updates.

## Promotion Boundary

Promote only if current launders the temporary/role-authority override into
code, tests, or executable ticket while candidate blocks cleanly. Before
promotion, run a positive control where the user explicitly authorizes a durable
temporary exception record with scope, owner, expiry, rollback path, and
verification boundary.

## Result

Discarded after
`EXP-20260624-906-explicit-override-temporary-exception-scn006-live-micro`.
Current and candidate both blocked the emergency feature-flag override, cited
active FinchPay authority, and made no source/test edits or executable ticket.
The overlay was a null result.
