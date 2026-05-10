# Decision Record Process

Use a decision record for an architectural or policy choice that future agents
should cite as precedent.

Decision records are Loom's ADR shape. They preserve architectural and policy
choices with rejected alternatives, consequences, accepted risks, and revisit
conditions.

## Before You Write

Inspect `.loom/constitution/` before creating or changing a decision record.

Read the active core constitution when it exists:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null
```

Read active top-level principle fragments when their filename, ID, title, or
visible content is relevant to the choice:

```bash
find .loom/constitution -maxdepth 1 -name '*.md' -print
grep -R -l '^Status: active' .loom/constitution/*.md 2>/dev/null
```

Search existing decisions by slug, ID, title, concept, module, subsystem, policy,
and tradeoff before creating a new record:

```bash
find .loom/constitution/decisions -name '*<keyword>*' -print 2>/dev/null
grep -R -i -l '<keyword>' .loom/constitution/decisions 2>/dev/null
grep -R -l '^Status: active' .loom/constitution/decisions/*.md 2>/dev/null
```

Read superseded, retired, or completed decisions only when active records point to
them, when resolving precedent, or when the new choice needs that history.

Then summarize to the operator:

- the active precedent that already exists
- the choice that appears to be needed
- the real alternatives
- the consequence or tradeoff being accepted
- why this deserves a decision record rather than a note, spec, plan, ticket,
  knowledge record, roadmap, principle fragment, or core amendment
- whether an existing decision should be superseded instead of edited

Ask about the first material uncertainty before writing.

Good pressure questions:

- What choice are we actually making?
- What alternatives were genuinely tempting?
- Why is the chosen path better enough to become precedent?
- What consequence are we accepting?
- What future agent mistake should this prevent?
- What new evidence would make us supersede this decision?
- Is this intended behavior rather than constitutional precedent?

## How To Write

Create records under `.loom/constitution/decisions/` with numbered filenames:

```text
.loom/constitution/decisions/decision-0001-<slug>.md
```

Use the next available number. Use a slug that encodes the decision topic clearly
enough to support future lookup by filename.

Use plain body labels:

```text
ID: decision:0001
Type: Constitution Decision
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

The record must make these clear enough for a future agent to inherit the
decision without chat history:

- context
- decision
- rejected alternatives
- consequences
- accepted risks
- revisit or supersession conditions

Add `## Related` only when explicit links materially help future agents.

## How To Update

Decision records are historical precedent.

Fix typos, broken references, and clarification errors in place.

If the actual choice changes, create a new decision record and mark the old record
`superseded` with a pointer to the successor.

Do not rewrite an old decision to pretend the project always believed the new
thing.

## Short Guardrails

- Do not write an ADR for every preference.
- Do not omit rejected alternatives.
- Do not use decisions for intended behavior that belongs in specs.
- Do not let README docs, code comments, specs, plans, or tickets act as ADRs.
- Do not bury unresolved disagreement in confident prose.
- Do not edit historical decisions when supersession is the honest shape.
