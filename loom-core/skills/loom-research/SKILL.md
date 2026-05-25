---
name: loom-research
description: "Use when investigation, source synthesis, option comparison, rejected paths, null results, tradeoffs, or evidence-backed conclusions should remain available to future Loom work."
---

# loom-research

Research owns durable investigation: questions, scope, sources, findings,
tradeoffs, rejected paths, null results, conclusions, limits, and recommended
downstream owners.

Research does not own intended behavior, durable policy, live execution,
observation truth, audit verdicts, ticket closure, or accepted reusable
explanation.

## Use This Skill When

Use it when:

- an investigation should remain available beyond this session
- options, frameworks, migrations, integrations, or implementation strategies need comparison
- external facts, source synthesis, current project reality, or source quality matter
- a spike, sketch, prototype, or experiment produced reusable conclusions
- a rejected path or null result would otherwise be rediscovered
- a ticket, plan, spec, constitution record, audit, or knowledge record needs investigation-backed support
- implementation discovery is too durable for a ticket journal but not yet accepted explanation

Small local investigation can stay in chat or a ticket journal when future work
would not be worse without a research record.

## Inspect

Research lives under `.loom/research/`.

```bash
find .loom/research -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: research:' .loom/research 2>/dev/null || true
grep -R '^Type: Research' .loom/research 2>/dev/null || true
grep -R '^Status:' .loom/research 2>/dev/null || true
grep -R '^Updated:' .loom/research 2>/dev/null || true
```

Raw support material may live under `.loom/research/artifacts/YYYYMMDD-<slug>/`,
but the Markdown record must stand on its own.

## Record Shape

Use date-prefixed IDs and matching filenames:

```text
ID: research:YYYYMMDD-<slug>
.loom/research/YYYYMMDD-<slug>.md
```

Required labels:

```text
ID: research:YYYYMMDD-<slug>
Type: Research
Status: active
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

Statuses:

- `active`: durable investigation is still being worked or evaluated.
- `completed`: conclusions and recommendations are bounded enough to cite.
- `superseded`: newer research or another surface replaces the conclusion.
- `cancelled`: investigation should not continue, with reason recorded.

Do not create draft research as a parking lot. If question, scope, and likely
consumer are unclear, keep shaping or route to the owner surface.

## Write Or Update

For creation or material update, read:

- `references/research-shape.md`
- `references/source-handling.md` when sources, current facts, or source quality matter

Use `templates/research.md`.

Create an `active` record only when the question is durable, scope is bounded,
the grounding path is plausible, and a likely downstream consumer is known.

Preserve findings separately from conclusions. Record tradeoffs when comparing
options. Capture rejected paths and null results when they prevent useful
rediscovery. Route recommendations to the surface that owns the next truth change.

When completing, superseding, or cancelling, preserve useful findings,
rejections, null results, limits, and downstream route; update `Status:` and
`Updated:`.

Create or cite evidence only when an observation must survive as inspectable
support. Promote settled reusable explanation to knowledge when future agents
should read the explanation first, not the investigation history.

## Stop Conditions

Stop and route before writing when:

- the question is vague or too broad to bound
- the likely source path or method is unknown
- no downstream consumer exists
- the record would decide intended behavior, policy, ticket closure, or audit verdict
- source quality is too weak for the conclusion being claimed
- sensitive data would need to be recorded instead of redacted or summarized

## Done Means

The record says what was investigated and why, how it was grounded, what findings
and tradeoffs were found, what paths were rejected, what conclusions are justified
with limits, and which downstream surface should consume the result.
