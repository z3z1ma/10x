---
id: evidence:codex-sessionstart-stdout-context
kind: evidence
status: recorded
created_at: 2026-04-26T05:59:22Z
updated_at: 2026-04-26T06:52:09Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:lx9nnztk
  research:
    - research:codex-plugin-distribution-surfaces
    - research:loom-install-distribution-methods
    - research:codex-command-skill-installation
external_refs:
  codex_docs:
    - https://developers.openai.com/codex/hooks
    - https://developers.openai.com/codex/plugins
    - https://developers.openai.com/codex/plugins/build
    - https://developers.openai.com/codex/config-advanced
  codex_source:
    - https://github.com/openai/codex
  inspiration:
    - https://github.com/obra/superpowers
---

# Summary

Observed that current Codex supports Claude-like hook configuration syntax for
`SessionStart`, and that plain `SessionStart` stdout is injected into the model's
context as additional developer context. This supports a Codex Loom adapter split
where the Codex plugin exposes canonical `skills/` and a Codex `hooks.json`
config layer optionally emits source-marked `loom-bootstrap` references at session
start.

This evidence also limits the claim: current inspected Codex source and docs prove
hook loading from Codex config layers, not installed-plugin manifest hook loading.
After `decision:0005`, plugin-owned hooks are no longer required for the remote
install completeness model; `loom-bootstrap` is the mandatory skill-packaged entry
point, and hooks are an optional preload boost.

# Procedure

- Cloned `https://github.com/openai/codex` into `/tmp/loom-codex-source` with
  `git clone --depth 1`.
- Inspected Codex hook source, especially:
  - `codex-rs/hooks/src/events/session_start.rs`
  - `codex-rs/core/src/hook_runtime.rs`
  - `codex-rs/hooks/src/engine/discovery.rs`
  - `codex-rs/config/src/hook_config.rs`
  - `codex-rs/core-plugins/src/manifest.rs`
  - `codex-rs/core-plugins/src/loader.rs`
- Fetched official Codex hooks, plugins, plugin-building, and advanced config docs.
- Inspected Superpowers at `/tmp/loom-superpowers.ug453Z/superpowers`, including
  `.codex-plugin/plugin.json` and `hooks/hooks.json`.
- Ran local Codex CLI help/version checks.
- Created a temporary Codex project hook under
  `/tmp/loom-codex-hook-probe.JqH4WM/.codex/hooks.json` and tested hidden stdout
  context visibility through `codex exec`.
- Added repository Codex adapter files:
  - `.codex-plugin/plugin.json`
  - `.agents/plugins/marketplace.json`
  - `.codex/config.toml`
  - `.codex/hooks.json`
  - `examples/adapters/codex-plugin-install/README.md`
- Ran repository-local `codex exec` startup probes against `.codex/hooks.json`,
  including one without a CLI `--enable codex_hooks` override after adding
  `.codex/config.toml`.
- Ran `CODEX_HOME=/tmp/loom-codex-marketplace.PAttCc codex plugin marketplace add
  /Users/alexanderbutler/code_projects/personal/agent-loom` to validate the
  marketplace catalog can be registered without touching the real Codex home.
- After critique found that local marketplace `source.path: "./"` is invalid for
  a repository-root plugin, changed the marketplace entry to Codex's documented
  Git-backed root plugin source form: `source: { "source": "url", "url":
  "https://github.com/z3z1ma/agent-loom.git" }`.
- Re-ran temp `CODEX_HOME=/tmp/loom-codex-marketplace.I2Q5CS codex plugin
  marketplace add /Users/alexanderbutler/code_projects/personal/agent-loom` after
  the marketplace source fix.
- Inspected plugin install/load source paths after remote-install acceptance was
  clarified as the product goal. Current source persists only plugin enabled
  config for installs, loads skills/MCP/apps from installed plugin cache roots, and
  discovers hooks from active config layers plus managed hook requirements.
- After `decision:0005`, updated `.codex/hooks.json` to read
  `skills/loom-bootstrap/references/*.md` and ran a repository-local startup probe
  for `LOOM_BOOTSTRAP_REFERENCE` markers.

# Artifacts

Codex source shows plain `SessionStart` stdout becomes additional model context.
In `codex-rs/hooks/src/events/session_start.rs`, successful non-empty stdout that
is not JSON is passed through `append_additional_context`:

```text
let additional_context = trimmed_stdout.to_string();
common::append_additional_context(..., additional_context)
```

Codex source records those contexts into the conversation as contextual developer
messages. In `codex-rs/core/src/hook_runtime.rs`, `record_additional_contexts`
converts additional contexts into response items and records them:

```text
let developer_messages = additional_context_messages(additional_contexts);
sess.record_conversation_items(turn_context, developer_messages.as_slice()).await;
```

