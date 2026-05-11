# Principle Fragment Process

Use a principle fragment for a small durable principle or constraint that should
shape future work but is not broad enough for the core constitution and is not a
concrete ADR-style choice.

Principle fragments live as top-level Markdown files under `.loom/constitution/`.
Use them for durable judgments smaller than the core project frame.

## Before You Write

Inspect `.loom/constitution/` before creating or changing a principle fragment.

Read the active core constitution when it exists:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null
```

Read active top-level principle fragments when their filename, ID, title, or
visible content is relevant to the proposed principle:

```bash
find .loom/constitution -maxdepth 1 -name '*.md' -print
grep -R -l '^Status: active' .loom/constitution/*.md 2>/dev/null
grep -R -i -l '<keyword>' .loom/constitution/*.md 2>/dev/null
```

Find relevant active decisions and roadmaps by slug, ID, title, topic,
referenced subsystem, or grep result:

```bash
find .loom/constitution -name '*<keyword>*' -print
grep -R -i -l '<keyword>' .loom/constitution
grep -R -l '^Status: active' .loom/constitution/decisions/*.md 2>/dev/null
grep -R -l '^Status: active' .loom/constitution/roadmap/*.md 2>/dev/null
```

Read superseded or retired records only when active records point to them, when
resolving precedent, or when the proposed principle needs that history.

Then summarize to the operator:

- the active principle or constraint that appears to be emerging
- why it matters for future work
- why it is not a core constitution amendment
- why it is not a decision record
- where it should apply
- where it should not apply
- whether it overlaps or conflicts with an active constitutional record

Ask about the first material uncertainty before writing.

Good pressure questions:

- What future mistake does this principle prevent?
- Is this actually a decision with rejected alternatives?
- Is this project-wide enough to belong in the core constitution?
- Where would applying this principle be wrong?
- What would cause us to promote, retire, or supersede it?
- What wording keeps the fragment small and hard to misuse?

## How To Write

Create top-level records under `.loom/constitution/`:

```text
.loom/constitution/<slug>.md
```

Use a slug that encodes the principle topic clearly enough to support future
lookup by filename.

Use plain body labels:

```text
ID: principle:<slug>
Type: Constitution Principle Fragment
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

Keep the fragment small. A useful principle fragment usually states:

- the principle
- why it matters
- where it applies
- where it does not apply
- what would cause promotion, retirement, or supersession when known

If the fragment needs many sections, it probably wants to become the core
constitution, a decision record, roadmap, spec, or knowledge record.

## How To Update

Principle fragments can be edited while they remain small.

If a fragment becomes broad project frame, fold it into the core constitution and
mark the fragment `superseded` or `retired`.

If a fragment becomes a concrete choice with alternatives and consequences,
promote it to a decision record.

If a fragment stops applying, mark it `retired` or `superseded` and say why.

## Short Guardrails

- Do not use principle fragments as scratch pads.
- Do not store live work or TODOs here.
- Do not use a fragment to dodge ADR rigor.
- Do not create fragments for slogans that do not change future behavior.
- Do not let many tiny fragments replace a readable core constitution.
- Do not keep expanding a fragment after it has become another record shape.
