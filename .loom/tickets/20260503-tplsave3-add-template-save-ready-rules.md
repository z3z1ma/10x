---
id: ticket:tplsave3
kind: ticket
status: ready
change_class: template-safety
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
  - ticket:vocabx08
---

# Summary

Add save-ready pruning rules to copy-heavy ticket and plan templates.

# Context

Council found large templates can teach agents to preserve unused branches,
placeholder text, and ceremony.

# Why Now

Templates are copied into real records. They must make the saved-record shape
explicit enough to avoid Markdown junk drawers.

# Scope

- Add concise save-ready instructions to ticket and plan templates.
- Preserve acceptance, evidence, critique, and closure gates.
- Update related references only if needed for consistency.

# Out Of Scope

- Do not create template generators, schemas, or separate canonical minimal/full
  template families.
- Do not remove required acceptance or critique guidance.

# Acceptance Criteria

- ACC-001: Ticket template tells agents to remove unused readiness branches and
  replace placeholders before saving.
- ACC-002: Plan template tells agents to remove unused wave examples/placeholders
  or replace them with meaningful `None - reason`.
- ACC-003: The rules preserve evidence, critique, acceptance, and retrospective
  closure gates.
- ACC-004: Evidence records targeted placeholder/template checks and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-004`
- `ticket:tplsave3#ACC-001`
- `ticket:tplsave3#ACC-002`
- `ticket:tplsave3#ACC-003`
- `ticket:tplsave3#ACC-004`
- `ticket:tplsave3#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-004` | pending | pending | open |
| `ticket:tplsave3#ACC-001` | pending | pending | open |
| `ticket:tplsave3#ACC-002` | pending | pending | open |
| `ticket:tplsave3#ACC-003` | pending | pending | open |
| `ticket:tplsave3#ACC-004` | pending | pending | open |
| `ticket:tplsave3#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-tickets/templates/ticket.md` and
`skills/loom-plans/templates/plan.md`.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: save-ready template pruning rules.
Write boundary: ticket and plan templates plus directly related references only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, placeholder observations, and critique
recommendation.

# Evidence

Expected: targeted checks for save-ready wording, unused branch removal guidance,
placeholder mentions, closure gates, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: templates directly shape future saved records.

Required critique profiles:

- template-safety
- closure-honesty
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

- `ticket:vocabx08`

# Journal

- 2026-05-03T04:09:51Z: Created from council template right-sizing finding.
