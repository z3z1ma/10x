---
id: ticket:50ded996
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T10:11:03Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  initiative:
    - initiative:skills-corpus-protocol-sharpening
  research:
    - research:skills-corpus-council-review
  evidence:
    - evidence:skills-corpus-council-review
    - evidence:ticket-risk-acceptance-grammar-validation
  critique:
    - critique:ticket-risk-acceptance-grammar-review
  packet:
    - packet:ralph-ticket-50ded996-20260502T095614Z
  plan:
    - plan:skills-corpus-protocol-sharpening
  supersedes:
    - ticket:3uv5l5fh
external_refs: {}
depends_on:
  - ticket:4e8ebe92
---

# Summary

Clarify ticket `change_class`, `risk_class`, critique policy, finding
disposition, accepted-risk handling, follow-up conversion, and acceptance-gate
grammar.

# Context

The council found ambiguity between ticket template requirements and references
that describe `change_class` and `risk_class` more conditionally. It also called
out the need for clearer critique finding disposition and follow-up conversion.

# Why Now

Tickets are the sole live execution ledger. If risk, critique, and acceptance
grammar are ambiguous, later Ralph slices may overclaim completion, skip required
review, or bury residual work instead of converting it into a ticket-owned
decision.

# Scope

- Decide and document when `change_class` and `risk_class` are required, including
  the lifecycle boundary for legacy tickets.
- Preserve or revise the current ticket template so it matches the selected rule.
- Explain the relationship between frontmatter `risk_class` and risk class inside
  `# Critique Disposition`.
- Clarify finding disposition grammar: resolved, accepted as risk, superseded by
  evidence, or converted into a linked follow-up ticket.
- Keep the acceptance gate fail-closed over unresolved required critique and
  missing evidence.
- Update `loom-critique` pointers only where needed so critique findings and
  ticket acceptance use the same disposition vocabulary.

# Non-goals

- Do not add a runtime acceptance checker.
- Do not change ticket status machine transitions unless the current transition
  guidance contradicts the accepted risk/follow-up grammar.
- Do not update packet grammar except where packet outcomes feed ticket
  acceptance; packet grammar belongs to `ticket:0cd38381`.

# Acceptance Criteria

- ACC-001: The ticket template and ticket references agree about whether
  `change_class` and `risk_class` are required.
- ACC-002: The relationship between frontmatter risk and critique-disposition
  risk is explicit enough to avoid duplicate contradictory risk claims.
- ACC-003: Critique finding dispositions are described in ticket-owned terms and
  include follow-up ticket conversion.
- ACC-004: Acceptance gate guidance still fails closed over missing mandatory
  critique, unresolved medium/high findings, and missing evidence.
- ACC-005: `loom-critique` and `loom-tickets` use compatible finding reference
  examples such as `critique:example-review#FIND-001`.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening#OBJ-002`
- `initiative:skills-corpus-protocol-sharpening#OBJ-005`
- `research:skills-corpus-council-review#CLAIM-006`
- `research:skills-corpus-council-review#CLAIM-009`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening#OBJ-002` | `evidence:ticket-risk-acceptance-grammar-validation` | `critique:ticket-risk-acceptance-grammar-review` | supported |
| `initiative:skills-corpus-protocol-sharpening#OBJ-005` | `evidence:ticket-risk-acceptance-grammar-validation` | `critique:ticket-risk-acceptance-grammar-review` | supported |
| `research:skills-corpus-council-review#CLAIM-006` | `evidence:skills-corpus-council-review`; `evidence:ticket-risk-acceptance-grammar-validation` | `critique:ticket-risk-acceptance-grammar-review` | supported |
| `research:skills-corpus-council-review#CLAIM-009` | `evidence:skills-corpus-council-review`; `evidence:ticket-risk-acceptance-grammar-validation` | `critique:ticket-risk-acceptance-grammar-review` | supported |

# Execution Notes

Choose one rule and make every touched surface agree. If strict ticket risk/change
fields are retained, explain why the ceremony earns its keep. If optionality is
kept, make the template and readiness guidance match that rule.

# Blockers

None. Dependency `ticket:4e8ebe92` is closed.

# Next Move / Next Route

Ralph implementation packet for ticket risk and acceptance grammar.

# Ralph Readiness

Bounded iteration:

Clarify ticket risk/change class strictness, critique finding disposition, and
acceptance gate follow-up conversion.

Write boundary:

- `skills/loom-tickets/**`
- `skills/loom-records/references/change-class.md`
- `skills/loom-critique/**` only for compatible finding-disposition pointers

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- selected strictness rule and rationale,
- examples of finding disposition and follow-up ticket conversion,
- validation output.

# Evidence

Recorded:

- `evidence:ticket-risk-acceptance-grammar-validation`
- `git diff --check` passed with no output.
- Targeted searches confirmed ticket classification lifecycle boundary,
  frontmatter risk alignment, accepted risk, superseded-by-evidence,
  follow-up conversion, and compatible finding examples.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale:

This changes ticket-owned acceptance and closure discipline.

Required critique profiles:

- protocol-change
- records-grammar
- routing-safety

Findings:

All findings resolved in `critique:ticket-risk-acceptance-grammar-review`.

Disposition status: complete

Deferral / not-required rationale:

Not deferred. Mandatory critique is recorded in
`critique:ticket-risk-acceptance-grammar-review`.

# Wiki Disposition

Deferred intentionally. Retrospective found no separate wiki page needed because
the accepted finding-disposition and follow-up conversion guidance now lives in
the ticket and critique owner surfaces. Final integration review may still choose
broader wiki promotion for the full sharpening pass.

# Acceptance Decision

Accepted by: OpenCode parent agent

Accepted at: 2026-05-02T10:11:03Z

Basis: Ralph packet `packet:ralph-ticket-50ded996-20260502T095614Z`, validation
evidence `evidence:ticket-risk-acceptance-grammar-validation`, and final oracle
critique `critique:ticket-risk-acceptance-grammar-review` with all findings
resolved.

Residual risks: Enforcement remains protocol/operator-driven rather than
automated; final corpus-wide validation remains owned by `ticket:cdf664af`.

# Dependencies

- `ticket:4e8ebe92`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the ticket risk and acceptance grammar slice.
- 2026-05-02T09:56:14Z: Started Ralph iteration
  `packet:ralph-ticket-50ded996-20260502T095614Z` for ticket risk and acceptance
  grammar.
- 2026-05-02T10:11:03Z: Accepted and closed after Ralph implementation,
  structural validation, oracle critique, resolved acceptance-grammar findings,
  and retrospective disposition. No ticket-scoped follow-up remains.
