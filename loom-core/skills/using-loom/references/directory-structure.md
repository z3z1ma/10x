# Directory Structure

Loom work lives under `.loom/`.

The tree is lazily materialized: empty directories may be absent until a record or
artifact needs them.

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
|-- knowledge/
`-- packets/
    `-- ralph/
```

## Surface Paths

- constitution records live under `.loom/constitution/`
- tickets live under `.loom/tickets/`
- research records live under `.loom/research/`
- specs live under `.loom/specs/`
- plans live under `.loom/plans/`
- evidence records live under `.loom/evidence/`
- audit records live under `.loom/audit/`
- knowledge records live flat under `.loom/knowledge/`
- Ralph packets live under `.loom/packets/ralph/`

Raw evidence artifacts may live under `.loom/evidence/artifacts/<slug>/` when the
evidence record points at them.

Raw research artifacts may live under `.loom/research/artifacts/<slug>/` when the
research record points at them.

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
  .loom/knowledge \
  .loom/packets/ralph
```

Do not require empty directories to exist before using Loom. A missing directory is
only a problem when the current work needs that surface.

## Directory Discipline

Use the surface path that matches the record's job.

Retrospective is a workflow over existing surfaces and has no directory of its own.

Packets are bounded worker contracts. They do not replace the records, evidence,
or audit they cite.

Artifacts support evidence and research records. The Markdown record should remain
understandable when an artifact directory is absent.
