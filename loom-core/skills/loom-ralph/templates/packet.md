# <Ralph Packet Title>

ID: packet:<YYYYMMDDTHHMMSSZ-target-or-task-slug>
Type: Packet
Status: compiled
Created: <YYYY-MM-DD HH:MM UTC>
Updated: <YYYY-MM-DD HH:MM UTC>
Target: <record ID, claim, path, diff, branch, package, or task slug>
Packet Kind: Ralph
Mode: <execution|review|research|synthesis|other>
Context Style: <live-reference|hermetic|hybrid>
Worker: <subagent|harness command|manual handoff>
Branch: <branch name, none, or unknown - reason>
Worktree: <path, none, or unknown - reason>

<!--
Add only when useful. Remove this comment before saving if unused.

Iteration: <positive integer or run label>
Risk: <low|medium|high> - <reason>
Verification Posture: <test-first|observation-first|none>
Review Lens: <audit, code review, evidence sufficiency, or another lens>
Change Class: <short label or prose>
-->

## Mission

<Describe what this one bounded worker run should accomplish and why this target
is ready for packetized work.>

## Context Bundle

<Name or inline the records, evidence, files, diffs, claims, external references,
or source excerpts the worker should rely on. Match this section to `Context
Style:`.>

Records:

- `<record-id>` - <why this record matters>

Evidence Or Artifacts:

- `<evidence-id or artifact path>` - <why this observation matters>

Files, Diffs, Or External References:

- `<path, diff, branch, URL, or reference>` - <why this source matters>

Inline Context:

<For hermetic or hybrid packets, paste the bounded excerpts, summaries, claims, or
diffs needed for the run. Remove this subsection when live references are enough.>

## Read Scope

<Name what the worker should inspect before or during the run.>

- <record, path, glob, command, artifact, claim, or source area>

## Write Scope

<Name exactly what the worker may change. Include records, artifacts, and paths.
Use `None - <reason>` where a category is intentionally read-only.>

Records Or Artifacts:

- `<record ID, .loom path, artifact path, or None - reason>` - <expected update>
- this packet - fill `## Worker Output` and update `Status:` when appropriate

Source Paths:

- `<path, glob, or None - reason>` - <allowed source/work-file change>

## Source Snapshot

<Record the target state, branch/worktree state, relevant records or files
inspected, and any known concurrent or dirty state that could affect freshness.
Keep this bounded.>

## Task

<Give the worker the exact task. Include non-goals and nearby work that should not
be pulled into this run.>

## Launch

<Optional. Name the intended launch transport and the thin wrapper instruction,
for example: read this packet first, stay inside it, and return the output
contract. Remove when the transport is obvious from top labels.>

## Evidence, Review, Or Verification Expectations

<State the concrete output expected for this mode. For implementation work, name
red/green or before/after evidence when relevant. For review work, name lenses and
finding expectations. For synthesis or research, name the expected artifact or
answer shape.>

## Stop Conditions

<Tell the worker when to return `blocked` or `escalate` instead of widening scope.>

- <stop condition>

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

If this run supports closure, acceptance, evidence, audit, research, knowledge, or
future recovery, preserve this output in the packet or in a cited durable record;
do not leave it only in transient launch output.

## Worker Output

<Worker fills this section or returns equivalent output through the launch
transport.>

## Follow-up

<Use after the worker returns when additional surface updates, audit, another
packet, or operator shaping is needed. Remove if unused.>
