---
id: research:codex-plugin-distribution-surfaces
kind: research
status: active
created_at: 2026-04-26T01:43:51Z
updated_at: 2026-05-07T19:30:00Z
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
    - research:codex-command-skill-installation
  ticket:
    - ticket:lx9nnztk
    - ticket:p9m4x2qt
  evidence:
    - evidence:codex-sessionstart-stdout-context
  critique:
    - critique:codex-plugin-hook-config-review
  decision:
    - decision:0005
    - decision:0006
external_refs:
  codex_docs:
    - https://developers.openai.com/codex/plugins
    - https://developers.openai.com/codex/plugins/build
    - https://developers.openai.com/codex/hooks
    - https://developers.openai.com/codex/skills
    - https://developers.openai.com/codex/guides/agents-md
    - https://developers.openai.com/codex/concepts/customization
    - https://developers.openai.com/codex/config-advanced
    - https://developers.openai.com/codex/cli/reference#codex-plugin-marketplace
    - https://developers.openai.com/codex/changelog
  codex_source:
    - https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/manifest.rs
    - https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/loader.rs
    - https://github.com/openai/codex/blob/main/codex-rs/plugin/src/plugin_namespace.rs
    - https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/plugin-json-spec.md
    - https://github.com/openai/plugins
---

# Question

Can Loom deliver a complete remote Codex install where normal users add the Loom
plugin and get `using-loom` plus canonical subsystem skills, without
pretending Codex plugins own more than current docs and source prove?

# Why This Matters

`ticket:lx9nnztk` was created when Codex plugin support looked incomplete and
thinly documented. Codex now has stronger plugin and marketplace docs, a CLI
marketplace command surface, and curated plugin examples. The ticket needs a
fresh source-backed next move before implementation so Loom does not either
underuse a native Codex package surface or overclaim plugin coverage for
always-on context preload.

The product goal is remote install for normal Codex users, not a cloned-repository
or project-local proof. `decision:0005` changes the completeness bar: a remote
plugin can be complete when it exposes the mandatory `using-loom` skill and
the harness/user instruction tells agents to use it first. A repository-local
`.codex/hooks.json` remains useful as an optional preload proof, not the release
boundary.

2026-04-26 update: `decision:0006` also removes fallback installers and top-level
command wrappers from the product surface. Codex command-adapter conclusions below
are historical unless promoted into canonical skills by later work.

The decision also supersedes optional command-wrapper distribution in Codex. Prior
`research:codex-command-skill-installation` remains historical evidence, but Codex
release work should package canonical Loom skills unless later work promotes a
workflow into a real `skills/` owner.

# Scope

Covered:

- official Codex plugin, hook, skill, `AGENTS.md`, customization, config, CLI,
  and changelog docs available on 2026-04-26
- OpenAI Codex source files that parse plugin manifests, load plugin components,
  and derive plugin namespaces for skills
- OpenAI's public plugin examples repository and built-in plugin-creator spec
- local Codex CLI command help for the installed `codex-cli 0.125.0`
- implications for `ticket:lx9nnztk`

Excluded:

- broad release packaging of a Codex plugin fixture
- installing or enabling a local Codex plugin in the user's real Codex config
- publishing a Codex marketplace package
- changing the existing direct Codex installer

# Method

- Read the existing Loom install initiative, plan, broad install research,
  Codex command-skill research, and Codex tickets.
- Fetched official Codex docs for plugins, plugin building, hooks, skills,
  `AGENTS.md`, customization, advanced config, CLI reference, and changelog.
- Inspected OpenAI Codex source for manifest parsing, plugin component loading,
  and plugin skill namespace derivation.
- Inspected OpenAI's public `openai/plugins` examples repository and the bundled
  `plugin-creator` spec.
- Ran local command help for `codex --version`, `codex plugin --help`,
  `codex plugin marketplace --help`, `codex plugin marketplace add --help`, and
  `codex features list`.
- Ran runtime `codex exec` probes showing `SessionStart` stdout visible as
  same-session context when hooks are loaded from CLI override or trusted project
  `.codex/hooks.json` config.
- Measured the top-level Loom `rules/*.md` corpus at 45,588 bytes to evaluate
  the risk of stuffing ordered rules into project instruction surfaces.

# Sources

Repository sources:

- `initiative:loom-install-experience`
- `plan:install-experience-harness-adapters`
- `research:loom-install-distribution-methods`
- `research:codex-command-skill-installation`
- `ticket:lx9nnztk`
- `ticket:p9m4x2qt`
- superseded installer history
- `INSTALL.md`
- `skills/using-loom/references/*.md` and `skills/*/SKILL.md`

