# Playbook Skill Corpus Relocation Implementation

ID: packet:20260515T230227Z-playbook-skill-corpus-relocation
Type: Packet
Status: consumed
Created: 2026-05-15 23:02 UTC
Updated: 2026-05-15 23:07 UTC
Target: ticket:20260515-playbook-skill-corpus-relocation
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 1
Risk: medium - moves shared Playbook package source path across adapters.
Verification Posture: observation-first
Change Class: Playbooks package layout relocation

## Mission

Implement `ticket:20260515-playbook-skill-corpus-relocation`: move the shared Playbook skill corpus out of top-level `loom-playbooks/skills/` so Gemini no longer auto-discovers Playbooks as extension skills, while preserving OpenCode commands and Claude/Cursor/Codex explicit-only skill surfaces through the relocated path.

## Context Bundle

Records:

- `ticket:20260515-playbook-skill-corpus-relocation` - target ticket, scope, acceptance, and current state.
- `decision:0001` - durable package decision selecting the corpus-move route.
- `research:20260515-gemini-playbooks-skills-root` - Gemini docs conflict that requires relocation.
- `plan:20260515-playbook-explicit-macros` - broader conversion plan and downstream tickets.
- `spec:playbook-explicit-macros` - behavior contract requiring Gemini commands and no Playbook skill exposure.
- `ticket:20260515-playbook-macro-catalog` and `audit:20260515-playbook-macro-catalog` - catalog seam and clear audit.
- `ticket:20260515-opencode-playbook-commands` and `audit:20260515-opencode-playbook-commands` - OpenCode command surface that must continue working after relocation.
- `ticket:20260515-native-playbook-explicit-surfaces` and `audit:20260515-native-playbook-explicit-surfaces` - native explicit-only surface that must follow the relocated path.
- `ticket:20260515-gemini-playbook-commands` - blocked downstream consumer.
- `AGENTS.md` - contributor guidance with current package path assumptions.

Evidence Or Artifacts:

- Prior audits are clear for catalog, OpenCode, and native explicit-only semantics before relocation.

Files, Diffs, Or External References:

- `loom-playbooks/skills/**` - source corpus to move.
- `loom-playbooks/playbooks/**` - recommended successor path unless implementation finds a better non-Gemini-discovered path.
- `loom-playbooks/loom-playbooks.mjs` - catalog loader and OpenCode command registration.
- `loom-playbooks/package.json` - package file list.
- `loom-playbooks/.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json` - native skill path references.
- `AGENTS.md` - package surface guidance.

