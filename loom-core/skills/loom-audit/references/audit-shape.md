# Audit Shape

Audit records a bounded Ralph adversarial review of a target, its claims, evidence,
scope, and risks.

## Create Audit Only When

Create an audit record only when:

- there is a concrete target
- the claim, risk, acceptance question, or review concern is clear enough to
  challenge
- a Ralph review run inspected the target or returned bounded review output
- the result should remain available
- a consuming ticket, plan, spec, research record, evidence record, constitution
  record, knowledge record, handoff, or future agent can use it

## Targets

Audit can target tickets, acceptance claims, closure stories, specs, plans,
research conclusions, evidence strength, constitution changes, code diffs,
branches, commits, pull requests, packages, handoffs, or external summaries.

Use `Target:` near the top for one short grepable handle. Use `## Target` for
branch, commit, diff range, PR, changed file set, record ID, claim ID, or why the
target needed audit.

## Bounded Audit Request

A good request gives the Ralph reviewer enough to review without inheriting the
implementer's assumptions. The ticket or audit target carries durable context; the
audit record preserves the returned result.

Include target handle, review question, claims or risks to challenge, records,
files, diffs, evidence or artifacts to inspect, lenses, boundaries, non-goals,
expected output with `FIND-*` findings and verdict, and excluded areas.

Keep the request narrow. Broad targets need multiple audit passes.

## Core Sections

Default sections:

- `## Summary`
- `## Target`
- `## Audit Scope And Lenses`
- `## Context And Evidence Reviewed`
- `## Findings`
- `## Verdict`
- `## Required Follow-up`
- `## Residual Risk`
- `## Related Records`

Audit does not use a journal. Create a new audit or note supersession when another
Ralph review pass is needed.

## Context And Boundaries

Name what the Ralph worker actually inspected: records, claim IDs, source files,
diffs, commits, PRs, screenshots, logs, tests, command output, worker reports, and
important omissions. Worker reports and summaries are claims, not proof.

For ticket work, audit is usually the review pass between implementation evidence
and closure. Challenge the ticket, acceptance, evidence, and diff; do not reopen
the whole project unless that is the target.

Audit reviews evidence strength but does not make weak evidence strong. If audit
discovers an observation that should persist, create or cite evidence. Route
unresolved intended behavior to specs, executable work to tickets, strategy to
plans, investigation to research, durable judgment to constitution, observations to
evidence, and reusable explanation to knowledge.
