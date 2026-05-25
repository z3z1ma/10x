# Roadmap Records

Use a roadmap record for durable strategic direction above ordinary plans,
tickets, and day-to-day progress.

A roadmap records strategic arc, current chapter, deferred work, assumptions,
tensions, and completion or supersession conditions.

## Before Writing

Inspect `.loom/constitution/`, then read:

- active `constitution:main`, when present
- relevant active principle fragments
- existing roadmap records by slug, ID, title, theme, milestone, strategic arc, or sequencing pressure
- relevant plans or tickets for facts only, not roadmap authority
- historical roadmap records only for cited strategy, completion history, or needed context

Summarize:

- current strategic direction
- the new theme, chapter, or sequencing pressure
- what is above ordinary planning
- what might belong in a plan, ticket, decision, spec, or principle instead
- whether an existing roadmap should be completed, retired, or superseded

Ask the first material uncertainty before writing.

## Shape

Create roadmap records under `.loom/constitution/roadmap/`:

```text
.loom/constitution/roadmap/<slug>.md
```

Use `templates/roadmap.md`.

Required labels:

```text
ID: roadmap:<slug>
Type: Constitution Roadmap
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

Write strategic judgment, not execution state. Useful content: strategic frame,
current chapter, milestones as signals, bets, assumptions, tensions, non-goals,
and completion/retirement/supersession conditions.

## Update Rules

- Minor clarifications can be edited in place.
- Material strategic changes usually need a successor roadmap or explicit supersession.
- Use `completed` when the strategic arc was fulfilled and remains useful as history.
- Use `superseded` when a new roadmap changes the strategic arc.
- Use `retired` when the roadmap no longer applies.

## Guardrails

- Do not make roadmap milestones into ticket checklists.
- Do not track owners, blockers, task status, or day-to-day progress here.
- Do not use roadmap to avoid writing a concrete plan.
- Do not silently rewrite strategy after direction changes.
- Do not pull speculative future chapters into active direction.
