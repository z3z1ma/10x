---
name: loom-constitution
description: "Use before work that may depend on or change durable project judgment, including identity, policy, principles, constraints, ADRs, roadmap direction, architectural precedent, or code changes where that judgment matters."
---

# loom-constitution

Constitution owns durable project judgment: identity, policy, principles,
constraints, architectural precedent, roadmap direction, and choices future agents
should not re-litigate.

It does not own intended behavior, live execution, evidence, audit verdicts,
research synthesis, or reusable explanation.

## Use This Skill When

Use it when work may depend on or change:

- project identity or non-identity
- durable policy, principle, or constraint
- ADR-style architectural or process precedent
- roadmap-level strategic direction
- a constitutional record's status, successor, or retirement

Do not create constitutional records for local preferences, task progress,
implementation notes, behavior contracts, ticket acceptance, or knowledge notes.

## Inspect

Constitution lives under `.loom/constitution/`.

Start here:

```bash
find .loom/constitution -name '*.md' -print 2>/dev/null
grep -R '^ID:' .loom/constitution 2>/dev/null || true
grep -R '^Type:' .loom/constitution 2>/dev/null || true
grep -R '^Status:' .loom/constitution 2>/dev/null || true
```

Read the active core constitution first when present:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null || true
```

Then read active top-level principle fragments and nested decisions or roadmaps
that match the current topic by slug, ID, title, subsystem, policy, or grep hit.
Historical records (`superseded`, `retired`, and completed roadmaps) are context
only; read them when an active record points there or precedent/history matters.

## Record Shapes

Constitution has four shapes:

- Core constitution: `.loom/constitution/constitution.md`, ID `constitution:main`.
- Decisions / ADRs: `.loom/constitution/decisions/decision-0001-<slug>.md`, IDs `decision:0001`, `decision:0002`, ...
- Roadmaps: `.loom/constitution/roadmap/<slug>.md`, IDs `roadmap:<slug>`.
- Principle fragments: `.loom/constitution/<slug>.md`, IDs `principle:<slug>`.

Every record uses plain labels near the top:

```text
ID: decision:0001
Type: Constitution Decision
Status: active
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

Statuses:

- Core constitution, decisions, principles: `draft`, `active`, `superseded`, `retired`.
- Roadmaps: `draft`, `active`, `completed`, `superseded`, `retired`.

Use `draft` only for unresolved judgment. Activate a constitutional record before
downstream work relies on it.

## Write Or Update

Before mutating constitution:

1. Inspect `.loom/constitution/` and read the active core constitution when present.
2. Read relevant active principle fragments, decisions, and roadmap records.
3. Identify the exact shape being changed.
4. Read the matching detail card.
5. Summarize the existing judgment, proposed change, affected records, and conflict risk.
6. Ask or escalate on the first material uncertainty before editing.

Detail cards:

- `references/core-constitution.md` for the broad project frame.
- `references/decision-records.md` for ADRs and citable decisions.
- `references/roadmap-records.md` for strategic direction.
- `references/principle-fragments.md` for small durable principles.

Update posture:

- Amend the core constitution directly when broad project frame changes.
- Clarify decisions in place only for typos or non-semantic fixes; supersede them with a new decision when the actual choice changes.
- Edit roadmap clarifications in place; use `completed`, `superseded`, or `retired` when the strategic arc changes or ends.
- Keep principle fragments small; fold broad ones into core constitution or promote concrete choices to decisions.

## Stop Conditions

Stop and route before writing when:

- the change is intended behavior, not judgment
- the change is live execution or ticket state
- the shape is unclear
- active constitutional records conflict
- the operator has not resolved a material policy, principle, roadmap, or precedent choice
- the proposed record would become a parking lot, task list, or transcript

## Done Means

Future agents can tell what judgment exists, what it encourages or forbids, what
alternative or failure mode should not be rediscovered, what would make it stale,
and which downstream records or code areas may need revisiting.
