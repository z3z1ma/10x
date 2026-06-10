# Decision 0002: Ticket-Owned Worker Handoffs

Status: active
Created: 2026-05-15
Updated: 2026-05-15

## Summary

Agent Loom will remove `packet` as an active Loom surface. Tickets and their linked records own durable worker and audit context; Ralph remains the named discipline for bounded worker and review runs. Transient launch prompts may carry run-specific instructions, but they must not become the durable source of truth.

## Context

`.loom/research/20260510-loom-loop-failure-analysis.md` and the follow-up 2026-05-13 tickets intentionally moved Loom toward packet-before-worker execution. That change solved a real failure mode: worker prompts could otherwise bypass the recovery graph, widen scope, or return unsupported closure claims.

The packet surface has now shown its own failure mode. It duplicates ticket scope and related references, creates a second place where execution truth can drift, and makes agents maintain a packet record even when the durable information properly belongs in the ticket. The operator selected the path where there is no future packet surface, while preserving Ralph as the bounded worker and audit discipline.

## Decision

Future Loom work should not create `.loom/packets/`, `packet:` IDs, or packet records as active execution artifacts.

Anything needed for future recovery belongs in the ticket or the surface that owns that truth:

- tickets own executable scope, related records, durable worker context, read/write boundaries, stop conditions, evidence posture, review posture, live state, worker-output reconciliation, and closure;
- specs own intended behavior;
- plans own multi-ticket strategy and decomposition;
- research owns investigation and tradeoffs;
- evidence owns observed validation facts;
- audit owns adversarial review findings and verdicts;
- knowledge owns reusable accepted understanding.

Ralph remains a named discipline for bounded worker and review runs. A Ralph run starts from a ticket, plan execution unit, audit target, or bounded evidence request, not from a packet file. The launch prompt can include transient execution instructions, but the durable mission, scope, constraints, references, evidence expectations, stop conditions, and reconciliation target must already live in the ticket or linked records.

Historical packet records may remain as historical artifacts when existing tickets, evidence, or audits cite them. They should not be rewritten to pretend packets never existed, and they should not guide future active workflow except as history.

## Alternatives

- Keep packets as the required worker contract. Rejected because packet records duplicate ticket-owned context and preserve a second truth surface for execution state.
- Retire Ralph language entirely and use generic sub-agent language. Rejected because the operator wants to keep Ralph as the bounded worker and audit discipline while removing only the packet artifact.
- Soft-deprecate packets while allowing optional packet records. Rejected because optional packets preserve the ambiguity and drift this decision is meant to eliminate.

## Consequences

Core Loom doctrine, record skills, Ralph/audit guidance, ticket templates, agent prompts, adapter permissions, Playbook macro bodies, generated command surfaces, docs, and validation checks need a coordinated migration from packet-owned execution contracts to ticket-owned worker handoffs.

Tickets must become slightly more explicit about durable worker context: likely read scope, write scope, related records, stop conditions, evidence posture, audit posture, and expected worker output. That is an accepted cost because it keeps durable execution truth in the work unit that owns live state and closure.

Worker launch prompts become intentionally transient. If a worker returns information needed for recovery, acceptance, evidence, audit, or future continuation, the parent must reconcile that output into the ticket, evidence, audit, or another owning surface rather than leaving it only in harness output.

Parallel worker coordination should use separate child tickets when units can close independently, or ticket-defined non-overlapping sub-scopes when one ticket truly owns one closure claim. Packet IDs must not be the coordination handle.

## Accepted Risks

- Tickets can become bloated if agents copy entire worker prompts into them. Mitigation: tickets should preserve durable context and output summaries, not transient prompt mechanics.
- Removing packet files reduces a standalone record of the exact launch. Mitigation: durable launch-relevant facts belong in tickets; transient prompt text only belongs in evidence if the exact prompt is itself needed as proof.
- Existing historical records and docs contain packet references. Mitigation: preserve historical `.loom` references as history, but remove packet requirements from active product doctrine and human-facing current docs.

## Revisit Or Supersede If

- Ticket records become too overloaded to remain usable as executable work units.
- A supported harness offers a durable, inspectable worker-run artifact that does not become a second Loom truth surface.
- Audit or evidence review repeatedly needs exact launch prompts as durable proof rather than ticket-owned scope and worker-output reconciliation.

## Related

- `.loom/specs/superseded/ticket-owned-worker-handoffs.md` - intended behavior contract for the new worker handoff model.
- `.loom/tickets/done/20260515-ticket-owned-worker-handoffs.md` - implementation plan consuming this decision.
- `.loom/research/20260510-loom-loop-failure-analysis.md` - historical reason packet-before-worker doctrine was introduced.
- `.loom/tickets/done/20260513-ticket-execution-ralph-language.md` - historical ticket that centered ticket execution on Ralph packets and is superseded in direction by this decision.
- `.loom/tickets/done/20260513-ralph-language-consolidation.md` - historical ticket that centered worker and audit language on Ralph packets and is superseded in direction by this decision.
