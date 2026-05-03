---
id: ticket:shipacc1
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
  - ticket:drives10
---

# Summary

Clarify that `acceptance_review` is ticket-owned closure evaluation and `loom-ship`
packages already-truthful work without closing tickets.

# Context

Council found acceptance review versus ship boundaries important for avoiding
shipping summaries as shadow closure decisions.

# Why Now

Shipping, PRs, and handoffs are support/transport surfaces. They must not replace
ticket-owned acceptance.

# Scope

- Strengthen `loom-ship` and route/ticket guidance around ship versus acceptance.
- Ensure `acceptance_review` remains a ticket-owned route.
- Keep ship useful for PR summaries, release notes, handoff packages, risk
  summaries, and follow-up lists.

# Out Of Scope

- Do not create a release ledger or ship-owned closure state.
- Do not require external PR tooling.

# Acceptance Criteria

- ACC-001: Corpus states `acceptance_review` evaluates ticket-owned closure.
- ACC-002: Corpus states `loom-ship` packages already-truthful work and does not
  close tickets.
- ACC-003: Route/ticket/ship guidance remains consistent with ticket ledger
  authority.
- ACC-004: Evidence records targeted acceptance/ship searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-011`
- `ticket:shipacc1#ACC-001`
- `ticket:shipacc1#ACC-002`
- `ticket:shipacc1#ACC-003`
- `ticket:shipacc1#ACC-004`
- `ticket:shipacc1#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-011` | pending | pending | open |
| `ticket:shipacc1#ACC-001` | pending | pending | open |
| `ticket:shipacc1#ACC-002` | pending | pending | open |
| `ticket:shipacc1#ACC-003` | pending | pending | open |
| `ticket:shipacc1#ACC-004` | pending | pending | open |
| `ticket:shipacc1#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-ship/SKILL.md`, ship references, route
vocabulary, and ticket acceptance/readiness references if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: acceptance-review versus ship boundary.
Write boundary: ship skill/references and directly related ticket/route guidance.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, acceptance/ship observations, and critique
recommendation.

# Evidence

Expected: targeted searches for `acceptance_review`, `ship`, closure, package,
ticket-owned acceptance, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: shipping summaries must not become closure decisions.

Required critique profiles:

- workflow-boundary
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

- `ticket:drives10`

# Journal

- 2026-05-03T04:09:51Z: Created from council acceptance-review versus ship finding.
