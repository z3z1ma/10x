---
id: critique:codex-plugin-hook-config-review
kind: critique
status: final
created_at: 2026-04-26T06:08:41Z
updated_at: 2026-04-26T06:35:59Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:lx9nnztk Codex plugin-plus-hook-config prototype
links:
  ticket:
    - ticket:lx9nnztk
  evidence:
    - evidence:codex-sessionstart-stdout-context
  research:
    - research:codex-plugin-distribution-surfaces
  decision:
    - decision:0005
external_refs:
  codex_docs:
    - https://developers.openai.com/codex/plugins/build
    - https://developers.openai.com/codex/hooks
  codex_source:
    - https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/marketplace.rs
---

# Summary

Reviewed the Codex plugin-plus-hook-config prototype for operator clarity,
evidence fidelity, and release-packaging risk.

# Review Target

Reviewed changed Codex adapter surfaces and linked records:

- `.codex-plugin/plugin.json`
- `.agents/plugins/marketplace.json`
- `.codex/config.toml`
- `.codex/hooks.json`
- `examples/adapters/codex-plugin-install/README.md`
- `examples/adapters/codex-command-adaptation/README.md`
- `INSTALL.md`
- `evidence:codex-sessionstart-stdout-context`
- `research:codex-plugin-distribution-surfaces`
- `ticket:lx9nnztk`

# Verdict

`superseded_by_decision_0005`

The plugin-plus-hook-config direction is acceptable as a local proof of Codex hook
mechanics, but it does not satisfy the clarified product goal: normal Codex users
should be able to add the remote Loom plugin and get a complete Loom install.

Post-decision update: `decision:0005` changes the product model by packaging the
mandatory doctrine as the `loom-bootstrap` skill. That supersedes the premise that
Codex plugin-owned hooks are required for remote install completeness. The remaining
Codex release question is installed plugin discovery of `loom-bootstrap` and other
Loom skills.

# Findings

## FIND-001: Local marketplace source path pointed at invalid repo root

Severity: high
Confidence: high
Disposition: resolved

Observation:

The first review pass found `.agents/plugins/marketplace.json` using local plugin
source path `./` for a repository-root plugin. Inspected Codex source rejects
local marketplace paths whose `./`-stripped value is empty, so the marketplace
could register while still failing to expose an installable local plugin entry.

Why it matters:

Operator docs would have implied that the local marketplace exposed `loom` when
only marketplace registration had been validated. That would make the plugin path
look more complete than the evidence supported.

Follow-up:

Resolved by changing `.agents/plugins/marketplace.json` to Codex's documented
Git-backed root-plugin source shape:

```json
{
  "source": "url",
  "url": "https://github.com/z3z1ma/agent-loom.git"
}
```

Docs and evidence now state that Codex local marketplace entries must point at a
non-empty plugin folder path, while repository-root plugins use the Git-backed
`source: "url"` shape.

Challenges:

- `ticket:lx9nnztk`
- `evidence:codex-sessionstart-stdout-context`

## FIND-002: Project-local hook proof does not satisfy remote plugin install

Severity: high
Confidence: high
Disposition: superseded by `decision:0005`

Observation:

The current Codex adapter requires `.codex/hooks.json` from a trusted project
config layer to load mandatory Loom rules. Source inspection shows installed
plugins persisting only `[plugins.<id>].enabled`, plugin loading contributing
skills/MCP/apps, and hook discovery reading active config layers plus managed hook
requirements. No source-proven path showed an installed remote plugin owning
always-on hook or instruction loading.

Why it matters:

The intended product goal is remote install for normal Codex users. If users on
downstream machines must clone this repository, trust a project-local `.codex/`
directory, or separately install user-level hooks, then the plugin alone is not the
product experience being designed.

Required follow-up:

Under the prior top-level-rules model, do not accept broad Codex release packaging
until one of these is true:

- Codex source/runtime proves plugin-owned hooks or plugin-owned instructions.
- Codex provides an equivalent marketplace-supported remote install mechanism for
  always-on rule context.
- Loom explicitly chooses a separate remote installer that mutates user-level hook
  config and documents that this is not plugin-only install.

`decision:0005` chose a different path: make the mandatory doctrine a
plugin-packaged bootstrap skill. Follow-up review should target whether that skill
is discoverable and operationally clear after install.

Challenges:

- `ticket:lx9nnztk`
- `research:codex-plugin-distribution-surfaces`
- `evidence:codex-sessionstart-stdout-context`

# Evidence Reviewed

- Codex docs pasted by the operator for plugin building and marketplace metadata.
- Official Codex hooks docs fetched during the workflow.
- `codex-rs/core-plugins/src/marketplace.rs` in `/tmp/loom-codex-source`.
- `codex-rs/hooks/src/events/session_start.rs` in `/tmp/loom-codex-source`.
- `codex-rs/core/src/hook_runtime.rs` in `/tmp/loom-codex-source`.
- Runtime `codex exec` hook-context probes recorded in
  `evidence:codex-sessionstart-stdout-context`.
- Temp `CODEX_HOME` `codex plugin marketplace add` output.
- `codex-rs/core/src/plugins/manager.rs`, `codex-rs/config/src/types.rs`, and
  `codex-rs/core-plugins/src/loader.rs` install/load paths.
- `git diff --check` and JSON structural validation after the fix.

# Residual Risks

- Installed Git-backed plugin skill invocation is not runtime-validated.
- Installed plugin manifest hook loading is not source- or runtime-proven and must
  not be claimed.
- The repository `.codex/hooks.json` is project-local; downstream always-on hook
  delivery still needs a user-level, managed, trusted-project, or future
  plugin-owned hook strategy.
- Windows shell behavior is untested.
- The matcher includes `compact` defensively, but current Codex docs/source only
  prove `startup`, `resume`, and `clear` as `SessionStart` sources.

# Required Follow-up

- Keep broad release packaging out of scope until installed Git-backed plugin skill
  discovery proves `loom-bootstrap` is available and operator guidance makes it
  mandatory first-use.
- Optional hook preload should be treated as an adapter boost, not the release
  completeness boundary.
- If Codex later source-proves plugin-owned hooks, revisit whether the Codex
  adapter can become a pure plugin install.
- If user-global Codex install is pursued, design a user-level or managed hook
  delivery path instead of relying on this repository's trusted project hook.

# Acceptance Recommendation

re-review under `decision:0005`
