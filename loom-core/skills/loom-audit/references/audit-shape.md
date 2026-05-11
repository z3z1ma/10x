# Audit Shape

Audit is fresh-context adversarial review of the target, evidence, scope, and
risks.

## The Fresh-Context Standard

A meaningful audit needs a reviewer who did not share the shaping or
implementation context.

The parent context may prepare a bounded review request and record the result. For
substantive audit, that request should be a Ralph packet under
`.loom/packets/ralph/`. The adversarial judgment itself must come from the
fresh-context pass.

Do not create `Type: Audit` for same-context self-review. When no fresh context is
available, say audit was not performed and use another surface for local notes.

## Create Audit Only When

Create an audit record when all of these are true:

- there is a concrete target to review
- the claim, risk, acceptance question, or review concern is clear enough to
  challenge
- a fresh-context pass inspected the target or returned bounded review output
- the result should remain available beyond the current session
- a consuming ticket, plan, spec, research record, evidence record, constitution
  record, knowledge record, handoff, or future agent can use the result

## Targets

Audit can target:

- tickets, acceptance claims, and closure stories
- specs and intended-behavior claims
- plans and decomposition or sequencing claims
- research conclusions and source-synthesis claims
- evidence strength and overclaiming risk
- constitution changes and durable-judgment claims
- code diffs, branches, commits, pull requests, packages, or handoffs
- external summaries or mirrored project state

Use `Target:` near the top for one short grepable handle.

Use `## Target` for details, such as branch, commit, diff range, PR, changed file
set, record ID, claim ID, or why the target needed audit.

## Bounded Audit Request

A good audit request gives the fresh context enough to review without inheriting
the implementer's assumptions.

Use a Ralph review packet for this request when audit is part of Loom work. The
packet carries the review target, context, lenses, read scope, write scope, stop
conditions, and output contract; the later audit record preserves the auditor's
result.

Include:

- target handle and concrete review question
- claims, acceptance criteria, or risks to challenge
- records, files, diffs, evidence, or artifacts to inspect
- lenses that matter for this pass
- scope boundaries and known non-goals
- expected output shape, including `FIND-*` findings and verdict
- any areas intentionally excluded from this pass

Keep the request bounded. A broad target may need multiple audit passes.

## Core Sections

Use the default sections unless an audit has a strong reason to vary:

- `## Summary`
- `## Target`
- `## Audit Scope And Lenses`
- `## Context And Evidence Reviewed`
- `## Findings`
- `## Verdict`
- `## Required Follow-up`
- `## Residual Risk`
- `## Related Records`

Audit does not use a journal. It records a review pass.

When another fresh-context pass is needed, create another audit record or clearly
note supersession in prose.

## Context And Evidence

An audit should name what the fresh context actually inspected.

Depending on target, this may include:

- tickets, specs, plans, research, evidence, constitution records, or knowledge
- claim IDs such as ticket acceptance criteria
- source files, diffs, commits, PRs, screenshots, logs, tests, or command output
- worker reports or implementation summaries, treated as claims rather than proof
- relevant omissions, unavailable evidence, stale state, or uninspected areas

Use source inspection when source reality is needed for judgment. Passing tests
support only the exact claim being reviewed. Summaries and worker reports are
context, not proof.

## Audit And Tickets

Audit may say a finding appears unresolved, a claim is unsupported, or changes are
needed before acceptance.

The ticket still owns live execution state, risk acceptance, finding disposition,
and closure. A ticket can cite `audit:YYYYMMDD-<slug>#FIND-001`, but the ticket
must record whether the finding was fixed, accepted as risk, superseded, converted
to follow-up work, or rejected with evidence.

For ticket work, audit is usually the fresh-context pass between implementation
evidence and closure. Keep that pass narrow when the ticket is narrow: challenge
the ticket, acceptance, evidence, and diff rather than reopening the whole project.

## Audit And Evidence

Audit reviews whether evidence supports the claim being made. Audit does not turn
weak evidence into strong evidence.

When audit discovers an observation that should persist independently, create or
cite evidence.

When audit identifies an evidence gap, route the gap to the consuming ticket,
plan, or evidence work.

## Audit And Other Surfaces

Route unresolved truth to its owner:

- intended behavior to specs
- executable work to tickets
- complex multi-ticket strategy to plans
- investigation and tradeoffs to research
- durable project judgment to constitution
- observations to evidence
- accepted reusable explanation to knowledge

Audit can challenge any of those surfaces. It does not replace them.
