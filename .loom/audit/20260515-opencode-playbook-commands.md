# OpenCode Playbook Commands Audit

ID: audit:20260515-opencode-playbook-commands
Type: Audit
Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Audited: 2026-05-15 22:00 UTC
Target: ticket:20260515-opencode-playbook-commands

## Summary

Ralph audit reviewed the OpenCode Playbook command implementation against `ticket:20260515-opencode-playbook-commands` ACC-001 through ACC-005. The verdict was clear with no material findings within scope.

## Target

The audit targeted the OpenCode package change in `loom-playbooks/loom-playbooks.mjs`: registering Playbooks through explicit `config.command` entries derived from the canonical macro catalog, and no longer registering the Playbook skill directory through `config.skills.paths`.

The audit did not target live OpenCode TUI invocation, negative natural-prompt activation harness tests, native adapter conversion, Gemini command conversion, docs/tests completion, or downstream plan items.

## Audit Scope And Lenses

Scope:

- Challenge ACC-001 through ACC-005 for the OpenCode command ticket.
- Review command registration and absence of Playbook skill-path registration.
- Review command/catalog alignment.
- Review smoke and pack evidence.
- Review whether the implementation stayed inside ticket scope.

Lenses:

- acceptance
- scope
- evidence sufficiency
- OpenCode activation semantics
- package inclusion
- follow-through for downstream validation

## Context And Evidence Reviewed

- Ralph packet: `packet:20260515T215943Z-opencode-playbook-commands-audit` - bounded review contract and returned audit output.
- `ticket:20260515-opencode-playbook-commands` - target ticket acceptance and current state.
- `packet:20260515T215226Z-opencode-playbook-commands` - implementation packet and worker output.
- `ticket:20260515-playbook-macro-catalog` - prerequisite catalog ticket.
- `audit:20260515-playbook-macro-catalog` - clear audit of the macro catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and remaining plan work.
- `spec:playbook-explicit-macros` - behavior contract for explicit Playbook macros.
- `research:20260515-playbook-command-surfaces` - OpenCode command surface research.
- `AGENTS.md` - package-shape and product-surface constraints.
- `loom-playbooks/loom-playbooks.mjs` - implementation diff.
- `loom-playbooks/package.json` - package dry-run and file inclusion context.
- `loom-playbooks/skills/**/SKILL.md` - runtime corpus used by the command catalog.

Observed validation from the Ralph audit run:

- Source inspection confirmed `configureOpenCode()` derives command entries through `readPlaybookCommands()` from `readPlaybookMacroCatalog()`, writes `config.command[name]`, and no longer writes `config.skills.paths` for `loom-playbooks/skills`.
- Source inspection confirmed each command template is the catalog macro `body` and each command description is the catalog macro `description`.
- `npm --prefix loom-playbooks run smoke` passed with `ok: true`, `commandCount: 25`, `macroCount: 25`, `commandChecks.ok: true`, no missing commands, no registered Playbook skill paths, `playbookSkillPathsRegistered: false`, `doesNotPreloadCoreDoctrine: true`, and `commandEntriesAreDeduped: true`.
- Direct Node import/config check passed with 25 commands, 25 macros, zero skill paths, and no missing commands.
- `npm --prefix loom-playbooks run pack:check` passed and included `loom-playbooks.mjs`, `package.json`, `README.md`, and all 25 `skills/**/SKILL.md` files required by the runtime catalog reader.
- `git diff --check` passed.

## Findings

None - no material findings within audited scope.

## Verdict

`clear` - ACC-001 through ACC-005 are supported within the reviewed scope. OpenCode Playbooks are registered through explicit `config.command` entries derived from the canonical macro catalog, the Playbook skill directory is not registered through OpenCode `config.skills.paths`, smoke validates command behavior and catalog alignment instead of implicit trigger-description quality, package dry-run includes files needed for command operation, and syntax/package checks passed.

This verdict does not claim live OpenCode TUI invocation, negative natural-prompt activation coverage, native adapter conversion, Gemini command conversion, docs/tests completion, or closure of downstream plan items.

## Required Follow-up

- Close `ticket:20260515-opencode-playbook-commands` if the consuming ticket accepts the residual risks as downstream validation concerns.
- Handle negative natural-prompt activation coverage in `ticket:20260515-playbook-explicit-macro-docs-tests`.
- Handle native adapter and Gemini conversion in their remaining plan tickets.

## Residual Risk

- OpenCode command semantics were judged from source-backed research, config mutation source inspection, smoke output, import checks, and pack dry-run, not an interactive OpenCode TUI invocation.
- Negative natural-prompt activation coverage remains unimplemented until the docs/tests/final validation ticket.
- This audit did not repeat exhaustive semantic review of all 25 Playbook bodies; it relied on the prior clear catalog audit for the shared macro-body seam.

## Related Records

- `ticket:20260515-opencode-playbook-commands` - consuming ticket.
- `packet:20260515T215943Z-opencode-playbook-commands-audit` - Ralph review packet that produced this verdict.
- `packet:20260515T215226Z-opencode-playbook-commands` - implementation packet reviewed by this audit.
- `audit:20260515-playbook-macro-catalog` - prior clear audit for the catalog seam.
- `spec:playbook-explicit-macros` - behavior contract.
