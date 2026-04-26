# Claude Plugin Install

## Transport Surface

- `.claude-plugin/plugin.json` makes the repository root loadable as a Claude Code
  plugin during local development.
- `.claude-plugin/marketplace.json` makes the repository root a local Claude Code
  marketplace named `agent-loom` with one plugin named `loom`.
- the plugin exposes canonical `skills/` and optional `commands/` directly from
  the repository root.
- Claude auto-loads the standard plugin `hooks/hooks.json`; the plugin manifest
  does not repeat that hook path.
- `hooks/hooks.json` registers a `SessionStart` command hook that runs
  `scripts/claude-sync-rules.sh`.
- `hooks/hooks.json` also registers a `UserPromptSubmit` command hook that runs
  `scripts/claude-loom-restart-guard.sh`.
- `scripts/claude-sync-rules.sh` generates one managed `loom.md` from canonical
  `${CLAUDE_PLUGIN_ROOT}/rules/*.md` into a Claude-loaded rule directory:
  `${CLAUDE_PROJECT_DIR}/.claude/rules/loom/` only when project Claude settings
  explicitly enable the `loom` plugin, otherwise `~/.claude/rules/loom/` for the
  user-level path.
- `scripts/claude-clean-rules.sh` removes generated managed rules for explicit
  user or project cleanup.

## Chosen Hybrid Shape

Use the Claude plugin for discoverable skills, command wrappers, and automatic
rule synchronization into Claude's user or project rule surface.

This avoids three wrong solutions:

- custom agents as a substitute for Loom's rule corpus
- hook stdout or dynamic context as the static rule loader
- plugin settings that pretend to register arbitrary always-on instructions

## Expected Properties

- plugin validation passes with `claude plugin validate .`
- plugin skills remain `SKILL.md` directories from canonical `skills/`
- command wrappers remain optional invocation surfaces from canonical `commands/`
- the plugin session hook generates one managed `loom.md` from canonical `rules/`
  into a
  scope-appropriate Claude rule surface without making generated files a new
  truth owner
- the sync chooses project rules only from an explicit `enabledPlugins` entry for
  `loom`, not from `.claude/` directory existence
- the sync is silent on success so hook stdout does not become a hidden context
  channel
- when the sync had to install or update rules for the current session, the
  prompt guard blocks user prompts and tells the user to restart before
  resubmitting

## Limitations

- Claude plugin docs do not currently describe an install-time script hook or a
  plugin manifest field for arbitrary always-on rules.
- The sync runs when a plugin-enabled session starts, not during the literal
  `claude plugin install` command.
- `${CLAUDE_PLUGIN_ROOT}` is the plugin installation/cache directory. Claude docs
  do not describe `${CLAUDE_PLUGIN_ROOT}/rules` as a loaded instruction surface.
- The generated single `loom.md` avoids depending on Claude's ordering of multiple
  user-rule files.
- Runtime validation showed newly generated project rules do not load in the same
  first plugin-enabled session. They load on the next session in the same project.
- The first prompt after a bootstrap sync is intentionally blocked because Claude
  has not loaded the newly created rule files yet.
- Claude plugin docs do not describe an uninstall lifecycle hook that would remove
  synchronized user-rule files automatically when the plugin is disabled or
  uninstalled.
- The marketplace currently uses source `./` for local/Git marketplace installs,
  which means the repository root is the plugin source. A release-packaged Claude
  plugin artifact should narrow this before broad distribution.

## Common Wrong Behavior

- calling a Claude plugin install complete when Loom rules were not installed
- relying on a plugin custom agent's prompt as the Loom operating layer
- printing static Loom rules from the `SessionStart` hook instead of installing
  them into Claude's real rule surface
- copying dogfooding `.loom/` records into the plugin package

## Cleanup

```bash
scripts/claude-clean-rules.sh user
CLAUDE_PROJECT_DIR=/path/to/project scripts/claude-clean-rules.sh project
```

The cleanup script only removes files named in `.loom-plugin-manifest`; it refuses
to clean a Loom rules directory without a managed manifest.