Codex source discovers hooks from active config layers. In
`codex-rs/hooks/src/engine/discovery.rs`, `load_hooks_json` looks for
`hooks.json` next to a config folder, and `load_toml_hooks_from_layer` reads inline
`hooks` from `config.toml`.

Official Codex hooks docs state:

```text
Codex discovers hooks next to active config layers in either of these forms:
- hooks.json
- inline [hooks] tables inside config.toml
```

They also state for `SessionStart`:

```text
Plain text on stdout is added as extra developer context.
```

Local Codex version:

```text
codex-cli 0.125.0
```

Feature flag state:

```text
codex_hooks stable true
plugins stable true
```

Temporary CLI override proof command shape:

```bash
codex exec --json --ignore-user-config --enable codex_hooks \
  -c 'hooks.SessionStart=[{matcher="startup",hooks=[{type="command",command="printf '\''HOOK_PROOF_VALUE=718293; HOOK_PROOF_SOURCE=codex-session-start-stdout\\n'\''",timeout=10}]}]' \
  --skip-git-repo-check --ephemeral --cd "/tmp/loom-codex-hook-probe.JqH4WM" \
  --sandbox read-only \
  "A hook may have provided a variable named HOOK_PROOF_VALUE..."
```

Observed model output:

```json
{"value":"718293","source":"codex-session-start-stdout","exact_quote":"HOOK_PROOF_VALUE=718293; HOOK_PROOF_SOURCE=codex-session-start-stdout"}
```

Historical repository hook proof command shape before `decision:0005`:

```bash
codex exec --json --enable codex_hooks --ephemeral --sandbox read-only \
  "From loaded context only, do not use tools. Return compact JSON with keys hook_markers_visible, rule_files_seen, rule_count, first_visible_rule_file, validation_honesty_quote. Look for LOOM_RULE_FILE source markers from session hook context. validation_honesty_quote should quote a short line from 07-validation-and-honesty.md if visible."
```

Observed model output before `decision:0005`:

```json
{"hook_markers_visible":true,"rule_files_seen":["01-core-identity.md","02-truth-and-authority.md","03-outer-loop.md","04-ralph-inner-loop.md","05-critique-and-wiki.md","06-filesystem-and-tooling.md","07-validation-and-honesty.md"],"rule_count":7,"first_visible_rule_file":"01-core-identity.md","validation_honesty_quote":"A child assertion is not enough."}
```

Follow-up repository hook proof after adding `.codex/config.toml` and using matcher
`startup|resume|clear|compact` also saw all seven rules without a CLI feature
override:

```json
{"hook_markers_visible":true,"rule_files_seen":["01-core-identity.md","02-truth-and-authority.md","03-outer-loop.md","04-ralph-inner-loop.md","05-critique-and-wiki.md","06-filesystem-and-tooling.md","07-validation-and-honesty.md"],"rule_count":7,"first_visible_rule_file":"01-core-identity.md","validation_honesty_quote":"Honesty is not failure."}
```

Post-`decision:0005` bootstrap reference hook proof command shape:

```bash
codex exec --json --ephemeral --sandbox read-only \
  "From loaded context only, do not use tools. Return compact JSON with keys bootstrap_markers_visible, reference_files_seen, reference_count, first_visible_reference, validation_honesty_quote. Look for LOOM_BOOTSTRAP_REFERENCE source markers from session hook context. validation_honesty_quote should quote a short line from 07-validation-and-honesty.md if visible."
```

Observed model output after moving the hook target to
`skills/loom-bootstrap/references/`:

```json
{"bootstrap_markers_visible":true,"reference_files_seen":["01-core-identity.md","02-truth-and-authority.md","03-outer-loop.md","04-ralph-inner-loop.md","05-critique-and-wiki.md","06-filesystem-and-tooling.md","07-validation-and-honesty.md"],"reference_count":7,"first_visible_reference":"01-core-identity.md","validation_honesty_quote":"A child assertion is not enough."}
```

Temporary Codex marketplace validation:

```text
Added marketplace `agent-loom` from /Users/alexanderbutler/code_projects/personal/agent-loom.
Installed marketplace root: /Users/alexanderbutler/code_projects/personal/agent-loom
```

After the marketplace source fix, the same registration check returned:

```text
Added marketplace `agent-loom` from /Users/alexanderbutler/code_projects/personal/agent-loom.
Installed marketplace root: /Users/alexanderbutler/code_projects/personal/agent-loom
```

Current marketplace plugin source shape:

