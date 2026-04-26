---
id: ticket:jt2vy25y
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-04-26T06:35:59Z
updated_at: 2026-04-26T07:23:57Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  decision:
    - decision:0005
    - decision:0006
  evidence:
    - evidence:bootstrap-skill-package-validation
    - evidence:codex-sessionstart-stdout-context
  critique:
    - critique:bootstrap-skill-package-review
  related:
    - ticket:lx9nnztk
    - ticket:cldrel01
    - ticket:6uy1rx20
depends_on: []
---

# Summary

Repackage Loom's mandatory bootstrap doctrine as a `loom-bootstrap` skill and make
`skills/` the only supported product surface across Codex, Claude, OpenCode,
Cursor, Gemini, and future harnesses.

# Context

The Codex remote install work showed that a plugin can package Loom skills but
does not currently source-provenly install always-on rule hooks. The operator
clarified the product goal: remote users should be able to add Loom as a plugin
or skill package with minimal extra setup. Moving the mandatory doctrine into a
bootstrap skill makes skills the primary package surface while preserving optional
always-on adapter preloading as a bonus.

# Why Now

This unblocks a simpler cross-harness story: install Loom through each harness's
native skill or plugin system, use `loom-bootstrap` first, and optionally preload
the same references when the harness supports it cleanly.

# Scope

- create a new `skills/loom-bootstrap` skill
- move the seven top-level rule files into `skills/loom-bootstrap/references/`
- update package/adapters to read those references instead of `rules/`
- remove the fallback Makefile, shell installer, and top-level command-wrapper
  product surfaces
- update public docs and constitutional framing for skill-packaged bootstrap
  doctrine
- preserve historical evidence records as historical where they describe old
  probes
- validate structural JSON, plugin smoke checks, and reference/path drift

# Non-goals

- do not add a runtime, daemon, MCP, or product CLI
- do not make adapter-generated instruction files canonical truth
- do not remove task-specific Loom skills
- do not claim remote plugin installs preload always-on context unless that is
  separately evidenced by the harness
- do not rewrite historical evidence to pretend old probes used new paths
- do not preserve fallback installers as supported distribution paths

# Acceptance Criteria

- `loom-bootstrap` exists with a mandatory first-use description and ordered
  references
- all canonical bootstrap doctrine lives under `skills/loom-bootstrap/references/`
- top-level `rules/` is no longer the canonical product surface
- install docs describe Loom as a skills package with bootstrap references
- Claude/Codex hook fixtures and OpenCode plugin code reference bootstrap
  references instead of `rules/`
- Makefile, shell installer, and top-level command-wrapper surfaces are removed
- constitutional decision records the policy shift
- validation covers JSON shape, OpenCode smoke output, and stale product path
  references
- critique is required before closure because this is a protocol-authority change

# Coverage

Covers:

- None - no spec-owned acceptance IDs exist. This ticket owns ticket-local
  acceptance for the bootstrap packaging mutation.

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| Loom can be distributed as a skill package with `loom-bootstrap` as mandatory entry point. | `evidence:bootstrap-skill-package-validation` | `critique:bootstrap-skill-package-review` | supported |
| Always-on adapter preload remains optional bonus, not canonical requirement. | `evidence:bootstrap-skill-package-validation`, `evidence:codex-sessionstart-stdout-context` | `critique:bootstrap-skill-package-review` | supported |
| Top-level `rules/` is retired as canonical product surface. | `evidence:bootstrap-skill-package-validation` | `critique:bootstrap-skill-package-review` | supported |
| Makefile, shell installer, and top-level command wrappers are removed as product surfaces. | `evidence:bootstrap-skill-package-validation` | `critique:bootstrap-skill-package-review` | supported |

# Execution Notes

Decision owners: `decision:0005`, `decision:0006`.

Primary product files affected: `skills/loom-bootstrap/`, `README.md`,
`PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, `AGENTS.md`, `open-loom.mjs`,
`package.json`, `hooks/hooks.json`, `.codex/hooks.json`, plugin manifests, and
adapter examples.

# Blockers

None.

# Next Move / Next Route

Closed after local edit, structural validation, mandatory critique, record
reconciliation, and acceptance disposition.

# Ralph Readiness

Not using Ralph for this pass; the operator asked to proceed and the change is
being made locally with direct validation.

# Evidence

Observed:

- `git diff --check`
- JSON validation for plugin/hook manifests
- `node open-loom.mjs --smoke`
- targeted searches for stale product references to `rules/`
- `npm pack --dry-run`
- `claude plugin validate`
- `npm pack --dry-run` package contents include `skills/` and exclude top-level
  `rules/`, `commands/`, Makefile, and shell installer surfaces

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale:

This changes Loom's bootstrap authority and package model.

Required critique profiles:

- protocol-change
- operator-clarity
- release-packaging

Findings:

`critique:bootstrap-skill-package-review` found stale fallback installer,
command-wrapper, and active record references. Follow-up edits removed the
Makefile, shell installer, top-level commands, command registration from native
plugin paths, stale fallback examples, and superseded/reconciled active research
and spec records that still taught the old model.

Disposition status: completed; all high-severity findings for this ticket are
resolved. Remaining release validation risks are linked follow-ups.

Deferral / not-required rationale:

None.

# Wiki Disposition

Completed. `wiki:harness-adapter-package-pattern`,
`initiative:loom-install-experience`, `plan:install-experience-harness-adapters`,
and relevant research/spec records now describe native skills-package adapters and
do not preserve fallback installers as current product paths.

# Acceptance Decision

Accepted by: OpenCode agent implementing operator directive
Accepted at: 2026-04-26T07:23:57Z
Basis: `decision:0005`, `decision:0006`, `evidence:bootstrap-skill-package-validation`,
`critique:bootstrap-skill-package-review`, package dry-run contents, OpenCode
smoke output, Claude plugin validation, JSON validation, and stale-record blocker
review.
Residual risks: Codex installed Git-backed plugin skill discovery remains in
`ticket:lx9nnztk`; Claude broad-release runtime hardening remains in
`ticket:cldrel01`; legacy user-local files from removed installers may remain on
machines that used older install targets and are accepted as local state outside
the product surface.

# Dependencies

Inherits context from `initiative:loom-install-experience`,
`plan:install-experience-harness-adapters`, and Codex remote install ticket
`ticket:lx9nnztk`.

# Journal

- 2026-04-26: created after operator clarified that Loom should become primarily a
  package of skills with a mandatory initialization/bootstrap skill.
- 2026-04-26: operator clarified that fallback installers, Makefile, shell script,
  and top-level command-wrapper product surfaces should be removed; `decision:0006`
  records the skills-only native-adapter policy.
- 2026-04-26: closed after final blocker review passed; residual Codex and Claude
  release validations remain linked follow-up work rather than blockers for this
  product-surface decision.
