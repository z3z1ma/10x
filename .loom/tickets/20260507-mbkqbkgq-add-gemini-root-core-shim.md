---
id: ticket:mbkqbkgq
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-07T23:20:14Z
updated_at: 2026-05-07T23:24:15Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:split-core-and-playbooks-packages
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0008
    - decision:0009
  research:
    - research:gemini-extension-subdirectory-feasibility
  ticket:
    - ticket:sbzmrvqv
  evidence:
    - evidence:gemini-root-core-shim-check
  critique:
    - critique:gemini-root-core-shim-review
external_refs: {}
depends_on:
  - ticket:sbzmrvqv
---

# Summary

Add a Gemini-specific repository-root core shim so `gemini extensions install` from
the repository root installs Loom core only, while docs continue to prefer clone
and explicit package-root links for full core plus playbooks installs.

# Context

`ticket:sbzmrvqv` closed with Gemini local package-root linking supported and
remote/repository-root install deferred. The operator has now accepted a
Gemini-only third install surface because Gemini tooling and crawlers index root
`gemini-extension.json` files.

`decision:0009` records the policy exception: the root Gemini extension may expose
core only, must not imply playbook installation, and must not become a general
root product surface.

# Scope

In:

- Add root Gemini extension metadata for core-only installation.
- Add root Gemini bootstrap context that loads using-Loom doctrine from
  `loom-core`.
- Add the smallest root core-skill exposure needed for Gemini root extension skill
  discovery without duplicating core files.
- Update `INSTALL.md` Gemini instructions to prefer clone/link, state root install
  is core-only, and avoid claiming playbook remote install.
- Update governing plan/spec/research records to reflect the Gemini root core shim
  exception.
- Validate root Gemini install from a temporary Gemini home and preserve evidence.
- Run mandatory critique before closure.

Out:

- Making root Gemini install include playbooks.
- Publishing Gemini release artifacts or creating separate distribution repos.
- Adding Gemini hooks for static using-Loom preload.
- Reintroducing a full root `skills/` compatibility bundle as a product surface.
- Updating README, ARCHITECTURE, PROTOCOL, AGENTS, or examples beyond the targeted
  `INSTALL.md` Gemini instructions.
- Changing non-Gemini harness package surfaces.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| A root `skills` shim may point at `loom-core/skills` for Gemini skill discovery. | yes | yes | accepted by `decision:0009` if validation proves Gemini sees core skills |
| Root Gemini install should use extension name `loom-core`. | yes | no | accepted unless validation shows a conflict |
| Clone/link remains the recommended full Gemini install path. | yes | no | accepted by operator and `decision:0009` |
| Symlink behavior does not survive Gemini install/copy. | yes | yes | use docs-only core context or choose a different shim before closure |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-006 — Gemini root core install and
  docs claim only the validated behavior.
- spec:core-and-playbooks-package-contract#ACC-009 — root Gemini shim exposes core
  only and keeps playbooks explicit.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Closed. Root Gemini shim implementation and install docs are in place; evidence
shows local root install exposes core context/skills only, and mandatory critique
passed with no findings.

Blockers:

- None.

Execution notes:

- Keep the root shim Gemini-specific and core-only.
- Do not copy core skills into a second root tree if a symlink works.
- Do not let install docs imply root install includes playbooks.
- Use a temporary Gemini home for validation.

Continuation note:

No action remains for this ticket. Remote GitHub root install should be rechecked
after these changes are published.

# Evidence

Disposition: sufficient

Records:

- evidence:gemini-root-core-shim-check

Gaps / limits:

- Local repository-root install validates the root shim and core-only skill set.
- Remote GitHub install is not validated until the changes exist in a remote source;
  local path install is the current proxy.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: This is a high-risk product-surface exception and changes
operator-facing install instructions.
Critique disposition: completed

Required critique profiles:

- protocol-change
- operator-surface
- package-metadata

Findings:

- No open findings in `critique:gemini-root-core-shim-review`.

Promotion disposition: deferred
Promotion / deferral rationale: Broader public docs cleanup and release notes remain
downstream plan units. The targeted Gemini install guidance was updated in
`INSTALL.md`.

Promoted / deferred:

- Deferred to public documentation and release-posture tickets.

Wiki disposition: not_required

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent
Accepted at: 2026-05-07T23:24:15Z
Basis: `decision:0009` authorizes the Gemini-only root core shim;
`evidence:gemini-root-core-shim-check` shows local root validation/install/list
behavior with core context/skills only; `critique:gemini-root-core-shim-review`
recommends no critique blockers.
Residual risks: Remote GitHub root install is not directly validated until these
changes are published. Root skill discovery depends on symlink behavior. Broader
non-Gemini public docs remain stale pending the public documentation ticket.

# Dependencies

Depends on `ticket:sbzmrvqv` because that ticket established the current Gemini
subdirectory limitation and local-link evidence.

# Journal

- 2026-05-07T23:20:14Z: Created after the operator accepted a Gemini-specific root
  core shim to support root `gemini-extension.json` indexing and core-only install.
- 2026-05-07T23:22:25Z: Added root `gemini-extension.json`, root
  `gemini-bootstrap.md`, and root `skills` symlink to `loom-core/skills`; recorded
  `evidence:gemini-root-core-shim-check` showing local Gemini root install exposes
  core only.
- 2026-05-07T23:22:25Z: Added install-doc warning to choose either the root core
  shortcut or the `loom-core` package-root link, not both, because both use the
  `loom-core` extension name.
- 2026-05-07T23:24:15Z: Mandatory critique
  `critique:gemini-root-core-shim-review` passed with no findings; closed the
  Gemini root core shim ticket with remote GitHub install recheck deferred until
  these changes are published.