## Read Scope

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md`
- `.loom/constitution/decisions/decision-0001-playbook-skill-corpus-root.md`
- `.loom/research/20260515-gemini-playbooks-skills-root.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/tickets/20260515-opencode-playbook-commands.md`
- `.loom/audit/20260515-opencode-playbook-commands.md`
- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md`
- `.loom/audit/20260515-native-playbook-explicit-surfaces.md`
- `.loom/tickets/20260515-gemini-playbook-commands.md`
- `AGENTS.md`
- `loom-playbooks/skills/**`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md` - update Current State and Journal with progress, blockers, evidence, or completion disposition.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `loom-playbooks/skills/**` - move away from top-level root.
- `loom-playbooks/playbooks/**` or chosen successor path - relocated corpus.
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `AGENTS.md`

Do not create Gemini `commands/*.toml`, broad docs/tests, or unrelated package changes in this packet.

## Source Snapshot

Current state before relocation:

- `loom-playbooks/skills/` exists and contains 25 Playbook directories with `SKILL.md` files.
- All 25 `SKILL.md` files include `disable-model-invocation: true` from the native explicit-only ticket.
- Each Playbook directory has `agents/openai.yaml` with `policy.allow_implicit_invocation: false` from the native explicit-only ticket.
- `loom-playbooks/loom-playbooks.mjs` reads from `skills/`, derives macro catalog entries, and registers OpenCode commands from that catalog.
- Claude/Cursor/Codex manifests still point at `./skills/`.
- `loom-playbooks/package.json` still packs `skills/`.
- `AGENTS.md` still describes `loom-playbooks/skills/` as the Playbooks product surface.

## Task

Implement the smallest package relocation that satisfies `ticket:20260515-playbook-skill-corpus-relocation#ACC-001` through `ACC-005`.

Guidance:

- Use `loom-playbooks/playbooks/` as the successor path unless a source-backed reason suggests a better non-Gemini-discovered name.
- Preserve all 25 Playbook directories, `SKILL.md` files, `disable-model-invocation: true`, and Codex `agents/openai.yaml` policies.
- Update OpenCode catalog loading so `npm --prefix loom-playbooks run smoke` still reports 25 commands and no Playbook skill paths.
- Update Claude/Cursor/Codex manifests to point to the relocated skill corpus path.
- Update package file inclusion so pack dry-run includes the relocated corpus and not stale top-level `skills/`.
- Update `AGENTS.md` only where contributor guidance and package path facts would otherwise be stale.
- Leave Gemini command TOML implementation to `ticket:20260515-gemini-playbook-commands`.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside scope, update the ticket and packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source/file inspection showing `loom-playbooks/skills/` no longer exists and the relocated path contains 25 Playbooks.
- Source/file inspection showing explicit-only metadata and Codex policies remain present for all 25 Playbooks.
- `npm --prefix loom-playbooks run smoke`.
- `npm --prefix loom-playbooks run pack:check`.
- `claude plugin validate "$PWD/loom-playbooks"` if available.
- Targeted grep for active stale references to `loom-playbooks/skills/` in source/docs/guidance outside historical Loom records.
- `git diff --check`.
- If a command is unavailable, record it honestly.

## Stop Conditions

- Stop and return `blocked` if moving the corpus breaks a first-class adapter in a way that cannot be fixed inside write scope.
- Stop and return `escalate` if relocation requires changing the spec or decision record.
- Stop instead of implementing Gemini command TOML, final docs/tests, or broad unrelated docs.
- Stop if the worktree changes under the same paths outside this packet.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

If this run supports closure, acceptance, evidence, audit, research, knowledge, or future recovery, preserve this output in the packet or in a cited durable record; do not leave it only in transient launch output.

## Worker Output

Outcome: continue

Files changed:

- Moved 25 Playbook directories from `loom-playbooks/skills/` to `loom-playbooks/playbooks/`; top-level `loom-playbooks/skills/` is no longer present.
- Updated `loom-playbooks/loom-playbooks.mjs` to read the Playbook corpus from `playbooks/` and keep OpenCode command registration free of Playbook `config.skills.paths`.
- Updated `loom-playbooks/package.json` to pack `playbooks/` instead of `skills/`.
- Updated `loom-playbooks/.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and `.codex-plugin/plugin.json` to reference `./playbooks/`.
- Updated `AGENTS.md` package-shape guidance from `loom-playbooks/skills/` to `loom-playbooks/playbooks/`.

Records changed:

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md` - current state and journal updated with returned packet output and residual stale-doc scope issue.
- `.loom/packets/ralph/20260515T230227Z-playbook-skill-corpus-relocation.md` - status set to consumed and worker output recorded.

Evidence, review findings, validation output, or observations gathered:

- Source inspection/counts: `loom-playbooks/skills/` is absent; `loom-playbooks/playbooks/` contains 25 `SKILL.md` files and 25 `agents/openai.yaml` files.
- Metadata counts: 25 `disable-model-invocation: true` entries across relocated `SKILL.md` files; 25 `allow_implicit_invocation: false` entries across relocated Codex policy files.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `skillCount: 25`, `commandCount: 25`, `macroCount: 25`, no missing commands, no registered Playbook skill paths, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed; dry-run tarball included `playbooks/**` files and did not include stale top-level `skills/**` files.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- Targeted stale-path grep outside `.loom/` found no stale Playbooks references in scoped package runtime files after the edit, but did find active docs outside write scope: `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md` still mention old `loom-playbooks/skills` or generic package `skills/` assumptions relevant to Playbooks.
- `git diff --check` passed.

What was not verified or reviewed:

- No Gemini command TOML was implemented or validated; that remains `ticket:20260515-gemini-playbook-commands`.
- No broad docs/tests were edited because they were outside this packet's write scope.
- No live OpenCode, Cursor, Codex, or Gemini runtime invocation was performed.
- No adversarial audit was performed in this packet.

Blockers, risks, or assumptions discovered:

- ACC-004 has a residual scope issue: active docs outside this packet's write scope still contain old Playbooks path/package-shape assumptions. Closure should wait until the consuming surface either widens scope for those docs or records an explicit follow-up/waiver.
- The relocation assumes Claude/Cursor/Codex plugin manifests accept `./playbooks/` as the skill corpus path; Claude plugin validation passed, but Cursor/Codex validators were not run because this packet did not request them and no repository command is listed.

Recommended next move for the consuming surface:

- Decide whether to run a narrow follow-up packet to update stale active docs (`INSTALL.md`, `README.md`, `ARCHITECTURE.md`, `loom-playbooks/README.md`) before audit/closure, or explicitly revise the ticket's ACC-004 evidence boundary. After that, run Ralph audit for the relocation ticket before closure.
