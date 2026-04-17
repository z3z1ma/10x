# Appendix G — Naming Conventions

## Directory Names

- use lowercase kebab-case for file names
- use flat sibling skill names prefixed with `loom-`

## Record Filenames

- constitution records: descriptive names
- decisions: `decision-0001-<slug>.md`
- roadmap records: `<slug>.md`
- initiatives: `<slug>.md`
- specs: `<slug>.md`
- plans: `<slug>.md`
- tickets: `YYYYMMDD-<token>-<slug>.md`
- critique records: `<slug>.md`
- docs records: `<slug>.md`

## Ticket Filenames

- generate one random lowercase alphanumeric token for each new ticket
- keep the canonical ticket ref stable as `ticket:<token>`
- prefix the filename with the UTC creation date as `YYYYMMDD`
- reuse that same token in the filename as `YYYYMMDD-<token>-<slug>.md`
- keep the descriptive slug lowercase kebab-case
- do not encode repository prefixes, scope markers, or autoincremented numbers in the filename

Examples:

- `ticket:14eh8c66` created on 2026-04-08 -> `20260408-14eh8c66-<slug>.md`
- `ticket:z8h0g58e` created on 2026-04-01 -> `20260401-z8h0g58e-<slug>.md`

## Ref Prefixes

- `constitution:`
- `decision:`
- `roadmap:`
- `research:`
- `initiative:`
- `spec:`
- `plan:`
- `ticket:`
- `critique:`
- `doc:`
- `packet:`

## Script Names

Script names should match the deterministic helper family names documented in the Loom bundle.
