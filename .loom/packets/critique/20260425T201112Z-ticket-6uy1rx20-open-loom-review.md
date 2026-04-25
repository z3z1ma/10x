---
id: packet:critique-ticket-6uy1rx20-open-loom-20260425T201112Z
kind: packet
packet_kind: critique
status: consumed
target: ticket:6uy1rx20
review_target:
  kind: code_change
  diff: open-loom working tree changes
mode: review
change_class: release-packaging
style: reference-first
created_at: 2026-04-25T20:11:12Z
updated_at: 2026-04-25T20:29:14Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records: []
  paths: []
parent_merge_scope:
  records:
    - critique:open-loom-review
    - ticket:6uy1rx20
  paths: []
source_fingerprint:
  git_commit: b9bdc32c15aa166194a202a221c524cef7c81049
  git_status_summary: dirty
  compiled_from:
    - ticket:6uy1rx20
    - packet:ralph-ticket-6uy1rx20-20260425T195559Z
    - evidence:open-loom-smoke
execution_context:
  branch: main
  worktree: none
  isolation: none
  destructive_commands: forbidden
  network: allowed
context_budget:
  posture: normal
  max_source_files: 12
  max_excerpt_lines_per_file: 120
  avoid_full_file_reads: true
sources:
  ticket:
    - ticket:6uy1rx20
  packet:
    - packet:ralph-ticket-6uy1rx20-20260425T195559Z
  evidence:
    - evidence:open-loom-smoke
  research:
    - research:loom-install-distribution-methods
links: {}
---

# Mission

Review `open-loom` for correctness, scope discipline, evidence
sufficiency, and operator clarity before `ticket:6uy1rx20` can move toward
acceptance.

# Governing Context

The target ticket wants a plugin-first OpenCode install path where normal users
eventually add one npm package plugin entry and local users can point OpenCode at
a cloned-repo file/path plugin entry. Git URL plugin specs are not recommended.

The bounded Ralph iteration added:

- `package.json`
- `open-loom.mjs`
- `examples/adapters/open-loom-install/README.md`
- `INSTALL.md` plugin guidance

Parent reconciliation corrected the plugin to match current OpenCode source:

- default export object with `id` and `server()`
- `experimental.chat.system.transform` mutates `output.system: string[]`

Evidence exists at `evidence:open-loom-smoke`:

- `node open-loom.mjs --smoke` reads 7 ordered rule files, reports block
  markers, and discovers 20 skills and 19 commands
- import-based Node check validates default export and hook mutation shape
- OpenCode CLI `1.14.22` temporary-home `opencode plugin file://... --global`
  detects a server target and writes the config entry
- real chat/TUI hook invocation remains unvalidated

# Review Lens

Named critique profiles to apply:

- `operator-clarity`
- `code-change`
- `test-coverage`

# Change Class

Declared as `release-packaging`. The review should focus on whether the package
plugin can mislead operators, whether the OpenCode plugin shape is plausible
against current source, and whether evidence is sufficient for the claims now in
the ticket and docs.

# Source Snapshot

Key paths to inspect:

- `open-loom.mjs`
- `package.json`
- `INSTALL.md`
- `examples/adapters/open-loom-install/README.md`
- `.loom/tickets/20260425-6uy1rx20-open-loom-install.md`
- `.loom/evidence/open-loom-smoke.md`
- `.loom/research/loom-install-distribution-methods.md` OpenCode section

External source facts already reviewed by parent:

- OpenCode `Hooks` defines `experimental.chat.system.transform(input, output)`
  with `output.system: string[]`.
- OpenCode `readV1Plugin` expects default export object with `server()` for
  server plugins, and path plugins need an `id`.

# Diff Under Review

Review the current working tree changes for the files listed above. Several Loom
planning/research records are also dirty from the parent install-experience work;
focus on `open-loom`, its evidence, and ticket reconciliation.

# Required Questions

- Does the plugin code match the current OpenCode plugin source closely enough
  for the current validation stage?
- Do `INSTALL.md` and fixture docs clearly distinguish `open-loom`, publication
  status, local file/path path, unsupported Git URL specs, and fallback
  requirements?
- Does the ticket overclaim runtime acceptance or first-class skill/command
  support?
- Is the evidence sufficient for `review_required`, and what remains before
  acceptance?
- Are there any scope violations, hidden generated truth copies, package-runtime
  creep, or misleading install recommendations?

# Stop Conditions

Escalate if the review needs real OpenCode model/chat execution, package
publication, or changes outside the review target to reach a verdict.

# Output Contract

Return:

- verdict
- findings with severity/confidence and file or record references
- evidence reviewed
- residual risks
- follow-up recommendation

# Working Notes

This is a one-pass critique because the target is medium risk but small and the
main required profile is operator clarity.

# Reviewer Output

Verdict: `pass_with_findings`.

Findings:

- OCP-001 / `critique:open-loom-review#FIND-001`: Runtime
  rule-injection evidence is still acceptance-blocking. Severity medium,
  confidence high. `open-loom` structurally matches current OpenCode source and
  server-target detection works, but no real OpenCode chat/TUI/model request has
  proven that `experimental.chat.system.transform` is invoked and that Loom rules
  reach the actual system prompt.
- OCP-002 / `critique:open-loom-review#FIND-002`: Optional
  command surface was treated as present by helper discovery. Severity low,
  confidence medium-high. The first `open-loom` version unconditionally read `commands/`,
  which could make optional commands a runtime assumption if a future package
  omits them.

Residual risks:

- OpenCode hook is experimental and may change.
- No npm publication/package-manager path is validated.
- Real model request/system prompt inclusion is unvalidated.
- Skills and commands remain fallback-only.
- Upstream source refs use moving `dev` URLs.

Recommendation:

Do not close yet. Record the critique, then either move `ticket:6uy1rx20` back to
`active` for a narrow runtime-validation packet or explicitly accept only the
structural plugin validation and create linked follow-up work before recommending
plugin-first OpenCode install as supported.

# Parent Merge Notes

Parent recorded `critique:open-loom-review`.

Parent fixed FIND-002 by making `inspectLoomBundle()` tolerate missing `commands/`
and `skills/` directories during helper discovery, then validated that a temporary
bundle with one skill and no commands reports `commandCount: 0`.

FIND-001 remains open. Parent moved `ticket:6uy1rx20` back to `active` for a
narrow runtime-validation or wording-softening follow-up before acceptance.
