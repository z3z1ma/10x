---
id: ticket:namefmt54
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T20:16:21Z
updated_at: 2026-05-03T20:17:55Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  evidence:
    - evidence:date-prefixed-owner-record-naming-validation
  critique:
    - critique:date-prefixed-owner-record-naming-review
external_refs: {}
depends_on: []
---

# Summary

Make initiative, plan, critique, and evidence filenames date-prefixed while
keeping canonical IDs semantic and date-free.

# Context

The user observed that initiatives, plans, and critiques have temporal relevance
similar to evidence, tickets, and Ralph packets. Those records are also likely
targets for future retention or cleanup policy, so their filenames should sort by
creation date before slug.

# Why Now

The records naming grammar is the source for new Loom record creation. Updating it
now prevents additional temporally relevant owner records from being created with
semantic-only filenames that are harder to scan or age-filter later.

# Scope

- Update naming guidance so initiatives, plans, critiques, and evidence use
  `.loom/<layer>/<YYYYMMDD>-<slug>.md` filenames.
- Keep canonical IDs as `initiative:<slug>`, `plan:<slug>`, `critique:<slug>`,
  and `evidence:<slug>`.
- Add owning-skill creation guidance for initiatives, plans, critiques, and
  evidence.
- Update validation guidance so date+slug records check slug/ID agreement and the
  filename date against `created_at`.
- Update critique packet parent path examples to the new direct-critique filename
  convention.
- Rename the current route-token simplification critique record to the
  date-prefixed critique filename convention while preserving its canonical ID.

# Out Of Scope

- Do not bulk-rename historical `.loom/initiatives`, `.loom/plans`, `.loom/critique`,
  or `.loom/evidence` records.
- Do not define the future retention policy itself.
- Do not put dates into canonical record IDs.
- Do not change ticket or packet filename conventions.

# Acceptance Criteria

- ACC-001: `skills/loom-records/references/naming-and-ids.md` documents date+slug
  filenames for initiative, plan, critique, and evidence records while keeping IDs
  date-free.
- ACC-002: Naming guidance explains that the date prefix is a discovery/retention
  aid, uses the record creation date, and leaves older non-prefixed records
  legacy-compatible unless intentionally reconciled.
- ACC-003: `loom-initiatives`, `loom-plans`, `loom-critique`, and `loom-evidence`
  skills each state the new creation filename convention.
- ACC-004: Validation guidance checks slug/ID agreement and `created_at` date for
  initiative, plan, critique, and evidence date+slug records without accidentally
  applying that rule to ticket token filenames.
- ACC-005: Critique packet parent path examples use the date-prefixed direct
  critique path convention.
- ACC-006: The current route-token simplification critique file follows the new
  critique filename convention without changing `id: critique:route-token-simplification-review`.
- ACC-007: Structural validation and mandatory critique support acceptance.

# Coverage

Covers:

- ticket:namefmt54#ACC-001
- ticket:namefmt54#ACC-002
- ticket:namefmt54#ACC-003
- ticket:namefmt54#ACC-004
- ticket:namefmt54#ACC-005
- ticket:namefmt54#ACC-006
- ticket:namefmt54#ACC-007

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ticket:namefmt54#ACC-001 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-002 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-003 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-004 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-005 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-006 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |
| ticket:namefmt54#ACC-007 | evidence:date-prefixed-owner-record-naming-validation | critique:date-prefixed-owner-record-naming-review | supported |

# Execution Notes

Implemented as a local protocol documentation and record-grammar edit. Existing
non-date historical records are intentionally left in place as legacy-compatible
records because bulk renames require separate path-reference reconciliation.

# Blockers

None.

# Evidence

Evidence status: sufficient for structural acceptance.

Evidence record:

- evidence:date-prefixed-owner-record-naming-validation

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: the change modifies shared naming grammar, validation behavior,
owner-skill creation guidance, and a current critique record path.

Required critique profiles:

- protocol-change
- workflow-boundary
- operator-clarity
- operator-surface

Findings:

- critique:date-prefixed-owner-record-naming-review#FIND-001 — resolved by adding
  evidence naming guidance to `skills/loom-evidence/SKILL.md`.
- critique:date-prefixed-owner-record-naming-review#FIND-002 — resolved by
  narrowing validation wording to initiative/plan/critique/evidence date+slug
  records and checking the filename date against `created_at`.
- critique:date-prefixed-owner-record-naming-review#FIND-003 — resolved by
  replacing age-only pruning language with temporal discovery and future
  retention/cleanup decision language.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- The accepted naming convention was promoted directly into the owning records
  grammar, owner skills, validation guidance, and critique packet template.

Deferred / not-required rationale:

No separate wiki, research, spec, plan, initiative, constitution, or memory
promotion is required because the durable lesson is now in the product-surface
protocol guidance that owns it.

# Wiki Disposition

N/A - no wiki promotion needed.

# Acceptance Decision

Accepted by: OpenCode
Accepted at: 2026-05-03T20:17:55Z
Basis: `evidence:date-prefixed-owner-record-naming-validation` and
`critique:date-prefixed-owner-record-naming-review` support all acceptance
criteria; mandatory critique findings were resolved.
Residual risks: Historical `.loom` records still use legacy non-date filenames;
renaming them should be a separate reconciliation pass if desired. Git sees the
route-token critique rename as a delete plus untracked add until both paths are
staged together.

# Dependencies

None.

# Journal

- 2026-05-03T20:16:21Z: Updated date-prefixed owner-record naming guidance,
  resolved critique findings, and recorded evidence.
- 2026-05-03T20:17:55Z: Ran final structural validation, accepted the evidence,
  and closed this ticket.
