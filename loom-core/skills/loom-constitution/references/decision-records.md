# Decision Records

Use a decision record for an architectural or policy choice future agents should
cite as precedent.

Decision records are Loom's ADRs. They preserve context, the chosen path,
rejected alternatives, consequences, accepted risks, and revisit conditions.

## Before Writing

Inspect `.loom/constitution/`, then read:

- active `constitution:main`, when present
- relevant active principle fragments
- existing decisions by slug, ID, title, concept, module, subsystem, policy, or tradeoff
- historical decisions only for cited precedent or needed history

Summarize:

- active precedent
- the choice being made
- real alternatives
- accepted consequences or tradeoffs
- why this is an ADR instead of a note, spec, plan, ticket, roadmap, principle, or core amendment
- whether an existing decision should be superseded

Ask the first material uncertainty before writing.

## Shape

Create records under `.loom/constitution/decisions/` with numbered filenames:

```text
.loom/constitution/decisions/decision-0001-<slug>.md
```

Use the next available number and `templates/decision.md`.

Required labels:

```text
ID: decision:0001
Type: Constitution Decision
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

The record must make context, decision, rejected alternatives, consequences,
accepted risks, and supersession conditions clear enough to inherit without chat
history.

## Update Rules

- Fix typos, broken links, and clarification errors in place.
- If the actual choice changes, create a new decision and mark the old one `superseded` with the successor.
- Do not rewrite old decisions to pretend the project always believed the new thing.

## Guardrails

- Do not write ADRs for every preference.
- Do not omit rejected alternatives.
- Do not use decisions for intended behavior that belongs in specs.
- Do not let README docs, code comments, specs, plans, or tickets act as ADRs.
- Do not bury unresolved disagreement in confident prose.
