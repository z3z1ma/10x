---
id: ticket:u02z7o9j
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T16:55:55Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
  packet:
    - packet:ralph-ticket-u02z7o9j-20260502T164630Z
  evidence:
    - evidence:ticket-local-acceptance-readiness-validation
  critique:
    - critique:ticket-local-acceptance-readiness-review
external_refs: {}
depends_on:
  - ticket:3twzep5n
---

# Summary

Clarify ticket-local `ACC-*` acceptance IDs and make ticket readiness route-neutral
instead of Ralph-biased.

# Context

Council findings `COUNCIL-FIND-007` and `COUNCIL-FIND-008` found that ticket-local
acceptance criteria are allowed but not clearly ID-shaped, and the ticket template
uses `# Ralph Readiness` even when critique/wiki packet handoffs are sibling
routes.

# Why Now

Ticket templates are copied frequently. Ambiguous acceptance IDs and Ralph-biased
readiness headings train fresh agents to guess or misroute bounded work.

# Scope

- Clarify whether and how ticket-local `ACC-*` IDs should be written and cited.
- Align claim coverage references for `ticket:<token>#ACC-001` if selected.
- Rename or reshape ticket readiness heading to cover local edit, Ralph,
  critique, wiki, evidence, and acceptance routes without blurring Ralph.
- Update relevant ticket readiness guidance and examples.

# Non-goals

- Do not change spec-owned acceptance contract grammar except to distinguish it
  from ticket-local criteria.
- Do not remove Ralph-specific requirements from Ralph packet guidance.

# Acceptance Criteria

- ACC-001: Ticket-local acceptance criteria have explicit ID/reference guidance.
- ACC-002: Ticket template readiness is route-neutral and does not imply all
  packetized work is Ralph.
- ACC-003: Claim coverage references and ticket guidance agree.
- ACC-004: Evidence records before/after searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-005`
- `ticket:u02z7o9j#ACC-001`
- `ticket:u02z7o9j#ACC-002`
- `ticket:u02z7o9j#ACC-003`
- `ticket:u02z7o9j#ACC-004`
- `ticket:u02z7o9j#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-005` | `evidence:ticket-local-acceptance-readiness-validation` | `critique:ticket-local-acceptance-readiness-review` | supported |
| `ticket:u02z7o9j#ACC-001` | `evidence:ticket-local-acceptance-readiness-validation` | `critique:ticket-local-acceptance-readiness-review` | supported |
| `ticket:u02z7o9j#ACC-002` | `evidence:ticket-local-acceptance-readiness-validation` | `critique:ticket-local-acceptance-readiness-review` | supported |
| `ticket:u02z7o9j#ACC-003` | `evidence:ticket-local-acceptance-readiness-validation` | `critique:ticket-local-acceptance-readiness-review` | supported |
| `ticket:u02z7o9j#ACC-004` | `evidence:ticket-local-acceptance-readiness-validation` | `critique:ticket-local-acceptance-readiness-review` | supported |
| `ticket:u02z7o9j#ACC-005` | `critique:ticket-local-acceptance-readiness-review` | `critique:ticket-local-acceptance-readiness-review` | supported |

# Execution Notes

Council affected surfaces include `skills/loom-tickets/templates/ticket.md`,
`skills/loom-records/references/claim-coverage.md`, `skills/loom-tickets/SKILL.md`,
and `skills/loom-tickets/references/readiness.md`.

# Blockers

None. Dependency `ticket:3twzep5n` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:9c2delu8`.

# Route Readiness

Route: ticket acceptance review completed.

Review target: child diff for ticket-local acceptance IDs and route-neutral ticket
readiness.

Required profiles: records-grammar, operator-clarity, routing-safety.

Evidence reviewed: `evidence:ticket-local-acceptance-readiness-validation`, the
Ralph child output, the git diff, and
`critique:ticket-local-acceptance-readiness-review`.

# Evidence

Created:

- `evidence:ticket-local-acceptance-readiness-validation` records before/after
  targeted searches, `git diff --check`, and manual structural comparison.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique for every ticket; ticket template
changes affect operator routing.

Required critique profiles:

- records-grammar
- operator-clarity
- routing-safety

Findings:

None - oracle critique passed with no findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no findings.

# Wiki Disposition

Retrospective disposition complete. Durable lessons were promoted directly into
the owner product surfaces: ticket template route readiness, ticket readiness
guidance, ticket acceptance gate guidance, ticket skill acceptance-boundary prose,
and claim coverage grammar. No separate wiki page, research record, spec,
constitution decision, or memory entry is needed for this ticket.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T16:55:55Z
Basis: Ralph packet `packet:ralph-ticket-u02z7o9j-20260502T164630Z`; evidence
`evidence:ticket-local-acceptance-readiness-validation`; oracle critique
`critique:ticket-local-acceptance-readiness-review` with no findings.
Residual risks: validation and critique were structural/textual; historical
dogfood tickets still using `# Ralph Readiness` remain outside this product-scope
ticket and do not change the shipped ticket template.

# Dependencies

- `ticket:3twzep5n`

# Journal

- 2026-05-02T15:25:50Z: Created from council findings `COUNCIL-FIND-007` and
  `COUNCIL-FIND-008`.
- 2026-05-02T16:46:30Z: Dependency closed. Moved to active and compiled Ralph
  packet `packet:ralph-ticket-u02z7o9j-20260502T164630Z` from commit
  `16bb2a3c1f71fb56215f52b6c3d111764213e21d`.
- 2026-05-02T16:48:46Z: Ralph child updated ticket guidance, ticket template,
  acceptance gate guidance, and claim coverage grammar for ticket-local `ACC-*`
  references and route-neutral readiness. Evidence recorded in
  `evidence:ticket-local-acceptance-readiness-validation`. Moved to
  `review_required` because mandatory oracle critique remains outstanding.
- 2026-05-02T16:51:09Z: Parent reconciliation added the missing ticket-local
  critique example in claim coverage, refreshed evidence, and consumed Ralph
  packet `packet:ralph-ticket-u02z7o9j-20260502T164630Z`.
- 2026-05-02T16:55:55Z: Oracle critique passed with no findings. Recorded final
  critique, retrospective disposition, and acceptance; closed ticket.
