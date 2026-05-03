---
id: ticket:bootinv1
kind: ticket
status: ready
change_class: protocol-authority
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
depends_on: []
---

# Summary

Add minimal first-contact bootstrap orientation for how a fresh model should see
Loom.

# Context

Council found that README's core orientation is stronger than the loaded
bootstrap surface. User specifically warned that bootstrap is the first thing a
model sees and must not leak internal framing.

# Why Now

Bootstrap doctrine governs every downstream workflow and should carry the minimal
worldview needed for placement, owner truth, and recoverable sessions.

# Scope

- Update `skills/loom-bootstrap/references/01-core-identity.md` only if possible.
- Add concise operational orientation: placement beats recency, the graph carries
  durable truth, sessions/workers are disposable, and records/packets/evidence /
  critique/reconciliation are the recovery path.
- Keep wording generic and immediately actionable for a never-seen-Loom model.

# Out Of Scope

- Do not add marketing, internal product positioning, viral framing, or external
  article references.
- Do not change the layer model.
- Do not add new bootstrap references unless critique requires it.

# Acceptance Criteria

- ACC-001: Bootstrap contains minimal first-contact orientation for Loom's
  worldview without relying on README.
- ACC-002: The new text is operational doctrine, not marketing or internal framing.
- ACC-003: Existing owner-layer, ticket-ledger, packet, evidence, critique, and
  wiki boundaries remain unchanged.
- ACC-004: Evidence records targeted bootstrap wording checks and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-001`
- `ticket:bootinv1#ACC-001`
- `ticket:bootinv1#ACC-002`
- `ticket:bootinv1#ACC-003`
- `ticket:bootinv1#ACC-004`
- `ticket:bootinv1#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-001` | pending | pending | open |
| `ticket:bootinv1#ACC-001` | pending | pending | open |
| `ticket:bootinv1#ACC-002` | pending | pending | open |
| `ticket:bootinv1#ACC-003` | pending | pending | open |
| `ticket:bootinv1#ACC-004` | pending | pending | open |
| `ticket:bootinv1#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched file: `skills/loom-bootstrap/references/01-core-identity.md`.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: minimal bootstrap orientation.
Write boundary: `skills/loom-bootstrap/references/01-core-identity.md`, this ticket,
one Ralph packet, one evidence record, and one critique record.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, before/after wording observations, evidence,
and critique recommendation.

# Evidence

Expected: targeted searches for new bootstrap orientation, absence of internal
framing/marketing language, boundary preservation, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: bootstrap authority affects every future Loom activation.

Required critique profiles:

- protocol-change
- operator-clarity
- owner-boundary

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

None.

# Journal

- 2026-05-03T04:09:51Z: Created from council finding to promote core orientation
  into bootstrap, constrained by user warning to avoid internal framing.
