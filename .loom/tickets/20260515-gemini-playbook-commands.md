# Gemini Playbook Commands

ID: ticket:20260515-gemini-playbook-commands
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - changes Gemini extension behavior from model-activated skills to command macros.
Priority: medium - completes true command-surface coverage for supported non-OpenCode adapters.
Depends On: ticket:20260515-playbook-skill-corpus-relocation

## Summary

Expose Loom Playbooks to Gemini CLI as extension command TOML prompt macros. The closure claim is that the Gemini Playbooks extension contributes explicit `/` commands derived from the canonical Playbook macro catalog and does not rely on Gemini model-activated skills for Playbooks.

## Related Records

- `plan:20260515-playbook-explicit-macros` - defines sequencing and validation posture for the Gemini unit.
- `ticket:20260515-playbook-macro-catalog` - provides the canonical macro source this ticket should consume.
- `spec:playbook-explicit-macros` - defines Gemini requirements, especially REQ-001, REQ-003, REQ-006, REQ-008, REQ-010, and REQ-011.
- `research:20260515-playbook-command-surfaces` - records Gemini extension command TOML support and model-activated skill risk.
- `research:20260515-gemini-playbooks-skills-root` - records the package-root blocker: Gemini auto-discovers `skills/` from the extension root.
- `decision:0001` - operator-selected route to move the shared skill corpus out of top-level `loom-playbooks/skills/`.
- `ticket:20260515-playbook-skill-corpus-relocation` - new hard prerequisite before Gemini commands can be implemented honestly.
- `audit:20260515-gemini-playbook-commands` - clear Ralph-backed audit for this ticket's closure claim.
- `loom-playbooks/gemini-extension.json` - current Gemini extension manifest.
- `loom-playbooks/skills/` - absent top-level directory that must remain absent for Gemini commands-only exposure.

## Scope

May change `loom-playbooks/gemini-extension.json`, add or update `loom-playbooks/commands/*.toml`, and adjust package-local Playbook files needed for Gemini command macro generation.

May update `loom-playbooks/loom-playbooks.mjs` if a package-local generator or inspection helper is the smallest safe way to keep Gemini command files aligned with the macro catalog.

Must use Gemini CLI custom command TOML semantics with required `prompt` and optional `description` fields. Must support explicit user invocation and not rely on `activate_skill` for Playbook entry.

Must not update OpenCode, Claude, Cursor, Codex, or general docs except for package-local Gemini extension metadata needed for command exposure.

## Acceptance

- ACC-001: The Gemini Playbooks extension contains command TOML files for the Playbook macro catalog with stable names, descriptions, and prompt bodies.
  - Evidence: Source inspection of `loom-playbooks/commands/*.toml` and comparison to the catalog count.
  - Audit: Review should challenge missing Playbooks, invalid TOML shape, or body drift.

- ACC-002: Gemini Playbooks no longer depend on Gemini skill activation for Playbook entry.
  - Evidence: Source inspection shows Playbook command files are the intended extension surface and no Gemini-specific Playbook skill exposure remains documented or configured.
  - Audit: Review should challenge whether Gemini can still auto-activate Playbooks from natural prompts through package-provided skill metadata.

- ACC-003: Gemini extension validation passes for the changed Playbooks extension.
  - Evidence: `gemini extensions validate "$PWD/loom-playbooks"`; root or Core validation too if this ticket touches those manifests.
  - Audit: Command evidence is sufficient for extension schema validity.

- ACC-004: Product-visible Gemini command content preserves Core routing and avoids contributor-only leakage.
  - Evidence: Targeted grep/source inspection over `loom-playbooks/commands/`.
  - Audit: Review should challenge activation semantics and product-surface leakage.

- ACC-005: Markdown and command files are syntactically clean.
  - Evidence: `git diff --check` and TOML or extension validation output.
  - Audit: Separate audit should focus on behavior semantics, not whitespace.

## Current State

Closed. Ralph packet `packet:20260515T233211Z-gemini-playbook-commands` returned `stop`: Gemini command TOML files now exist for all 25 canonical Playbook macros, generated from `readPlaybookMacroCatalog()` with stable `loom-*` filenames, catalog descriptions, and prompt bodies that preserve the explicit macro preamble. `loom-playbooks/gemini-extension.json` now describes Playbooks as Gemini commands rather than skills.

Evidence gathered: command-file/catalog comparison passed with 25 macros, 25 command files, no missing files, and no mismatches; `loom-playbooks/skills/` remains absent; `gemini extensions validate "$PWD/loom-playbooks"` passed; `git diff --check` passed; targeted command leakage grep found only the generic phrase `test harness to system under test` in the debugging Playbook body, not package/test-harness leakage. `audit:20260515-gemini-playbook-commands` returned `clear` with no material findings within scope, supporting closure for ACC-001 through ACC-005.

Residual limits: no live Gemini command invocation was performed; root/Core Gemini extension validation was not run because this ticket only changed `loom-playbooks/`; command generation currently writes the catalog's current command set but does not delete stale command TOML files if the catalog later shrinks. Broader docs/tests and activation validation remain with `ticket:20260515-playbook-explicit-macro-docs-tests`.

## Journal

- 2026-05-15: Created ticket from `plan:20260515-playbook-explicit-macros`; depends on the canonical macro catalog ticket.
- 2026-05-15: Set status to blocked after `research:20260515-gemini-playbooks-skills-root` confirmed that Gemini auto-discovers top-level extension `skills/`; current package root shape cannot be commands-only without moving skills or splitting the Gemini extension root.
- 2026-05-15: Added dependency on `ticket:20260515-playbook-skill-corpus-relocation` after operator selected the corpus-move route in `decision:0001`.
- 2026-05-15: Set status back to open after `ticket:20260515-playbook-skill-corpus-relocation` closed with clear audit and removed top-level `loom-playbooks/skills/`.
- 2026-05-15: Set status to active and launched `packet:20260515T233211Z-gemini-playbook-commands` for Gemini command TOML implementation.
- 2026-05-15: `packet:20260515T233211Z-gemini-playbook-commands` returned `stop`: added 25 Gemini `commands/*.toml` files from the canonical macro catalog, updated the Gemini extension description from Playbook skills to commands, confirmed top-level `loom-playbooks/skills/` is absent, passed catalog/file alignment inspection, passed `gemini extensions validate "$PWD/loom-playbooks"`, and passed `git diff --check`. Moved ticket to review for Ralph audit before closure.
- 2026-05-15: Recorded `audit:20260515-gemini-playbook-commands` from `packet:20260515T234251Z-gemini-playbook-commands-audit`; verdict `clear`, no material findings, ACC-001 through ACC-005 supported within scope.
- 2026-05-15: Closed ticket. Acceptance is satisfied by the generated 25 Gemini command TOML files, command/catalog equivalence, absent top-level `loom-playbooks/skills/`, Playbooks-only Gemini extension validation, `git diff --check`, targeted leakage inspection, and clear Ralph-backed audit. Residual limits remain documented in Current State.
