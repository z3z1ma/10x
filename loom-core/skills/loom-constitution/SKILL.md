---
name: loom-constitution
description: "Use before work that may depend on or change durable project judgment, including identity, policy, principles, constraints, ADRs, roadmap direction, architectural precedent, or code changes where that judgment matters."
---

# loom-constitution

Constitution is Loom's durable judgment layer.

It holds project judgments future agents should inherit before they make or
evaluate important changes.

## How To Read Constitution

Constitutional records live under `.loom/constitution/`.

When this skill is loaded, inspect the constitutional surface directly:

```bash
find .loom/constitution -name '*.md' -print
grep -R '^ID:' .loom/constitution
grep -R '^Type:' .loom/constitution
grep -R '^Status:' .loom/constitution
```

If `.loom/constitution/` is absent or contains no Markdown files, no Loom
constitutional guidance is currently present.

Start with active top-level constitutional records:

```bash
find .loom/constitution -maxdepth 1 -name '*.md' -print
grep -R -l '^Status: active' .loom/constitution/*.md 2>/dev/null
```

Read the active core constitution first when it exists:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null
```

Then read active top-level principle fragments when their filenames, IDs, titles,
or visible content appear relevant to the current work.

Use filenames and slugs as semantic routing hints. Prefer focused lookup before
reading nested constitutional records:

```bash
find .loom/constitution -name '*<keyword>*' -print
grep -R -i -l '<keyword>' .loom/constitution
grep -R -l '^Status: active' .loom/constitution/decisions/*.md 2>/dev/null
grep -R -l '^Status: active' .loom/constitution/roadmap/*.md 2>/dev/null
```

Read active decision records, roadmap records, and other nested records when they
are relevant to the current work by slug, ID, title, topic, referenced subsystem,
or grep result.

Treat `superseded`, `retired`, and `completed` records as historical context.
Read them only when active records point to them, when resolving precedent, or
when the current work needs that history.

Create or edit constitutional records only when the operator asks for a
constitutional change or the work clearly requires one.

## Record Shapes

Constitution has four shapes:

* Core constitution: optional broad project frame at `.loom/constitution/constitution.md`.
* Decisions / ADRs: citable architectural or policy precedent under `.loom/constitution/decisions/`.
* Roadmap records: durable strategic direction under `.loom/constitution/roadmap/`.
* Principle fragments: small durable principle or constraint fragments as top-level files under `.loom/constitution/`.

Each record uses plain body labels near the top:

```text
ID: decision:0001
Type: Constitution Decision
Status: active
Created: 2026-05-08
Updated: 2026-05-08
```

Use these IDs by convention:

* `constitution:main` for the optional core constitution
* `decision:0001`, `decision:0002`, ... for ADRs
* `roadmap:<slug>` for roadmaps
* `principle:<slug>` for lightweight principle fragments

Use these statuses unless a record explains otherwise: `draft`, `active`,
`completed`, `superseded`, and `retired`.

Relationships can appear naturally in prose. Add a `## Related` section only when
explicit links materially help future agents.

## What Belongs Here

Use constitution for durable project judgment:

* identity: what this project is and is not
* principles: how future work should be judged
* constraints: what future work must respect or refuse
* decisions / ADRs: choices future agents should not re-litigate from scratch
* roadmap direction: strategic sequencing above ordinary plans and tickets
* principle fragments: small durable fragments that are not yet core-constitution or ADR shaped

If the truth is live execution, it does not belong here. If the truth is intended
behavior, it belongs in the behavior/spec layer when that exists. If the truth is
accepted explanation, it belongs in knowledge. Constitution is for
judgment that should shape future work.

## When Records Change

Before creating, updating, retiring, or superseding constitutional records:

1. Inspect the constitutional surface.
2. Read the active core constitution when it exists.
3. Read active top-level principle fragments relevant to the change.
4. Find and read active nested records relevant to the change by slug, ID, title,
   topic, referenced subsystem, or grep result.
5. Read superseded, retired, or completed records only when needed to understand
   precedent or resolve a reference.
6. Identify the constitutional shape being changed.
7. Read the relevant shape reference.
8. Summarize the existing durable judgment and the proposed change.
9. Ask about the first material uncertainty before mutating files.

Use these references:

* `references/core-constitution.md` for `.loom/constitution/constitution.md`
* `references/decision-records.md` for ADRs and citable decisions
* `references/roadmap-records.md` for roadmap direction
* `references/principle-fragments.md` for lightweight top-level principle fragments

If the shape is unclear, route before writing. Do not guess and create a record.

## Update Posture

The core constitution is a living document when it exists. Amend it directly when
the broad project frame changes.

Decision records are historical precedent. If the decision changes materially,
create a new decision and mark the old one `superseded`.

Roadmaps are strategic records, not progress logs. Minor clarifications are fine;
material strategic changes usually deserve a successor roadmap or an explicit
supersession.

Principle fragments can be edited while they remain small. If a fragment becomes
broad project frame, fold it into the core constitution. If it becomes a concrete
choice, promote it to a decision record.

## Done Means

Constitutional work is done when future agents can answer:

* What judgment exists here?
* What future work does it encourage, constrain, or rule out?
* What alternative or failure mode should not be rediscovered?
* What would make this judgment stale, superseded, completed, or retired?
* Which downstream records or code areas may need to be revisited?
