# Ticket-Owned Worker Handoffs

Status: active
Created: 2026-05-15
Updated: 2026-05-15

## Summary

This spec defines Loom's intended worker and audit handoff behavior after retiring packets as an active surface: tickets own durable execution context, while Ralph remains the bounded worker and review discipline.

Downstream tickets should cite this spec when removing packet language from Core doctrine, ticket/audit/Ralph skills, agent prompts, Playbooks, adapter permissions, docs, or validation checks.

## Product Slice

This spec owns the behavior contract for bounded Loom worker and review runs: where durable execution context lives, how transient launch prompts relate to tickets, how worker output is reconciled, and how Ralph remains useful without packet records.

This spec does not own exact source implementation, harness-specific sub-agent invocation syntax, individual Playbook workflow content except where it mentions worker handoff mechanics, or historical packet records already cited by old tickets and audits.

## Spec Set Coverage

This spec fills the behavior gap created by `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md`. Without it, implementation tickets would have to infer whether packet removal means retiring Ralph, making worker prompts authoritative, or moving packet fields into an unspecified new surface.

Adjacent behavior outside this spec:

- `.loom/specs/loom-driver-agent.md` owns the explicit Driver persona that coordinates these runs.
- `.loom/specs/loom-weaver-agent.md` owns the outer-loop shaping persona and does not authorize worker execution.
- `.loom/specs/playbook-explicit-macros.md` owns Playbook invocation behavior; Playbooks must preserve this worker handoff model when they mention execution.

## Problem

Packet records were introduced to prevent unbounded sub-agent prompts from bypassing Loom's recovery graph. They solved that failure mode, but they also created a second execution-truth surface beside the ticket. In practice, the durable fields a packet carried are ticket fields: scope, related records, read and write boundaries, constraints, stop conditions, evidence posture, review posture, and worker-output reconciliation.

The intended model must keep bounded worker discipline without preserving packet records as a separate artifact.

## Desired Behavior

A bounded Loom worker or review run starts from graph-supported execution state: usually a ticket, plan execution unit with child ticket, audit target, or bounded evidence request. The durable contract for the run lives in that ticket or linked records.

The launch prompt is a transient transport wrapper. It may say which ticket to read, name the immediate run objective, remind the worker of current constraints, and request a structured result. It must not be the only durable place that names scope, acceptance, related records, write boundaries, stop conditions, evidence expectations, or output needed for future continuation.

Ralph remains the name for the bounded worker and review discipline. Ralph no longer implies a `packet:` record or `.loom/packets/` path.

## Not Doing

- Do not create future `.loom/packets/` records or `packet:` IDs.
- Do not retire Ralph as a named worker and audit discipline.
- Do not make transient launch prompts authoritative durable records.
- Do not delete, rewrite, or reinterpret historical packet records that existing tickets, evidence, or audits cite.
- Do not move intended behavior, research conclusions, evidence observations, or audit verdicts into tickets merely because packets are gone; those surfaces still own their truths.
- Do not use one ticket for several independent worker units that need separate closure stories; split into child tickets instead.

## Requirements

- REQ-001: Loom MUST NOT create packet records, `packet:` IDs, or `.loom/packets/` paths for future active worker or review handoffs.

- REQ-002: Tickets MUST own the durable execution context needed for bounded worker and review runs, including scope, related records, likely read and write boundaries, constraints, stop conditions, evidence posture, review posture, and expected worker-output reconciliation.

- REQ-003: Ralph MUST remain the named discipline for bounded worker and review runs, but Ralph runs MUST start from tickets, plan execution units with child tickets, audit targets, or bounded evidence requests rather than packet files.

- REQ-004: A worker launch prompt MAY carry transient run instructions, but any fact needed for future recovery, acceptance, evidence, audit, closure, or continuation MUST be reconciled into the ticket or another owning Loom surface.

- REQ-005: Worker reports MUST be treated as claims until reconciled against ticket scope, changed files, changed records, and evidence. A returned worker message is not acceptance evidence by itself.

- REQ-006: Substantive audit MUST run as a bounded Ralph review from the ticket, evidence, diffs, and linked records, then be recorded in `.loom/audit/` after the review returns. Audit verdicts do not live in transient launch prompts.

- REQ-007: Parallel worker coordination MUST use separate child tickets when closure claims are independent, or ticket-defined non-overlapping sub-scopes when one ticket truly owns the closure claim. Packet IDs MUST NOT be the coordination handle.

- REQ-008: Historical packet records MAY remain available as historical artifacts and citations, but active doctrine, templates, prompts, and docs MUST NOT teach future agents to create or depend on new packet records.

## Scenarios

### SCN-001: Ticket-Owned Worker Run

Exercises: REQ-002, REQ-003, REQ-004, REQ-005

