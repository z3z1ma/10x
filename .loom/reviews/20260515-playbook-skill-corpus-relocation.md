# Playbook Skill Corpus Relocation Audit

Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Target: .loom/tickets/done/20260515-playbook-skill-corpus-relocation.md

## Summary

Ralph audit reviewed the Playbook skill corpus relocation against `.loom/tickets/done/20260515-playbook-skill-corpus-relocation.md` ACC-001 through ACC-005. The verdict was clear with no material findings within scope.

## Target

The audit targeted the package-layout relocation that moved the Playbook corpus from top-level `loom-playbooks/skills/` to `loom-playbooks/playbooks/`, updated package code and native manifests to the new path, aligned active docs/guidance, and left Gemini command TOML work for the downstream ticket.

## Audit Scope And Lenses

Scope:

- Challenge ACC-001 through ACC-005 for the relocation ticket.
- Verify top-level `loom-playbooks/skills/` absence and relocated corpus completeness.
- Verify OpenCode, Claude, Cursor, Codex, package files, docs, and guidance point at the relocated path.
- Verify no Gemini command TOML or broad behavior rewrite was folded into the relocation ticket.

Lenses:

- acceptance
- scope
- package path integrity
- Gemini skill exposure risk
- evidence sufficiency
- product-surface leakage and stale guidance

## Context And Evidence Reviewed

- Ralph packet: `former packet 20260515T231741Z-playbook-skill-corpus-relocation-audit` - bounded review contract and returned audit output.
- `.loom/tickets/done/20260515-playbook-skill-corpus-relocation.md` - target ticket acceptance and current state.
- `former packet 20260515T230227Z-playbook-skill-corpus-relocation` - relocation implementation packet and evidence.
- `former packet 20260515T231048Z-playbook-relocation-doc-paths` - docs path follow-up packet and evidence.
- `.loom/decisions/superseded/playbook-skill-corpus-root.md` - durable package decision selecting corpus relocation.
- `.loom/research/20260515-gemini-playbooks-skills-root.md` - Gemini extension skills root conflict.
- `.loom/specs/playbook-explicit-macros.md` - behavior contract.
- `.loom/tickets/20260515-playbook-explicit-macros.md` - sequencing and downstream Gemini ticket.
- `.loom/reviews/20260515-opencode-playbook-commands.md` and `.loom/reviews/20260515-native-playbook-explicit-surfaces.md` - prior clear audits for surfaces updated by relocation.
- `loom-playbooks/playbooks/**` - relocated corpus.
- `loom-playbooks/loom-playbooks.mjs`, `loom-playbooks/package.json`, native plugin manifests, `AGENTS.md`, `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md`.

Observed validation from the Ralph audit run:

- `loom-playbooks/skills/` is absent.
- `loom-playbooks/playbooks/` contains 25 `SKILL.md` files and 25 `agents/openai.yaml` files.
- 25 `disable-model-invocation: true` entries and 25 `allow_implicit_invocation: false` entries are present in the relocated corpus.
- `loom-playbooks/loom-playbooks.mjs` reads from `playbooks/`, registers commands through `config.command`, and does not register Playbook skill paths.
- `loom-playbooks/package.json` packs `playbooks/`; Claude, Cursor, and Codex manifests all reference `./playbooks/`.
- Scoped docs and guidance now reference `loom-playbooks/playbooks/` where they describe the relocated Playbooks corpus.
- Every relocated Playbook `SKILL.md` and `agents/openai.yaml` matches the corresponding pre-move source under `loom-playbooks/skills/`.
- `npm --prefix loom-playbooks run smoke` passed with 25 skills, 25 commands, 25 macros, no missing commands, no registered Playbook skill paths, and `playbookSkillPathsRegistered: false`.
- `npm --prefix loom-playbooks run pack:check` passed; dry-run includes `playbooks/**` and no stale top-level `skills/**` files.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `rg --glob '!/.loom/**' --glob '!.loom/**' 'loom-playbooks/skills' .` returned no matches.
- `git diff --check` passed.

## Findings

None - no material findings within audited scope.

## Verdict

`clear` - ACC-001 through ACC-005 are supported within the reviewed scope. The top-level Playbooks extension `skills/` directory is absent, the relocated `playbooks/` corpus preserves all 25 Playbooks and explicit-only metadata, OpenCode registers 25 explicit commands without Playbook skill paths, Claude/Cursor/Codex manifests and package inclusion point at the relocated corpus, active non-Loom guidance no longer references `loom-playbooks/skills/`, and the diff did not implement Gemini command TOML or broad behavior rewrites.

This verdict does not claim live OpenCode, Cursor, Codex, or Gemini runtime invocation; Gemini extension validation; Cursor or Codex native validator coverage; or exhaustive semantic review of every Playbook body.

## Required Follow-up

- Close `.loom/tickets/done/20260515-playbook-skill-corpus-relocation.md` if the consuming ticket accepts the residual validation limits.
- Unblock `.loom/tickets/done/20260515-gemini-playbook-commands.md`, which can now add Gemini command TOML under a Playbooks extension root with no top-level `skills/` directory.
- Final docs/tests work remains in `.loom/tickets/done/20260515-playbook-explicit-macro-docs-tests.md`.

## Residual Risk

- Cursor and Codex native behavior remains supported by source/manifests and prior clear audit, not live runtime or validator evidence.
- Gemini auto-discovery risk was judged from source layout and Gemini research; with no top-level `loom-playbooks/skills/` directory present, this audit found no remaining Playbook skill corpus for Gemini to auto-discover from the Playbooks extension root.

## Related Records

- `.loom/tickets/done/20260515-playbook-skill-corpus-relocation.md` - consuming ticket.
- `former packet 20260515T231741Z-playbook-skill-corpus-relocation-audit` - Ralph review packet that produced this verdict.
- `former packet 20260515T230227Z-playbook-skill-corpus-relocation` - relocation implementation packet.
- `former packet 20260515T231048Z-playbook-relocation-doc-paths` - docs path follow-up packet.
- `.loom/decisions/superseded/playbook-skill-corpus-root.md` - package decision this ticket implemented.
- `.loom/tickets/done/20260515-gemini-playbook-commands.md` - downstream ticket unblocked by relocation.
