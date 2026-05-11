---
id: critique:gemini-root-core-shim-review
kind: critique
status: final
created_at: 2026-05-07T23:24:15Z
updated_at: 2026-05-07T23:24:15Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:mbkqbkgq Gemini root core shim"
links:
  ticket:
    - ticket:mbkqbkgq
  evidence:
    - evidence:gemini-root-core-shim-check
  decision:
    - decision:0009
  spec:
    - spec:core-and-playbooks-package-contract
  plan:
    - plan:split-core-and-playbooks-packages
external_refs: {}
---

# Summary

Reviewed the Gemini root core shim implementation, product-surface exception, and
targeted install documentation update.

# Review Target

Target: `ticket:mbkqbkgq`, root `gemini-extension.json`, root
`gemini-bootstrap.md`, root `skills` symlink to `loom-core/skills`, targeted
`INSTALL.md` Gemini instructions, `decision:0009`, spec/plan/research
reconciliation, and `evidence:gemini-root-core-shim-check`.

Profiles: `protocol-change`, `operator-surface`, and `package-metadata`.

# Verdict

`pass`

The implementation matches the accepted exception: root Gemini install validates
and installs as `loom-core`, exposes the root bootstrap context and core skills,
does not expose playbook skills, and the targeted install docs state that clone and
explicit package-root links remain preferred for full installs. The root `skills`
surface is documented as a Gemini shim exception rather than reinstated as the
general product surface.

# Findings

None - no findings.

# Evidence Reviewed

- `decision:0009`
- `ticket:mbkqbkgq`
- `evidence:gemini-root-core-shim-check`
- `spec:core-and-playbooks-package-contract#REQ-006`
- `spec:core-and-playbooks-package-contract#REQ-012`
- `spec:core-and-playbooks-package-contract#REQ-016`
- `spec:core-and-playbooks-package-contract#ACC-006`
- `spec:core-and-playbooks-package-contract#ACC-009`
- `INSTALL.md:154-217`
- Root `gemini-extension.json`
- Root `gemini-bootstrap.md`
- Root `skills` symlink target check: `skills -> loom-core/skills`
- `node` JSON parse check for Gemini manifests
- `gemini extensions validate "$PWD"`
- `gemini extensions install "$PWD" --consent`
- `gemini extensions list`
- `git diff --check` for tracked changed records/docs
- `git diff --check --no-index` for new root Gemini files

# Residual Risks

- Remote GitHub root install is not directly validated until these changes exist on
  the remote branch. Local path install is a strong proxy for source-root behavior
  but not a remote fetch test.
- Gemini root skill discovery depends on symlink behavior. The local CLI follows
  the symlink; archive-based or non-POSIX distribution may need separate evidence.
- `INSTALL.md` still has other non-Gemini sections from the older single-root docs;
  this ticket intentionally targeted Gemini only. Full public docs cleanup remains
  a downstream release-documentation task.
- The root shortcut and package-root `loom-core` link use the same Gemini extension
  name. The docs now warn users to choose one core route, but this should be
  rechecked if Gemini changes extension identity behavior.

# Required Follow-up

None before closing `ticket:mbkqbkgq`.

Before release acceptance, run the broader public documentation ticket and recheck
remote GitHub root install after the root shim is available remotely.

# Acceptance Recommendation

`no-critique-blockers`

The ticket acceptance gate may close the Gemini root core shim slice with the
residual risks recorded above.
