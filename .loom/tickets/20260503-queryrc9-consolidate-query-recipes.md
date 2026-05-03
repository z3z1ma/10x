---
id: ticket:queryrc9
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T06:05:27Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
external_refs: {}
depends_on:
  - ticket:localed7
---

# Summary

Consolidate common Markdown-native graph query recipes for cold start, tickets,
packets, claims, critique, and placeholders.

# Context

Council found the filesystem-as-API doctrine strong but query recipes scattered.

# Why Now

Agents need a compact operator surface that improves recovery without requiring a
hidden index, dashboard, MCP, or CLI.

# Scope

- Add or consolidate a records query recipe reference.
- Include common recipes: active/open tickets, stale compiled packets, claim to
  evidence/critique trace, open critique findings, stale/superseded records,
  placeholders, and cold-start orientation.
- Link from records/tooling/workspace guidance if needed.

# Out Of Scope

- Do not add generated indexes, dashboards, MCP dependencies, schema validators,
  or command wrappers as protocol truth.
- Do not make every recipe mandatory for every task.

# Acceptance Criteria

- ACC-001: Common graph queries are discoverable from the records/tooling surface.
- ACC-002: Recipes use ordinary filesystem tools and remain examples, not runtime
  dependencies.
- ACC-003: Recipes cover stale compiled packets and claim/evidence/critique traces.
- ACC-004: Evidence records targeted query-recipe searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009`
- `ticket:queryrc9#ACC-001`
- `ticket:queryrc9#ACC-002`
- `ticket:queryrc9#ACC-003`
- `ticket:queryrc9#ACC-004`
- `ticket:queryrc9#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009` | `evidence:query-recipe-validation` | `critique:query-recipe-rereview` | supported |
| `ticket:queryrc9#ACC-001` | `evidence:query-recipe-validation` | `critique:query-recipe-rereview` | supported |
| `ticket:queryrc9#ACC-002` | `evidence:query-recipe-validation` | `critique:query-recipe-rereview` | supported |
| `ticket:queryrc9#ACC-003` | `evidence:query-recipe-validation` | `critique:query-recipe-rereview` | supported |
| `ticket:queryrc9#ACC-004` | `evidence:query-recipe-validation` | `critique:query-recipe-rereview` | supported |
| `ticket:queryrc9#ACC-005` | None - critique outcome is the acceptance instrument | `critique:query-recipe-rereview` | supported |

# Execution Notes

Likely touched files: `skills/loom-records/references/query-and-linking.md`, maybe
new `skills/loom-records/references/query-recipes.md`, records skill read order,
and bootstrap tooling reference if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:drives10`.

Ralph packet `packet:ralph-ticket-queryrc9-20260503T055023Z` completed in scope,
evidence was recorded, initial mandatory critique found two issues, both issues
were resolved, mandatory critique re-review passed with no findings, and
acceptance is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:query-recipe-validation`, initial critique
`critique:query-recipe-review`, and final re-review
`critique:query-recipe-rereview` support closure. Both initial findings were
resolved.

# Evidence

Recorded: `evidence:query-recipe-validation`, including the repair check after
initial critique.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: query recipes shape cold-start recovery and must not become a
hidden runtime expectation.

Required critique profiles:

- operator-clarity
- records-grammar
- workflow-boundary

Findings:

`critique:query-recipe-review#FIND-001` - resolved by reconciling ticket live
state, evidence disposition, critique disposition, claim matrix, and next route
away from stale Ralph execution.

`critique:query-recipe-review#FIND-002` - resolved by expanding the cold-start
query to include `.loom/research`, `.loom/specs`, other owner surfaces, and typed
link targets; repair evidence is recorded in `evidence:query-recipe-validation`.

`critique:query-recipe-rereview` - no new findings; mandatory critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Query recipe consolidation was promoted directly into
  `skills/loom-records/references/query-and-linking.md`.
- Query recipe discoverability was promoted into `skills/loom-records/SKILL.md`
  and the bootstrap filesystem/tooling reference.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to records query/linking guidance and bootstrap tooling.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in
records query/linking guidance and the bootstrap tooling pointer.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T06:05:27Z
Basis: Ralph packet `packet:ralph-ticket-queryrc9-20260503T055023Z`; evidence
`evidence:query-recipe-validation`; initial critique
`critique:query-recipe-review`; final no-findings re-review
`critique:query-recipe-rereview`.
Residual risks: Query recipes are discovery aids and can produce false positives;
operators must still read owning records. Validation remains manual and
structural, which is appropriate for this Markdown-only protocol change.

# Dependencies

- `ticket:localed7`

# Journal

- 2026-05-03T04:09:51Z: Created from council query-recipe ergonomics finding.
- 2026-05-03T05:50:23Z: Started Ralph iteration
  `packet:ralph-ticket-queryrc9-20260503T055023Z` from clean `main` at
  `477b6fe`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T05:54:48Z: Ralph iteration
  `packet:ralph-ticket-queryrc9-20260503T055023Z` completed in scope. Evidence
  recorded in `evidence:query-recipe-validation`; next route is mandatory
  critique.
- 2026-05-03T06:00:45Z: Mandatory critique
  `critique:query-recipe-review` found one medium ticket-ledger issue and one low
  cold-start coverage issue; next route is repair and critique re-review.
- 2026-05-03T06:01:35Z: Reconciled ticket live state for
  `critique:query-recipe-review#FIND-001` and expanded cold-start query coverage
  for `critique:query-recipe-review#FIND-002`; rechecked evidence and routed to
  mandatory critique re-review.
- 2026-05-03T06:05:27Z: Mandatory critique re-review
  `critique:query-recipe-rereview` passed with no findings. Parent dispositioned
  both initial findings as resolved and accepted closure.