External sources are listed in frontmatter under `external_refs`.

Local observations:

- `codex --version` returned `codex-cli 0.125.0` during the hook follow-up.
- `codex plugin --help` exposes only the `marketplace` subcommand under
  `plugin` in the installed CLI.
- `codex plugin marketplace add --help` accepts GitHub shorthand, HTTP(S) Git
  URLs, SSH URLs, and local marketplace root directories.
- `codex features list` reported `codex_hooks stable true` and
  `plugins stable true`.
- A `SessionStart` hook probe returned hidden value `718293` from plain hook
  stdout in model-visible context.
- A repository `.codex/hooks.json` startup probe saw all then-current
  `LOOM_RULE_FILE` rule markers and quoted `A child assertion is not enough.` from
  `07-validation-and-honesty.md`.
- A temp `CODEX_HOME` `codex plugin marketplace add` run registered the local
  `agent-loom` marketplace from the repository root.
- Source inspection found Codex local marketplace paths reject `./` as empty;
  repository-root plugins should use the documented Git-backed `source: "url"`
  shape.
- Source inspection found installed plugin config persists only
  `[plugins.<marketplace/plugin>.enabled]`; plugin loading reads skills, MCP, and
  apps from the installed cache copy, while hook discovery reads active config
  layers and managed hook requirements, not installed plugin manifests.
- The former top-level rule corpus is now the eight ordered `using-loom`
  references.

# Evidence

## Codex Plugin Model

Official Codex docs now describe plugins as the installable distribution unit
for reusable Codex workflows. They can bundle:

- skills
- app integrations or connectors
- MCP servers
- presentation assets and interface metadata

The docs explicitly say skills remain the authoring format, while plugins are
the installable distribution unit when a workflow should be shared beyond local
authoring.

This is a stronger first-class fit than the existing direct Codex installer for
Loom skills because Codex users can browse, install, enable, disable, and upgrade
plugins through Codex's plugin surfaces.

## Manifest Shape

The official plugin root shape is:

```text
my-plugin/
  .codex-plugin/plugin.json
  skills/
  .mcp.json
  .app.json
  assets/
```

