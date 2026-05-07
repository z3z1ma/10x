---
id: critique:core-playbooks-package-contract-review
kind: critique
status: final
created_at: 2026-05-07T21:44:08Z
updated_at: 2026-05-07T21:44:08Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "spec:core-and-playbooks-package-contract"
links:
  spec:
    - spec:core-and-playbooks-package-contract
    - spec:opencode-plugin-install-contract
  decision:
    - decision:0008
  plan:
    - plan:split-core-and-playbooks-packages
  research:
    - research:core-workflow-plugin-split-feasibility
  initiative:
    - initiative:loom-install-experience
external_refs: {}
---

# Summary

Reviewed the full spec defining the `loom-core` and `loom-playbooks` package
contract, including requirements, scenarios, acceptance coverage, evidence plan,
and reconciliation of the older OpenCode single-package spec.

# Review Target

Direct artifact critique of `.loom/specs/core-and-playbooks-package-contract.md`.

The review used `protocol-change`, `operator-surface`, and `evidence sufficiency`
lenses because the spec constrains package layout, install claims, and downstream
ticket acceptance.

# Verdict

`pass`

The spec is precise enough for downstream tickets to implement the package split
without re-litigating the boundary. Requirements use stable IDs, scenarios cover
core-only, full, missing-core, catalog, OpenCode, Codex, Gemini, and stale-path
cases, and acceptance criteria are mapped to evidence targets. The prior active
OpenCode single-package spec was marked superseded, which avoids conflicting
active intended-behavior owners.

# Findings

None - no findings.

# Evidence Reviewed

- Read `spec:core-and-playbooks-package-contract` for full spec sections,
  normative requirements, scenarios, acceptance IDs, coverage table, evidence
  plan, assumptions, and open questions.
- Checked the spec has stable `REQ-*`, `SCN-*`, and `ACC-*` IDs.
- Checked placeholder and trailing-whitespace scans on the new spec.
- Checked plan and initiative links now reference the new spec.
- Checked `spec:opencode-plugin-install-contract` was changed to `status:
  superseded` with a supersession note pointing to the new contract and
  `decision:0008`.

# Residual Risks

- The source tree has not yet been migrated; the spec defines intended behavior,
  not current implementation reality.
- OpenCode split package details still need their own implementation/evidence
  ticket.
- Codex installed-plugin hooks and Gemini two-extension behavior remain evidence
  gates, correctly represented as requirements that block claims rather than the
  package layout.

# Required Follow-up

No follow-up is required before downstream tickets cite this spec. Implementation
tickets should cite relevant `ACC-*` IDs and preserve evidence for package tree,
membership, harness metadata, OpenCode smoke checks, Codex/Gemini runtime gates,
and stale path reconciliation.

# Acceptance Recommendation

`no-critique-blockers`