```json
{
  "name": "loom",
  "source": {
    "source": "url",
    "url": "https://github.com/z3z1ma/agent-loom.git"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Source-backed reason for this shape: Codex marketplace local paths must start
with `./` and must not be empty after stripping that prefix; the inspected source
rejects local `source.path: "./"`. Codex docs state Git-backed entries should use
`source: "url"` when the plugin lives at the repository root.

Installed plugin source inspection:

- `codex-rs/core/src/plugins/manager.rs` install flow materializes the plugin,
  installs it into the plugin store, then writes only
  `plugins.<marketplace/plugin>.enabled = true` into Codex config.
- `codex-rs/config/src/types.rs` defines `PluginConfig` with only an `enabled`
  boolean.
- `codex-rs/core-plugins/src/loader.rs` loads plugin skills, MCP servers, and apps
  from installed plugin roots.
- `codex-rs/hooks/src/engine/discovery.rs` discovers hooks from active config-layer
  `hooks.json`, inline config-layer `[hooks]`, and managed hook requirements. It
  does not walk installed plugin roots.

Temporary Codex home config written by that command:

```toml
[marketplaces.agent-loom]
last_updated = "2026-04-26T06:02:35Z"
source_type = "local"
source = "/Users/alexanderbutler/code_projects/personal/agent-loom"
```

Superpowers comparison:

- `.codex-plugin/plugin.json` exposes `skills: "./skills/"` and interface metadata.
- `hooks/hooks.json` uses a Claude-style `SessionStart` hook matcher
  `startup|clear|compact` for the Claude plugin path.
- The inspected Superpowers Codex plugin manifest does not list a Codex plugin
  hook field.

# Supports Claims

- `ticket:lx9nnztk` acceptance: Codex can use `SessionStart` hook stdout for
  same-session Loom bootstrap context when hooks are loaded from an active Codex
  config layer.
- `ticket:lx9nnztk` acceptance: a repository-root Codex plugin can expose
  canonical Loom skills through `.codex-plugin/plugin.json` and
  `.agents/plugins/marketplace.json`.
- `research:codex-plugin-distribution-surfaces` conclusion update: Codex plugins
  are appropriate for `loom-bootstrap` and subsystem skills, while Codex hooks are
  an evidenced optional preload route for bootstrap context.

# Challenges Claims

- Challenges earlier `ticket:lx9nnztk` and research wording that mandatory Loom
  doctrine must be delivered outside skills for Codex. `loom-bootstrap` now owns
  the portable entry point, and Codex hook stdout is an evidenced optional preload
  route for trusted config layers.
- Challenges any stronger claim that a Codex installed plugin can itself own hook
  loading; inspected source and docs still route hooks through active Codex config
  layers.

# Environment

Commit: `18fac92`
Branch: `main`
Runtime: `codex-cli 0.125.0`
OS: `Darwin`
Relevant config: repository `.codex/config.toml` enables `codex_hooks`; repository
`.codex/hooks.json` defines source-marked per-bootstrap-reference `SessionStart`
commands.

# Validity

Valid for: Codex CLI `0.125.0` hook config behavior and source inspection from
the cloned `openai/codex` repository on 2026-04-26.

Recheck when: Codex plugin manifest parsing adds a source-proven `hooks` field,
Codex changes `SessionStart` source names, `loom-bootstrap` references grow
materially, or the minimum supported Codex CLI version changes.

# Limitations

- Project-local hooks require the project `.codex/` layer to be trusted.
- Runtime validation did not prove installed-plugin manifest hook loading.
- Runtime validation did not prove plugin skill invocation from an installed
  Git-backed marketplace plugin.
- Source inspection shows current installed plugins do not appear to own always-on
  hook or instruction loading; after `decision:0005`, that limits optional preload
  rather than blocking the skills-package model.
- Current Codex docs/source name `startup`, `resume`, and `clear` as
  `SessionStart` sources; no separate `compact` source was found.
- Evidence depends on model self-report from loaded context, not direct internal
  context inspection.
- Windows shell behavior is not validated.

# Result

The repository now has a Codex adapter fixture that mirrors the Claude per-rule
hook strategy as closely as current Codex evidence supports:

- `.codex-plugin/plugin.json` packages canonical Loom skills.
- `.agents/plugins/marketplace.json` exposes an `agent-loom` marketplace with a
  Git-backed repository-root `loom` plugin entry.
- `.codex/hooks.json` emits one source-marked stdout block per `loom-bootstrap`
  reference at `SessionStart`.
- a runtime startup probe saw all seven bootstrap references in same-session
  context.

# Interpretation

It is justified to document Codex hook stdout as an optional bootstrap-context
preload route for trusted Codex config layers and to use a Codex Git-backed root
plugin for a skills-package spike. It is not justified to claim that installing
the Codex plugin alone installs always-on hook context in arbitrary projects. The
remaining remote-install evidence gap is installed plugin discovery of
`loom-bootstrap`.

# Related Records

- `ticket:lx9nnztk`
- `research:codex-plugin-distribution-surfaces`
- `research:loom-install-distribution-methods`
- `research:codex-command-skill-installation`
- `examples/adapters/codex-plugin-install/README.md`
