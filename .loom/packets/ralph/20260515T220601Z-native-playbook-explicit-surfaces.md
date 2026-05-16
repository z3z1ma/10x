# Native Playbook Explicit Surfaces Implementation

ID: packet:20260515T220601Z-native-playbook-explicit-surfaces
Type: Packet
Status: consumed
Created: 2026-05-15 22:06 UTC
Updated: 2026-05-15 22:13 UTC
Target: ticket:20260515-native-playbook-explicit-surfaces
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 1
Risk: medium - changes Claude, Cursor, and Codex plugin-facing Playbook invocation behavior.
Verification Posture: observation-first
Change Class: Native plugin explicit-only Playbook surfaces

## Mission

Implement `ticket:20260515-native-playbook-explicit-surfaces`: update Claude Code, Cursor, and Codex Playbook plugin surfaces so Playbooks are available only through explicit commands or explicit-only skills, without overclaiming unsupported Codex custom slash commands.

## Context Bundle

Records:

- `ticket:20260515-native-playbook-explicit-surfaces` - target ticket, scope, acceptance, and current state.
- `ticket:20260515-playbook-macro-catalog` - closed prerequisite defining the shared macro catalog.
- `audit:20260515-playbook-macro-catalog` - clear audit of the macro catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and downstream context.
- `spec:playbook-explicit-macros` - behavior contract for explicit Playbook macro or explicit-only skill behavior.
- `research:20260515-playbook-command-surfaces` - source-backed support matrix for Claude, Cursor, and Codex.
- `AGENTS.md` - product-surface leakage and adapter constraints.

Evidence Or Artifacts:

- `audit:20260515-playbook-macro-catalog` established that the catalog body seam is safe for downstream adapter use.

Files, Diffs, Or External References:

- `loom-playbooks/.claude-plugin/plugin.json` - current Claude Playbooks manifest.
- `loom-playbooks/.cursor-plugin/plugin.json` - current Cursor Playbooks manifest.
- `loom-playbooks/.codex-plugin/plugin.json` - current Codex Playbooks manifest.
- `loom-playbooks/skills/**/SKILL.md` - current Playbook skills; may need explicit-only frontmatter for Claude/Cursor and metadata for Codex.
- `loom-playbooks/skills/**/agents/openai.yaml` - likely Codex explicit-only policy location if using skill-local policy files.

## Read Scope

- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `AGENTS.md`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `loom-playbooks/skills/**/SKILL.md`
- `loom-playbooks/skills/**/agents/openai.yaml` if present or created

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md` - update Current State and Journal with progress, blockers, evidence, or completion disposition.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `loom-playbooks/skills/**/SKILL.md`
- `loom-playbooks/skills/**/agents/openai.yaml`

Do not edit OpenCode command registration, Gemini command files, broad docs, tests, or unrelated package metadata in this packet.

## Source Snapshot

Current native Playbooks manifests expose `skills: "./skills/"` for Claude, Cursor, and Codex. Current Playbook `SKILL.md` files have `name` and `description` frontmatter, but no explicit-only controls. Current Codex plugin interface text says Playbooks provide optional workflow coordinator skills and default prompts suggest using Playbooks when installed.

Research constraints:

- Claude Code supports plugin `commands/` and skills, but commands are merged into skills; `disable-model-invocation: true` is the critical explicit-only control if using skills.
- Cursor supports plugin commands and skills; `disable-model-invocation: true` makes skills behave like explicit slash commands.
- Codex plugin docs support skills and `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; current research does not support claiming plugin-contributed custom Playbook slash commands.

## Task

Implement the smallest native adapter change that satisfies `ticket:20260515-native-playbook-explicit-surfaces#ACC-001` through `ACC-005`.

Guidance:

