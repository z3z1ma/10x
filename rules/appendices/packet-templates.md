# Appendix D — Packet Templates

## Purpose

These templates describe the minimum useful shape of common packet families.

They are not meant to replace packet compilation logic. They are meant to make the packet contract legible to the parent before launch and to the child during execution.

Each packet should make it easy to answer:

- what this run is for
- what sources matter
- what the child may do
- what the child must return
- how the parent should interpret the result

## Ticket Execution Packet

Use this packet for bounded implementation or mutation against a ticket target.

### Parent intent

The parent has one ticket-owned execution step that is specific enough for one bounded child run.

### Must include

- target ticket ref
- governing plan, spec, research, or constitution refs when those materially constrain the work
- current ticket state excerpt or full body
- scope information
- allowed write set
- verification expectations
- continue/stop/blocked/escalate output contract

### Good child instruction shape

The packet should make it obvious that the child is expected to:

- perform one bounded execution step
- stay inside the declared scope and write boundary
- report what changed
- report verification
- recommend the next durable state transition

## Critique Packet

Use this packet for bounded review-only analysis.

### Parent intent

The parent wants an adversarial review of a specific target against a specific review question.

### Must include

- target under review
- review question
- focus areas
- severity and confidence scales
- evidence set
- output contract for verdict, findings, residual risk, and follow-up actions

### Good child instruction shape

The packet should tell the child to produce evidence-backed review, not implementation.

## Docs Update Packet

Use this packet for accepted-shape explanation work.

### Parent intent

The parent wants accepted truth sources turned into a durable explanation for a known audience.

### Must include

- target doc
- accepted system shape
- intended audience
- verification basis
- truth sources
- stale triggers
- allowed write set

### Good child instruction shape

The packet should make it obvious that the child is expected to explain accepted truth clearly rather than speculate or expand unfinished work.

## Diagnostic Packet

Use this packet to identify issues, gaps, or blockers without write authority.

The packet should clearly say:

- what system or artifact is being diagnosed
- what question the diagnosis should answer
- what evidence is available
- what form the findings should take

## Reconciliation Packet

Use this packet to compare child output or artifacts with canonical truth and suggest acceptance or follow-up actions.

The packet should help the parent answer:

- what happened in the child run
- what canonical records now need updating
- what evidence is strong enough to accept
- what gaps still require more work
