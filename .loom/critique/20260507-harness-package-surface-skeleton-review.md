---
id: critique:harness-package-surface-skeleton-review
kind: critique
status: final
created_at: 2026-05-07T22:34:47Z
updated_at: 2026-05-07T22:34:47Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:7h8u6oxp harness package surface skeleton"
links:
  ticket:
    - ticket:7h8u6oxp
  packet:
    - packet:ralph-ticket-7h8u6oxp-20260507T222124Z
  evidence:
    - evidence:harness-package-surface-skeleton-check
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0008
external_refs: {}
---

# Summary

Reviewed the common non-OpenCode native harness package skeleton after package-root
metadata was added for Claude, Codex, Cursor, and Gemini and root catalogs were
updated to list `loom-core` and `loom-playbooks`.

# Review Target

Direct implementation critique of `ticket:7h8u6oxp`, Ralph packet
`packet:ralph-ticket-7h8u6oxp-20260507T222124Z`, evidence
`evidence:harness-package-surface-skeleton-check`, and current source surfaces:

- `.claude-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`
- `.cursor-plugin/marketplace.json`
- package-root Claude, Codex, Cursor, and Gemini manifests
- `loom-core/claude-hooks/hooks.json`
- `loom-core/gemini-bootstrap.md`

Profiles: `protocol-change`, `operator-surface`, and `package-metadata`.

# Verdict

`pass_for_scoped_acceptance`

No open medium/high findings remain for the scoped structural harness-skeleton
ticket.

# Findings

No open findings.

# Follow-up Review Notes

An initial critique found a medium-severity Cursor root discovery gap: package-root
Cursor manifests existed, but no root `.cursor-plugin/marketplace.json` listed the
two package roots. The follow-up added `.cursor-plugin/marketplace.json`, and the
final review verified it lists both roots:

- `.cursor-plugin/marketplace.json` lists `loom-core` with source `loom-core`.
- `.cursor-plugin/marketplace.json` lists `loom-playbooks` with source
  `loom-playbooks`.

# Evidence Reviewed

- `decision:0008`
- `plan:split-core-and-playbooks-packages`, especially Unit: Rebuild Harness
  Package Surfaces
- `spec:core-and-playbooks-package-contract#ACC-004`, `#ACC-006`, and scoped
  `#ACC-007`
- `research:core-workflow-plugin-split-feasibility`
- `research:codex-plugin-distribution-surfaces`
- `ticket:7h8u6oxp`
- Ralph packet `packet:ralph-ticket-7h8u6oxp-20260507T222124Z`
- `evidence:harness-package-surface-skeleton-check`
- Root catalogs for Claude, Codex, and Cursor
- Package-root manifests for Claude, Codex, Cursor, and Gemini
- Core Claude hook and Gemini bootstrap files
- Fresh read-only structural checks: JSON parse for 12 current JSON files and
  scoped `git diff --check` with no output

# Residual Risks

- This is structural evidence only; Claude, Codex, Cursor, Gemini, OpenCode, and
  generic harness runtime install/discovery behavior remain unvalidated.
- Codex installed-plugin preload and Gemini two-extension support remain deferred
  evidence needs.
- OpenCode split, public docs/examples, release packaging, and global `ACC-007`
  cleanup remain out of this ticket's scope.
- New package-root files and new root Cursor marketplace file are untracked until
  staging/commit review includes them.

# Required Follow-up

No follow-up is required before scoped ticket acceptance. Later tickets still need
to own runtime validation, OpenCode packages, and public docs/examples.

# Acceptance Recommendation

`accept_scoped_ticket`
