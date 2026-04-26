---
id: research:harness-install-surfaces
kind: research
status: superseded
created_at: 2026-04-18T03:03:47Z
updated_at: 2026-04-26T07:23:57Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:ffg8elkb
    - ticket:rd48g1kg
  research:
    - research:codex-command-skill-installation
  evidence:
    - evidence:cursor-harness-install-validation
  decision:
    - decision:0006
---

# Supersession Note

This research is historical. `decision:0006` supersedes its recommendations by
removing fallback installers, top-level `rules/`, and top-level `commands/` as
supported product surfaces. Current install work should use native harness plugin,
extension, or skill-package systems that expose canonical `skills/`, with
`loom-bootstrap` as the mandatory entry skill.

# Question

Historical question: what user-level install surfaces did OpenCode, Claude Code,
Codex, Gemini CLI, and Cursor expose for direct copy installs before Loom adopted
the native skills-package strategy?

# Why This Matters

The repository wants a simple global install path from the canonical shipped
bundle, not from dogfooding `.loom/` or `.opencode/` state.

If the harness surfaces differ, the installer needs to map Loom truthfully
instead of pretending every harness uses the same directory structure or file
format.

# Scope

- inspect only the canonical product surfaces: top-level `rules/`, `skills/`,
  and optional `commands/`
- identify user-level install paths for OpenCode, Claude Code, Codex, Gemini
  CLI, and Cursor
- note where a harness supports direct copies versus where translation is
  required
- inspect local home-directory state only to confirm currently used config
  locations

# Method

Read official harness docs for user-level config, instruction, skill, and
command locations.

Cross-check those findings against the local filesystem under
`~/.config/opencode/`, `~/.claude/`, `~/.codex/`, and `~/.gemini/`.

# Sources

- OpenCode config docs: `https://opencode.ai/docs/en/config/`
- Claude Code `.claude` directory docs:
  `https://code.claude.com/docs/en/claude-directory.md`
- Codex AGENTS docs:
  `https://developers.openai.com/codex/guides/agents-md`
- Codex skills docs: `https://developers.openai.com/codex/skills`
- Gemini CLI configuration docs:
  `https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html`
- Gemini CLI custom commands docs:
  `https://google-gemini.github.io/gemini-cli/docs/cli/custom-commands.html`
- Gemini CLI command reference snippets documenting `~/.gemini/agents` and
  `~/.gemini/commands`
- Cursor rules docs: `https://cursor.com/docs/rules`
- Cursor commands docs: `https://cursor.com/docs/commands`
- Cursor 2.4 changelog for Agent Skills:
  `https://cursor.com/changelog/2-4`
- Cursor agent best-practices note on rules vs skills:
  `https://cursor.com/blog/agent-best-practices`
- Cursor support guidance for global commands and user/project skills:
  `https://forum.cursor.com/t/custom-commands-no-longer-function-at-all-in-cursor/138221`
  and
  `https://forum.cursor.com/t/cursor-doesnt-know-new-skills-arens-saved/158507`
- local files: `~/.claude/settings.json`, `~/.codex/config.toml`,
  `~/.gemini/settings.json`, `~/.config/opencode/`, and absence/presence checks
  under `~/.cursor/`

# Evidence

- OpenCode user config lives in `~/.config/opencode/`; global commands and
  skills live in plural subdirectories there, while always-on rules are best
  wired through `~/.config/opencode/opencode.json` via the `instructions` array.
- Claude Code reads global instructions and extensions from `~/.claude/`,
  including `~/.claude/rules/`, `~/.claude/skills/`, and
  `~/.claude/commands/`.
- Codex uses a split global surface:
  `~/.codex/AGENTS.md` for always-on instructions,
  `$HOME/.agents/skills` for global skills, and skills as the current reusable
  workflow surface.
- Codex skills support explicit `$skill` invocation and can disable implicit
  invocation with `agents/openai.yaml` policy `allow_implicit_invocation: false`.
- Codex's `~/.codex/rules/` is a shell-exec policy surface, not an equivalent
  home for Loom Markdown rules, so Loom rules should not be copied there.
- Gemini CLI uses `~/.gemini/settings.json` plus hierarchical context from
  `~/.gemini/GEMINI.md`; custom commands live in `~/.gemini/commands/` and use
  TOML, not Markdown.
- Gemini CLI supports user-level subagents in `~/.gemini/agents/` and supports
  skill discovery with `.agents/skills` / `~/.agents/skills` as the generic
  cross-tool skill location.
- Cursor project rules live in `.cursor/rules/*.mdc`, and Cursor user rules are
  configured through Cursor settings rather than a documented Markdown file.
- Cursor custom commands are Markdown files in `.cursor/commands/`; support
  guidance also describes `~/.cursor/commands/` for global user commands.
- Cursor Agent Skills are defined by `SKILL.md` files. Current support guidance
  identifies `~/.cursor/skills/` for user-level skills and `.cursor/skills/`
  for project-level skills, while `~/.cursor/skills-cursor/` is reserved for
  Cursor-managed built-ins.
- The local machine already has user config roots at `~/.claude/`, `~/.codex/`,
  `~/.gemini/`, and `~/.config/opencode/`, matching the documented locations.
  No existing `~/.cursor/` user install tree was present during the inspection.

# Conclusions

- Claude Code can accept a near-direct copy of Loom's canonical bundle into
  matching global directories.
- OpenCode can also accept direct copies for `skills/` and `commands/`, but its
  always-on rules need a small config update so the installed rule files are
  loaded.
- Codex and Gemini CLI both need translation for at least one surface:
  Codex needs Loom rules aggregated into `~/.codex/AGENTS.md` and Loom commands
  adapted into explicit-only skill directories; Gemini commands need
  Markdown-to-TOML conversion.
- `~/.agents/skills` is the most interoperable global skill destination for
  both Codex and Gemini CLI.
- Cursor can take Loom skills directly under `~/.cursor/skills/` and command
  Markdown under `~/.cursor/commands/`.
- Cursor does not expose a documented global Markdown rules directory equivalent
  to project `.cursor/rules/*.mdc`; the global install should write Loom's
  rules into Cursor User Rules as a managed block.

# Recommendations

Superseded by `decision:0006`.

Do not add or restore a Makefile, shell installer, direct copy installer, or
top-level command-wrapper distribution. Native harness adapters should expose
canonical `skills/`; optional preload should read from
`skills/loom-bootstrap/references/` when a harness supports it cleanly.

# Open Questions

- Whether Gemini CLI should receive Loom commands as top-level `/name` commands
  or under a namespaced subtree such as `/loom:name` for collision safety.
- Whether future Codex UI behavior should show the generated command adapter
  skill name or the original slash-command-style display name more prominently.

# Linked Work

- `ticket:ffg8elkb`
