---
id: ticket:50ded996
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T09:28:53Z
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

- Decide and document whether `change_class` and `risk_class` are required for
  every ticket or only when evidence/critique/packet posture depends on them.
- Preserve or revise the current ticket template so it matches the selected rule.
- Explain the relationship between frontmatter `risk_class` and risk class inside
  `# Critique Disposition`.
- Clarify finding disposition grammar: resolved, accepted as risk, deferred with
  rationale when allowed, or converted into a linked follow-up ticket.
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
| `initiative:skills-corpus-protocol-sharpening#OBJ-002` | implementation evidence pending | mandatory critique pending | open |
| `initiative:skills-corpus-protocol-sharpening#OBJ-005` | implementation evidence pending | mandatory critique pending | open |
| `research:skills-corpus-council-review#CLAIM-006` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |
| `research:skills-corpus-council-review#CLAIM-009` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |

# Execution Notes

Choose one rule and make every touched surface agree. If strict ticket risk/change
fields are retained, explain why the ceremony earns its keep. If optionality is
kept, make the template and readiness guidance match that rule.

# Blockers

Do not start until `ticket:4e8ebe92` lands or is intentionally deferred, because
follow-up and accepted-risk references may depend on shared semantic link grammar.

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

Expected:

- `git diff --check`
- targeted grep checks for `change_class`, `risk_class`, critique disposition,
  accepted risk, follow-up, and `FIND-*` references
- manual comparison against acceptance gate guardrails

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

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is mandatory.

# Wiki Disposition

Pending. Finding-to-follow-up conversion may deserve wiki promotion if it becomes
a reusable operator pattern beyond the ticket references.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:4e8ebe92`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the ticket risk and acceptance grammar slice.
