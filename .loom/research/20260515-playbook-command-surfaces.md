# Playbook Command Surfaces

Status: completed
Created: 2026-05-15
Updated: 2026-05-15

## Summary

Loom Playbooks can be moved away from automatic skill activation, but the exact
explicit macro surface differs by harness. OpenCode and Gemini have true custom
prompt-command files, Claude and Cursor can ship commands and also support
explicit-only skills, while Codex currently documents plugin-packaged skills with
explicit invocation and `allow_implicit_invocation: false`, not plugin-contributed
custom slash-command prompt files.

## Question

Can Loom Playbooks be distributed as explicitly invoked command or prompt macros
across Agent Loom's supported harnesses, so they no longer auto-activate as
workflow skills during ordinary natural-language work?

## Scope

Covered:

- Supported harnesses currently named by this repository: OpenCode, Claude Code,
  Codex, Cursor, and Gemini CLI.
- Repository package and manifest surfaces that currently expose Playbooks as
  skills.
- Official documentation available on 2026-05-15 for command, prompt, skill,
  plugin, and extension surfaces.
- Prior Loom research on Playbook activation stacking and direct agent surfaces.

Excluded:

- Live runtime validation in each harness.
- Implementing the Playbook conversion.
- Designing final command names, argument conventions, or generated file layout.
- Non-supported harnesses.

## Method And Sources

- `.loom/research/20260515-playbooks-core-activation-pressure.md` - current diagnosis that
  Playbooks are useful lenses but harmful when installed as broad auto-activated
  skills.
- `.loom/evidence/20260515-playbook-activation-stacking.md` - OpenCode observations that
  simple prompts loaded multiple Playbook skills.
- `.loom/research/20260514-direct-interactive-agent-surfaces.md` - existing supported
  harness matrix and adapter-source survey.
- `loom-playbooks/loom-playbooks.mjs` - current OpenCode package registers the
  whole `skills/` tree through `config.skills.paths`.
- `loom-playbooks/.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  `.cursor-plugin/plugin.json`, and `gemini-extension.json` - current native
  package manifests expose skills, not commands.
- OpenCode docs `https://opencode.ai/docs/commands/` and config schema
  `https://opencode.ai/config.json`, accessed 2026-05-15.
- OpenCode plugin docs `https://opencode.ai/docs/plugins/`, accessed 2026-05-15.
- Claude Code docs `https://docs.anthropic.com/en/docs/claude-code/skills`,
  `https://docs.anthropic.com/en/docs/claude-code/commands`, and
  `https://docs.anthropic.com/en/docs/claude-code/plugins-reference`, accessed
  2026-05-15.
- Codex docs `https://developers.openai.com/codex/plugins`,
  `https://developers.openai.com/codex/plugins/build`,
  `https://developers.openai.com/codex/skills`,
  `https://developers.openai.com/codex/cli/slash-commands`,
  `https://developers.openai.com/codex/ide/slash-commands`, and
  `https://developers.openai.com/codex/app/commands`, accessed 2026-05-15.
- Cursor docs `https://cursor.com/docs/plugins`,
  `https://cursor.com/docs/reference/plugins`, and
  `https://cursor.com/docs/skills`, accessed 2026-05-15.
- Gemini CLI docs
  `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/index.md`,
  `docs/extensions/writing-extensions.md`, `docs/extensions/reference.md`,
  `docs/cli/custom-commands.md`, and `docs/cli/skills.md`, accessed 2026-05-15.

## Findings

### Current Playbook Exposure

- Playbooks currently ship as 25 model-visible skills. `loom-playbooks.mjs`
  registers the package `skills/` directory through OpenCode `config.skills.paths`,
  and the Claude, Codex, and Cursor manifests point at `./skills/`.

- The current shape is exactly what creates activation pressure: Core says every
  relevant Loom skill must be invoked before action, so broad Playbook skill
  descriptions become mandatory first-action candidates once installed.

### OpenCode

- OpenCode supports true custom commands. Commands can be defined in the JSON
  `command` config or by Markdown files under `~/.config/opencode/commands/` or
  project `.opencode/commands/`.

- OpenCode command files are prompt templates invoked with `/command`. They support
  `$ARGUMENTS`, positional arguments, shell output injection, file references, and
  optional `agent`, `subtask`, and `model` settings.

- OpenCode plugins can mutate config, and the config schema includes a `command`
  object with `template`, `description`, `agent`, `model`, and `subtask`. Therefore
  `loom-playbooks.mjs` can add Playbook commands directly without exposing them as
  skills.

