# Ralph Packet Reference

## Purpose

Use this reference when the parent needs to assemble a packet for one bounded Ralph execution run.

The packet should give a fresh worker enough context to execute one bounded iteration without reconstructing the workflow from chat history.

## Minimum Packet Contract

An execution packet for Ralph should include, in concrete terms:

1. target ticket
2. governing plan, spec, research, or constitution refs that materially constrain the work
3. packet mode and packet style
4. scope information
5. trust boundary
6. allowed write set
7. verification expectations
8. output contract
9. stop and escalation conditions

If any of those are missing, the packet is structurally present but operationally weak.

## What A Strong Ralph Packet Should Help A Fresh Worker Understand

A strong Ralph packet should let a fresh worker understand:

- what exact ticket is bound to the run
- what larger plan or spec context constrains the ticket
- what the concrete problem framing is right now
- what the worker may change and what it may only read
- what evidence the parent expects before the iteration can count as landed
- what should happen if the worker gets blocked, reaches a stopping point, or discovers a mismatch between packet and reality

## Positive Assembly Checklist

Before launching the child, confirm that the packet tells the child:

- what work to do
- where the work is allowed to happen
- which records matter most
- what completion looks like
- what verification to run or report
- what to return to the parent

Also confirm that the packet says enough about:

- why this bounded iteration exists now
- what prior packet or run family it belongs to
- what would make the packet stale before reuse

## Good Default

For most execution work in this repo, the parent should compile:

- subsystem: Ralph
- target kind: ticket
- mode: `execution`
- style: `reference-first` unless hermetic replayability is the stronger need
- write boundary: target ticket plus any explicitly approved additional refs or paths

That default is strong because it keeps the run small, keeps ticket truth primary, and still makes the packet durable enough for later inspection.

## Packet Review Questions

Before launch, read the packet once as if you were the child and ask:

1. do I know exactly what ticket owns this work
2. do I know which records matter most
3. do I know what I am allowed to change
4. do I know what verification matters
5. do I know what to return if I get blocked or discover a mismatch

If the answer to any of those is no, the packet is not ready yet.

## Parent Assembly Procedure

Before launching a Ralph worker, the parent should do this in order:

1. read the ticket and the governing context
2. decide whether the next move is truly bounded execution rather than critique or docs work
3. decide the write boundary
4. decide packet mode and packet style
5. compile the packet
6. read the packet once as if you were the child
7. launch only after the packet reads like a local contract rather than a reminder note

## What The Packet Should Cause The Child To Do

The child should be able to infer this procedure from the packet:

1. read the packet completely
2. perform one bounded execution step
3. keep within scope and write authority
4. keep the ticket truthful if ticket mutation is allowed
5. report outcome, evidence, blockers, and next recommendation before exit

## Example Strong Packet Summary

```text
Target: ticket:0002
Mode: execution
Style: reference-first
Scope: derived from the target ticket's `repository_scope`
Allowed write set: target ticket, one verification record, packet-family run artifacts
Verification expectation: report helper validation and scope confirmation evidence
Output contract: outcome, changed records, verification summary, blockers, and continue/stop/blocked/escalate recommendation
```

## Example Weak Packet Summary

```text
Target: the helper work
Mode: execution
```

Why this is weak:

- the target is ambiguous
- the scope is missing
- the write boundary is missing
- the parent would not be able to reconcile the result truthfully

## Failure Conditions

Treat the packet contract as insufficient when:

- the worker would need to guess which ticket owns the work
- the packet gives execution authority without a concrete write boundary
- the verification expectation is missing or hand-wavy
- the output contract is too thin for the parent to reconcile truthfully afterward

## Persistence Rule

Packets persist by default as durable Ralph run artifacts.

The parent may supersede an older packet, but should not rely on memory or chat history in place of the persisted artifact.

Persistence matters because later readers should be able to inspect the exact handoff contract the worker received.
