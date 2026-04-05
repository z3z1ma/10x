# Layer Boundaries

Loom keeps durable work understandable by giving each kind of artifact a clear job.

## Kinds Of Artifact

1. core rules
2. skills
3. canonical records
4. packets and runs

## Ownership

- Core rules define meaning, authority, trust boundaries, and invariants.
- Skills define task-specific operating instructions.
- Canonical records define durable project state.
- Packets and runs define bounded child execution handoff and results.

Use these ownership rules continuously. If one kind of artifact starts behaving like another, reconcile the drift instead of tolerating it.

If you need the required sections and intent for each record kind, read `appendices/layer-schemas.md`.

If you need the shared frontmatter and status conventions that span multiple kinds, read `appendices/common-schema-conventions.md`.

## Canonicality Rule

Being stored under `.loom/` does not automatically make an artifact canonical. The following are canonical:

- `.loom/constitution/`
- `.loom/research/`
- `.loom/initiatives/`
- `.loom/specs/`
- `.loom/plans/`
- `.loom/tickets/`
- `.loom/critique/`
- `.loom/docs/`

The following are durable but non-canonical:

- `.loom/runs/`
- `.loom/verification/`
- `.loom/memories/`

## Layer Discipline

- Canonical records MUST link to evidence and artifacts explicitly.
- Packets MAY summarize or embed canonical records but do not outrank them.
- Derived dashboards and reports are disposable unless promoted into canonical records.

When in doubt, ask which kind of artifact owns the next durable truth change. Then route to that artifact instead of improvising a hybrid.
