# Playbook Doc Compression Alignment Validation

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

Validation observations for `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md`. The observations cover line-count reduction, generated command alignment, Playbook explicit macro posture, product-surface leakage searches, and package checks after the Playbook/doc compression edits.

## Observations

- Observation: Targeted line counts changed from 8,846 total lines before edits to 8,661 total lines after edits across `loom-playbooks/playbooks/*/SKILL.md`, `loom-playbooks/commands/*.toml`, `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `loom-core/README.md`, and `loom-playbooks/README.md`.
  - Procedure/source: `wc -l loom-playbooks/playbooks/*/SKILL.md loom-playbooks/commands/*.toml README.md PROTOCOL.md ARCHITECTURE.md loom-core/README.md loom-playbooks/README.md` before and after the edits.
  - Actual result: Net reduction of 185 lines in the targeted surfaces. Each Playbook source and generated command dropped three lines; `PROTOCOL.md` dropped 16 lines; `ARCHITECTURE.md` dropped 19 lines.

- Observation: Generated command surfaces were regenerated from the Playbook source corpus.
  - Procedure/source: `node loom-playbooks/loom-playbooks.mjs --write-gemini-commands`.
  - Actual result: The command writer reported `written: 25` and listed all 25 `loom-playbooks/commands/*.toml` files.

- Observation: Source/generated command catalog alignment passed.
  - Procedure/source: `node --input-type=module -e 'import { inspectPlaybookMacroCatalog, inspectLoomPlaybooksBundle } from "./loom-playbooks/loom-playbooks.mjs"; ...'`.
  - Actual result: `macrosOk: true`, `commandOk: true`, `macroCount: 25`, `commandCount: 25`, `missingCommands: []`, `registeredPlaybookSkillPaths: []`, and `explicitDescriptionPrefixFailures: []`.

- Observation: Playbooks package smoke validation passed.
  - Procedure/source: `npm --prefix loom-playbooks run smoke`.
  - Actual result: Smoke output reported `ok: true`, `doesNotPreloadCoreDoctrine: true`, `skillCount: 25`, `commandCount: 25`, `playbookSkillPathsRegistered: false`, and command/macro checks with no missing commands or explicit description prefix failures.

- Observation: Playbooks package dry-run pack check passed.
  - Procedure/source: `npm --prefix loom-playbooks run pack:check`.
  - Actual result: The command reran the smoke check successfully and completed `npm pack --dry-run` for `@z3z1ma/open-loom-playbooks@0.3.0`, reporting 53 files and package details without error.

- Observation: Markdown and source diff whitespace check passed.
  - Procedure/source: `git diff --check`.
  - Actual result: Command exited successfully with no output.

- Observation: Targeted stale-doctrine and explicitness search found no old Playbook routing block, no generic explicit description prefix, and no removed full bootstrap load-order headings in touched docs.
  - Procedure/source: Grep search for `Ensure the \`using-loom\` skill is loaded before applying this workflow`, `When routing to any named Loom skill`, `Explicit optional workflow macro for`, `natural-language task text`, and `Load order:` over touched docs, Playbooks, generated commands, and generator.
  - Actual result: No matching files were found.

- Observation: Targeted source inspection found the compressed explicit macro preamble and Core discipline references remain in Playbook generated commands and source.
  - Procedure/source: Grep search for `Follow any named Loom skill fully`, `ticket-owned Ralph`, `loom-evidence`, `loom-audit`, `Status: review`, `Ralph-backed audit`, `Preserve Core surface ownership`, `natural-prompt activation`, `config.skills.paths`, and `registered through config.command` over `loom-playbooks`.
  - Actual result: Matches show the generated command preamble preserves Core surface ownership, ticket shaping, evidence, audit, ticket-owned Ralph discipline, and natural-prompt non-activation; Playbook source and commands retain evidence/audit/Ralph references; package inspection code still checks no Playbook skill path is registered and commands come from `config.command`.

- Observation: Targeted product-surface leakage search over Playbook model-visible and package surfaces found no new contributor-facing leakage in Playbook bodies or commands.
  - Procedure/source: Grep search for `package smoke`, `adapter self-justification`, `dogfood assumptions`, `repository workflow`, `skill-description policy`, `npm packaging`, `source-repo-only`, `why Loom is built`, `Loom Mill`, `doesNotPreloadCoreDoctrine`, and `test harness details` over `loom-playbooks`.
  - Actual result: The only match was `doesNotPreloadCoreDoctrine` inside `loom-playbooks/loom-playbooks.mjs` smoke output code, not model-visible Playbook doctrine.

## Artifacts

- No raw artifact directory was created. Command summaries above are sufficient for this validation dossier.

## What This Shows

- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md#ACC-001` - supports - Playbook source and generated macro language was shortened while preserving Core routing, evidence, audit, ticket, and ticket-owned Ralph references.
- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md#ACC-002` - supports - command files were regenerated and catalog comparison reported no missing or stale commands.
- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md#ACC-003` - supports - touched docs removed verbose bootstrap file lists and stale activation prose while keeping Core as the owning doctrine source.
- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md#ACC-004` - supports - static package inspection still reports explicit command registration, no Playbook skill paths, and no natural-prompt activation framing in generated macro text.
- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md#ACC-005` - supports - Playbooks smoke, Playbooks pack check, generated command comparison, targeted searches, and `git diff --check` passed.

## What This Does Not Show

This dossier does not prove live harness natural-prompt behavior in OpenCode, Claude, Codex, Cursor, or Gemini. It does not audit the changes; the ticket still needs a fresh-context audit before closure. It also does not validate unrelated dirty Core compression changes already present in the worktree.

## Related Records

- `.loom/tickets/done/20260525-playbook-doc-compression-alignment.md` - consuming ticket.
- `.loom/specs/playbook-explicit-macros.md` - explicit Playbook behavior contract.
- `.loom/specs/loom-protocol-compression.md` - compression and product-surface hygiene contract.
- `.loom/knowledge/playbook-activation-tests-procedure.md` - limits of static activation validation.
