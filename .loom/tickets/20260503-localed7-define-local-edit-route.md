---
id: ticket:localed7
kind: ticket
status: ready
change_class: workflow-boundary
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
  - ticket:reconchk
---

# Summary

Define the cheap `local_edit` route so Loom can remain lightweight without
becoming a bypass around ticket truth.

# Context

Council found README's minimum durable state principle strong, but the skills
corpus needs a clearer operational local-edit path.

# Why Now

Agents need to know when small edits do not need Ralph while still preserving
truth in tickets when a ticket owns the work.

# Scope

- Add a local-edit reference or targeted guidance in workspace/ticket/records
  routing.
- Define when local edit is honest, what ticket update is required, when evidence
  is needed, and when to escalate to Ralph/spec/research/critique.

# Out Of Scope

- Do not create a `loom-local-edit` skill or a bypass mode.
- Do not remove Ralph for implementation-sized work.

# Acceptance Criteria

- ACC-001: Corpus defines when `local_edit` is appropriate.
- ACC-002: Corpus states local edit does not bypass ticket-owned live state when a
  ticket owns the work.
- ACC-003: Corpus names escalation triggers for behavior/protocol/risky changes.
- ACC-004: Evidence records targeted `local_edit` searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008`
- `ticket:localed7#ACC-001`
- `ticket:localed7#ACC-002`
- `ticket:localed7#ACC-003`
- `ticket:localed7#ACC-004`
- `ticket:localed7#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008` | pending | pending | open |
| `ticket:localed7#ACC-001` | pending | pending | open |
| `ticket:localed7#ACC-002` | pending | pending | open |
| `ticket:localed7#ACC-003` | pending | pending | open |
| `ticket:localed7#ACC-004` | pending | pending | open |
| `ticket:localed7#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-workspace/references/routing.md`,
`skills/loom-tickets/references/readiness.md`, and route vocabulary if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: local edit route definition.
Write boundary: workspace/ticket/records routing references only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, local-edit wording observations, and
critique recommendation.

# Evidence

Expected: targeted searches for `local_edit`, Ralph escalation, ticket-owned live
state, evidence conditions, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: local edit guidance protects minimum durable state without
weakening recovery.

Required critique profiles:

- workflow-boundary
- operator-clarity
- ticket-truth

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

- `ticket:reconchk`

# Journal

- 2026-05-03T04:09:51Z: Created from council local-edit ergonomics finding.
