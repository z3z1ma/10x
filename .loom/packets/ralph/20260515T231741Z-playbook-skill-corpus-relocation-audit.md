# Playbook Skill Corpus Relocation Audit

ID: packet:20260515T231741Z-playbook-skill-corpus-relocation-audit
Type: Packet
Status: consumed
Created: 2026-05-15 23:17 UTC
Updated: 2026-05-15 23:21 UTC
Target: ticket:20260515-playbook-skill-corpus-relocation
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: audit-1
Risk: medium - relocation changes shared adapter package paths and unblocks Gemini commands.
Review Lens: audit, acceptance, scope, package path integrity, Gemini skill exposure, evidence sufficiency
Change Class: Playbooks corpus relocation review

## Mission

Perform a bounded adversarial audit of `ticket:20260515-playbook-skill-corpus-relocation` against ACC-001 through ACC-005 after the corpus move and doc path follow-up. Determine whether the ticket can honestly close or whether changes are needed before Gemini command implementation proceeds.

## Context Bundle

Records:

- `ticket:20260515-playbook-skill-corpus-relocation` - target ticket, acceptance, current state, and packet summaries.
- `packet:20260515T230227Z-playbook-skill-corpus-relocation` - corpus relocation implementation packet and evidence.
- `packet:20260515T231048Z-playbook-relocation-doc-paths` - docs path follow-up packet and evidence.
- `decision:0001` - package decision selecting corpus move.
- `research:20260515-gemini-playbooks-skills-root` - Gemini docs conflict.
- `spec:playbook-explicit-macros` - behavior contract requiring Gemini command-only Playbooks.
- `plan:20260515-playbook-explicit-macros` - sequencing and downstream Gemini ticket.
- `audit:20260515-opencode-playbook-commands` and `audit:20260515-native-playbook-explicit-surfaces` - prior clear audits for surfaces affected by relocation.

Files:

