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
- tickets: `<repo-short-slug>-0001-<slug>.md`
- critique records: `<slug>.md`
- docs records: `<slug>.md`

## Ticket Filename Prefixes

- derive the ticket filename prefix from the owning repository's git remote when available
- use the remote repository name, not the host or full URL, as the source string
- if no parseable remote is available, fall back to the repository directory name
- convert that source string into a short slug by taking the first three characters of the first token plus the first character of each later token or digit chunk, capped at eight characters
- keep ticket refs stable as `ticket:0001`; only the filename prefix is repository-derived
- if the ticket scope is `multi_repository`, use the fixed filename prefix `multi`
- if the ticket scope is `workspace`, use the fixed filename prefix `wksp`

Examples:

- `agent-loom` -> `agel2-0001-<slug>.md`
- `payments-api` -> `paya-0001-<slug>.md`
- `cli` -> `cli-0001-<slug>.md`
- `multi_repository` ticket -> `multi-0001-<slug>.md`
- `workspace` ticket -> `wksp-0001-<slug>.md`

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