The official minimal manifest is a JSON object with `name`, `version`,
`description`, and `skills`, for example:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Reusable greeting workflow",
  "skills": "./skills/"
}
```

OpenAI Codex source-backed manifest parsing currently models these component
paths:

- `skills`
- `mcpServers`
- `apps`

It also models `interface` presentation fields such as display names, default
prompts, icons, logos, screenshots, category, capabilities, and external URLs.

Manifest paths must be relative to the plugin root, start with `./`, avoid `..`,
and stay inside the plugin root. Invalid paths are ignored with warnings in the
source-level parser.

## Marketplace Shape

Codex can read marketplace files from:

- the official curated plugin directory
- `$REPO_ROOT/.agents/plugins/marketplace.json`
- `$REPO_ROOT/.claude-plugin/marketplace.json`
- `~/.agents/plugins/marketplace.json`

The official repo marketplace shape includes top-level `name`, optional
`interface.displayName`, and a `plugins` array. Each plugin entry points at a
local or Git-backed source and includes installation/authentication policy and a
category.

For a local repo marketplace, docs show plugin entries like:

```json
{
  "name": "local-example-plugins",
  "interface": {
    "displayName": "Local Example Plugins"
  },
  "plugins": [
    {
      "name": "my-plugin",
      "source": {
        "source": "local",
        "path": "./plugins/my-plugin"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Local marketplace plugin paths must point at a non-empty plugin directory under
the marketplace root, such as `./plugins/my-plugin`. Source inspection confirms
that `source.path: "./"` is invalid because the path is empty after the required
`./` prefix is stripped. When a plugin lives at the repository root, Codex docs
use the Git-backed `source: "url"` shape instead.

Codex installs plugin artifacts into
`~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/`. For local
plugins, Codex loads the installed cache copy rather than the marketplace source
directly.

## CLI Surface

The current official CLI reference marks `codex plugin marketplace` as
experimental and documents:

```text
codex plugin marketplace add <source> [--ref REF] [--sparse PATH]
codex plugin marketplace upgrade [marketplace-name]
codex plugin marketplace remove <marketplace-name>
```

Supported marketplace sources include GitHub shorthand, HTTP(S) Git URLs, SSH
URLs, and local marketplace root directories. The installed local CLI version
`codex-cli 0.125.0` exposes the same marketplace add shape, but plugin
install/enable still appears to be driven through the interactive `/plugins`
browser or app-server/plugin APIs, not a simple documented `codex plugin install`
CLI command.

The 2026-04 Codex changelog shows rapid plugin movement: remote plugin list/read,
remote/cross-repo/local marketplace sources, app-server plugin install, and
marketplace upgrade support changed between CLI 0.122.0 and 0.125.0. A Codex
plugin implementation ticket should therefore record the tested CLI version and
not assume all documented behavior exists in older installed CLIs.

## Skills Loaded From Plugins

Official skill docs say Codex skills are directories with required `SKILL.md`
frontmatter `name` and `description`, optional `scripts/`, `references/`,
`assets/`, and optional `agents/openai.yaml` for UI metadata, invocation policy,
and dependencies.

Source-level loader behavior supports:

- default `skills/` under the plugin root
- an additional or configured manifest `skills` path
- loaded plugin skills with `SkillScope::User`
- product restriction filtering
- disabled skill path config

OpenAI source for plugin namespace derivation walks up from a skill path until
it finds a `.codex-plugin/plugin.json`. The manifest `name` becomes the plugin
namespace when present. That implies a Loom plugin named `loom` can expose
namespaced plugin skills such as `loom:<skill-name>` in Codex contexts.

Direct non-plugin skill duplicates are not merged according to official skills
docs; both may appear in selectors. Plugin namespacing lowers collision risk,
but `ticket:lx9nnztk` should still validate actual runtime selector and explicit
invocation behavior for `loom` plugin skills.

## Always-On Instruction Surface

Official Codex customization docs treat `AGENTS.md` as the durable project and
global instruction layer. Official `AGENTS.md` docs describe the discovery chain:

- global Codex home: `AGENTS.override.md` first, otherwise `AGENTS.md`
- project scope: root-to-current-directory `AGENTS.override.md`, then
  `AGENTS.md`, then configured fallback filenames
- project docs stop at `project_doc_max_bytes`, documented as 32 KiB by default

Official Codex hooks docs prove a better optional preload route for Loom using-Loom
references than mirroring the full corpus into `AGENTS.md`: Codex discovers hooks from
`hooks.json` files or inline `[hooks]` tables next to active config layers, and
plain `SessionStart` stdout is added as extra developer context. The current
runtime values documented for `SessionStart` matching are `startup`, `resume`,
and `clear`.

The plugin docs and source inspected here still do not show a plugin manifest
field that installs or injects global/project `AGENTS.md` instructions, and the
current source manifest parser models `skills`, `mcpServers`, `apps`, and
`interface`, not plugin-owned hooks. Source inspection also shows plugin install
persisting only an enabled flag under user plugin config. Hook discovery walks
config layers and managed hook requirements, not installed plugin cache roots.

That makes the current hook shape a useful optional context-preload proof, not the
remote product boundary. A remote `loom` plugin can package `using-loom`; the
mandatory first-use instruction should point agents there when hooks are not
preloading context.

The former Loom rule corpus measured 45,588 bytes before moving into
skill-packaged using-Loom references. A project-local strategy that blindly mirrors all
using-Loom references into project `AGENTS.md` risks colliding with the documented
32 KiB default project-doc budget. A global `~/.codex/AGENTS.md` managed block may
still work differently, but implementation work should observe rather than assume
full using-Loom loading.

## Hooks, Commands, And Agents

The plugin surface has inconsistencies that matter for Loom:

- official plugin docs emphasize skills, apps, MCP, and assets
- the OpenAI `openai/plugins` README mentions optional plugin-level `agents/`,
  `commands/`, and `hooks.json`
- the built-in plugin-creator spec includes a `hooks` field in its sample
  manifest
- current OpenAI Codex source manifest parsing inspected here models `skills`,
  `mcpServers`, `apps`, and `interface`, but not `hooks`, `commands`, `agents`,
  or `AGENTS.md`

This means Loom should not depend on plugin-owned hooks, plugin commands, or
plugin agents for the Codex first-class install path until the target Codex
CLI/runtime version proves those fields are loaded and supported. Codex hooks are
still viable for optional using-Loom preload when installed as user, managed, or
trusted project config-layer hooks. Command wrappers are not part of the current
product surface.

# Rejected Options

## Pure Remote Codex Plugin Install Under Top-Level Rules

Rejected under the pre-`decision:0005` model because official docs and inspected
source do not show plugins owning Codex's always-on instruction or hook loading
chain. `decision:0005` supersedes this rejection by moving mandatory doctrine
into `using-loom`, making installed skill discovery the key question instead
of plugin-owned hooks.

## Plugin-Owned Hooks As Rule Context

Rejected as a release claim for the next iteration. Codex hooks are documented as
config-layer hooks under `~/.codex` and trusted project `.codex/` layers.
Plugin-level hook support is not consistently documented or source-verified
through the inspected manifest loader. The evidenced path is direct
`SessionStart` hook stdout from Codex config, not a plugin manifest claiming hook
ownership.

## Plugin Commands As Loom Command Wrappers

Rejected. Codex's stable workflow command story in the inspected docs is skills,
not plugin command files. After `decision:0006`, command-wrapper distribution is
not part of the product surface.

## Unchanged Direct Skill Copy As The Final Product Path

Rejected. Direct copying into `$HOME/.agents/skills` may have worked as a local
prototype, but `decision:0006` rejects fallback copy installers as supported
product shape. Codex work should validate plugin skill discovery instead.

# Null Results

- No documented `codex plugin validate` command was found in official docs or in
  the installed local `codex-cli 0.125.0` help surface.
- No official or inspected source path showed `.codex-plugin/plugin.json` as an
  `AGENTS.md` or always-on instruction installer.
- No source-proven installed-plugin hook loader was found in the current Codex
  plugin manifest parser or plugin loading path.
- No source-proven path was found where installing a plugin writes user-level
  hook config, project hook config, or global `AGENTS.md` instructions.

# Conclusions

Codex has a real first-class plugin distribution surface for Loom's reusable
workflow skills and a real `SessionStart` hook surface for optional using-Loom
preload. Together they are strong enough for a Codex native-plugin proof, not a
fallback copy installer.

After `decision:0005`, Codex plugins can be a complete Loom package if installed
plugin skill discovery exposes `using-loom` and the other Loom skills. The
evidence-backed split is:

- plugin package: `using-loom` plus canonical Loom subsystem skills through a
  repository-root plugin manifest and a Git-backed marketplace entry, optional
  future MCP/app metadata if a later ticket needs it
- Codex hook config: optional ordered preload of `using-loom` references
  through trusted project or user-level `SessionStart` hooks when explicitly
  configured outside the product package

The current implementation should stay scoped as a prototype/proof fixture until
installed Git-backed plugin skill discovery proves `using-loom` is available
and operator guidance makes it mandatory first-use.

# Recommendations

1. Keep the repository-root Codex plugin shape as a remote skills package spike:
   `.codex-plugin/plugin.json` points at canonical `skills/` and
   `.agents/plugins/marketplace.json` exposes an `agent-loom` marketplace with a
   Git-backed repository-root plugin entry.
2. Do not treat `.codex/hooks.json` as product packaging. Keep it only as a
   trusted project-local proof of optional using-Loom-reference preload.
3. Validate installed Git-backed plugin discovery for `using-loom` before
   accepting Codex remote packaging.
4. Do not put generated command adapter skills into canonical top-level `skills/`;
   revisit command folding separately.
5. Treat plugin-owned hooks, commands, and agents as experimental or unverified
   for Loom until a target Codex runtime proves them.
6. Record `codex-cli 0.125.0` as the runtime used for hook context validation.
7. Require critique before accepting broad release packaging because operator
   clarity depends on not overstating what plugin installation alone does.

# Open Questions

- Does installed Git-backed plugin discovery expose `using-loom` in the target
  Codex runtime, and what explicit invocation or selector shape should docs teach?
- Should the Codex plugin include a minimal user-facing default prompt that points
  at `using-loom` before other Loom work?
- Should a future release artifact copy the repository-root Codex plugin shape
  directly, or publish a narrower derivative package that excludes dogfooding
  records and unsupported surfaces?
- If a workflow needs a Codex-specific entry point later, should it become a real
  Loom skill or remain outside the product surface?
- Does the target Codex runtime expose plugin skills as `loom:<skill-name>` in
  explicit `$` invocation syntax, `@` plugin syntax, or both?
- Does installed-plugin skill discovery preserve any per-skill policy metadata
  needed by canonical Loom skills?
- What minimum Codex CLI version should Loom document once installed marketplace
  skill invocation and hook configuration are validated beyond this repository?
- Can global `~/.codex/AGENTS.md` safely exceed 32 KiB while project docs remain
  capped, or should Loom generate a shorter Codex-specific always-on summary?

# Linked Work

- `initiative:loom-install-experience`
- `plan:install-experience-harness-adapters`
- `research:loom-install-distribution-methods`
- `research:codex-command-skill-installation`
- `ticket:lx9nnztk`
- `ticket:p9m4x2qt`
