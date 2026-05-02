---
id: critique:shared-record-grammar-review
kind: critique
status: final
created_at: 2026-05-02T09:39:09Z
updated_at: 2026-05-02T09:39:09Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:4e8ebe92
links:
  tickets:
    - ticket:4e8ebe92
  evidence:
    - evidence:shared-record-grammar-validation
  packets:
    - packet:ralph-ticket-4e8ebe92-20260502T091549Z
external_refs: {}
---

# Summary

Oracle-assisted critique of shared record and objective grammar changes for
`ticket:4e8ebe92`.

# Review Target

Reviewed current diff for:

- `skills/loom-records/**`
- `skills/loom-initiatives/**`
- relevant `.loom/**` objective-reference reconciliation
- `research:skills-corpus-council-review` question resolution

Reviewed against `ticket:4e8ebe92` acceptance criteria ACC-001 through ACC-006
with records-grammar, protocol-change, and operator-clarity profiles.

# Verdict

`pass_with_findings`.

Two oracle passes found blocking grammar issues during iteration. The fixer and
parent resolved them before final review. The final oracle pass found no remaining
grammar inconsistency; only parent ticket/packet reconciliation remained.

# Findings

## FIND-001: Objective reference form was not reconciled across records

Severity: high

Confidence: high

Disposition: resolved

Observation:

The initial implementation selected `initiative:<slug>#OBJ-001`, but active ticket
and packet records still used the old split form such as
`` `initiative:<slug>` OBJ-001 ``.

Why it matters:

If the graph itself keeps using the old form, the documented grep-friendly grammar
does not recover objective coverage reliably.

Follow-up:

Resolved by normalizing relevant `.loom/**` objective references to
`initiative:<slug>#OBJ-*` and updating research questions to record the chosen
form.

Challenges:

- `ticket:4e8ebe92` ACC-001
- `ticket:4e8ebe92` ACC-006

## FIND-002: Packet ID/path grammar table omitted current packet families

Severity: high

Confidence: high

Disposition: resolved

Observation:

The first kind/ID/path table listed only Ralph packet IDs and paths even though
the corpus ships Ralph, critique, and wiki packet templates.

Why it matters:

The table claimed to describe current supported families. Omitting critique/wiki
packets would make validators and operators falsely treat supported packet kinds
as drift.

Follow-up:

Resolved by listing `packet_kind: ralph`, `packet_kind: critique`, and
`packet_kind: wiki` ID/path rows.

Challenges:

- `ticket:4e8ebe92` ACC-003

## FIND-003: Supersession guidance conflated records with claims

Severity: high

Confidence: high

Disposition: resolved

Observation:

The first semantic-link update said superseded records or claims should use
`status: superseded`, which would incorrectly apply record lifecycle status to
individual `OBJ-*`, `REQ-*`, `ACC-*`, or `CLAIM-*` IDs.

Why it matters:

Claim or criterion supersession is narrower than record supersession. Conflating
them can retire an otherwise-current owner record by accident.

Follow-up:

Resolved by distinguishing record supersession from claim/criterion ID
supersession.

Challenges:

- `ticket:4e8ebe92` ACC-005

## FIND-004: Memory kind guidance remained ambiguous for validators

Severity: medium

Confidence: high

Disposition: resolved

Observation:

The first pass allowed optional `kind: memory` metadata but listed memory only as a
"memory support file" in the kind table.

Why it matters:

Validators need to understand that memory files usually lack canonical IDs, while
optional `kind: memory` remains support metadata and not a canonical truth owner.

Follow-up:

Resolved by adding optional `memory` support metadata guidance to the kind/ID/path
table and frontmatter exception wording.

Challenges:

- `ticket:4e8ebe92` ACC-004

## FIND-005: ID/path query examples were mislabeled as complete checks

Severity: medium

Confidence: high

Disposition: resolved

Observation:

The first query examples omitted constitution, decision, roadmap, workspace, and
packet subfamilies while being labeled as known-shape checks.

Why it matters:

ACC-006 requires ordinary grep guidance that does not mislead operators into
thinking a partial query is a schema validator.

Follow-up:

Resolved by expanding the discovery query and labeling it as discovery rather than
a validator.

Challenges:

- `ticket:4e8ebe92` ACC-006

# Evidence Reviewed

- Ralph packet `packet:ralph-ticket-4e8ebe92-20260502T091549Z`
- Validation evidence `evidence:shared-record-grammar-validation`
- Oracle critique pass `ses_21802daabffe1vRJbGDw3DrK43`
- Oracle critique pass `ses_217fa6e02ffeAauMKnWSloKSmI`
- Final oracle critique pass `ses_217f5279bffefk2upyJxpbjRGt`
- Current diff for `skills/loom-records/**`, `skills/loom-initiatives/**`, and
  related `.loom/**` reference reconciliation

# Residual Risks

- Future validators must honor that the `kind:` table describes current supported
  corpus usage, not a closed global vocabulary.
- Packet family ID/path details are summarized, not exhaustively specified. This
  is acceptable for this ticket's scope and can be sharpened by packet grammar
  work in `ticket:0cd38381` if needed.

# Required Follow-up

No required follow-up blocks this ticket's acceptance.

# Acceptance Recommendation

Close-ready. The ticket has structural evidence and final oracle review with all
blocking findings resolved.
