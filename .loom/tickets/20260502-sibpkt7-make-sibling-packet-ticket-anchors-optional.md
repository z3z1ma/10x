---
id: ticket:sibpkt7
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T22:03:13Z
updated_at: 2026-05-02T23:18:54Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-template-grammar-safety-pass
  plan:
    - plan:skills-corpus-template-grammar-safety-pass
  packet:
    - packet:ralph-ticket-sibpkt7-20260502T230712Z
  evidence:
    - evidence:sibling-packet-ticket-anchor-validation
  critique:
    - critique:sibling-packet-ticket-anchor-review
    - critique:sibling-packet-ticket-anchor-rereview
external_refs: {}
depends_on:
  - ticket:pktprov4
---

# Summary

Make ticket references optional in critique/wiki packet templates when the target
is not ticket-centered.

# Context

Council finding `NC-007` found critique/wiki packet templates that still assume
ticket-centered targets or parent merge scopes.

# Why Now

Critique and wiki are sibling workflows. Their packets may target records, pages,
or source sets without a ticket anchor.

# Scope

- Update critique and wiki packet templates to allow ticket-less targets with
  `None - rationale` examples where appropriate.
- Preserve ticket-centered examples where tickets are real targets.
- Keep critique/wiki packet discipline separate from Ralph.

# Out Of Scope

- Do not remove ticket links where tickets actually own execution.
- Do not make critique/wiki packets canonical owner layers.

# Acceptance Criteria

- ACC-001: Critique packet template supports non-ticket review targets.
- ACC-002: Wiki packet template supports non-ticket synthesis targets.
- ACC-003: Ticket refs and parent merge scope are explicit with `None - rationale`
  where absent.
- ACC-004: Evidence records sibling packet template searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-007`
- `ticket:sibpkt7#ACC-001`
- `ticket:sibpkt7#ACC-002`
- `ticket:sibpkt7#ACC-003`
- `ticket:sibpkt7#ACC-004`
- `ticket:sibpkt7#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-template-grammar-safety-pass#OBJ-007` | `evidence:sibling-packet-ticket-anchor-validation` | `critique:sibling-packet-ticket-anchor-rereview` | supported |
| `ticket:sibpkt7#ACC-001` | `evidence:sibling-packet-ticket-anchor-validation` | `critique:sibling-packet-ticket-anchor-review#SIBPKT7-FIND-002` resolved; `critique:sibling-packet-ticket-anchor-rereview` passed | supported |
| `ticket:sibpkt7#ACC-002` | `evidence:sibling-packet-ticket-anchor-validation` | `critique:sibling-packet-ticket-anchor-rereview` | supported |
| `ticket:sibpkt7#ACC-003` | `evidence:sibling-packet-ticket-anchor-validation` | `critique:sibling-packet-ticket-anchor-review#SIBPKT7-FIND-001` resolved; `critique:sibling-packet-ticket-anchor-rereview` passed | supported |
| `ticket:sibpkt7#ACC-004` | `evidence:sibling-packet-ticket-anchor-validation` | `critique:sibling-packet-ticket-anchor-rereview` | supported |
| `ticket:sibpkt7#ACC-005` | `critique:sibling-packet-ticket-anchor-rereview` | oracle re-review passed with no findings | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-critique/templates/critique-packet.md`
and `skills/loom-wiki/templates/wiki-packet.md`.

# Blockers

None - dependency `ticket:pktprov4` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:phsafe8`.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:sibling-packet-ticket-anchor-validation`, initial critique
`critique:sibling-packet-ticket-anchor-review`, and passing oracle re-review
`critique:sibling-packet-ticket-anchor-rereview` support closure.

# Evidence

Expected: before/after searches for ticket refs, `None - rationale`, parent merge
scope, critique/wiki packet templates, and `git diff --check`.

Observed: `evidence:sibling-packet-ticket-anchor-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: sibling packet templates must not make tickets mandatory where
the workflow target is not ticket-owned.

Required critique profiles:

- owner-boundary
- records-grammar
- operator-clarity

Findings:

Initial oracle critique `critique:sibling-packet-ticket-anchor-review` found:

- `SIBPKT7-FIND-001` - resolved by replacing empty
  `packet:ralph-ticket-sibpkt7-20260502T230712Z` `parent_merge_scope.paths` with
  concrete parent-reconciled paths.
- `SIBPKT7-FIND-002` - resolved by clarifying critique path-set review encoding
  with existing `review_target` fields.

Oracle re-review `critique:sibling-packet-ticket-anchor-rereview` confirmed both
findings resolved and found no new findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Optional ticket-anchor wording was promoted directly into
  `skills/loom-critique/templates/critique-packet.md` and
  `skills/loom-wiki/templates/wiki-packet.md`.
- Critique path-set review encoding guidance was promoted directly into
  `skills/loom-critique/templates/critique-packet.md` during finding remediation.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched critique/wiki packet templates.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T23:18:54Z
Basis: Ralph packet `packet:ralph-ticket-sibpkt7-20260502T230712Z`; evidence
`evidence:sibling-packet-ticket-anchor-validation`; initial oracle critique
`critique:sibling-packet-ticket-anchor-review`; passing oracle re-review
`critique:sibling-packet-ticket-anchor-rereview`.
Residual risks: validation is structural/manual. Historical critique/wiki packets
were not migrated or validated, consistent with ticket scope.

# Dependencies

- `ticket:pktprov4`

# Journal

- 2026-05-02T22:03:13Z: Created from council finding `NC-007`.
- 2026-05-02T23:07:12Z: Confirmed dependency `ticket:pktprov4` is closed,
  compiled Ralph packet `packet:ralph-ticket-sibpkt7-20260502T230712Z`, and
  moved ticket to `active`.
- 2026-05-02T23:09:05Z: Ralph child made critique/wiki packet ticket anchors
  optional in the targeted templates, recorded
  `evidence:sibling-packet-ticket-anchor-validation`, and moved ticket to
  `review_required` for mandatory oracle critique.
- 2026-05-02T23:11:23Z: Parent reconciled Ralph output, removed obsolete route
  duplication, marked `packet:ralph-ticket-sibpkt7-20260502T230712Z` consumed,
  and confirmed the ticket is ready for mandatory oracle critique.
- 2026-05-02T23:15:30Z: Initial oracle critique
  `critique:sibling-packet-ticket-anchor-review` found two issues. Parent applied
  fixes for empty parent merge paths and critique path-set target encoding; ticket
  remains `review_required` pending oracle re-review.
- 2026-05-02T23:18:54Z: Oracle re-review
  `critique:sibling-packet-ticket-anchor-rereview` confirmed both prior findings
  resolved and found no new findings. Parent recorded retrospective / promotion
  disposition and accepted closure.
