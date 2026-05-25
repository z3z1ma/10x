# Core Constitution

Use the core constitution only for a broad living frame: project identity,
non-identity, principles, constraints, and current constitutional direction.

Create or amend it only when future agents should inherit project-level judgment
across many decisions or work streams.

## Before Editing

Inspect the surface, then read:

- active `constitution:main`, when present
- relevant active top-level principle fragments
- relevant active decisions and roadmaps by slug, ID, title, topic, subsystem, or grep hit
- historical records only for cited precedent, conflict, or needed history

Summarize to the operator:

- existing broad project judgment
- what frame appears to change
- affected principles, decisions, or roadmaps
- why this belongs in core constitution instead of a smaller constitutional shape
- any conflict with active records

Ask the first material uncertainty before editing.

## Shape

Use `templates/constitution.md`.

Required labels:

```text
ID: constitution:main
Type: Constitution Core
Status: active
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>
```

Amend the smallest section that changes the project frame. Preserve durable
judgment, not conversation transcript.

Use natural inline refs. Add `## Related` only when links materially help future
agents navigate.

## Guardrails

- Do not turn the core constitution into a task list.
- Do not store live execution state, owners, blockers, or progress here.
- Do not hide a concrete ADR, roadmap, spec, plan, ticket, or knowledge note inside broad prose.
- Do not rewrite project identity to make the current task easier.
- Do not silently override active decisions, roadmaps, or principles.