GIVEN an open ticket has scope, related records, acceptance, likely write boundaries, stop conditions, and evidence posture
WHEN a bounded worker run is needed
THEN the coordinator launches the worker from the ticket and linked records
AND uses only transient prompt text for run transport
AND reconciles returned claims into the ticket, evidence, audit, or another owning surface.

### SCN-002: Missing Durable Context

Exercises: REQ-002, REQ-004

GIVEN a worker launch would require scope, constraints, related references, or evidence expectations that are not in the ticket or linked records
WHEN the coordinator prepares the run
THEN the coordinator updates or blocks the ticket before launch instead of hiding durable context in the prompt.

### SCN-003: Audit Review

Exercises: REQ-005, REQ-006

GIVEN implementation evidence exists for a non-trivial ticket
WHEN an adversarial review would materially improve trust
THEN the coordinator launches a bounded Ralph review from the ticket, diffs, evidence, and linked records
AND records the returned findings in an audit record
AND leaves closure disposition in the ticket.

### SCN-004: Parallel Work

Exercises: REQ-007

GIVEN two work units can run independently
WHEN they have separate closure stories
THEN the plan or coordinator creates separate child tickets
AND each worker run starts from its child ticket
AND integration is reconciled through ticket state, evidence, and audit rather than packet IDs.

### SCN-005: Historical Packet Citation

Exercises: REQ-008

GIVEN an old closed ticket cites a historical packet
WHEN current doctrine is updated
THEN the historical citation remains true as history
AND current active instructions stop teaching future packet creation.

## Evidence Plan

- REQ-001 / REQ-008: Targeted grep over active product surfaces shows no instruction to create `.loom/packets/`, `packet:` records, or Ralph packet files, excluding historical `.loom` records.
- REQ-002 / SCN-001: Source inspection of ticket skill guidance and templates shows tickets carry durable worker context and output reconciliation expectations.
- REQ-003 / SCN-001: Source inspection of Ralph, Driver, and audit guidance shows Ralph remains as bounded worker/review discipline without packet records.
- REQ-004 / SCN-002: Source inspection shows transient launch prompts are not durable truth and returned worker output is reconciled into owning surfaces.
- REQ-006 / SCN-003: Audit guidance and examples show review findings are recorded in audit after bounded review returns.
- REQ-007 / SCN-004: Parallel coordination guidance uses child tickets or ticket-defined sub-scopes rather than packet IDs.

## Quality Bar

After implementation, a future agent should understand that removing packets does not mean unbounded worker prompts. The ticket is the durable execution contract; the prompt is transport; Ralph is the bounded discipline; evidence and audit remain separate proof surfaces.

## Interface Contract

- Inputs: Open tickets, plan execution units with child tickets, audit targets, bounded evidence requests, and explicit operator instructions to coordinate worker or review runs.
- Outputs: Worker launch prompts, worker-output reconciliation in tickets, evidence observations, audit records after review, and truthful ticket state transitions.
- Side effects: Writes durable context to `.loom/tickets/`, observations to `.loom/evidence/`, and review findings to `.loom/audit/`; does not create `.loom/packets/` for future work.
- Error semantics: If durable context is missing, stop and update or block the ticket rather than launching from prompt-only context.
- Compatibility or deprecation: Historical packet records remain historical artifacts. Active product doctrine treats packet creation as retired.

## Examples And Non-Examples

Example worker launch posture:

"Read `.loom/tickets/done/20260515-core-ticket-owned-worker-doctrine.md` and its related records first. Execute only ACC-001 through ACC-003 within the ticket scope, stop if source reality contradicts the ticket, and return changed files, validation, unverified claims, and recommended next state for ticket reconciliation."

Non-example worker launch posture:

"Here is the full scope and acceptance in this prompt; do the work and tell me if it worked." 

Non-example record behavior:

Creating `former packet 20260515T..` for a future worker run, or leaving the only evidence-relevant worker output in a transient sub-agent message.

## Constraints

- This spec implements `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md`.
- The source migration must not delete or rewrite historical `.loom/packets` records as part of current-product cleanup.
- Product-visible doctrine must not explain this change as repository dogfood process; it should teach the runtime behavior directly.

## Related Records

- `.loom/decisions/decision-0002-ticket-owned-worker-handoffs.md` - durable decision removing packets as an active surface while keeping Ralph.
- `.loom/tickets/20260515-ticket-owned-worker-handoffs.md` - coordinated source migration plan.
- `.loom/specs/loom-driver-agent.md` - Driver persona that coordinates ticket-owned Ralph runs.
- `.loom/specs/loom-weaver-agent.md` - Weaver persona that shapes records before execution.
- `.loom/specs/playbook-explicit-macros.md` - Playbooks must preserve this model when adding workflow pressure.
