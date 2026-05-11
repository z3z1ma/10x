# Core Constitution Process

Use the core constitution only when the project needs a broad living frame for
identity, principles, constraints, and current constitutional direction.

The core constitution is optional. Create or amend it only when the operator is
making durable project-level judgment that future agents should inherit across many
decisions and work streams.

## Before You Change It

Inspect `.loom/constitution/` before mutating the core constitution.

Read the active core constitution when it exists:

```bash
grep -R -l '^ID: constitution:main' .loom/constitution/*.md 2>/dev/null
```

Read active top-level principle fragments when their filename, ID, title, or
visible content is relevant to the proposed change:

```bash
find .loom/constitution -maxdepth 1 -name '*.md' -print
grep -R -l '^Status: active' .loom/constitution/*.md 2>/dev/null
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
resolving precedent, or when the proposed change needs that history.

Then summarize to the operator:

- what broad project judgment already exists
- what durable frame appears to be changing
- which active decision, roadmap, or principle fragment may be affected
- whether the change belongs in the core constitution
- whether a smaller constitutional shape would preserve the judgment better
- whether any active record conflicts with the proposed amendment

Ask about the first material uncertainty before editing.

Good pressure questions:

- What should future agents do differently after this change?
- Is this project-wide judgment or a local decision?
- What future work is now encouraged, constrained, or ruled out?
- What existing constitutional record would this contradict, narrow, or supersede?
- What wording would prevent an agent from overextending this principle?
- Is this actually an ADR, roadmap, principle fragment, spec, plan, or ticket?

## How To Update

The core constitution is living. Amend the smallest section that changes the
project frame.

Do not preserve a conversation transcript. Preserve the durable judgment that
survived the conversation.

Use plain body labels at the top:

```text
ID: constitution:main
Type: Constitution Core
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

Inline references are enough when natural. Add `## Related` only when explicit
links materially help future agents.

If the amendment contradicts an active decision, roadmap, or principle fragment,
surface the conflict before editing. Do not silently blend conflicting
constitutional records in prose.

If the change is a concrete choice with meaningful alternatives and consequences,
write or update a decision record instead.

If the change is strategic sequencing above execution plans, write or update a
roadmap record instead.

If the change is a small durable principle that is not yet broad project frame,
write or update a principle fragment instead.

## Short Guardrails

- Do not turn the core constitution into a task list.
- Do not put one-off implementation details here.
- Do not hide an ADR inside broad principle prose.
- Do not store live execution state here.
- Do not rewrite project identity to make the current task easier.
- Do not silently override active decisions, roadmaps, or principle fragments.
- Do not expand the core constitution when a smaller constitutional record is enough.
