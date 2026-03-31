# Appendix J — Acceptance And Packet Playbook

## Purpose

This appendix puts three closely related parent-side decisions in one place:

1. when a packet is fresh enough to reuse
2. what packet lineage fields mean
3. how the parent decides whether to continue, review, accept, document, or close work

Use this appendix when the repository feels structurally complete but the next operational decision is still unclear.

## Packet Freshness Decision Rule

Treat a packet as fresh enough to reuse only when all of the following are true:

1. the target record has not changed materially
2. the governing source records have not changed materially
3. the repository/worktree scope has not changed materially
4. the allowed write boundary has not changed materially
5. the intended child task is still the same bounded task

If any of those are false, compile a fresh packet.

## What Counts As A Material Change

Examples of material target or source changes:

- ticket acceptance criteria changed
- packet mode changed from review to execution
- plan/spec constraints changed
- scope widened from one repo to another
- truth-boundary doctrine changed

Examples of non-material changes:

- typo fixes in unrelated prose
- added notes that do not change the bounded task contract

When unsure, prefer recompiling.

## Packet Lineage Fields

Current packet lineage in this repository should answer three questions.

### `run_family`

What continuing target or run family this packet belongs to.

Use it to group packets for the same ticket or review target.

### `prior_packet`

Which earlier packet in the same family came immediately before this one.

Use it when the new packet is part of a sequence rather than a stand-alone first packet.

### `supersedes`

Which older packet this packet intentionally replaces as the current preferred handoff contract.

Use it when a new packet should become the preferred forward path for the same bounded work.

## Parent Acceptance And Reconciliation Sequence

After any bounded child run returns, the parent should work through this sequence.

### 1. Scope and authority check

Ask:

- did the child stay within declared repository/worktree scope
- did the child stay within the allowed write set

If no, do not accept the result as normal progress.

### 2. Evidence check

Ask:

- what verification was actually performed
- what durable evidence was produced or linked

If the child claims completion without evidence, the parent should treat that as incomplete.

### 3. Ticket-ledger reconciliation check

Ask:

- has the ticket been updated so it tells the truth about the new state
- are blockers, risks, and docs disposition current

If no, the parent should reconcile the ticket before treating the run as accepted workflow history.

### 4. Critique/docs policy check

Ask:

- does the change class require critique before acceptance
- does the change now require docs work for truthful explanation

If yes, route to the owning subsystem instead of closing the work early.

### 5. Closure check

Ask:

- are acceptance criteria satisfied
- is required verification complete
- is the durable record graph coherent

Only then should the parent consider `complete_pending_acceptance` or `closed`.

## Quick Outcome Matrix

### Child says `continue`

Typical parent interpretation:

- ticket remains `active`
- next owner is usually `loom-ralph` or `loom-tickets`

### Child says `stop`

Typical parent interpretation:

- bounded execution step is finished
- ticket often moves to `review_required` or `complete_pending_acceptance`
- next owner is often `loom-critique`, `loom-docs`, or final ticket reconciliation

### Child says `blocked`

Typical parent interpretation:

- ticket usually moves to `blocked`
- blocker must be made explicit

### Child says `escalate`

Typical parent interpretation:

- parent chooses a higher-order next owner such as `loom-critique`, `loom-plans`, `loom-specs`, or `loom-workspace`

## Why This Appendix Exists

The repository already contains the pieces of this logic across rules, skills, appendices, and verification records.

This appendix exists so a fresh agent can read one place and apply the policy without guessing how those pieces combine.