- `loom-playbooks/playbooks/**` - relocated Playbook corpus.
- `loom-playbooks/skills/**` - should be absent as top-level extension directory.
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `AGENTS.md`, `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, `loom-playbooks/README.md`

## Read Scope

- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md`
- `.loom/packets/ralph/20260515T230227Z-playbook-skill-corpus-relocation.md`
- `.loom/packets/ralph/20260515T231048Z-playbook-relocation-doc-paths.md`
- `.loom/constitution/decisions/decision-0001-playbook-skill-corpus-root.md`
- `.loom/research/20260515-gemini-playbooks-skills-root.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/audit/20260515-opencode-playbook-commands.md`
- `.loom/audit/20260515-native-playbook-explicit-surfaces.md`
- `loom-playbooks/playbooks/**`
- `loom-playbooks/skills/**`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `AGENTS.md`
- `INSTALL.md`
- `README.md`
- `ARCHITECTURE.md`
- `loom-playbooks/README.md`
- Current git status and diff for relocation-related files.

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output`, update `Status:`, and include findings and verdict.

Source Paths:

- None - this is a review packet. Do not edit source or tickets. Return findings for the parent to record and disposition.

## Source Snapshot

Implementation summary to challenge:

- `loom-playbooks/skills/` was moved to `loom-playbooks/playbooks/`.
- `loom-playbooks/loom-playbooks.mjs` now reads the Playbook corpus from `playbooks/`.
- `loom-playbooks/package.json` packs `playbooks/` instead of `skills/`.
- Claude, Cursor, and Codex manifests point to `./playbooks/`.
- `AGENTS.md` and path-specific docs now reference `loom-playbooks/playbooks/`.
- First packet passed smoke, pack, Claude validation, counts, and `git diff --check`; follow-up packet passed stale-path grep outside `.loom/` and `git diff --check`.

## Task

Review the target ticket, diff, file layout, and evidence. Focus on:

- ACC-001: Is top-level `loom-playbooks/skills/` absent, and does `loom-playbooks/playbooks/` contain all 25 Playbooks with `SKILL.md`, `disable-model-invocation`, and Codex policies preserved?
- ACC-002: Does OpenCode still expose 25 explicit commands from the relocated catalog and no Playbook skill path?
- ACC-003: Do Claude/Cursor/Codex manifests reference the relocated path, and does Claude plugin validation pass?
- ACC-004: Are package inclusion and active guidance/docs aligned with the relocated path, with no stale active `loom-playbooks/skills/` references outside `.loom/`?
- ACC-005: Was the change limited to relocation/path alignment, without Gemini TOML commands or broad behavior rewrites?
- Risk: Could Gemini still auto-discover Playbook skills from the extension root after this move?

Do not fix issues. Return findings with file/line or record references when practical, plus a verdict.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, perform the bounded audit, update this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Inspect filesystem layout for absence of `loom-playbooks/skills/` and count Playbooks under `loom-playbooks/playbooks/`.
- Run `npm --prefix loom-playbooks run smoke` if useful.
- Run `npm --prefix loom-playbooks run pack:check` if useful.
- Run `claude plugin validate "$PWD/loom-playbooks"` if available.
- Run targeted stale path grep outside `.loom/`.
- Run `git diff --check`.
- Findings should use `FIND-*` IDs for material issues, or say no material findings within scope.
- Verdict should be one of `clear`, `concerns`, `changes-needed`, or `inconclusive`, with limits.

## Stop Conditions

- Stop and return `inconclusive` if relocation source changes under review.
- Stop instead of modifying source or tickets.
- Stop and name missing context if adapter package behavior cannot be judged from available files and commands.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

The review output must include any `FIND-*` findings and a bounded audit verdict that can be recorded under `.loom/audit/`.

## Worker Output

Outcome: stop

Files changed:

- None.

Records changed:

- `.loom/packets/ralph/20260515T231741Z-playbook-skill-corpus-relocation-audit.md` - status and Worker Output updated with this bounded audit result.

Evidence, review findings, validation output, or observations gathered:

- Source inspection: `loom-playbooks/skills/` is absent; `loom-playbooks/playbooks/` contains 25 `SKILL.md` files and 25 `agents/openai.yaml` files.
- Metadata inspection: found 25 `disable-model-invocation: true` entries in relocated Playbook `SKILL.md` files and 25 `allow_implicit_invocation: false` entries in relocated Codex policy files.
- Source inspection: `loom-playbooks/loom-playbooks.mjs` reads from `playbooks/`, registers commands through `config.command`, and does not register Playbook skill paths through `config.skills.paths`.
- Source inspection: `loom-playbooks/package.json` packs `playbooks/`; Claude, Cursor, and Codex manifests all reference `./playbooks/`.
- Source inspection: docs and contributor guidance in the scoped files now reference `loom-playbooks/playbooks/` where they describe the relocated Playbooks corpus; Core `loom-core/skills/` references remain intact.
- Scope inspection: no Gemini command TOML files were introduced, and the relocation-related diff is limited to path relocation/alignment across the scoped package, manifest, guidance, docs, and record files.
- Content preservation check: every relocated Playbook `SKILL.md` and `agents/openai.yaml` matches the corresponding staged pre-move source under `loom-playbooks/skills/`.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `skillCount: 25`, `commandCount: 25`, `macroCount: 25`, no missing commands, no registered Playbook skill paths, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed; dry-run tarball includes `playbooks/**` files and no stale top-level `skills/**` files.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `rg --glob '!/.loom/**' --glob '!.loom/**' 'loom-playbooks/skills' .` returned no matches.
- `git diff --check` passed.

Findings:

- None - no material findings within audited scope.

Verdict:

- `clear` - ACC-001 through ACC-005 are supported within the reviewed scope. The top-level Playbooks extension `skills/` directory is absent, the relocated `playbooks/` corpus preserves all 25 Playbooks and explicit-only metadata, OpenCode registers 25 explicit commands without Playbook skill paths, Claude/Cursor/Codex manifests and package inclusion point at the relocated corpus, active non-Loom guidance no longer references `loom-playbooks/skills/`, and the diff did not implement Gemini command TOML or broad behavior rewrites.

What was not verified or reviewed:

- No live OpenCode, Cursor, Codex, or Gemini runtime invocation was performed.
- No `gemini extensions validate "$PWD/loom-playbooks"` was run because Gemini command implementation remains out of scope for this ticket.
- Cursor and Codex native validators were not run because no repository command is listed and this packet only expected Claude validation.
- No exhaustive semantic review of every Playbook body was performed beyond relocation/content preservation and explicit-only metadata checks.

Blockers, risks, or assumptions discovered:

- No blockers discovered.
- Residual risk: native adapter behavior for Cursor and Codex still relies on source/manifests and prior clear native audit rather than live runtime or validator evidence.
- Residual risk: Gemini auto-discovery risk was judged from source layout and prior research; with no top-level `loom-playbooks/skills/` directory present, this audit found no remaining Playbook skill corpus for Gemini to auto-discover from the Playbooks extension root.

Recommended next move for the consuming surface:

- Record a matching audit record under `.loom/audit/` and close `ticket:20260515-playbook-skill-corpus-relocation` if the consuming ticket accepts the stated residual validation limits.
