# Ralph Artifact Schema Reference

## Purpose

Ralph artifacts preserve the durable history of one bounded execution run family without replacing ticket truth.

Use Ralph artifacts to answer:

- what packet launched the run
- what execution attempt happened
- what the child reported
- what reconciliation followed

## Core Rule

Ralph artifacts are durable run artifacts, not canonical execution truth.

The ticket still owns live execution state.

Ralph artifacts exist to make bounded execution observable and resumable, not to become a second ledger.

## Expected Artifact Family

The simplest useful Ralph artifact set is:

- a packet file
- optional iteration notes when multiple bounded attempts happen in one run family
- optional reconciliation notes when parent-side interpretation needs to be preserved

If runtime or launch-observability artifacts are later added, they should help a later reader understand what happened during the bounded run without replacing the ticket or verification records.

## Artifact Ownership Rule

Use Ralph artifacts to preserve what the child was told, what happened during the bounded run, and how the parent interpreted the result.

Do not use Ralph artifacts as a shadow ticket ledger. If the run changes execution truth, the ticket must absorb that truth.

## Packet Expectations

A Ralph packet should clearly identify:

- target ticket ref
- packet mode and style
- scope and allowed write set
- relevant source refs
- verification expectations
- output contract

Good Ralph packets are detail-first. A worker should not need to reverse-engineer the current ticket state from neighboring artifacts.

## Frontmatter And Structural Expectations

Ralph packet and run artifacts should preserve enough structure that a later reader can answer:

- what subsystem produced the artifact
- what target ticket or run family it belongs to
- what scope and write boundary applied
- what packet lineage or freshness assumption was in force
- what outcome the parent accepted, rejected, or deferred

## Iteration Note Expectations

If iteration notes are used, each note should say:

- what changed between this attempt and the last one
- what the child attempted
- what verification happened
- why the next move is continue, stop, blocked, or escalate

Iteration notes are useful when one run family has several bounded attempts and the parent wants durable insight into how the loop moved over time.

## Reconciliation Note Expectations

Use a reconciliation note when the parent needs durable explanation of how packet output was interpreted back into ticket truth.

That note should explain:

- which outputs were accepted
- which claims required parent-side correction
- which ticket sections or statuses changed as a result

## Runtime Failure Expectations

If a Ralph execution attempt fails, stalls, or exits without durable ticket activity, the durable artifact family should make that visible.

A useful failure note or failure-oriented iteration note should say:

- what packet launched the attempt
- what part of the attempt failed or stayed incomplete
- whether the failure was caused by scope, stale context, missing evidence, missing write authority, or tool/runtime issues
- what the parent should do next

## Failure Cases To Avoid

- packet artifacts with no clear target ticket
- iteration notes that do not explain why the next move is continue, stop, blocked, or escalate
- reconciliation notes that say a child made progress but never explain how ticket truth changed
- durable run artifacts that leave the parent unable to reconstruct what actually happened

## Done Means

- the Ralph artifact family explains one bounded run or run family clearly
- packet, outcome, and reconciliation can be understood without transcript memory
- the artifacts support ticket truth rather than competing with it
