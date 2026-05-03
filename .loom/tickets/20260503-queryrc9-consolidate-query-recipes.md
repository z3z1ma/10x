---
id: ticket:queryrc9
kind: ticket
status: ready
change_class: records-grammar
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
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
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009` | pending | pending | open |
| `ticket:queryrc9#ACC-001` | pending | pending | open |
| `ticket:queryrc9#ACC-002` | pending | pending | open |
| `ticket:queryrc9#ACC-003` | pending | pending | open |
| `ticket:queryrc9#ACC-004` | pending | pending | open |
| `ticket:queryrc9#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-records/references/query-and-linking.md`, maybe
new `skills/loom-records/references/query-recipes.md`, records skill read order,
and bootstrap tooling reference if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: query recipe consolidation.
Write boundary: records query references and directly related read-order/tooling
links.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, query recipe observations, and critique
recommendation.

# Evidence

Expected: targeted searches for active ticket, compiled packet, claim trace,
critique findings, placeholder scan, ordinary tools, and `git diff --check`.

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

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Pending after critique.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

- `ticket:localed7`

# Journal

- 2026-05-03T04:09:51Z: Created from council query-recipe ergonomics finding.
