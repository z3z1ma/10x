---
id: ticket:drives10
kind: ticket
status: ready
change_class: workflow-boundary
risk_class: high
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
  - ticket:queryrc9
---

# Summary

Tighten `loom-drive` and saved support artifact boundaries so drive cannot become
a shadow ledger.

# Context

Council found drive valuable but the highest-risk workflow for duplicating ticket
truth or creating support-ledger drift.

# Why Now

Drive coordinates broad delegated objectives. It must clearly decline one-ticket
work and keep support artifacts reconciled into owner records.

# Scope

- Add prominent `Do not use drive for` guidance for small/ticket-ready work.
- Tighten saved support artifact rules: owner workflow, reconciliation target,
  prune/supersession condition, and no truth ownership.
- Preserve current drive capability for multi-phase objectives.

# Out Of Scope

- Do not add `.loom/drive/`, scheduler, daemon, DB, or drive state file.
- Do not make saved handoffs packets or canonical truth owners.

# Acceptance Criteria

- ACC-001: Drive guidance clearly says when not to use drive.
- ACC-002: Saved support artifact guidance names owner, reconciliation target, and
  prune/supersession condition.
- ACC-003: Guidance preserves ticket-owned live state and support noncanonicality.
- ACC-004: Evidence records targeted drive/support searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-010`
- `ticket:drives10#ACC-001`
- `ticket:drives10#ACC-002`
- `ticket:drives10#ACC-003`
- `ticket:drives10#ACC-004`
- `ticket:drives10#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-010` | pending | pending | open |
| `ticket:drives10#ACC-001` | pending | pending | open |
| `ticket:drives10#ACC-002` | pending | pending | open |
| `ticket:drives10#ACC-003` | pending | pending | open |
| `ticket:drives10#ACC-004` | pending | pending | open |
| `ticket:drives10#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-drive/SKILL.md`, drive support/handoff
references/templates, and records support-artifact guidance if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: drive/support boundary tightening.
Write boundary: drive skill/references/templates and directly related support
grammar only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, drive/support boundary observations, and
critique recommendation.

# Evidence

Expected: targeted searches for `Do not use drive`, support artifact owner,
reconciliation target, prune/supersession, noncanonical support, and
`git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: drive can otherwise become a second ledger.

Required critique profiles:

- workflow-boundary
- owner-boundary
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

- `ticket:queryrc9`

# Journal

- 2026-05-03T04:09:51Z: Created from council drive/support boundary finding.
