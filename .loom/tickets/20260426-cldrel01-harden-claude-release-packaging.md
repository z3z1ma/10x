---
id: ticket:cldrel01
kind: ticket
status: proposed
change_class: release-packaging
risk_class: medium
created_at: 2026-04-26T01:04:44Z
updated_at: 2026-04-26T01:04:44Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  research:
    - research:loom-install-distribution-methods
  wiki:
    - wiki:harness-adapter-package-pattern
  ticket:
    - ticket:q7h1d05q
  evidence:
    - evidence:claude-plugin-hybrid
  critique:
    - critique:claude-plugin-integration-review
depends_on: []
---

# Summary

Harden the accepted local/prototype Claude plugin integration for broad
marketplace-style distribution.

# Context

`ticket:q7h1d05q` accepted the Claude hybrid plugin as a local/prototype
integration. Its acceptance decision explicitly left release-packaging risks
outside that prototype: broad `source: "./"`, explicit cleanup rather than
uninstall lifecycle support, unproven installed-plugin skill/command invocation,
broad `loom@...` project-scope matching, and unproven Windows/non-bash support.

# Why Now

This ticket is proposed so those residual risks have one execution owner if the
project decides to recommend Claude marketplace distribution beyond local
prototype use.

# Scope

- decide whether Claude distribution needs a narrower package artifact instead of
  marketplace source `./`
- inspect or validate marketplace cache contents for the chosen package source
- validate runtime skill and command invocation from an installed marketplace
  plugin, not only from `--plugin-dir`
- decide whether project-scope detection should require exact `loom@agent-loom`
  identity instead of broad `loom@...`
- decide the cleanup UX for plugin disable/uninstall in the absence of a Claude
  uninstall hook
- decide whether POSIX shell hooks are acceptable for supported Claude platforms or
  whether a cross-platform helper is required
- update install docs, fixture notes, evidence, and critique if the prototype is
  promoted to release-grade distribution

# Non-goals

- do not reopen the local/prototype acceptance from `ticket:q7h1d05q`
- do not replace Loom always-on rules with a Claude custom agent
- do not make generated Claude rule files canonical Loom source

# Acceptance Criteria

- package source and cache contents are validated or intentionally constrained
- installed marketplace plugin skills and commands are exercised or the gap is
  explicitly accepted with rationale
- project-scope matching behavior is narrowed or explicitly accepted as broad
- cleanup behavior for disable/uninstall is documented and validated as far as
  Claude supports
- platform support for hook scripts is stated truthfully
- release docs distinguish local/prototype install from broad marketplace
  distribution

# Coverage

Covers:

- None - no spec-owned acceptance IDs exist. This ticket owns the release
  hardening questions left by `ticket:q7h1d05q`.

# Claim Matrix

| Claim | Coverage | Evidence | Notes |
| --- | --- | --- | --- |
| Claude local/prototype hybrid integration is accepted. | supported | `ticket:q7h1d05q`, `evidence:claude-plugin-hybrid`, `critique:claude-plugin-integration-review` | This ticket must not relitigate local/prototype acceptance. |
| Claude marketplace source `./` is release-ready. | pending | None | Requires cache-content audit or narrower package decision. |
| Installed marketplace plugin skills/commands work at runtime. | pending | None | Local prototype validated rules and install shape, not installed-plugin skill/command invocation. |

# Blockers

None. This ticket is proposed future work, not an active blocker.

# Next Move / Next Route

Promote to `ready` only if the project decides to pursue Claude distribution
beyond local/prototype use.

# Ralph Readiness

Not Ralph-ready yet. The first step is a release-packaging scoping pass that
decides package source shape and validation target.

# Evidence

Evidence so far:

- `evidence:claude-plugin-hybrid`
- `critique:claude-plugin-integration-review`

Expected evidence:

- marketplace cache-content inspection
- installed plugin runtime skill/command invocation proof or accepted limitation
- cleanup/disable validation or documented unsupported lifecycle
- platform support validation or explicit platform limitation

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:
Release packaging can mislead operators if local/prototype constraints are
presented as broad marketplace guarantees.

Findings:

None - no critique yet.

Disposition status: pending

# Wiki Disposition

`wiki:harness-adapter-package-pattern` now records the accepted Claude hybrid
pattern and links this follow-up as the release-hardening owner.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

Related to closed `ticket:q7h1d05q`; no hard dependency blocks proposing this
future work.

# Journal

- 2026-04-26: created during Claude effort retrospective to keep release-grade
  residual risks from living only in the closed prototype ticket or chat.