- OpenCode command macros are user-invoked in the TUI. They do not need to be part
  of the model's automatic skill-selection list.

### Claude Code

- Claude Code now treats custom commands as part of the skills mechanism. The docs
  say custom commands have been merged into skills: a `.claude/commands/deploy.md`
  file and a `.claude/skills/deploy/SKILL.md` both create `/deploy`, and existing
  `.claude/commands/` files keep working.

- Claude plugin manifests support both `skills` and `commands` component paths.
  The plugin reference says plugin `commands/` are flat Markdown files and can be
  listed through the `commands` manifest key.

- Claude's crucial explicit-only control is `disable-model-invocation: true`.
  When set on a skill, only the user can invoke it with `/name`; Claude cannot
  auto-load it based on natural language, and its description is not in the model
  context.

- For Loom Playbooks, Claude can either ship a `commands/` directory or ship
  skills with `disable-model-invocation: true`. Because Claude says commands are
  merged into skills, the explicit-only flag is the safer requirement to prevent
  Playbooks from re-entering automatic activation.

### Codex

- Codex has built-in slash commands in CLI, IDE, and app surfaces, but the fetched
  command docs describe built-in control commands, not user/plugin-defined custom
  slash commands.

- Codex plugin docs currently say plugins bundle skills, apps, MCP servers, and
  hooks. The build docs show a manifest with `skills`, `mcpServers`, `apps`,
  `hooks`, and install-surface `interface.defaultPrompt`, but not a `commands` or
  `prompts` component path.

- Codex skills can be explicitly invoked. The app docs say users can type `$` to
  invoke skills, and the plugin docs say users can type `@` to invoke a plugin or
  one of its bundled skills explicitly. The skills docs say explicit invocation is
  one activation mode.

- Codex skills support `agents/openai.yaml` with `policy.allow_implicit_invocation:
  false`. The docs say that when false, Codex will not implicitly invoke the skill
  from the user prompt; explicit `$skill` invocation still works.

- Therefore the supported Codex route is explicit-only Playbook skills, not a
  separate plugin-contributed prompt-command surface. `interface.defaultPrompt` is
  install-surface suggestion text, not a reusable prompt macro catalog.

### Cursor

- Cursor plugins can package commands. The plugin docs and reference list
  `commands/` as a component, support `commands` in the manifest, and define command
  files as `.md`, `.mdc`, `.markdown`, or `.txt` under `commands/` with optional
  `name` and `description` frontmatter.

- Cursor skills can also be manually invoked with `/skill-name`, and Cursor's
  skills docs include `disable-model-invocation: true`, explicitly described as
  making a skill behave like a traditional slash command that is only included when
  the user types `/skill-name`.

- Cursor includes a built-in migration path from slash commands to skills, where
  migrated slash commands become skills with `disable-model-invocation: true` to
  preserve explicit invocation behavior.

- For Loom Playbooks, Cursor can ship either plugin commands or explicit-only
  skills. Explicit-only skills may fit Cursor's current direction better, but true
  plugin command files are documented.

### Gemini CLI

- Gemini CLI extensions explicitly package custom commands. The extension overview
  says extensions can include custom commands; the writing guide shows `commands/`
  TOML files; the reference says extensions provide custom commands by placing TOML
  files in a `commands/` subdirectory.

- Gemini custom commands are user-invoked prompt macros such as `/fs:grep-code`.
  They support required `prompt`, optional `description`, `{{args}}`, shell
  injection with confirmation, and file injection. Commands may be global under
  `~/.gemini/commands/` or project-local under `.gemini/commands/`.

- Extension commands have lower precedence than user or project commands. If an
  extension command conflicts, Gemini prefixes it with the extension name.

- Gemini skills remain model-activated through `activate_skill`, so moving
  Playbooks to `commands/` is the cleaner way to prevent model-driven activation in
  Gemini.

## Tradeoffs

- True command files where available.
  Strength: best matches the desired product behavior: user-invoked prompt macros,
  no model-triggered activation. Weakness: each harness has different file formats,
  naming, substitution, and manifest/discovery rules.

- Explicit-only skills where command components are unavailable or merged into
  skills.
  Strength: preserves package distribution and progressive loading while stopping
  implicit activation in Claude, Cursor, and Codex. Weakness: still called skills,
  so Core wording and install docs must be clear that these are user-invoked
  macros, not Loom-owned first-action routes.

