---
id: critique:open-loom-review
kind: critique
status: final
created_at: 2026-04-25T20:15:06Z
updated_at: 2026-04-25T21:29:31Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: open-loom OpenCode plugin working tree change for ticket:6uy1rx20
links:
  ticket:
    - ticket:6uy1rx20
  packet:
    - packet:ralph-ticket-6uy1rx20-20260425T195559Z
    - packet:critique-ticket-6uy1rx20-open-loom-20260425T201112Z
  evidence:
    - evidence:open-loom-smoke
  follow_up_critique:
    - critique:open-loom-config-hook-review
external_refs:
  opencode_source:
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/plugin/shared.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/test/plugin/trigger.test.ts
---

# Summary

Reviewed the `open-loom` OpenCode plugin, package metadata, install docs, fixture
notes, ticket reconciliation, and evidence for `ticket:6uy1rx20`.

This critique reviewed the earlier chat-transform implementation. That
implementation has been superseded by the current `config(config)` implementation
recorded in `evidence:open-loom-smoke`.

# Review Target

Working tree change from the first OpenCode Ralph implementation iteration:

- `package.json`
- `open-loom.mjs`
- `examples/adapters/open-loom-install/README.md`
- `INSTALL.md`
- `ticket:6uy1rx20`
- `evidence:open-loom-smoke`
- OpenCode section of `research:loom-install-distribution-methods`

The critique used profiles `operator-clarity`, `code-change`, and
`test-coverage`.

# Verdict

`pass_with_findings`.

The original review findings are resolved or superseded. The corrected
`config(config)` implementation should receive focused review before npm
publication.

# Findings

## FIND-001: Runtime rule-injection evidence is still acceptance-blocking

Severity: medium

Confidence: high

Disposition: resolved by implementation replacement

Observation:

The reviewed implementation structurally matched current OpenCode source, the
local hook check worked, and `opencode plugin file://... --global` detected a
server target under a temporary `HOME`. No real OpenCode chat/TUI/model request
had proven that `experimental.chat.system.transform` was invoked and that Loom
rules reached the actual system prompt.

Disposition update:

The current `open-loom` implementation no longer uses
`experimental.chat.system.transform` for Loom rules. It uses OpenCode's
`config(config)` hook to register ordered rule files through `config.instructions`,
which is OpenCode's documented instruction-file surface. `evidence:open-loom-smoke`
records `opencode debug config` and `opencode debug skill` validation for this
route.

References:

- `INSTALL.md`
- `examples/adapters/open-loom-install/README.md`
- `ticket:6uy1rx20`
- `evidence:open-loom-smoke`

Why it matters:

The docs give actionable local plugin-entry guidance. Without runtime hook
validation, operators may interpret the plugin entry as a supported always-on
Loom install when only structural behavior and CLI server-target detection are
proven.

Follow-up:

Resolved by replacing the route with `config.instructions`. A fresh focused review
should inspect the corrected `config(config)` implementation before npm
publication.

Challenges:

No longer challenges the current `config.instructions` claim. The finding applies
to the superseded chat-transform implementation.

## FIND-002: Optional command surface was treated as present by helper discovery

Severity: low

Confidence: medium-high

Disposition: resolved

Observation:

The first `open-loom` version had `inspectLoomBundle()` unconditionally read the
`commands/` directory. Current repository and package metadata include
`commands/`, so the smoke check passed, but Loom describes commands as optional
wrapper surfaces.

References:

- `open-loom.mjs`
- `INSTALL.md`
- `examples/adapters/open-loom-install/README.md`

Why it matters:

If a future OpenCode package trims commands or a local clone omits them, helper
inspection should not accidentally make optional commands a runtime requirement.

Follow-up:

Resolved in parent reconciliation by making the plugin tolerate missing
`commands/` and `skills/` directories during bundle inspection. The parent ran a
Node check showing a temporary bundle with one skill and no commands returns
`commandCount: 0` instead of failing.

Challenges:

None - no current claim was false; this was a plugin robustness issue.

# Evidence Reviewed

- Critique packet `packet:critique-ticket-6uy1rx20-open-loom-20260425T201112Z`
- Ralph packet `packet:ralph-ticket-6uy1rx20-20260425T195559Z`
- `open-loom.mjs`
- `package.json`
- `INSTALL.md`
- `examples/adapters/open-loom-install/README.md`
- `ticket:6uy1rx20`
- `evidence:open-loom-smoke`
- OpenCode section of `research:loom-install-distribution-methods`
- `node open-loom.mjs --smoke`
- import/default-export/hook-shape Node check
- temporary-home `opencode plugin file://... --global` output
- `git diff --check`

# Residual Risks

- OpenCode plugin APIs may change.
- No real model request has validated downstream provider payload inclusion, but
  `config.instructions` is the documented config surface OpenCode uses for
  instruction files.
- Npm publication and package-manager installation are not validated.
- Skills and commands now route through `config.skills.paths` and
  `config.command`; package publication remains unvalidated.
- External source references use moving OpenCode `dev` branch URLs.

# Required Follow-up

Before npm publication, run a focused review of the corrected `config(config)`
implementation and re-run package checks.

# Acceptance Recommendation

`superseded by follow-up review`.

The original findings are resolved or superseded. The corrected `config(config)`
implementation was reviewed in `critique:open-loom-config-hook-review`.
