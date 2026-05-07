---
id: research:loom-install-distribution-methods
kind: research
status: active
created_at: 2026-04-25T18:25:20Z
updated_at: 2026-05-07T21:35:47Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:install-experience-harness-adapters
  spec:
    - spec:opencode-plugin-install-contract
  wiki:
    - wiki:harness-adapter-package-pattern
  research:
    - research:harness-install-surfaces
    - research:codex-command-skill-installation
    - research:codex-plugin-distribution-surfaces
  decision:
    - decision:0005
    - decision:0006
    - decision:0008
  ticket:
    - ticket:6uy1rx20
    - ticket:us1brnsv
    - ticket:q7h1d05q
    - ticket:cldrel01
    - ticket:lx9nnztk
    - ticket:7ex8w32y
    - ticket:3t93tsci
    - ticket:ffg8elkb
    - ticket:p9m4x2qt
    - ticket:rd48g1kg
  evidence:
    - evidence:open-loom-smoke
    - evidence:cursor-harness-install-validation
    - evidence:claude-plugin-hybrid
    - evidence:claude-sessionstart-stdout-context
    - evidence:codex-sessionstart-stdout-context
  critique:
    - critique:codex-plugin-hook-config-review
external_refs:
  claude_code:
    - https://code.claude.com/docs/en/plugins
    - https://code.claude.com/docs/en/plugins-reference
    - https://code.claude.com/docs/en/settings
    - https://code.claude.com/docs/en/hooks
    - https://code.claude.com/docs/en/skills
    - https://code.claude.com/docs/en/memory
    - https://code.claude.com/docs/en/plugin-marketplaces
    - https://github.com/obra/superpowers
  codex:
    - https://developers.openai.com/codex/plugins
    - https://developers.openai.com/codex/skills
    - https://developers.openai.com/codex/guides/agents-md
    - https://developers.openai.com/codex/plugins/build
    - https://developers.openai.com/codex/cli/reference#codex-plugin-marketplace
    - https://developers.openai.com/codex/concepts/customization
    - https://developers.openai.com/codex/config-advanced
    - https://developers.openai.com/codex/changelog
  opencode:
    - https://opencode.ai/docs/config/
    - https://opencode.ai/docs/plugins/
    - https://opencode.ai/docs/skills/
    - https://opencode.ai/docs/commands/
  opencode_source:
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/plugin/shared.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/plugin/loader.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/config/plugin.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/test/plugin/shared.test.ts
    - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/test/plugin/trigger.test.ts
  gemini_cli:
    - https://geminicli.com/docs/extensions/
    - https://geminicli.com/docs/extensions/reference/
    - https://geminicli.com/docs/cli/skills/
    - https://geminicli.com/docs/cli/custom-commands/
  cursor:
    - https://cursor.com/docs/rules
    - https://cursor.com/docs/skills
    - https://cursor.com/docs/plugins
    - https://cursor.com/docs/reference/plugins
  agent_skills:
    - https://agentskills.io/specification
  installer_precedents:
    - https://brew.sh/
    - https://rust-lang.org/tools/install/
    - https://docs.astral.sh/uv/getting-started/installation/
    - https://ohmyz.sh/
    - https://ui.shadcn.com/docs/installation
    - https://code.visualstudio.com/api/working-with-extensions/publishing-extension
---

# Question

What installation and distribution model should Loom use so OpenCode, Claude
Code, Codex, Gemini CLI, and Cursor users get a first-class install experience
without turning Loom into a runtime, hidden helper system, or harness-specific
ontology?

# Why This Matters

2026-05-07 update: the mandatory entry skill is now `using-loom`; the former
entry-skill name is historical unless a current owner record still explicitly
says otherwise.

2026-05-07 later update: `decision:0008` supersedes the single top-level
`skills/` product surface described in much of this research. Current downstream
work should use the `loom-core/` and `loom-playbooks/` package-root model. Text
below that describes top-level `skills/` as the current product surface is
historical evidence unless a newer owner record explicitly preserves it.

2026-04-26 update: `decision:0005` and `decision:0006` supersede older
conclusions in this research that treated top-level `rules/`, top-level
`commands/`, Makefile, or `scripts/install-loom.sh` as supported install surfaces.
Historical evidence and rejected options below still describe the state when they
were gathered; current downstream work should inherit `skills/` as the product
surface and `using-loom` as the mandatory entry skill.

Earlier installer work proved that global copy installs were possible, but
`decision:0006` rejected that shape as a supported product surface.

The current product stance is simpler:

- `skills/` is the product surface
- `skills/using-loom` is the mandatory entry skill
- native harness adapters expose the same `skills/` package
- Claude and OpenCode may preload using-Loom references because their native
  adapter surfaces support it cleanly
- Makefile, shell installer, top-level `rules/`, and top-level `commands/` are no
  longer supported install surfaces

This research preserves the historical comparison, but its old fallback-install
recommendations are superseded by `decision:0006`.

# Scope

Covered:

