---
id: critique:core-playbooks-constitutional-decision-review
kind: critique
status: final
created_at: 2026-05-07T21:38:23Z
updated_at: 2026-05-07T21:38:23Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "decision:0008 and related constitutional product-surface reconciliation"
links:
  decision:
    - decision:0008
    - decision:0006
    - decision:0005
    - decision:0007
  plan:
    - plan:split-core-and-playbooks-packages
  research:
    - research:core-workflow-plugin-split-feasibility
  initiative:
    - initiative:loom-install-experience
external_refs: {}
---

# Summary

Reviewed the constitutional decision that replaces the single root `skills/`
product surface with `loom-core/` and `loom-playbooks/`, plus the related
reconciliation edits to `constitution:main`, `decision:0005`, `decision:0006`,
`decision:0007`, the split plan, install research, and install initiative links.

# Review Target

Direct artifact critique of:

- `.loom/constitution/decisions/decision-0008-core-and-playbooks-package-roots.md`
- `.loom/constitution/constitution.md`
- `.loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md`
- `.loom/constitution/decisions/decision-0006-skills-only-product-surface-native-adapters.md`
- `.loom/constitution/decisions/decision-0007-positive-skill-surface-over-counterexample-calibration.md`
- `.loom/plans/20260507-split-core-and-playbooks-packages.md`
- `.loom/research/core-workflow-plugin-split-feasibility.md`
- `.loom/research/loom-install-distribution-methods.md`
- `.loom/initiatives/loom-install-experience.md`

The review used the `protocol-change` and `operator-surface` lenses because this
changes Loom's product authority and future install guidance.

# Verdict

`pass`

The constitutional decision is explicit, citable, and constraining. It states the
new package roots, core/playbook membership, dependency boundary, rejected routes,
and supersession of the prior single-root product-surface decision. Related active
constitutional records were reconciled enough to prevent a future agent from
treating root `skills/` as the active product surface.

# Findings

None - no findings.

# Evidence Reviewed

- Read `decision:0008` for required decision sections, package-root policy,
  alternatives, consequences, revisit conditions, and supersession language.
- Read the diff for `.loom/constitution`, the split plan, split research, install
  research, and install initiative link reconciliation.
- Checked decision frontmatter for `id`, `kind`, `status`, `created_at`, and
  `updated_at` fields.
- Checked `decision:0008` has the expected major decision sections.
- Checked the split plan still has required plan sections after linking
  `decision:0008`.
- Searched `.loom/constitution` for stale active claims that the product surface
  is top-level `skills/`; the remaining direct stale statement is inside
  `decision:0006`, which now has `status: superseded` and an explicit
  supersession note.
- Searched `.loom/constitution` for stale Codex hook claims from the older
  `decision:0005` rationale and found none after reconciliation.

# Residual Risks

- Public docs, AGENTS guidance, package manifests, examples, and actual directory
  layout still need downstream implementation work before the repository matches
  `decision:0008`.
- Existing root `skills/` still exists physically until migration tickets execute.
- Gemini two-extension behavior and Codex installed-plugin hook behavior remain
  evidence gaps, as the decision and plan state.

# Required Follow-up

No follow-up is required before accepting the constitutional decision itself.
Downstream implementation should proceed through the active split plan and create
bounded tickets for contract, doctrine decoupling, package-root moves, harness
surfaces, docs, evidence, and final critique.

# Acceptance Recommendation

`no-critique-blockers`
