---
id: ticket:shipacc1
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T06:32:06Z
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
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-011` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |
| `ticket:shipacc1#ACC-001` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |
| `ticket:shipacc1#ACC-002` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |
| `ticket:shipacc1#ACC-003` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |
| `ticket:shipacc1#ACC-004` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |
| `ticket:shipacc1#ACC-005` | `evidence:acceptance-ship-boundary-validation` | `critique:acceptance-ship-boundary-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-ship/SKILL.md`, ship references, route
vocabulary, and ticket acceptance/readiness references if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to follow-up tickets.

Ralph packet `packet:ralph-ticket-shipacc1-20260503T061600Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Ralph readiness:
Bounded iteration: acceptance-review versus ship boundary.
Write boundary: ship skill/references and directly related ticket/route guidance.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, acceptance/ship observations, and critique
recommendation.

Acceptance review readiness:
Evidence `evidence:acceptance-ship-boundary-validation` and mandatory critique
`critique:acceptance-ship-boundary-review` support closure with no findings.

# Evidence

Recorded:

- `evidence:acceptance-ship-boundary-validation`

The evidence records targeted searches for `acceptance_review`, `ship`, closure,
package, ticket-owned acceptance, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: shipping summaries must not become closure decisions.

Required critique profiles:

- workflow-boundary
- closure-honesty
- operator-clarity

Findings:

`critique:acceptance-ship-boundary-review` - no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Acceptance-review versus ship boundaries were promoted into `loom-ship`, route
  vocabulary, ticket readiness, and workspace routing guidance.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to ship, route, ticket-readiness, and workspace-routing
references.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in ship,
route, ticket-readiness, and workspace-routing references.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T06:32:06Z
Basis: Ralph packet `packet:ralph-ticket-shipacc1-20260503T061600Z`; evidence
`evidence:acceptance-ship-boundary-validation`; mandatory critique
`critique:acceptance-ship-boundary-review` with no findings.
Residual risks: Documentation-only enforcement depends on future operators
following route and ship guidance. Evidence is structural/textual, appropriate
for a Markdown protocol guidance change.

# Dependencies

- `ticket:drives10`

# Journal

- 2026-05-03T04:09:51Z: Created from council acceptance-review versus ship finding.
- 2026-05-03T06:16:00Z: Started Ralph iteration
  `packet:ralph-ticket-shipacc1-20260503T061600Z` from clean `main` at
  `02858e0`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T06:29:18Z: Ralph iteration consumed. Product edits landed inside
  packet write scope, `evidence:acceptance-ship-boundary-validation` recorded,
  and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T06:32:06Z: Mandatory critique
  `critique:acceptance-ship-boundary-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
