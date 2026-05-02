---
id: critique:route-vocabulary-review
kind: critique
status: final
created_at: 2026-05-02T19:13:21Z
updated_at: 2026-05-02T19:15:17Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:rtvocab1 route vocabulary normalization
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:rtvocab1
  evidence:
    - evidence:route-vocabulary-validation
  packet:
    - packet:ralph-ticket-rtvocab1-20260502T190248Z
external_refs: {}
---

# Summary

Oracle critique reviewed `ticket:rtvocab1` route vocabulary normalization for
protocol-change, operator-clarity, and routing-safety risks.

The route vocabulary content was acceptable. One medium packet reconciliation
finding was identified, resolved by parent reconciliation, and confirmed resolved
by oracle re-check.

# Review Target

- Ticket: `ticket:rtvocab1`
- Evidence: `evidence:route-vocabulary-validation`
- Ralph packet: `packet:ralph-ticket-rtvocab1-20260502T190248Z`
- Product surfaces: `skills/loom-records`, `skills/loom-drive`,
  `skills/loom-tickets`, and `skills/loom-workspace`
- Oracle task session: `ses_215e7610affeQufvaGRvAEQ6AN`

# Verdict

`pass` after repair and re-check.

No findings remain. The packet lifecycle finding was resolved before ticket
acceptance.

# Findings

## RTVOCAB1-FIND-001: Ralph packet still looked unconsumed after child output returned

Severity: medium
Confidence: high
State: open

Observation:

The Ralph packet had child output populated but still used `status: compiled` and
`# Parent Merge Notes` said `Pending child execution.`

Why it matters:

This weakens checkpoint/resume safety because a fresh agent would see child output
and ticket updates while the packet still claimed to be pending execution.

Follow-up:

Resolved. Parent set `packet:ralph-ticket-rtvocab1-20260502T190248Z` to
`consumed` and replaced parent merge notes with the reconciliation result. Oracle
re-check confirmed no stale `Pending child execution` remained and returned
`pass` with no findings.

Challenges:

- `ticket:rtvocab1#ACC-005`

# Evidence Reviewed

- Current `git status --short` and `git diff` for the route vocabulary diff.
- `git diff --check`, with no output.
- `ticket:rtvocab1`.
- `evidence:route-vocabulary-validation`.
- `packet:ralph-ticket-rtvocab1-20260502T190248Z`.
- `plan:skills-corpus-council-precision-pass`.
- `initiative:skills-corpus-council-precision-pass`.
- Changed product surfaces under `skills/loom-records`, `skills/loom-drive`,
  `skills/loom-tickets`, and `skills/loom-workspace`.
- Oracle re-check of packet status, parent merge notes, ticket state, evidence,
  and targeted stale route/lifecycle searches.

# Residual Risks

- The canonical route token set is sufficient for scoped drive/ticket/workspace
  changes, but future route-bearing work in other workflow skills should extend or
  cite the shared vocabulary rather than inventing local route tokens.
- Some non-scoped product prose still uses phrase-style route wording. This was
  not blocking for this ticket because active route-bearing examples were scoped to
  drive, ticket, and workspace normalization.

# Required Follow-up

None before ticket acceptance.

# Acceptance Recommendation

Close-ready.
