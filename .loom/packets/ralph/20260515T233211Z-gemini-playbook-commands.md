# Gemini Playbook Commands Implementation

ID: packet:20260515T233211Z-gemini-playbook-commands
Type: Packet
Status: consumed
Created: 2026-05-15 23:32 UTC
Updated: 2026-05-15 23:37 UTC
Target: ticket:20260515-gemini-playbook-commands
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 1
Risk: medium - adds Gemini command files and must avoid reintroducing Gemini skill exposure.
Verification Posture: observation-first
Change Class: Gemini extension command surface

## Mission

Implement `ticket:20260515-gemini-playbook-commands`: add Gemini CLI extension command TOML files for all Playbooks from the canonical macro catalog, validate the Playbooks Gemini extension, and confirm no top-level `loom-playbooks/skills/` directory is present.

## Context Bundle

Records:

- `ticket:20260515-gemini-playbook-commands` - target ticket, scope, acceptance, and current state.
- `ticket:20260515-playbook-skill-corpus-relocation` and `audit:20260515-playbook-skill-corpus-relocation` - closed prerequisite that removed top-level `skills/`.
- `decision:0001` - package decision requiring one Playbooks Gemini root without top-level skills.
- `research:20260515-gemini-playbooks-skills-root` - Gemini docs reason this matters.
- `ticket:20260515-playbook-macro-catalog` and `audit:20260515-playbook-macro-catalog` - macro catalog seam and audit.
- `spec:playbook-explicit-macros` - behavior contract for Gemini commands.
- `plan:20260515-playbook-explicit-macros` - broader plan and remaining final docs/tests ticket.
- `AGENTS.md` - validation guidance and package surface constraints.

Files:

- `loom-playbooks/gemini-extension.json` - Gemini extension manifest.
- `loom-playbooks/commands/*.toml` - command files to add.
- `loom-playbooks/loom-playbooks.mjs` - macro catalog source and optional command generation/inspection helpers.
- `loom-playbooks/playbooks/**/SKILL.md` - relocated Playbook corpus read by the macro catalog.
- `loom-playbooks/skills/**` - should remain absent.

## Read Scope

