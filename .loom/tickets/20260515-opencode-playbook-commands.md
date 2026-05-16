# OpenCode Playbook Commands

ID: ticket:20260515-opencode-playbook-commands
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - changes the OpenCode package entrypoint and smoke expectations for Playbooks.
Priority: high - OpenCode is the local package surface with executable smoke and pack checks.
Depends On: ticket:20260515-playbook-macro-catalog

## Summary

Convert the OpenCode Playbooks package from implicit skill-path registration to explicit command registration. The closure claim is that installing `loom-playbooks/loom-playbooks.mjs` contributes Playbook commands without registering the Playbook skill directory for automatic model activation.

## Related Records

- `plan:20260515-playbook-explicit-macros` - defines sequencing and validation posture for the broader conversion.
- `ticket:20260515-playbook-macro-catalog` - provides the canonical macro source this ticket should consume.
- `spec:playbook-explicit-macros` - defines OpenCode requirements, especially REQ-001, REQ-003, REQ-006, REQ-008, REQ-010, and REQ-011.
- `research:20260515-playbook-command-surfaces` - records that OpenCode supports command config and plugin config mutation.
- `audit:20260515-opencode-playbook-commands` - clear Ralph-backed review of ACC-001 through ACC-005.
- `loom-playbooks/loom-playbooks.mjs` - current OpenCode package entrypoint.
- `loom-playbooks/package.json` - package files list and smoke scripts.

## Scope

May change `loom-playbooks/loom-playbooks.mjs`, `loom-playbooks/package.json`, and the canonical catalog files created by `ticket:20260515-playbook-macro-catalog` only as needed for OpenCode command registration and package inclusion.

Must remove or disable OpenCode `config.skills.paths` registration for Playbooks. Core skill registration is out of scope and must remain unchanged.

May update Playbooks smoke output so it reports command registration, command count, deduping, and absence of Core doctrine preload. Do not keep smoke checks that reward Playbook trigger-description prefixes for implicit activation.

Must not update Claude, Cursor, Codex, Gemini, docs, or global activation tests except for package output directly tied to OpenCode smoke.

## Acceptance

- ACC-001: `configureOpenCode` registers Playbook command entries or equivalent explicit OpenCode command surfaces and does not add `loom-playbooks/skills` to `config.skills.paths`.
  - Evidence: Source inspection and `npm --prefix loom-playbooks run smoke` output showing commands are exposed and skill paths are not.
  - Audit: Review should challenge whether any implicit Playbook skill path remains reachable through OpenCode package config.

- ACC-002: OpenCode command entries are generated from or aligned with the canonical macro catalog and include stable names, descriptions, and prompt bodies.
  - Evidence: Source inspection or smoke output comparing command count to catalog count.
  - Audit: Review should challenge body drift and missing Playbooks.

- ACC-003: OpenCode smoke checks reflect explicit macro behavior and no longer enforce broad Playbook trigger-description prefixes as activation quality.
  - Evidence: `npm --prefix loom-playbooks run smoke` output and source inspection of smoke assertions.
  - Audit: Command evidence is sufficient if smoke output directly shows the changed assertions.

- ACC-004: Package dry-run includes the files needed for OpenCode command operation.
  - Evidence: `npm --prefix loom-playbooks run pack:check` output.
  - Audit: Command evidence is sufficient for package-file inclusion.

- ACC-005: Markdown and package changes are syntactically clean.
  - Evidence: `git diff --check` and any package-specific smoke or pack output.
  - Audit: Separate audit should focus on activation semantics, not whitespace.

## Current State

Closed. Ralph packet `packet:20260515T215226Z-opencode-playbook-commands` updated `loom-playbooks/loom-playbooks.mjs` so `configureOpenCode()` registers 25 Playbook entries through `config.command` from `readPlaybookMacroCatalog().body` and no longer registers `loom-playbooks/skills` through `config.skills.paths`. Smoke, pack dry-run, direct Node import inspection, and `git diff --check` passed.

Audit `audit:20260515-opencode-playbook-commands` returned `clear` with no material findings. ACC-001 through ACC-005 are satisfied for the OpenCode package closure claim. Residual risks remain routed to downstream tickets: no live OpenCode TUI command invocation was run, and negative natural-prompt activation coverage belongs to `ticket:20260515-playbook-explicit-macro-docs-tests`.

## Journal

- 2026-05-15: Created ticket from `plan:20260515-playbook-explicit-macros`; depends on the canonical macro catalog ticket.
- 2026-05-15: Set status to active and launched `packet:20260515T215226Z-opencode-playbook-commands` after the catalog ticket closed.
- 2026-05-15: `packet:20260515T215226Z-opencode-playbook-commands` returned `stop`: OpenCode Playbooks now register explicit commands from the macro catalog and do not register Playbook skill paths. Evidence gathered: `npm --prefix loom-playbooks run smoke` passed with `commandCount: 25`, `macroCount: 25`, `registeredPlaybookSkillPaths: []`, and `playbookSkillPathsRegistered: false`; direct Node import check reported `commandCount: 25`, `macroCount: 25`, `skillPathCount: 0`, and no missing commands; `npm --prefix loom-playbooks run pack:check` passed and included `loom-playbooks.mjs` plus `skills/`; `git diff --check` passed. Moved ticket to review for acceptance/audit.
- 2026-05-15: Recorded clear Ralph-backed audit in `audit:20260515-opencode-playbook-commands` and closed the ticket. Remaining OpenCode natural-prompt negative validation is routed to the final docs/tests ticket.
