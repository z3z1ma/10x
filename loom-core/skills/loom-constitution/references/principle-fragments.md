# Principle Fragments

Use a principle fragment for a small durable principle or constraint that should
shape future work but is not broad enough for core constitution and is not a
concrete ADR-style choice.

Fragments live as top-level Markdown files under `.loom/constitution/`.

## Before Writing

Inspect `.loom/constitution/`, then read:

- active `constitution:main`, when present
- relevant active principle fragments
- relevant active decisions and roadmaps by slug, ID, title, topic, subsystem, or grep hit
- historical records only for cited precedent, conflict, or needed history

Summarize:

- emerging principle or constraint
- why it matters for future work
- where it applies and does not apply
- why it is not core constitution or a decision record
- overlap or conflict with active constitutional records

Ask the first material uncertainty before writing.

## Shape

Create top-level records:

```text
.loom/constitution/<slug>.md
```

Use `templates/principle-fragment.md`.

Required labels:

```text
ID: principle:<slug>
Type: Constitution Principle Fragment
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

A useful fragment states the principle, why it matters, where it applies, where it
does not, and what would cause promotion, retirement, or supersession.

## Update Rules

- Edit while the fragment remains small.
- Fold broad project frame into core constitution and mark the fragment `superseded` or `retired`.
- Promote concrete choices with alternatives and consequences to decision records.
- Retire or supersede fragments that stop applying.

## Guardrails

- Do not use fragments as scratch pads or TODO lists.
- Do not dodge ADR rigor with a vague principle.
- Do not create slogans that do not change future behavior.
- Do not let many tiny fragments replace a readable core constitution.
- Do not keep expanding a fragment after it has become another record shape.