- Loom's product and historical installer constraints from `constitution:main`,
  `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, and superseded
  installer records
- existing Loom install records: `research:harness-install-surfaces`,
  `research:codex-command-skill-installation`, `ticket:ffg8elkb`,
  `ticket:p9m4x2qt`, `ticket:rd48g1kg`, and
  `evidence:cursor-harness-install-validation`
- first-party/current install and extension docs for OpenCode, Claude Code,
  Codex, Gemini CLI, Cursor, and the Agent Skills specification
- popular install precedent categories: plugin marketplaces, package managers,
  `curl | sh` installers, standalone tool installers, project scaffolders,
  extension packages, and manual clone/link workflows

Excluded:

- implementation changes to the current installer
- choosing final file paths for future adapter packages
- runtime UI validation inside every harness
- adding support for unsupported harnesses
- publishing any marketplace package
- treating external package registries as Loom truth owners

# Method

Repository inspection:

- read `constitution:main` and the public product framing docs
- read `Makefile`, `scripts/install-loom.sh`, and `INSTALL.md`
- read prior install research and tickets
- inspected supported harness values and per-harness installer branches in the
  current shell script

External source inspection:

- fetched official docs for Claude Code plugins, settings, hooks, skills, and
  memory/instruction loading
- fetched official Codex docs for Agent Skills, `AGENTS.md`, and plugins
- fetched OpenCode docs for config, plugins, skills, and commands
- fetched Gemini CLI docs for extensions, extension reference, skills, and custom
  commands
- fetched Cursor docs for rules, skills, plugins, and plugin reference
- fetched the Agent Skills specification
- fetched official or project docs for installer precedents including Homebrew,
  Rust/rustup, uv, Oh My Zsh, shadcn/ui, and VS Code extension publishing

Source quality notes:

- official product docs are treated as primary evidence for current surfaces
- prior Loom tickets and evidence are treated as repository-local evidence for
  what has already been implemented and validated
- docs that returned `404`, redirects, or incomplete extracted content are noted
  as null results rather than silently treated as evidence
- product docs for these harnesses are changing quickly, so implementation work
  should recheck the exact docs before mutating adapter behavior

# Sources

Repository sources:

- `constitution:main`
- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `INSTALL.md`
- `Makefile`
- `scripts/install-loom.sh`
- `research:harness-install-surfaces`
- `research:codex-command-skill-installation`
- `research:codex-plugin-distribution-surfaces`
- `ticket:ffg8elkb`
- `ticket:p9m4x2qt`
- `ticket:rd48g1kg`
- `evidence:cursor-harness-install-validation`

External sources are listed in `external_refs` frontmatter and cited by section
below.

# Evidence

## Loom Product Constraints

`constitution:main`, `README.md`, `PROTOCOL.md`, and `ARCHITECTURE.md` establish
these relevant constraints:

- Loom is a Markdown-native control plane, not a runtime, daemon, MCP bundle,
  dashboard, model router, or product CLI.
- The protocol core is `skills/`, especially `using-loom`, plus templates,
  references, and canonical examples.
- Record creation, packet compilation, validation, and graph inspection are
  visible protocol behaviors taught through Markdown guidance and ordinary file
  tools, not hidden helper behavior.
- Harness adapters may expose or preload Loom, but they must not define Loom
  truth.
- Deleting fallback installers or command wrappers must not delete a Loom
  capability.
- A valid install model must make `using-loom` discoverable before work and
  preserve on-demand subsystem skills without requiring a central Loom runtime.

These constraints rule out install strategies that make a CLI, plugin runtime,
marketplace package, generated aggregate file, or helper database the semantic
owner of Loom.

## Historical Installer Baseline

Earlier work validated direct copy installs into harness config roots. That
baseline is now superseded by `decision:0006` and should not be treated as the
current product path.

The historical installer remains useful evidence that several harnesses can read
Loom skills or instruction surfaces, but the accepted product direction is native
plugin, extension, or skill-package installation of canonical `skills/`.

## Common Loom Surfaces To Preserve

Any install strategy must map these source surfaces honestly:

| Loom source surface | Required install property | Notes |
| --- | --- | --- |
| `skills/using-loom/SKILL.md` and `skills/using-loom/references/*.md` | Mandatory first skill and ordered using-Loom doctrine. | A harness may preload references, but the skill remains the portable entry point. |
| `skills/*/SKILL.md` | Discoverable by name and description, full content hydrated only when relevant. | This maps well to Agent Skills style surfaces. |
| `skills/*/references/` and `skills/*/templates/` | Readable on demand relative to each skill root. | A packaging format must preserve directories, not flatten skills into prose. |
| `commands/*.md` | Optional explicit workflow wrappers. | Commands are adapter prompts, not the owner of Loom workflows. |
| `optional-utilities/` | Not default protocol install. | May be installed manually or by explicit local choice. |
| `.loom/` dogfooding records | Not product install. | Canonical records in this repo are project truth for this repo only. |
| `.opencode/` dogfooding surface | Not product install. | It is a consumption surface, not source protocol corpus. |

## Agent Skills As A Portable Skill Plane

The Agent Skills specification and harness docs show strong convergence around a
directory with `SKILL.md`, YAML frontmatter, and optional supporting directories.

Doc-backed facts:

- Agent Skills require a skill directory containing `SKILL.md` with YAML
  frontmatter and Markdown body.
- Required common fields in the Agent Skills specification are `name` and
  `description`; `name` must match the parent directory and be lowercase
  alphanumeric with hyphens.
- Optional directories such as `scripts/`, `references/`, and `assets/` are
  expected by the spec and by several harness docs.
- Progressive disclosure is central: metadata is visible initially, full
  `SKILL.md` loads on activation, and resources load only when needed.
- Codex, OpenCode, Gemini CLI, and Cursor all document support for
  `~/.agents/skills` or project `.agents/skills` in some form.
- Claude Code documents `~/.claude/skills` and plugin/project skill paths, but
  the fetched Claude docs do not identify `~/.agents/skills` as a Claude skill
  discovery path.

Implication for Loom:

- Loom skills already fit the broad `SKILL.md` shape.
- A generic `~/.agents/skills` install can reduce duplicated skill copies across
  Codex, Gemini CLI, Cursor, and OpenCode.
- A generic Agent Skills install still needs `using-loom` first-use to be
  explicit unless a native adapter preloads the same using-Loom references.
- Claude Code still needs a Claude-native skill destination unless future Claude
  docs add generic `.agents/skills` support.

## Claude Code

Doc-backed install surfaces:

- User settings live in `~/.claude/settings.json`; some global config lives in
  `~/.claude.json` instead.
- Managed settings exist at OS-level managed paths and have highest precedence.
- User instructions can live in `~/.claude/CLAUDE.md`.
- Claude Code loads `CLAUDE.md` files and supports imports with `@path` up to a
  documented recursion limit.
- Claude Code reads `CLAUDE.md`, not `AGENTS.md`, though a `CLAUDE.md` can import
  `@AGENTS.md`.
- User-level rules live in `~/.claude/rules/`; project rules live in
  `.claude/rules/` and can be unconditional or path-scoped.
- Personal skills live in `~/.claude/skills/<skill-name>/SKILL.md`.
- Project skills live in `.claude/skills/<skill-name>/SKILL.md`.
- Plugin skills live at `<plugin>/skills/<skill-name>/SKILL.md` and are
  namespaced by plugin.
- Claude Code plugins are directories with `.claude-plugin/plugin.json` and may
  include `skills/`, `commands/`, `agents/`, `hooks/hooks.json`, MCP/LSP config,
  monitors, `bin/`, and limited default settings.
- Claude plugin manifests can point component paths at existing plugin-root
  directories such as `./skills/` and `./commands/`; custom component paths replace
  defaults unless the defaults are included explicitly.
- Claude auto-loads the standard plugin `hooks/hooks.json` path. Local marketplace
  install showed a plugin manifest should not also declare `"hooks":
  "./hooks/hooks.json"`, because that duplicate declaration produces a hook-load
  error after install even though schema validation passes.
- Claude plugin hooks can run command hooks on `SessionStart` and
  `UserPromptSubmit`; plugin docs show hooks may use `${CLAUDE_PLUGIN_ROOT}` and
  `${CLAUDE_PLUGIN_DATA}`. `UserPromptSubmit` can block prompt processing with a
  user-visible reason.
- `${CLAUDE_PLUGIN_ROOT}` is the plugin installation directory, not the user or
  project `.claude` settings directory. For marketplace installs, docs say
  plugins are copied into `~/.claude/plugins/cache`; local `claude plugin list
  --json` showed project-scoped plugins with `installPath` under that cache and a
  separate `projectPath`.
- Claude plugin `settings.json` supports only `agent` and `subagentStatusLine` in
  the fetched docs; unknown keys are ignored.
- Claude plugins can be installed from marketplaces and tested locally with
  `claude --plugin-dir`.
- Claude marketplaces use `.claude-plugin/marketplace.json`; relative plugin
  sources such as `./` resolve from the marketplace root, not from
  `.claude-plugin/`.

using-Loom preload fit:

- Claude's clean always-on instruction surfaces are `CLAUDE.md` and
  `.claude/rules/*.md` / `~/.claude/rules/*.md`.
- Claude docs state user-level rules load at launch, but the fetched docs do not
  specify a deterministic filename ordering contract for multiple rule files.
- The fetched plugin docs do not state that the `claude plugin install` command
  runs arbitrary setup code, adds always-on doctrine, or appends to `CLAUDE.md`.
- A plugin can include a custom agent and set it as the main thread through plugin
  settings, but that is not equivalent to exposing Loom's using-Loom doctrine as a
  reusable skill package. It changes the agent selection/system prompt rather than
  exposing `using-loom`.
- Hook docs say static context should use `CLAUDE.md` when no script is needed,
  but they also state that `SessionStart` stdout is added as Claude context.
  `evidence:claude-sessionstart-stdout-context` observed local plugin hooks that
  emit source-marked bootstrap reference files and make the marker visible to
  Claude in the same startup session.
- `obra/superpowers` uses a similar `SessionStart` matcher shape
  (`startup|clear|compact`) and emits Claude context from a plugin hook, though it
  uses structured `hookSpecificOutput.additionalContext` rather than raw `cat`.

Assessment:

- Claude plugins are attractive for packaging Loom skills, namespacing, versioning,
  and marketplace distribution.
- Claude plugins expose `skills/`; optional using-Loom preload uses plugin
  `SessionStart` stdout rather than manifest-only always-on instructions.
- The accepted Claude adapter direction is automated native-plus-preload: a Claude
  plugin exposes canonical `skills`, and a plugin `SessionStart` hook emits
  canonical using-Loom references as same-session, source-marked per-reference
  stdout context.
- Direct copy to `~/.claude` is no longer a supported fallback path after
  `decision:0006`.
- Runtime probes showed per-reference hook stdout made all then-current
  using-Loom references visible in same-session startup context.
- The per-reference design relies on source markers and best-effort sleep
  staggering.
  `01-core-identity.md` appeared first in repeated probes, but strict order after
  that is not guaranteed because Claude runs matching hooks concurrently.
- Disabling or uninstalling the plugin follows Claude's plugin manager UX because
  the active preload path is plugin hook context emitted at session start.
- Local marketplace install validates `loom@agent-loom` can install without
  hook-load errors after relying on standard hook auto-loading instead of a
  duplicate manifest `hooks` field.
- Hook-context loading is accepted for the Claude adapter only in the per-reference
  raw stdout form implemented by `ticket:cldrel01`. Monolithic full-corpus raw
  stdout and structured additional context were previewed/truncated. Plugin-root
  `CLAUDE.md` and `.claude/rules/loom.md` did not load under local `--plugin-dir`.
  Arbitrary 26-command chunking worked once but was rejected as too brittle.

## Codex

Doc-backed install surfaces:

- Codex home defaults to `~/.codex` unless `CODEX_HOME` is set.
- Global instructions use `AGENTS.override.md` first if present, otherwise
  `AGENTS.md`; only the first non-empty global file is used.
- Project instructions are loaded by walking from project root to current working
  directory and concatenating one instruction file per directory.
- Combined project docs stop once `project_doc_max_bytes` is reached; the default
  documented value is `32 KiB`.
- Codex skills are directories with required `SKILL.md` frontmatter `name` and
  `description`.
- User skills live under `$HOME/.agents/skills`; repo/project and admin/system
  tiers also exist.
- Codex supports explicit `$skill` invocation and implicit invocation based on
  description.
- Optional `agents/openai.yaml` can set UI metadata and
  `policy.allow_implicit_invocation`.
- `allow_implicit_invocation` defaults to `true`; setting it to `false` preserves
  explicit invocation while preventing automatic selection.
- Codex plugins use `.codex-plugin/plugin.json` and can package `skills/`, MCP
  servers, apps/connectors, and assets.
- Codex plugin marketplaces are JSON catalogs under repo or user `.agents/plugins`
  paths, and plugins install into a Codex plugin cache.
- `codex plugin marketplace add` can add local, GitHub shorthand, HTTP(S) Git,
  and SSH marketplace sources.
- The official CLI reference marks `codex plugin marketplace` experimental.
- Installed local `codex-cli 0.125.0` exposes marketplace add/upgrade/remove but
  not a simple non-interactive `codex plugin install` command.
- OpenAI source inspected in `research:codex-plugin-distribution-surfaces` models
  plugin manifest paths for `skills`, `mcpServers`, `apps`, and `interface`, not
  `AGENTS.md`, `commands`, `agents`, or source-proven plugin-owned hooks.
- Installed plugin config in inspected source is only an enabled flag, and plugin
  loading contributes skills/MCP/apps from the installed cache rather than hooks.
- Codex hooks are documented as config-layer hooks from `hooks.json` files or
  inline `[hooks]` tables next to active config layers.
- Codex `SessionStart` plain stdout is documented and runtime-observed as extra
  developer context.
- Plugin skill paths are namespaced from the plugin manifest name in inspected
  source, which should reduce collision risk for a `loom` plugin but still needs
  runtime validation.

Always-on rule fit:

- Codex's durable user instruction surface is `~/.codex/AGENTS.md` or
  `AGENTS.override.md`.
- Codex's hook-based always-on context surface is `SessionStart` stdout from a
  user, managed, or trusted project config layer.
- The fetched Codex plugin docs do not describe plugins as a mechanism for
  always-on instructions or source-proven plugin-owned hooks.
- Prior research already found that `~/.codex/rules/` is not a Markdown rules
  instruction surface for Loom; it should not receive Loom rules.

Assessment:

- Codex plugins are a good candidate for distributing Loom skills. Completeness now
  depends on installed plugin skill discovery for `using-loom`, not
  plugin-owned hooks.
- Command-wrapper distribution is no longer part of the product surface after
  `decision:0006`.
- The repository-root Codex plugin spike can package canonical Loom skills and
  uses `.codex/hooks.json` only as a trusted project-local per-rule `SessionStart`
  stdout proof.
- The `AGENTS.md` size budget remains relevant only for optional using-Loom preload
  instructions. Loom should not mirror the full using-Loom corpus into `AGENTS.md`
  as a product install path.
- Current focused recommendation: do not accept Codex as a complete remote plugin
  install yet. Use the plugin-plus-hook-config proof for repository-local
  validation while installed Git-backed plugin skill discovery remains unproven.
  Do not preserve a direct fallback installer. See
  `research:codex-plugin-distribution-surfaces`,
  `evidence:codex-sessionstart-stdout-context`, and `ticket:lx9nnztk`.

## OpenCode

Doc-backed install surfaces:

- Global config lives at `~/.config/opencode/opencode.json`.
- The `instructions` field accepts an array of paths and glob patterns for
  always-on/model instructions.
- Global commands live in `~/.config/opencode/commands/`; project commands live
  in `.opencode/commands/`.
- OpenCode custom commands can be Markdown files, with filename as command name
  and `$ARGUMENTS` / positional variables for arguments.
- Global skills can live in `~/.config/opencode/skills/<name>/SKILL.md`.
- OpenCode also discovers compatible skills from `~/.claude/skills`,
  `~/.agents/skills`, and project equivalents.
- OpenCode plugins are JavaScript/TypeScript modules exporting plugin functions
  and hooks. They can be local files or npm packages listed in config. Npm
  plugins are installed automatically with Bun and cached under
  `~/.cache/opencode/node_modules/`.
- The fetched OpenCode plugin docs describe hooks, events, custom tools,
  environment injection, and TUI behavior, but do not state that plugins package
  rules, skills, or commands as static resources.
- Official plugin docs show `plugin` array examples with npm package names only;
  they do not document GitHub repository shorthands as supported plugin specs.
- Source-level config handling accepts `plugin` entries as a string or
  `[string, options]`, with arbitrary options records.
- Source-level path handling treats specs starting with `file://`, `.`, or an
  absolute path as file plugins; other specs are treated as npm-style specs and
  passed to `Npm.add` after bare package names are normalized to `@latest`.
- Source-level `parsePluginSpecifier` tests cover bare npm packages, scoped
  packages, `npm:` protocol specs, aliases, and Git URLs such as
  `git+https://github.com/opencode/acme.git` and
  `git+ssh://git@github.com/opencode/acme.git`.
- The operator checked current OpenCode plugin loading and reported that Git URL
  plugin installs are not supported in practice. Treat npm publication and local
  file/path plugins as the viable distribution paths unless future runtime
  evidence contradicts this.
- The deeper source inspection did not find first-class `skill` or `command`
  registration fields on the plugin `Hooks` interface.
- The plugin `Hooks` interface does include `experimental.chat.system.transform`,
  which can mutate the system prompt array, but the better OpenCode route for
  Loom rules is now `config(config)` mutating the documented `instructions`
  config surface.
- The plugin `Hooks` interface includes `command.execute.before`, but source
  inspection shows that hook runs only after an existing command is resolved; it
  does not prove slash-command registration.
- `evidence:open-loom-smoke` validated `open-loom`, which reads ordered
  `skills/using-loom/references/*.md`, default-exports an OpenCode-shaped
  object with `id: "open-loom"` and `server()`, and uses the plugin
  `config(config)` hook to register ordered using-Loom references through
  `config.instructions` and bundled skills through `config.skills.paths`.
  OpenCode CLI `1.14.22` validated the resolved config and skill discovery in an
  isolated temporary environment. Follow-up validation also proved local
  package-root plugin resolution, clean-project skill loading with 20 skills, and
  package dry-run contents. The package now declares `engines.opencode:
  >=1.14.22 <2`.
- `open-loom@0.1.0` is published on npm. A normal repo-root `opencode.json` with
  `plugin: ["open-loom@0.1.0"]` can load the package from OpenCode's package
  cache and expose using-Loom references and skills. In isolated cold-cache
  validation, OpenCode `1.14.22` can log `NpmInstallFailedError` on the first
  config-file run while still caching the package; a second run in the same cache
  succeeds.

using-Loom preload fit:

- OpenCode has a direct, clean preload route through `open-loom`: the plugin
  `config(config)` hook appends package absolute paths for
  `skills/using-loom/references/*.md` to `config.instructions`.

Assessment:

- The ideal OpenCode user experience is a plugin-first install: the user adds one
  entry to the `plugin` array in `opencode.json`, and the plugin exposes bundled
  using-Loom references and skills.
- That ideal is now accepted for `open-loom@0.1.0` on OpenCode `>=1.14.22 <2`,
  with the cold-cache first-run installer caveat tracked by `ticket:us1brnsv`.
  Official docs did not state this full static-resource registration shape; it is
  supported by source inspection and runtime evidence.
- A plugin can read its own bundled files using normal JavaScript module
  techniques such as `import.meta.url` in the repository/package-root `open-loom`.
- Separate first-class plugin registration fields for skills were not found, but
  `config.skills.paths` is sufficient for current OpenCode `1.14.22` validation.
- GitHub-based plugin installation should not be recommended for OpenCode. The
  viable plugin distribution paths are an npm package for normal users and a
  cloned repo plus file/local path plugin entry for users who want to consume the
  repository directly.
- The preferred plugin design should consume or expose Loom's existing Markdown
  files from the package or cloned repository where practical, rather than
  generating a second plugin-owned Markdown corpus.

## Gemini CLI

Doc-backed install surfaces:

- Gemini CLI extensions distribute prompts, MCP servers, custom commands,
  themes, hooks, sub-agents, and agent skills.
- Extensions are installed with commands such as
  `gemini extensions install <source>` from GitHub repositories or local paths.
- Extensions load from `<home>/.gemini/extensions`; installing creates a copy,
  while linking local extensions uses a symlink for immediate testing.
- Each extension root must contain `gemini-extension.json`.
- `gemini-extension.json` supports fields including `name`, `version`,
  `description`, `mcpServers`, `contextFileName`, `excludeTools`, `plan`,
  `settings`, and `themes`.
- `contextFileName` names a context file loaded from the extension directory;
  if omitted and `GEMINI.md` exists, `GEMINI.md` is loaded.
- Extensions can package agent skills under `skills/<name>/SKILL.md`.
- Gemini skills are based on the Agent Skills open standard and may live in
  `.gemini/skills`, `.agents/skills`, `~/.gemini/skills`, `~/.agents/skills`, or
  inside extensions.
- Skill precedence is Workspace > User > Extension; within user/workspace tiers,
  `.agents/skills` overrides `.gemini/skills`.
- Gemini custom commands are TOML files under `~/.gemini/commands/` or project
  `.gemini/commands/`; subdirectories produce namespaced commands such as
  `/git:commit`.
- Gemini custom commands require a `prompt` string and optional `description`;
  Loom does not currently ship a command-wrapper product surface.

using-Loom preload fit:

- Gemini extensions can load a context file from the extension directory,
  defaulting to `GEMINI.md` when present.
- This may be a strong native fit if the extension can expose `skills/` and, when
  desired, preload `using-loom` references through its context file.

Assessment:

- Gemini CLI extensions are a strong candidate for a first-class Loom install
  package.
- A Gemini extension could package canonical skills under `skills/` and optionally
  preload using-Loom references through an extension `GEMINI.md` or configured
  context file.
- The current direct install is serviceable, but a Gemini extension may better
  support install/update/disable/link workflows and avoids hand-editing global
  `GEMINI.md`.
- Implementation should verify whether extension skills are discoverable and
  whether optional using-Loom preload context is loaded with the right priority in
  actual sessions.

## Cursor

Doc-backed install surfaces:

- Cursor User Rules are global preferences in Cursor Settings -> Rules and apply
  across Agent Chat.
- Cursor Project Rules live in `.cursor/rules`; `.mdc` frontmatter supports
  fields such as `description`, `globs`, and `alwaysApply`.
- Rule application shapes include always-apply, intelligent/relevance-based,
  file-specific, and manual `@` mention.
- Cursor also supports `AGENTS.md` in project roots or subdirectories, with
  nested files applying to descendants.
- Cursor skills are Agent Skills directories with `SKILL.md`; user/global paths
  include `~/.agents/skills` and `~/.cursor/skills`.
- Cursor also loads compatible skill paths from Claude and Codex locations.
- `disable-model-invocation: true` can make a skill explicit-only.
- Cursor plugins are Git-backed bundles with `.cursor-plugin/plugin.json`.
- Cursor plugins can package rules, skills, agents, commands, MCP servers, and
  hooks.
- Cursor plugin component discovery includes `rules/`, `skills/`, `agents/`,
  `commands/`, `hooks/hooks.json`, and `mcp.json` unless manifest paths override.
- Cursor plugin rules are generally `.mdc` files in `rules/` with YAML
  frontmatter.
- Cursor plugin commands can be `.md`, `.mdc`, `.markdown`, or `.txt` files with
  optional `name` and `description` frontmatter.
- Cursor plugins can be installed from the marketplace at project or user level;
  team marketplaces can make plugins required or optional.
- Local plugin testing uses `~/.cursor/plugins/local`, including symlinked plugin
  repositories.

using-Loom preload fit:

- Cursor plugin rules may be a clean native way to preload using-Loom
  references if generated rule files can set `alwaysApply: true` and preserve
  enough attribution.
- This may be better than directly mutating Cursor User Rules storage, which the
  current installer does through a SQLite-backed state path on macOS.

Assessment:

- Cursor plugins are a strong candidate for first-class Loom distribution because
  they can package skills and optional preload surfaces.
- The current Cursor installer is useful proof, but User Rules database mutation
  is more brittle than a documented plugin package path.
- A Cursor plugin adapter may need generated `.mdc` rule frontmatter for optional
  preload, but those generated files would be packaging outputs, not semantic
  owners.
- Implementation should verify actual Cursor behavior for plugin rule ordering,
  `alwaysApply`, user-level install scope, and local plugin reload/discovery.

## Cross-Harness Plugin And Extension Fit

| Harness | First-class package surface | Exposes skills? | Optional using-Loom preload? | Current fit |
| --- | --- | --- | --- | --- |
| Claude Code | `.claude-plugin/plugin.json` plugins plus `.claude-plugin/marketplace.json` | Yes. | Yes, through source-marked `SessionStart` stdout. | Native plugin with optional preload; release hardening remains. |
| Codex | `.codex-plugin/plugin.json` plugins and marketplaces | Target yes; installed Git-backed skill discovery still needs validation. | Only through config-layer hooks, not plugin ownership. | Active remote plugin validation target. |
| OpenCode | JS/TS plugins via npm package or local file/path specs | Yes, via `config.skills.paths`. | Yes, via `config(config)` adding using-Loom references to `config.instructions`. | `open-loom` npm/local distribution. |
| Gemini CLI | `gemini-extension.json` extensions | Target yes. | To be validated through native extension context if used. | Native extension candidate. |
| Cursor | `.cursor-plugin/plugin.json` plugins | Target yes. | To be validated through native plugin/rule context if used. | Native plugin candidate. |

The strongest current product direction is native skills-package exposure per
harness. Claude and OpenCode have validated optional using-Loom preload paths.
Codex, Gemini, and Cursor should be accepted only after their native paths expose
`skills/` and preserve `using-loom` first-use. OpenCode distribution should
assume npm publication for normal users and a local file/path plugin entry for
cloned-repo use, not Git URL plugin specs.

## Existing Install Surfaces Compared

| Surface | Strengths | Weaknesses | Loom use |
| --- | --- | --- | --- |
| Direct user config copy | Transparent historical proof. | Requires per-harness mutation logic and careful uninstall. | Superseded as a supported product path by `decision:0006`. |
| Managed single-file block | Preserves existing user content when marker logic is correct. | Harder to validate in UI; conflicts possible; size and precedence concerns. | Historical fallback pattern, not current product surface. |
| Generic `~/.agents/skills` | Portable for some harnesses; reduces duplicated skills. | Harness support varies; does not itself enforce `using-loom` first-use. | Use only when it is the harness-native skill surface. |
| Native plugin/extension package | Better install/update/disable/marketplace UX; documents package boundaries. | Harness-specific package files; may not cover optional preload. | Preferred product path when it exposes `skills/`. |
| Project-local install | Version-controlled and team-visible. | Not a global user install; can pollute projects if used casually. | Good for teams adopting Loom per repository. |
| Manual clone/link | Maximum transparency and low tooling. | Poor uninstall/update UX; user must know harness paths. | Useful developer/testing path, not best default. |

## Installer Precedent Comparison

Popular installer patterns provide useful product lessons but do not transfer
directly to Loom.

### Package Managers

Homebrew precedent:

- one-line shell installer bootstraps the package manager itself
- packages install into Homebrew-owned directories and symlink into a prefix
- Homebrew avoids installing files outside its prefix
- formulae/casks provide update and distribution conventions

VS Code extension marketplace precedent:

- extensions can be packaged as `.vsix` files for private/off-market install
- marketplace publishing provides discovery, versioning, publisher identity, and
  install analytics
- compatibility is declared through metadata such as `engines.vscode`

Loom implication:

- Package managers are good at installing a bundle or binary, but they do not
  solve per-harness instruction registration.
- A Homebrew formula for Loom could fetch the repo or install adapter packages,
  but it would still need post-install guidance or a separate adapter step to
  mutate harness config.
- A plugin marketplace is closer to the UX Loom wants when the harness's plugin
  system can express all needed surfaces.

### Standalone Shell Installers

uv precedent:

- supports `curl | sh`, PowerShell, package managers, Docker, Cargo, GitHub
  releases, and self-update for standalone installs
- lets users inspect installer scripts before execution
- documents update and uninstall differences by install method
- uses an opt-out environment variable for PATH mutation

rustup precedent:

- manages toolchains across channels and platforms
- installs binaries under a user-owned tool directory
- documents update and uninstall commands
- PATH setup is explicitly documented as a common source of post-install issues

Loom implication:

- A standalone installer script can be acceptable as a bootstrap/fallback, but it
  must make mutations explicit and reversible.
- Loom does not install a binary toolchain, so PATH management is not the main
  issue. The analogous risk is hidden mutation of harness config.
- If Loom keeps shell install, it should document update and uninstall clearly
  per method and support a dry-run or inspection posture before mutation.

### Dotfile And Framework Installers

Oh My Zsh precedent:

- the fetched homepage confirms a community-driven Zsh configuration framework
  with plugins and themes, but the extracted content did not provide detailed
  installer behavior.

Loom implication:

- Dotfile installers are an intuitive comparison because Loom installs into user
  config directories, but Loom must be stricter about not overwriting or owning
  unrelated user config.

### Project Scaffolders And Source-Copy Tools

shadcn/ui precedent:

- uses a CLI/init model for project setup across supported frameworks
- framework-specific guides distinguish new-project and existing-project setup

Loom implication:

- Project bootstrap could be a valid separate workflow for repositories that want
  Loom checked in as part of a project.
- Source-copy/project-scaffold patterns are less ideal for global user-level
  harness install because Loom's active surfaces live in harness config roots,
  not only in the target project.

## Option Comparison For Loom

| Option | Description | Pros | Cons | Research judgment |
| --- | --- | --- | --- | --- |
| Keep current Makefile/script as-is | Continue one shell adapter for all harnesses. | Historical proof existed. | Fragile, script-owned knowledge, weak first-class UX. | Reject; removed by `decision:0006`. |
| One monolithic `loom install` CLI | Build a real Loom installer command. | Could centralize validation and UX. | Conflicts with constitutional no-product-CLI direction and risks hidden ontology. | Reject for core. |
| Harness-native plugin/extension packages | Build per-harness packages that expose `skills/`. | Better install/update/disable/marketplace fit. | Surface coverage differs; adapters must not own semantics. | Preferred product path. |
| Generic Agent Skills install | Install skills once under `~/.agents/skills`. | Portable and reduces duplication. | Harness support varies; using-Loom first-use still needs instruction. | Use only where it is native to the harness. |
| Project-local Loom adoption | Commit Loom-compatible instructions/skills into a repository. | Version-controlled team adoption. | Different from global/native install; can mix product and project state. | Project adoption path, not package distribution. |
| Package manager formula | Homebrew/Nix/etc installs Loom bundle. | Familiar install/update. | Does not register with harnesses alone. | Optional distribution wrapper only. |
| `curl | sh` remote installer | One-line install from GitHub. | Easy onboarding. | Trust and mutation risk; hard to review if script changes remotely. | Reject for product distribution. |
| Manual clone/link | User clones repo and symlinks/copies surfaces. | Transparent and hackable. | High friction, poor uninstall/update. | Developer path, not default UX. |

# Rejected Options

## Plugin-Only Install For Every Harness

Rejected because native package coverage is uneven.

- The current direction is not one identical plugin mechanism everywhere; it is
  native skill-package distribution everywhere.
- Optional using-Loom preload is adapter-specific and must not become a fallback
  installer requirement.
- Harness support should be accepted only when that harness exposes `skills/` and
  preserves `using-loom` first-use.

## Generic On-Demand Skills As The Whole Entry Path

Superseded by `decision:0005`. The accepted shape is not an ordinary on-demand
subsystem skill; it is the mandatory `using-loom` entry skill. Harnesses may
preload its references, but the portable completeness path is explicit first-use
of `using-loom`.

## Claude Hook Hack For Loading Rules

Superseded in part by later Claude evidence. The accepted Claude adapter uses
plugin `SessionStart` stdout as optional source-marked using-Loom preload, not as a
fallback installer or doctrine owner. The residual risk is release hardening, not
the product surface model.

## Codex `~/.codex/rules/` For Loom Markdown Rules

Rejected by prior research because that surface is not equivalent to Loom
Markdown instructions. using-Loom references should remain under
`skills/using-loom/references/` and may be preloaded only through an actual
Codex instruction/context surface when that preload is explicitly configured.

## Cursor User Rules Database Mutation As The Strategic Endpoint

Rejected as the long-term ideal. Cursor work should evaluate native plugin or
skill-package distribution of `skills/` instead of direct state database writes.

## Package Manager As The Sole Install Story

Rejected because package managers can install the bundle but cannot by themselves
make each harness discover `skills/` or enforce `using-loom` first-use.

## Generated Aggregates As Canonical Truth

Rejected because generated instruction files or harness wrappers are adapter
outputs. Canonical behavior stays in `skills/`, especially `skills/using-loom`,
and the templates and references inside skills.

# Null Results

- Exa web search hit its free MCP rate limit during earlier broad discovery, so
  this record relies on direct official-doc fetches and repository inspection
  rather than additional web search result expansion.
- `https://cursor.com/docs/commands` returned `404` during direct fetch. Cursor
  command facts in this record come from Cursor plugin reference docs and prior
  repository research rather than that URL.
- `https://docs.anthropic.com/en/docs/claude-code/plugins` redirected to
  `https://code.claude.com/docs/en/plugins`; the redirect was blocked by the
  fetch tool, so the canonical `code.claude.com` URL was used directly.
- The fetched Oh My Zsh homepage did not expose detailed install, backup, update,
  or uninstall behavior in the extracted content, so it is not used as strong
  evidence beyond the broad dotfile-framework analogy.
- The fetched shadcn/ui installation page did not expose enough detail about the
  source-copy `add` model or registry update philosophy to use it as strong
  evidence beyond project scaffold/init comparison.

# Conclusions

1. Loom needs a per-harness install strategy, not a single universal adapter
   model.

2. The best install mechanism is the most native mechanism that can expose the
   `skills/` package and preserve mandatory `using-loom` first-use without
   changing Loom's source of truth.

3. Cursor plugins and Gemini CLI extensions remain native package candidates, but
   their acceptance should depend on exposing `skills/` and preserving
   `using-loom` first-use, not on copying fallback installer behavior.

4. Claude Code plugins and Codex plugins should be evaluated as native skills
   packages. Claude can additionally preload using-Loom references through plugin
   `SessionStart` stdout; Codex installed plugin skill discovery remains the next
   evidence gap.

5. OpenCode should continue through `open-loom` plugin-first validation. The
   ideal UX is a single `plugin` array entry in `opencode.json`. Current evidence
   validates local file plugin loading and `config(config)` registration for
   ordered using-Loom references and bundled skills. Operator validation indicates
   Git URL plugin specs are not supported, so npm publication and local file/path
   entries are the viable distribution paths.

6. Portable Agent Skills are the common product denominator for Loom across
   harnesses. A complete Loom install is a native package exposing `skills/` plus
   mandatory `using-loom` first-use; optional preload is an optimization.

7. `Makefile`, `scripts/install-loom.sh`, top-level `rules/`, and top-level
   `commands/` are removed as supported product surfaces by `decision:0006`.

8. The current install architecture has two layers:

- canonical product source: `skills/`, especially `skills/using-loom`, plus
  templates and references inside skills
- native adapter outputs: per-harness plugin/extension metadata and optional
  using-Loom preload hooks derived from the canonical source

9. Adapter outputs need validation fixtures and disable/uninstall expectations,
   but they must remain derivative. The project should be able to replace them
   without changing Loom's protocol truth.

# Recommendations

## Strategic Recommendation

Adopt a native skills-package strategy:

- use first-class plugin, extension, or skill-package systems to expose `skills/`
- require `using-loom` as the mandatory entry skill for every harness
- use optional using-Loom reference preload only when the native adapter can deliver
  it cleanly, as with Claude and OpenCode
- do not preserve fallback copy installers or top-level command wrappers as product
  surfaces

## Per-Harness Recommendation

| Harness | Recommended next strategy | Rationale |
| --- | --- | --- |
| OpenCode | Accepted plugin-first install via `open-loom@0.1.0`; investigate cold-cache first-run caveat separately. | Ideal UX is one `plugin` entry; npm package distribution and local file/path entries are validated. `ticket:us1brnsv` owns the remaining first-run package behavior. |
| Claude Code | Use the native plugin to expose `skills/` and optionally preload using-Loom references through `SessionStart` stdout. | Skills remain the product surface; preload is an adapter bonus with documented ordering limits. |
| Codex | Validate Git-backed plugin skill discovery for `using-loom`. | Plugins package skills; project-local hooks are optional preload proof, not product install. |
| Gemini CLI | Prototype a native extension or skill-package adapter. | Acceptance depends on exposing `skills/` and preserving `using-loom` first-use. |
| Cursor | Prototype a native plugin or skill-package adapter. | Acceptance depends on exposing `skills/` without treating generated rule files as product truth. |

## Implementation Sequencing Recommendation

1. Keep the fallback installer removed; do not reintroduce it while prototyping
   native adapters.
2. Prototype Cursor plugin or skill-package packaging around `skills/` and
   `using-loom` first-use.
3. Prototype Gemini extension packaging around `skills/` and `using-loom`
   first-use.
4. Use the accepted OpenCode package as the first concrete adapter-package
   precedent, but do not assume other harnesses expose equivalent APIs.
5. Re-evaluate Claude and Codex native plugin shapes after installed skill
   discovery evidence improves.
6. Treat shared `~/.agents/skills` only as a harness-native surface if a harness
   explicitly supports it; do not recreate a cross-harness copy installer.
7. Update `INSTALL.md` only after the preferred path is implemented or at least
   captured in a ready ticket.

## Validation Recommendation

For any future install implementation ticket, require evidence for:

- native package contents and adapter metadata
- disable/uninstall behavior through the harness's native package manager when
  available
- `using-loom` is discoverable as the mandatory entry skill
- optional using-Loom preload, when present, points at
  `skills/using-loom/references/`
- skills are discoverable by name/description without eagerly loading full skill
  references/templates
- adapter outputs identify their Loom source files
- plugin or extension packages can be installed, disabled, or linked through the
  harness's documented commands where applicable

## Documentation Recommendation

Split future install docs into two conceptual modes:

- native harness install: install or enable a plugin, extension, or skill package
  that exposes `skills/`
- adapter/package development: validate harness-specific plugin or extension
  packages against canonical Loom skills

# Open Questions

- Which harnesses can consume `skills/` directly, and which require native package
  metadata around the same directory?
- Should the Claude marketplace continue using source `./` for local/Git testing,
  or should a narrower release-packaged Claude plugin artifact be introduced
  before broad distribution?
- Can Cursor plugin rules set `alwaysApply: true` and preserve numeric rule order
  well enough to replace User Rules mutation?
- Does Gemini extension context loading preserve the mandatory ordered Loom rule
  behavior in real sessions?
- Should generated adapter packages live in the repository as committed fixtures,
  be generated only during release, or remain examples under `examples/`?
- What is the root cause of OpenCode `1.14.22` logging `NpmInstallFailedError` on
  the first cold-cache npm-package config-file run before succeeding on a second
  run?
- How should versioning work for adapter packages if Loom itself is source-only
  Markdown?
- Should install docs recommend marketplace installs for users and direct clone
  installs for contributors?
- Which install validations belong as evidence records versus non-normative
  adapter fixtures?

# Linked Work

- Initiative: `initiative:loom-install-experience`
- Plan: `plan:install-experience-harness-adapters`
- Harness ticket: `ticket:6uy1rx20` - OpenCode plugin-first install path
- Follow-up ticket: `ticket:us1brnsv` - OpenCode cold-cache npm-plugin first-run
  behavior
- Spec: `spec:opencode-plugin-install-contract`
- Wiki: `wiki:harness-adapter-package-pattern`
- Harness ticket: `ticket:q7h1d05q` - Claude Code hybrid install path
- Claude hybrid evidence: `evidence:claude-plugin-hybrid`
- Harness ticket: `ticket:lx9nnztk` - Codex hybrid plugin install path
- Harness ticket: `ticket:7ex8w32y` - Gemini CLI extension install path
- Harness ticket: `ticket:3t93tsci` - Cursor plugin install path
- Prior path-mapping research: `research:harness-install-surfaces`
- Prior Codex command adapter research: `research:codex-command-skill-installation`
- Focused Codex plugin research: `research:codex-plugin-distribution-surfaces`
- Prior installer ticket: `ticket:ffg8elkb`
- Prior Codex adapter ticket: `ticket:p9m4x2qt`
- Prior Cursor installer ticket: `ticket:rd48g1kg`
- Prior Cursor validation evidence: `evidence:cursor-harness-install-validation`

Downstream work should create bounded tickets before adding or changing native
adapter package directories.
