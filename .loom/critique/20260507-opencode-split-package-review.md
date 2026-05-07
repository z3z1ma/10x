---
id: critique:opencode-split-package-review
kind: critique
status: final
created_at: 2026-05-07T22:47:28Z
updated_at: 2026-05-07T22:47:28Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:xtt24452 OpenCode split packages"
links:
  ticket:
    - ticket:xtt24452
  packet:
    - packet:ralph-ticket-xtt24452-20260507T223743Z
  evidence:
    - evidence:opencode-split-package-check
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0008
external_refs: {}
---

# Summary

Reviewed the OpenCode package split after `open-loom-core` and
`open-loom-playbooks` package roots were added, the repository root package was
made private/non-published, and playbooks metadata was updated to state its
`open-loom-core` dependency.

# Review Target

Direct implementation critique of `ticket:xtt24452`, Ralph packet
`packet:ralph-ticket-xtt24452-20260507T223743Z`, evidence
`evidence:opencode-split-package-check`, and source changes to root/package-root
OpenCode package files.

Profiles: `protocol-change`, `operator-surface`, `package-metadata`, and
`code-structure`.

# Verdict

`pass_for_scoped_acceptance`

No open medium/high findings remain for the scoped OpenCode split package ticket.

# Findings

No open findings.

# Follow-up Review Notes

An initial critique found that `loom-playbooks/package.json` did not state the
core package dependency clearly enough. The follow-up added both:

- description text naming `open-loom-core`
- `peerDependencies.open-loom-core: ^0.1.10`

The final critique verified that the dependency signal is present and that the
evidence now avoids overstating `git diff --check` coverage for untracked
package-root files.

# Evidence Reviewed

- `decision:0008`
- `plan:split-core-and-playbooks-packages`, especially Unit: Split OpenCode
  Packages
- `spec:core-and-playbooks-package-contract#REQ-010`, `#REQ-015`, `#ACC-005`, and
  scoped `#ACC-007`
- `ticket:xtt24452`
- Ralph packet `packet:ralph-ticket-xtt24452-20260507T223743Z`
- `evidence:opencode-split-package-check`
- `package.json`
- deleted root `open-loom.mjs`
- `loom-core/package.json`
- `loom-core/open-loom-core.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/open-loom-playbooks.mjs`
- Fresh smoke checks for both package modules and scoped `git diff --check`

# Residual Risks

- No real OpenCode install/plugin-array validation was performed.
- `peerDependencies` states the package dependency but does not itself guarantee
  OpenCode will load/register core; docs/operator config remain later-scope work.
- Public docs, examples, release packaging, and final stale-reference cleanup remain
  later-ticket scope.
- New package-root OpenCode files are untracked until staging/commit review includes
  them.

# Required Follow-up

No follow-up is required before scoped ticket acceptance. Later tickets still need
to own runtime validation, public docs/examples, and final release-posture review.

# Acceptance Recommendation

`accept_scoped_ticket`
