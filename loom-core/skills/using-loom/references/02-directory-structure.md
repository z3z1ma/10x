# Directory Structure

Loom work lives under `.loom/`. The tree is lazy: missing empty directories are
fine until the current work needs that surface.

## Canonical Tree

```text
.loom/
|-- constitution/
|   |-- constitution.md
|   |-- decisions/
|   `-- roadmap/
|-- tickets/
|-- research/
|   `-- artifacts/
|-- specs/
|-- plans/
|-- evidence/
|   `-- artifacts/
|-- audit/
`-- knowledge/
```

## Surface Paths

- constitution: `.loom/constitution/`
- tickets: `.loom/tickets/`
- research: `.loom/research/`
- specs: `.loom/specs/`
- plans: `.loom/plans/`
- evidence: `.loom/evidence/`
- audit: `.loom/audit/`
- knowledge: `.loom/knowledge/`

Raw evidence artifacts may live under `.loom/evidence/artifacts/YYYYMMDD-<slug>/`
and raw research artifacts under `.loom/research/artifacts/YYYYMMDD-<slug>/` when
the owning Markdown record points at them.

## Bootstrap

Create directories when needed:

```bash
mkdir -p \
  .loom/constitution/decisions \
  .loom/constitution/roadmap \
  .loom/tickets \
  .loom/research/artifacts \
  .loom/specs \
  .loom/plans \
  .loom/evidence/artifacts \
  .loom/audit \
  .loom/knowledge
```

## Directory Discipline

Use the surface path that matches the record's job. Retrospective is a workflow
over existing surfaces and has no directory of its own.

Tickets hold durable context for bounded worker and review runs. Transient launch
prompts do not replace the records, evidence, or audit they cite.

Artifacts support evidence and research. The Markdown record should remain
understandable even if an artifact directory is absent.
