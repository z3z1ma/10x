# Layer Boundaries

Loom keeps durable work understandable by giving each kind of artifact a clear job. Because every artifact is a Markdown file in a known directory, the directory tree itself enforces layer boundaries. There is no runtime dispatch -- the path tells you what kind of artifact you are looking at.

## Kinds Of Artifact

1. **Core rules** (`rules/`) -- meaning, authority, trust boundaries, invariants
2. **Skills** (`skills/`) -- task-specific operating instructions
3. **Canonical records** (`.loom/{constitution,research,initiatives,specs,plans,tickets,critique,docs}/`) -- durable project state
4. **Packets and runs** (`.loom/runs/`, `.loom/verification/`) -- bounded child execution handoff and evidence

Use these ownership rules continuously. If one kind of artifact starts behaving like another, reconcile the drift instead of tolerating it.

If you need the required sections and intent for each record kind, read `appendices/layer-schemas.md`.

If you need the shared frontmatter and status conventions that span multiple kinds, read `appendices/common-schema-conventions.md`.

## Canonicality

Being stored under `.loom/` does not automatically make an artifact canonical. The canonical subtrees are:

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

This distinction matters because canonical records are the source of project truth. Non-canonical artifacts support that truth but do not outrank it.

## The Directory Tree Is The Schema

Because layer boundaries are directory boundaries, standard tools give you layer-aware operations for free:

```bash
# All canonical records
find .loom/{constitution,research,initiatives,specs,plans,tickets,critique,docs} -name "*.md"

# Everything in the execution ledger
ls .loom/tickets/

# All run artifacts for a subsystem
find .loom/runs/ralph -name "*.md"

# Cross-layer reference check
grep -R "spec:packet-governance" .loom
```

No query API is needed. The directory structure makes `find` a record-discovery tool and `grep` a graph-query tool. This is not a workaround -- it is the intended design.

## Layer Discipline

- Canonical records MUST link to evidence and artifacts explicitly.
- Packets MAY summarize or embed canonical records but do not outrank them.
- Derived dashboards and reports are disposable unless promoted into canonical records.
- Structural helper CLIs scaffold or validate records. They do not replace reading, editing, or searching with standard tools.
- When deleting or renaming a canonical record, reconcile its typed links and other direct references across `.loom/` before removing or moving the file.

When in doubt, ask which kind of artifact owns the next durable truth change. Then route to that artifact instead of improvising a hybrid.
