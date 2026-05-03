---
id: ticket:vocabx08
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
  - ticket:trustbd2
---

# Summary

Consolidate route/status/disposition vocabulary boundaries so agents do not mix
route tokens, lifecycle statuses, ticket states, child outcomes, critique states,
or ticket-owned dispositions.

# Context

Council found the vocabulary model strong but vulnerable to duplicated lists and
`continue`/`stop` ambiguity.

# Why Now

Template and workflow edits later in this pass should point at canonical
vocabulary instead of spreading drift.

# Scope

- Strengthen `route-vocabulary` and `status-lifecycle` as canonical references.
- Update nearby surfaces that duplicate or blur vocabulary boundaries.
- Explicitly distinguish route tokens from Ralph child outcomes when useful.

# Out Of Scope

- Do not create runtime enums, validators, command routers, or schemas.
- Do not rename existing route tokens unless unavoidable.

# Acceptance Criteria

- ACC-001: Canonical route and status sources are clear and cross-linked.
- ACC-002: Guidance distinguishes route tokens, ticket states, record statuses,
  packet statuses, child outcomes, critique finding states, and ticket-owned
  dispositions.
- ACC-003: `continue` and `stop` route-token examples cannot be confused with
  Ralph child outcomes.
- ACC-004: Evidence records targeted vocabulary searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-003`
- `ticket:vocabx08#ACC-001`
- `ticket:vocabx08#ACC-002`
- `ticket:vocabx08#ACC-003`
- `ticket:vocabx08#ACC-004`
- `ticket:vocabx08#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-003` | pending | pending | open |
| `ticket:vocabx08#ACC-001` | pending | pending | open |
| `ticket:vocabx08#ACC-002` | pending | pending | open |
| `ticket:vocabx08#ACC-003` | pending | pending | open |
| `ticket:vocabx08#ACC-004` | pending | pending | open |
| `ticket:vocabx08#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-records/references/route-vocabulary.md`,
`skills/loom-records/references/status-lifecycle.md`, and small dependent
cross-references if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: route/status vocabulary consolidation.
Write boundary: targeted records references and dependent route snippets only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, vocabulary search observations, and
critique recommendation.

# Evidence

Expected: targeted searches for route tokens, child outcomes, finding states,
finding dispositions, packet statuses, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: vocabulary drift can mislead ticket closure and route selection.

Required critique profiles:

- records-grammar
- routing-safety
- operator-clarity

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

- `ticket:trustbd2`

# Journal

- 2026-05-03T04:09:51Z: Created from council vocabulary consolidation finding.