- Prefer explicit-only skills for Claude and Cursor if that avoids duplicating all Playbook bodies while satisfying the docs. Add `disable-model-invocation: true` in the harness-supported frontmatter/location.
- For Codex, add the explicit-only policy using skill-local `agents/openai.yaml` files or the documented equivalent with `policy.allow_implicit_invocation: false`.
- Update native plugin descriptions and Codex interface text so they describe explicit-only Playbook lenses, not broad natural-language autoactivation.
- Do not claim Codex custom slash commands.
- Keep the shared Playbook body source; do not copy 25 bodies into adapter-specific command files unless source-backed docs and the ticket make that necessary.
- Preserve product-surface cleanliness: no package smoke, dogfood, test harness details, npm packaging, or contributor workflow commentary in model-visible content.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside scope, update the ticket and packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source inspection showing Claude explicit-only behavior for all Playbooks.
- Source inspection showing Cursor explicit-only behavior for all Playbooks.
- Source inspection showing Codex `allow_implicit_invocation: false` or documented equivalent for all Playbooks.
- Source inspection showing plugin metadata does not claim unsupported Codex custom prompt commands.
- Run `claude plugin validate "$PWD/loom-playbooks"` if available.
- Run `git diff --check`.
- If a validator is unavailable, record that honestly in Worker Output.

## Stop Conditions

- Stop and return `blocked` if the exact frontmatter or Codex policy shape cannot be determined from available docs, source, or existing repo patterns.
- Stop and return `escalate` if satisfying Claude or Cursor requires command files that duplicate all bodies and conflicts with the catalog drift constraint.
- Stop instead of editing Gemini, OpenCode, docs, tests, or broad package files.
- Stop if a native validator reveals a schema conflict that cannot be resolved inside write scope.

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

Outcome: stop

Files changed:

- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `loom-playbooks/skills/**/SKILL.md` - 25 Playbook skill frontmatter files now include `disable-model-invocation: true`.
- `loom-playbooks/skills/**/agents/openai.yaml` - 25 new Codex policy files with `policy.allow_implicit_invocation: false`.

Records changed:

- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md`
- `.loom/packets/ralph/20260515T220601Z-native-playbook-explicit-surfaces.md`

Evidence, review findings, validation output, or observations gathered:

- Source inspection found 25 `disable-model-invocation: true` entries across 25 Playbook `SKILL.md` files, supporting Claude and Cursor explicit-only skill behavior.
- Source inspection found 25 `allow_implicit_invocation: false` entries across 25 Codex `agents/openai.yaml` files, one per Playbook.
- Source inspection of `loom-playbooks/.codex-plugin/plugin.json` found no custom slash-command or unsupported Codex prompt-command claim; metadata now describes explicit invocation and warns not to treat Playbooks as automatic natural-language routes.
- Targeted leakage grep over Playbooks Markdown, JSON, and YAML found one existing generic phrase, `test harness to system under test`, in the debugging Playbook. This is runtime debugging guidance, not contributor-only package smoke, adapter mechanics, dogfood state, npm packaging, or repository workflow leakage.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.

What was not verified or reviewed:

- Cursor native plugin validation was not run; the packet did not require a Cursor validator and no repository command is listed for it.
- Codex native plugin validation was not run; the packet required source inspection for Codex policy and no Codex validator command is listed in `AGENTS.md`.
- No live Claude, Cursor, or Codex runtime invocation was exercised.
- No audit was performed in this implementation packet.

Blockers, risks, or assumptions discovered:

- No blockers.
- Residual risk: native plugin consumers must honor the documented frontmatter and `agents/openai.yaml` policy fields as researched; runtime activation behavior still needs later adapter or activation validation if available.
- Residual risk: the implementation keeps the shared Playbook skill bodies in place and adds explicit-only metadata rather than generating adapter-specific command bodies from the macro catalog; this is the minimal route allowed by the ticket and avoids body duplication, but audit should still challenge ACC-004 alignment.
- Pre-existing uncommitted changes and untracked Loom records were present before this packet, including `loom-playbooks/loom-playbooks.mjs`; this packet did not modify that out-of-scope file.

Recommended next move for the consuming surface:

- Move `ticket:20260515-native-playbook-explicit-surfaces` through Ralph-backed audit/acceptance review against ACC-001 through ACC-005 before closure.
