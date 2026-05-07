---
id: critique:gemini-extension-route-review
kind: critique
status: final
created_at: 2026-05-07T23:07:49Z
updated_at: 2026-05-07T23:07:49Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:sbzmrvqv Gemini extension distribution route"
links:
  ticket:
    - ticket:sbzmrvqv
  evidence:
    - evidence:gemini-extension-local-link-route-check
  spec:
    - spec:core-and-playbooks-package-contract
  research:
    - research:gemini-extension-subdirectory-feasibility
  plan:
    - plan:split-core-and-playbooks-packages
external_refs: {}
---

# Summary

Reviewed the Gemini distribution route disposition for the core/playbooks package
split, focusing on operator-surface clarity and package-metadata evidence
sufficiency.

# Review Target

Target: `ticket:sbzmrvqv`, its linked evidence
`evidence:gemini-extension-local-link-route-check`, governing Gemini research,
and the relevant `spec:core-and-playbooks-package-contract#ACC-006` contract.

This review was required because Gemini install guidance is an operator-facing
release surface and an incorrect install claim would mislead users.

# Verdict

`pass`

The ticket now makes a narrow, supportable route disposition: Gemini is locally
linkable from explicit `loom-core/` and `loom-playbooks/` package roots, while
remote/repository-root Gemini install remains deferred until a separate source is
validated or upstream subdirectory install support exists. The ticket no longer
overclaims full public-docs cleanup for `ACC-006`.

# Findings

None - no findings.

# Evidence Reviewed

- `ticket:sbzmrvqv`
- `evidence:gemini-extension-local-link-route-check`
- `research:gemini-extension-subdirectory-feasibility`
- `spec:core-and-playbooks-package-contract#REQ-012`
- `spec:core-and-playbooks-package-contract#SCN-007`
- `spec:core-and-playbooks-package-contract#ACC-006`
- `plan:split-core-and-playbooks-packages`
- `INSTALL.md:154-178`, inspected because it still contains stale root Gemini
  install guidance that downstream docs work must reconcile
- `git diff --check` for the changed Gemini ticket/evidence/research/plan/spec
  records, observed with no output before this critique record was written
- Targeted placeholder/stale-plan greps for the Gemini ticket and plan

# Residual Risks

- Public docs still contain stale root Gemini install guidance. This is acceptable
  for closing the route ticket only because public docs are explicitly out of
  scope and deferred to the plan's public documentation unit; it is not acceptable
  for release acceptance.
- No remote Gemini install source has been validated. The ticket disposition must
  remain remote-deferred unless future evidence proves a separate distribution
  route.
- Interactive Gemini context ordering is not validated beyond `gemini extensions
  list` showing the core context file.
- The evidence is tied to Gemini CLI `0.34.0`; newer Gemini CLI behavior should be
  rechecked before release docs are finalized.

# Required Follow-up

None before closing `ticket:sbzmrvqv` as a route-disposition ticket.

Before release acceptance, downstream public documentation work must replace the
stale root Gemini instructions with the route established here: explicit local
package-root linking and remote support deferred unless a validated remote source
exists.

# Acceptance Recommendation

`no-critique-blockers`

The ticket's acceptance gate may close the Gemini route-disposition slice if it
cites the local-link evidence, this critique, and the residual documentation and
remote-install risks as deferred to downstream release/documentation work.
