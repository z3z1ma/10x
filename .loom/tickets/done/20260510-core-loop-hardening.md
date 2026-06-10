# Core Loop Hardening

Status: done
Created: 2026-05-10
Updated: 2026-05-10

Legacy note: Risk — medium - changes core protocol language that shapes future agent behavior across shipped skills and docs.

## Summary

Harden Loom's shipped skill corpus so vague product work stays in the outer loop until shaped, complex work is sliced into ticket-ready units before execution, and fresh/separate worker runs use on-disk Ralph packets as their handoff contract.

This needs more than one ticket because shaping semantics, slicing semantics, Ralph/audit handoff, and public docs are distinct protocol claims with different file owners and verification lenses.

## Related Records

- `.loom/research/20260510-loom-loop-failure-analysis.md` - identifies the observed failure seams and recommended hardening path.
- `.loom/evidence/20260510-opencode-session-loop-failures.md` - records the eval transcript and record observations that motivate this plan.

## Strategy

Use a Core-first route. Update the authoritative Core skills and references first, then align playbooks and public docs that restate or trigger the same behavior. Keep the language positive and operational: shape before contract, split before ticket, packet before worker launch, evidence and audit before closure.

Do not add new runtime assumptions, validators, scripts, dashboards, or hidden machinery. This is a Markdown corpus change.

## Execution Units

### Unit: Outer-Loop And Slicing Doctrine

Ticket: .loom/tickets/done/20260510-shaping-slicing-doctrine.md

Strengthen `using-loom`, shaping references, ticket creation, plan creation, and slicing guidance so broad/vague work is shaped with the operator and complex work becomes ticket-ready child units before execution.

### Unit: Ralph And Audit Handoff Doctrine

Ticket: .loom/tickets/done/20260510-ralph-audit-handoff-doctrine.md

Strengthen Ralph, audit, ticket acting, and worker-oriented playbook guidance so bounded worker runs are compiled as `.loom/packets/ralph/` packet files and launched with thin packet-path prompts.

### Unit: Playbook And Public Doc Alignment

Ticket: .loom/tickets/done/20260510-playbook-doc-alignment.md

Align frontend/source/incremental/review playbooks and public docs with Core's shaping, slicing, and packetized worker semantics without creating a second protocol surface.

### Unit: Verification And Fresh Review

Ticket: .loom/tickets/done/20260510-loop-hardening-verification.md

Run package smoke/pack checks and Markdown diff checks, then use a Ralph packet for fresh-context review of the corpus change before final closure.

## Milestones

### Milestone: Core Semantics Hardened

Child tickets: .loom/tickets/done/20260510-shaping-slicing-doctrine.md, .loom/tickets/done/20260510-ralph-audit-handoff-doctrine.md

The authoritative Core skills state the intended outer-loop, slicing, and packet mechanics directly.

### Milestone: Surfaces Aligned

Child tickets: .loom/tickets/done/20260510-playbook-doc-alignment.md

Playbooks and public docs reinforce Core without adding a parallel protocol.

### Milestone: Evidence And Review Complete

Child tickets: .loom/tickets/done/20260510-loop-hardening-verification.md

Checks and fresh review support a bounded closure claim.

## Current State

Completed. Core, playbook, and public doc edits are implemented. All child tickets
are closed. Command evidence is recorded in
`.loom/evidence/20260510-loop-hardening-checks.md`, and packetized fresh-context review is
recorded in `.loom/reviews/20260510-loop-hardening-review.md` with a clear verdict.

Residual risk: only live follow-up evals can prove the changed instructions improve
future agent behavior.

## Journal

- 2026-05-10: Created plan from eval failure analysis with four child execution units.
- 2026-05-10: Implemented shaping/slicing doctrine, Ralph/audit handoff doctrine,
  and playbook/doc alignment slices; recorded package and Markdown check evidence.
- 2026-05-10: Completed plan after packetized fresh-context review returned clear
  and all child tickets closed.
