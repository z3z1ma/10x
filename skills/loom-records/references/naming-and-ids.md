# Naming And IDs

Loom uses canonical IDs for reference integrity and filenames for discovery.

Use both.

## Canonical ID Families

- `constitution:main`
- `decision:0001`
- `roadmap:<slug>`
- `initiative:<slug>`
- `research:<slug>`
- `spec:<slug>`
- `plan:<slug>`
- `ticket:<token>`
- `critique:<slug>`
- `wiki:<slug>`
- `evidence:<slug>`
- `packet:ralph-ticket-<token>-<UTC compact timestamp>`
- `workspace:main`

## Filename Guidance

### Stable semantic records

Use a semantic slug:

- `.loom/specs/<slug>.md`
- `.loom/plans/<slug>.md`
- `.loom/wiki/workflows/<slug>.md`

### Tickets

Use date + token + slug:

- `.loom/tickets/<YYYYMMDD>-<token>-<short-slug>.md`

The ticket's canonical ID should be only the token:

- `ticket:<token>`

### Packets

Use timestamp + subsystem + target:

- `.loom/packets/ralph/<UTC compact timestamp>-ticket-<token>-iter-01.md`

### Decisions

Use an ordered prefix:

- `.loom/constitution/decisions/decision-0001-packet-discipline.md`

## Why Both Matter

Canonical IDs make references durable.

Filenames make discovery cheap.

One is for graph integrity.
One is for human and agent navigation.

## Slug Guidance

Prefer lowercase, words separated by hyphens, and filenames that say what the record is about.
