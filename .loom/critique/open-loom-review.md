---
id: critique:open-loom-review
kind: critique
status: final
created_at: 2026-04-25T20:15:06Z
updated_at: 2026-04-25T20:29:14Z
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
external_refs:
  opencode_source:
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/plugin/shared.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/test/plugin/trigger.test.ts
---

# Summary

Reviewed the `open-loom` OpenCode plugin, package metadata, install docs, fixture
notes, ticket reconciliation, and evidence for `ticket:6uy1rx20`.

`open-loom` is acceptable as a structural plugin validation surface, but not
ready for final OpenCode plugin-first install acceptance because real chat/TUI
hook invocation is still unvalidated.

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

`open-loom` may remain, and the record graph honestly distinguishes structural
evidence from full runtime acceptance. The ticket needs active follow-up before
closure or final supported-install recommendation.

# Findings

## FIND-001: Runtime rule-injection evidence is still acceptance-blocking

Severity: medium

Confidence: high

Disposition: open

Observation:

`open-loom` structurally matches current OpenCode source, the local hook check
works, and `opencode plugin file://... --global` detects a server target under a
temporary `HOME`. No real OpenCode chat/TUI/model request has proven that
`experimental.chat.system.transform` is invoked and that Loom rules reach the
actual system prompt.

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

Run one narrow runtime validation packet against OpenCode chat/TUI if feasible.
If that is not feasible, soften install wording and explicitly keep OpenCode
`instructions` as the supported rules fallback, not only the skills/commands
fallback.

Challenges:

Challenges any interpretation of `ticket:6uy1rx20` ordered-rule injection as
fully runtime-accepted. The current ticket and evidence correctly limit the
claim as structural/partial.

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

- OpenCode hook is experimental and may change.
- No real OpenCode chat/TUI/model request has validated system-prompt inclusion.
- Npm publication and package-manager installation are not validated.
- Skills and commands remain fallback-only.
- External source references use moving OpenCode `dev` branch URLs.

# Required Follow-up

Before acceptance or closure, either:

- run a narrow runtime validation packet that proves OpenCode invokes the hook in
  an actual chat/TUI path, or
- explicitly accept only the structural plugin validation and create linked follow-up
  work for runtime validation before recommending plugin-first OpenCode install
  as supported.

# Acceptance Recommendation

`active follow-up required`.

Move `ticket:6uy1rx20` back to `active` for runtime validation or wording
softening. Do not close the ticket yet.