- Keep Playbooks as ordinary auto-invoked skills with narrower descriptions.
  Strength: smallest package change. Weakness: does not solve the worst failure
  mode, because broad natural language can still trigger Playbooks before Core
  shaping finishes.

## Rejected Paths And Null Results

- A universal `commands/` directory is not supported across all harnesses. OpenCode
  and Gemini use different command file formats, Claude commands are now merged
  into skills, Cursor documents command files, and Codex plugin docs do not expose a
  command or prompt component.

- Treating Codex `interface.defaultPrompt` as reusable prompt macros is rejected.
  The field appears in plugin install/presentation metadata, while reusable
  workflow packaging is documented as skills.

- Treating Codex built-in slash commands as a plugin extension point is rejected by
  current docs. The CLI, IDE, and app command pages list built-in commands and
  explicit skill invocation, not custom plugin-contributed slash prompt files.

- Leaving Gemini Playbooks as extension skills would not solve the activation
  problem, because Gemini skill discovery injects skill metadata and lets the model
  activate matching skills.

## Conclusions

- The operator's command-macro direction is substantially right. Playbooks are
  better modeled as explicit user-invoked workflow macros than model-activated Loom
  skills.

- The product should use a harness-adapted implementation, not one file shape:
  OpenCode `command` config or command Markdown, Claude commands or explicit-only
  skills, Codex explicit-only skills with `allow_implicit_invocation: false`, Cursor
  commands or explicit-only skills, and Gemini `commands/*.toml`.

- Codex is the limiting harness. Current public docs do not support the claim that
  Codex plugins can contribute custom prompt commands separate from skills. The
  safe Codex design is to package each Playbook as a skill that cannot be implicitly
  invoked and must be called explicitly with `$skill` or plugin explicit invocation.

- Core auto-activation doctrine should continue to apply to Core record skills. It
  should not require agents to invoke Playbook macros automatically; Playbooks must
  be outside the model's first-action skill-selection pressure where the harness
  permits it, or marked explicit-only where the harness routes commands through
  skills.

## Recommendations

- Convert Playbooks from auto-activated skills to explicit macros.

- Use the following target surfaces:
  - OpenCode: add `config.command` entries from `loom-playbooks.mjs`, probably
    generated from a canonical Playbook source tree.
  - Claude Code: ship `commands/` or explicit-only `skills/`; require
    `disable-model-invocation: true` if the implementation uses skills.
  - Codex: keep Playbooks as skills but add `agents/openai.yaml` with
    `policy.allow_implicit_invocation: false` for each Playbook, and document `$`
    or explicit plugin/skill invocation instead of custom slash commands.
  - Cursor: ship plugin `commands/` or explicit-only skills with
    `disable-model-invocation: true`; prefer the form that local validation shows is
    surfaced best in Cursor's UI.
  - Gemini CLI: ship `commands/*.toml` in the Playbooks extension and remove the
    Playbook `skills/` exposure.

- Keep a canonical source for Playbook bodies and generate/adapt harness-specific
  command files from it if the implementation would otherwise create five drifting
  copies.

- Update `using-loom` activation discipline so Playbook macros are explicitly not
  part of the mandatory 1% skill activation loop unless the user invokes one or a
  Core record skill deliberately routes to one as optional guidance.

- Create a spec for the Playbook macro behavior before implementation. It should
  define explicit invocation, no implicit model activation, argument handling,
  command naming, relationship to Core record skills, and supported-harness limits.

- Then create a plan or tickets to convert package surfaces, docs, smoke checks,
  and activation tests together.

## Open Questions

- Should the macro names keep the `loom-` prefix, use a namespaced form such as
  `/loom:debugging`, or vary by harness to match each command system's convention?
- Should Claude and Cursor prefer command files or explicit-only skills when both
  are documented?
- Should OpenCode commands dispatch the current primary agent or specify a Loom
  agent for any Playbook macro?
- How much of each Playbook body should be included directly in prompt macros versus
  kept in shared references to avoid package drift?

## Related Records

- `.loom/research/20260515-playbooks-core-activation-pressure.md` - explains why automatic
  Playbook skill activation harms Core routing.
- `.loom/evidence/20260515-playbook-activation-stacking.md` - preserves observed activation
  stacking.
- `.loom/research/20260514-direct-interactive-agent-surfaces.md` - prior harness capability
  survey for named agents.
- `loom-playbooks/` - current package surface to convert.
