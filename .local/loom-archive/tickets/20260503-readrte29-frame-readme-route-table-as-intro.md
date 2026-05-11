---
id: ticket:readrte29
kind: ticket
status: closed
change_class: documentation-explanation
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T08:54:24Z
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
    - research:skills-corpus-third-pass-follow-up-validation
  critique:
    - critique:readme-route-table-framing-review
external_refs: {}
depends_on:
  - ticket:shipacc1
  - ticket:readwsh23
---

# Summary

Frame the README routing table as introductory and point to route vocabulary for
complete saved-field grammar.

# Context

The README has an introductory routing table, while `route-vocabulary.md` owns the
complete saved-field route vocabulary.

# Why Now

New readers should not treat the README table as the complete route-token source.

# Scope

- Add concise README wording that the route table is introductory.
- Point to `skills/loom-records/references/route-vocabulary.md` as the complete
  saved-field vocabulary owner.

# Out Of Scope

- Do not duplicate the full route vocabulary in README.
- Do not change route tokens.

# Acceptance Criteria

- ACC-001: README routing table is framed as introductory.
- ACC-002: README points to `route-vocabulary.md` for complete saved-field route
  grammar.
- ACC-003: README remains concise and product-facing.
- ACC-004: Evidence records targeted README route-table searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-030`
- `ticket:readrte29#ACC-001`
- `ticket:readrte29#ACC-002`
- `ticket:readrte29#ACC-003`
- `ticket:readrte29#ACC-004`
- `ticket:readrte29#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-030` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |
| `ticket:readrte29#ACC-001` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |
| `ticket:readrte29#ACC-002` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |
| `ticket:readrte29#ACC-003` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |
| `ticket:readrte29#ACC-004` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |
| `ticket:readrte29#ACC-005` | `evidence:readme-route-table-framing-validation` | `critique:readme-route-table-framing-review` | supported |

# Execution Notes

Likely touched file: `README.md`.

# Blockers

None - prerequisites `ticket:shipacc1` and `ticket:readwsh23` are closed and
pushed.

# Next Move / Next Route

Closed. Commit and push this ticket before final plan/initiative acceptance
review.

Ralph packet `packet:ralph-ticket-readrte29-20260503T085013Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Ralph readiness:
Bounded iteration: README route-table introductory framing.
Write boundary: README routing section only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed file, README route framing observations, and
critique recommendation.

Acceptance review readiness:
Evidence `evidence:readme-route-table-framing-validation` and mandatory critique
`critique:readme-route-table-framing-review` support closure.

# Evidence

Expected: targeted searches for introductory, route vocabulary, saved-field
grammar, route table, and `git diff --check`.

Recorded:

- `evidence:readme-route-table-framing-validation`

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: README route framing can mislead fresh operators.

Required critique profiles:

- route-vocabulary
- product-framing
- operator-clarity

Findings:

`critique:readme-route-table-framing-review`: no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- README route-table introductory framing was promoted into the README routing
  section.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable explanation is local to README orientation, with complete grammar owned
by `skills/loom-records/references/route-vocabulary.md`.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in README
orientation and points to route vocabulary for complete grammar.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T08:54:24Z
Basis: Ralph packet `packet:ralph-ticket-readrte29-20260503T085013Z`; evidence
`evidence:readme-route-table-framing-validation`; mandatory critique
`critique:readme-route-table-framing-review` with no findings.
Residual risks: The README route table remains intentionally non-exhaustive;
future edits must keep `route-vocabulary.md` canonical.

# Dependencies

- `ticket:shipacc1`
- `ticket:readwsh23`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass secondary polish finding.
- 2026-05-03T08:50:13Z: Parent confirmed prerequisites are closed and pushed,
  moved this ticket to active, and compiled Ralph iteration 1.
- 2026-05-03T08:51:36Z: Ralph child returned `stop`; parent accepted the scoped
  implementation output, recorded evidence, consumed the packet, and moved to
  mandatory critique.
- 2026-05-03T08:54:24Z: Mandatory critique
  `critique:readme-route-table-framing-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
