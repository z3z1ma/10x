# Native Playbook Explicit Surfaces

ID: ticket:20260515-native-playbook-explicit-surfaces
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - changes Claude, Cursor, and Codex plugin-facing Playbook behavior and must avoid overclaiming unsupported Codex commands.
Priority: medium - native adapter surfaces should align before docs and final validation are rewritten.
Depends On: ticket:20260515-playbook-macro-catalog

## Summary

Update Claude Code, Cursor, and Codex Playbook plugin surfaces so Playbooks are explicit-only. The closure claim is that these native adapters no longer present Playbooks as ordinary implicitly invokable workflow skills: Claude and Cursor use commands or `disable-model-invocation: true`, and Codex uses explicit-only skills with `policy.allow_implicit_invocation: false`.

## Related Records

- `plan:20260515-playbook-explicit-macros` - defines sequencing and validation posture for this adapter unit.
- `ticket:20260515-playbook-macro-catalog` - provides the canonical macro source this ticket should consume.
- `spec:playbook-explicit-macros` - defines explicit-only requirements for Claude, Cursor, and Codex.
- `research:20260515-playbook-command-surfaces` - records command and explicit-only skill support by harness.
- `audit:20260515-native-playbook-explicit-surfaces` - clear Ralph-backed review of ACC-001 through ACC-005.
- `loom-playbooks/.claude-plugin/plugin.json` - current Claude plugin manifest.
- `loom-playbooks/.cursor-plugin/plugin.json` - current Cursor plugin manifest.
- `loom-playbooks/.codex-plugin/plugin.json` - current Codex plugin manifest.
- `loom-playbooks/skills/` - current shared Playbook skill corpus, if the implementation keeps explicit-only skills for these adapters.

## Scope

May change Claude, Cursor, and Codex plugin manifests, adapter-specific command or skill files, explicit-only skill metadata, and package-local files needed for those plugin surfaces.

Claude and Cursor may use command files or explicit-only skills. If skills are used, they must include `disable-model-invocation: true` in the harness-supported location.

Codex must use explicit-only plugin skills with `policy.allow_implicit_invocation: false` unless source-backed research added after `research:20260515-playbook-command-surfaces` proves plugin-contributed prompt commands.

Must not claim Codex custom Playbook slash commands. Must not update OpenCode, Gemini, or general docs except for inline plugin metadata required for native surfaces.

## Acceptance

- ACC-001: Claude Playbooks are exposed through commands or explicit-only skills, and no Claude Playbook surface remains implicitly model-invokable.
  - Evidence: Source inspection of `.claude-plugin` manifest and any command or skill metadata; `claude plugin validate "$PWD/loom-playbooks"` if available and applicable.
  - Audit: Review should challenge whether Claude's commands-as-skills merger could still cause implicit invocation.

- ACC-002: Cursor Playbooks are exposed through commands or explicit-only skills, and no Cursor Playbook surface remains implicitly model-invokable.
  - Evidence: Source inspection of `.cursor-plugin` manifest and any command or skill metadata.
  - Audit: Review should challenge whether the chosen Cursor surface matches current docs and preserves explicit invocation.

- ACC-003: Codex Playbooks use explicit-only skills with `policy.allow_implicit_invocation: false` and documentation-facing plugin metadata does not claim unsupported custom prompt commands.
  - Evidence: Source inspection of `.codex-plugin` manifest, skill-local `agents/openai.yaml` or equivalent policy files, and Codex interface text.
  - Audit: Review should challenge whether Codex support is honest about `$skill` or plugin explicit invocation and avoids slash-command claims.

- ACC-004: Native adapter Playbook bodies are generated from or aligned with the canonical macro catalog.
  - Evidence: Source inspection comparing adapter surfaces to the catalog or generation path.
  - Audit: Review should challenge body drift and missing Playbooks.

- ACC-005: Product-visible native adapter content avoids contributor-only package smoke, adapter mechanics, dogfood state, npm packaging, test harness details, and repository workflow commentary.
  - Evidence: Targeted grep/source inspection over changed native adapter command or skill files.
  - Audit: Review should challenge product-surface leakage before closure.

## Current State

Closed. Ralph packet `packet:20260515T220601Z-native-playbook-explicit-surfaces` implemented the minimal documented explicit-only skill route for Claude, Cursor, and Codex. All 25 Playbook `SKILL.md` files now set `disable-model-invocation: true` for Claude/Cursor explicit-only behavior, and each Playbook now has a Codex `agents/openai.yaml` with `policy.allow_implicit_invocation: false`. Native plugin metadata now describes Playbooks as explicit-only workflow lenses and the Codex interface text avoids custom slash-command claims.

Evidence gathered: source inspection found 25 `disable-model-invocation: true` entries across 25 Playbook skills, 25 `allow_implicit_invocation: false` policy entries across 25 Codex skill-local policy files, no unsupported Codex slash-command/custom-command claims in the Codex plugin metadata, and no material contributor-only leakage in the changed native surfaces. `claude plugin validate "$PWD/loom-playbooks"` passed, and `git diff --check` passed. The only leakage-pattern grep hit was existing generic debugging content, `test harness to system under test`, not package/test-harness workflow leakage.

Audit `audit:20260515-native-playbook-explicit-surfaces` returned `clear` with no material findings. ACC-001 through ACC-005 are satisfied for the native adapter closure claim. Residual limits are explicit: no live Claude, Cursor, or Codex runtime invocation was run; Cursor and Codex native validators were not run; and native explicit-only skill surfaces rely on explicit-only metadata plus shared `SKILL.md` bodies rather than generated macro preamble bodies.

## Journal

- 2026-05-15: Created ticket from `plan:20260515-playbook-explicit-macros`; depends on the canonical macro catalog ticket.
- 2026-05-15: Set status to active and launched `packet:20260515T220601Z-native-playbook-explicit-surfaces` after the catalog ticket closed.
- 2026-05-15: `packet:20260515T220601Z-native-playbook-explicit-surfaces` returned `stop`: added Claude/Cursor explicit-only frontmatter to all 25 Playbooks, added Codex per-skill `agents/openai.yaml` explicit-only policies, tightened native plugin metadata, validated the Claude plugin, and ran `git diff --check`. Moved ticket to review because audit/acceptance review is the next closure step.
- 2026-05-15: Recorded clear Ralph-backed audit in `audit:20260515-native-playbook-explicit-surfaces` and closed the ticket with runtime-validation limits explicit.
