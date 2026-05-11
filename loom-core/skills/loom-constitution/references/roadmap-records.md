# Roadmap Record Process

Use a roadmap record for durable strategic direction above ordinary plans,
tickets, and day-to-day progress.

A roadmap records strategic arc, current chapter, and work that should not be
pulled forward yet.

## Before You Write

Inspect `.loom/constitution/` before creating or changing a roadmap record.

Read the active core constitution when it exists:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null || true
```

Read active top-level principle fragments when their filename, ID, title, or
visible content is relevant to the roadmap:

```bash
find .loom/constitution -maxdepth 1 -name '*.md' -print 2>/dev/null
grep -R -l '^Status: active' .loom/constitution/*.md 2>/dev/null || true
grep -R -i -l '<keyword>' .loom/constitution/*.md 2>/dev/null || true
```

Search existing roadmap records by slug, ID, title, theme, milestone, strategic
arc, and sequencing pressure before creating a new record:

```bash
find .loom/constitution/roadmap -name '*<keyword>*' -print 2>/dev/null
grep -R -i -l '<keyword>' .loom/constitution/roadmap 2>/dev/null
grep -R -l '^Status: active' .loom/constitution/roadmap/*.md 2>/dev/null || true
```

Inspect relevant plans or work records when they can answer factual questions,
but do not let them own roadmap judgment.

Read superseded, retired, or completed records only when active records point to
them, when resolving strategic history, or when the roadmap change needs that
history.

Then summarize to the operator:

- the current strategic direction already recorded
- the new theme, chapter, or sequencing pressure
- what appears to be above ordinary planning
- what might be better handled as a plan, ticket, decision record, spec, or
  principle fragment
- whether an existing roadmap should be completed, retired, or superseded

Ask about the first material uncertainty before writing.

Good pressure questions:

- What strategic direction should future agents inherit?
- What chapter are we in now?
- What should explicitly not be pulled forward yet?
- Which milestones are strategic signals rather than task completions?
- What assumption would reorder or invalidate this roadmap?
- When should this roadmap be completed, superseded, or retired?

## How To Write

Create roadmap records under `.loom/constitution/roadmap/`:

```text
.loom/constitution/roadmap/<slug>.md
```

Use a slug that encodes the strategic theme clearly enough to support future
lookup by filename.

Use plain body labels:

```text
ID: roadmap:<slug>
Type: Constitution Roadmap
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

Write strategic judgment, not execution state.

Useful roadmap sections include:

- strategic frame
- current chapter
- milestones as strategic signals
- bets and assumptions
- tensions
- non-goals / not yet
- completion, retirement, or supersession conditions

Keep live sequencing, owners, blockers, task status, and progress in plans,
tickets, or other work records.

## How To Update

Minor clarifications can be edited in place.

Material strategic changes usually deserve a successor roadmap or explicit
supersession.

Use `completed` when the roadmap's strategic arc has been fulfilled and remains
useful as history.

Use `superseded` when a new roadmap changes the strategic arc.

Use `retired` when the roadmap no longer applies and should not guide future
work.

## Short Guardrails

- Do not make roadmap milestones into ticket checklists.
- Do not track day-to-day progress here.
- Do not use roadmap to avoid writing a concrete plan.
- Do not silently rewrite strategy after the project changes direction.
- Do not pull speculative future chapters into active direction.
- Do not store implementation details unless they define strategic constraints.