- `.loom/tickets/20260515-gemini-playbook-commands.md`
- `.loom/tickets/20260515-playbook-skill-corpus-relocation.md`
- `.loom/audit/20260515-playbook-skill-corpus-relocation.md`
- `.loom/constitution/decisions/decision-0001-playbook-skill-corpus-root.md`
- `.loom/research/20260515-gemini-playbooks-skills-root.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `AGENTS.md`
- `loom-playbooks/gemini-extension.json`
- `loom-playbooks/commands/**` if present
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/playbooks/**/SKILL.md`
- `loom-playbooks/skills/**` if present

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-gemini-playbook-commands.md` - update Current State and Journal with progress, blockers, evidence, or completion disposition.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `loom-playbooks/gemini-extension.json`
- `loom-playbooks/commands/*.toml`
- `loom-playbooks/loom-playbooks.mjs` - only if needed for command generation or inspection helpers.

Do not edit OpenCode, Claude, Cursor, Codex manifests, the relocated Playbook body corpus, broad docs/tests, or final activation tests in this packet unless a validation failure requires a narrow package-local fix inside the paths above.

## Source Snapshot

Current state:

- `loom-playbooks/skills/` is absent after relocation.
- `loom-playbooks/playbooks/` contains 25 Playbooks and is the macro catalog source.
- `loom-playbooks/loom-playbooks.mjs` exports `readPlaybookMacroCatalog()` and reads from the relocated corpus.
- `loom-playbooks/gemini-extension.json` exists but no Gemini Playbook command TOML files exist yet.

Gemini command docs from research:

- Extension commands are TOML files under `commands/`.
- Required field: `prompt`.
- Optional field: `description`.
- The command name comes from the file path relative to `commands/`.
- Commands are user-invoked; extension skills under top-level `skills/` are model-invoked and must remain absent.

## Task

Implement the smallest Gemini command surface that satisfies `ticket:20260515-gemini-playbook-commands#ACC-001` through `ACC-005`.

Guidance:

- Generate or write one TOML command per `readPlaybookMacroCatalog()` entry.
- Prefer command filenames that preserve the stable macro names, such as `commands/loom-idea-refine.toml`, unless Gemini validation rejects the shape.
- Use each macro's `description` as the TOML `description` and each macro's `body` as the TOML `prompt`, preserving the explicit macro preamble.
- Avoid shell injection and file injection in generated prompts; static prompt bodies are enough.
- If adding helper functions to `loom-playbooks.mjs`, keep them package-local and minimal.
- Do not reintroduce `loom-playbooks/skills/`.
- Do not broaden into docs/tests final validation.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside scope, update the ticket and packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source inspection comparing command file count to macro catalog count.
- Source inspection or helper output showing command descriptions and prompts align with the macro catalog.
- Confirmation that `loom-playbooks/skills/` is absent.
- `gemini extensions validate "$PWD/loom-playbooks"` if available.
- `git diff --check`.
- If TOML validation requires a command or parser not available locally, record that honestly and use source inspection.

## Stop Conditions

- Stop and return `blocked` if Gemini command TOML cannot safely encode the macro bodies without a broader generator or escaped format decision.
- Stop and return `blocked` if Gemini validation fails for reasons that require changing the package-root decision or moving the corpus again.
- Stop instead of editing final docs/tests or unrelated adapter files.
- Stop if any change would reintroduce top-level `loom-playbooks/skills/`.

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

- `loom-playbooks/loom-playbooks.mjs` - added package-local Gemini command TOML generation helpers and a `--write-gemini-commands` entrypoint that emits files from `readPlaybookMacroCatalog()`.
- `loom-playbooks/gemini-extension.json` - changed the Gemini extension description from Playbook skills to Playbook commands.
- `loom-playbooks/commands/*.toml` - added 25 Gemini command files with stable `loom-*` names, catalog descriptions, and catalog prompt bodies preserving the explicit macro preamble.

Records changed:

- `.loom/tickets/20260515-gemini-playbook-commands.md` - updated Current State and Journal, and moved status to `review` for audit before closure.
- `.loom/packets/ralph/20260515T233211Z-gemini-playbook-commands.md` - recorded this worker output and marked the packet consumed.

Evidence, review findings, validation output, or observations gathered:

- `node loom-playbooks/loom-playbooks.mjs --write-gemini-commands` wrote 25 command files.
- Catalog/file comparison passed: 25 macros, 25 command files, no missing command files, and no mismatched TOML content.
- `loom-playbooks/skills/**` glob returned no files, confirming the top-level Playbooks skills directory remains absent.
- `gemini extensions validate "$PWD/loom-playbooks"` passed with `Extension /Users/alexanderbutler/code_projects/personal/agent-loom/loom-playbooks has been successfully validated.`
- `git diff --check` passed with no output.
- Targeted leakage grep over `loom-playbooks/commands/*.toml` found one generic phrase in `loom-debugging-and-error-recovery.toml`: `test harness to system under test`; this is inherited Playbook domain language, not package smoke, adapter mechanics, dogfood, npm packaging, repository workflow, or source-repo leakage.
- `loom-playbooks/gemini-extension.json` no longer contains `skills` in its description.

What was not verified or reviewed:

- No live Gemini command invocation was performed; verification is extension validation plus source/catalog inspection.
- No separate adversarial audit was performed in this packet.
- Root or Core Gemini validation was not run because this packet changed only `loom-playbooks/` surfaces.
- Final docs/tests and activation tests remain out of scope for the downstream final validation ticket.

Blockers, risks, or assumptions discovered:

- No blocker discovered.
- Residual risk: command TOML content is large because each command embeds the complete macro body; Gemini schema validation accepted it, but live invocation remains untested.
- Assumption: TOML multiline literal strings are safe for the current catalog because source inspection found no triple single-quote sequences in descriptions or bodies; the generator fails closed if one appears later.

Recommended next move for the consuming surface:

- Run a Ralph audit packet against `ticket:20260515-gemini-playbook-commands` before closure, focusing on ACC-001 through ACC-005: missing Playbooks, TOML shape, body drift from the macro catalog, Gemini skill exposure absence, product-surface leakage, and evidence sufficiency.
