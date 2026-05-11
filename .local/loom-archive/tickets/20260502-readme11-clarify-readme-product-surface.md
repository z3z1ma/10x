---
id: ticket:readme11
kind: ticket
status: closed
change_class: documentation-explanation
risk_class: medium
created_at: 2026-05-02T22:03:13Z
updated_at: 2026-05-03T00:22:36Z
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
    - packet:ralph-ticket-readme11-20260503T001418Z
  evidence:
    - evidence:readme-product-surface-framing-validation
  critique:
    - critique:readme-product-surface-framing-review
external_refs: {}
depends_on:
  - ticket:routewf10
  - ticket:phsafe8
  - ticket:critrec9
---

# Summary

Clarify README product-surface framing so `skills/` is the package surface and
other files are explanatory, maintainer, adapter, example, or packaging support.

# Context

Council finding `NC-011` found README wording that may blur the product surface
with repo support docs, adapters, or examples.

# Why Now

Public package framing should reinforce the skills-only product boundary and avoid
making support surfaces look like protocol truth owners.

# Scope

- Review README product-surface and install/framing language.
- Clarify `skills/` as the protocol product surface.
- Keep support docs/adapters/examples framed as explanatory or packaging support.

# Out Of Scope

- Do not rewrite the README for style alone.
- Do not change install mechanics or add command surfaces.

# Acceptance Criteria

- ACC-001: README clearly names `skills/` as the product surface.
- ACC-002: README does not imply support docs, adapters, examples, or packaging
  files own protocol truth.
- ACC-003: README remains clear for public readers.
- ACC-004: Evidence records README framing searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-011`
- `ticket:readme11#ACC-001`
- `ticket:readme11#ACC-002`
- `ticket:readme11#ACC-003`
- `ticket:readme11#ACC-004`
- `ticket:readme11#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-template-grammar-safety-pass#OBJ-011` | `evidence:readme-product-surface-framing-validation` | `critique:readme-product-surface-framing-review` | supported |
| `ticket:readme11#ACC-001` | `evidence:readme-product-surface-framing-validation` | `critique:readme-product-surface-framing-review` | supported |
| `ticket:readme11#ACC-002` | `evidence:readme-product-surface-framing-validation` | `critique:readme-product-surface-framing-review` | supported |
| `ticket:readme11#ACC-003` | `evidence:readme-product-surface-framing-validation` | `critique:readme-product-surface-framing-review` | supported |
| `ticket:readme11#ACC-004` | `evidence:readme-product-surface-framing-validation` | `critique:readme-product-surface-framing-review` | supported |
| `ticket:readme11#ACC-005` | `critique:readme-product-surface-framing-review` | oracle critique passed with no findings | supported |

# Execution Notes

Likely touched surface is `README.md`; inspect nearby install/framing docs only if
README changes need consistency checks.

# Blockers

Depends on `ticket:routewf10`, `ticket:phsafe8`, and `ticket:critrec9`.

# Next Move / Next Route

Closed. Commit and push this ticket, then close the parent plan/initiative and
run the next council pass.

# Route Readiness

Acceptance review readiness:

Evidence `evidence:readme-product-surface-framing-validation` and oracle critique
`critique:readme-product-surface-framing-review` support closure with no
findings.

# Evidence

Recorded: `evidence:readme-product-surface-framing-validation` with before/after
README searches for product surface/support/adapters/examples/packaging/truth-owner
framing and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: README public framing can misrepresent protocol authority.

Required critique profiles:

- product-framing
- owner-boundary
- operator-clarity

Findings:

`critique:readme-product-surface-framing-review` - no findings; mandatory oracle
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Product-surface framing was promoted directly into `README.md`.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the public product framing itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched README product-surface framing.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T00:22:36Z
Basis: Ralph packet `packet:ralph-ticket-readme11-20260503T001418Z`; evidence
`evidence:readme-product-surface-framing-validation`; oracle critique
`critique:readme-product-surface-framing-review` with no findings.
Residual risks: public-reader clarity is judgment-based; no user comprehension
test was performed.

# Dependencies

- `ticket:routewf10`
- `ticket:phsafe8`
- `ticket:critrec9`

# Journal

- 2026-05-02T22:03:13Z: Created from council finding `NC-011`.
- 2026-05-03T00:14:18Z: Moved to `active` and compiled
  `packet:ralph-ticket-readme11-20260503T001418Z` for bounded README
  product-surface framing cleanup.
- 2026-05-03T00:16:25Z: Ralph child updated `README.md`, recorded
  `evidence:readme-product-surface-framing-validation`, and moved ticket to
  `review_required` for mandatory oracle critique.
- 2026-05-03T00:19:24Z: Parent accepted bounded Ralph output, marked
  `packet:ralph-ticket-readme11-20260503T001418Z` consumed, and kept ticket in
  `review_required` pending mandatory oracle critique.
- 2026-05-03T00:22:36Z: Mandatory oracle critique
  `critique:readme-product-surface-framing-review` passed with no findings.
  Parent recorded retrospective / promotion disposition and accepted closure.
