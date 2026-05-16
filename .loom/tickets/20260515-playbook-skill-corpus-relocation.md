# Playbook Skill Corpus Relocation

ID: ticket:20260515-playbook-skill-corpus-relocation
Type: Ticket
Status: closed
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - moves a shared Playbook package path consumed by OpenCode, Claude, Cursor, Codex, Gemini, package files, and contributor guidance.
Priority: high - unblocks Gemini command-only Playbooks while preserving one Playbooks extension root.
Depends On: ticket:20260515-playbook-macro-catalog

## Summary

Relocate the shared Playbook skill corpus out of top-level `loom-playbooks/skills/` so Gemini does not auto-discover Playbooks as extension skills from the `loom-playbooks/` root. The closure claim is that non-Gemini adapters and package code consume the relocated corpus, while the top-level `skills/` directory is gone from the Playbooks extension root.

## Related Records

- `decision:0001` - durable decision to keep the `loom-playbooks/` Gemini extension root and move the shared skill corpus away from top-level `skills/`.
- `research:20260515-gemini-playbooks-skills-root` - source-backed Gemini auto-discovery conflict that this ticket resolves.
- `audit:20260515-playbook-skill-corpus-relocation` - clear Ralph-backed review of ACC-001 through ACC-005.
- `plan:20260515-playbook-explicit-macros` - broader conversion plan now updated with this prerequisite unit.
- `spec:playbook-explicit-macros` - requires Gemini command macros and no Playbook skill exposure.
- `ticket:20260515-playbook-macro-catalog` - closed prerequisite that created the catalog seam.
- `ticket:20260515-opencode-playbook-commands` - closed ticket whose OpenCode catalog reader must be updated to the relocated path.
- `ticket:20260515-native-playbook-explicit-surfaces` - closed ticket whose native plugin manifests and explicit-only metadata must follow the relocated path.
- `ticket:20260515-gemini-playbook-commands` - blocked consumer that requires top-level `skills/` removal before command TOML work can honestly proceed.
- `AGENTS.md` - contributor guidance currently states `loom-playbooks/skills/` as a product surface and must be updated with the new package shape.

## Scope

May move the shared Playbook skill directories from `loom-playbooks/skills/` to a non-Gemini-discovered package path such as `loom-playbooks/playbooks/`, preserving all `SKILL.md` files and Codex `agents/openai.yaml` policy files.

May update package code, native plugin manifests, NPM package files, smoke checks, validation references, and contributor guidance that must change for the relocated corpus to remain functional.

Likely write areas:

- `loom-playbooks/skills/**` move source.
- `loom-playbooks/playbooks/**` or chosen successor path.
- `loom-playbooks/loom-playbooks.mjs` catalog and OpenCode command loading path.
- `loom-playbooks/package.json` package `files` list.
- `loom-playbooks/.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json` native skill path entries.
- `AGENTS.md` contributor/package-shape guidance.
- Narrow docs path alignment in `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md` when stale references to the relocated corpus would make ACC-004 false.
- Loom tickets or plan records only as needed to keep execution state truthful.

Must not implement Gemini `commands/*.toml` in this ticket. That remains `ticket:20260515-gemini-playbook-commands` after relocation closes.

Must not rewrite individual Playbook workflow content except for path-relative fixes required by the move.

## Acceptance

- ACC-001: Top-level `loom-playbooks/skills/` no longer exists as a directory in the Playbooks extension root, and the relocated corpus contains all 25 Playbooks with their `SKILL.md` files and explicit-only metadata preserved.
  - Evidence: Source inspection or file listing comparing pre/post Playbook count and confirming no top-level `loom-playbooks/skills/` directory remains.
  - Audit: Review should challenge whether Gemini would still discover a top-level extension `skills/` directory.

- ACC-002: OpenCode Playbooks still register 25 explicit commands from the macro catalog after relocation and do not register Playbook skill paths.
  - Evidence: `npm --prefix loom-playbooks run smoke` and direct source or Node import inspection.
  - Audit: Review should challenge whether the catalog reader accidentally points at the old path or raw bodies without explicit macro framing.

- ACC-003: Claude, Cursor, and Codex plugin manifests reference the relocated corpus path, and native explicit-only metadata remains present for all 25 Playbooks.
  - Evidence: Source inspection of manifests, frontmatter counts, Codex policy counts, and `claude plugin validate "$PWD/loom-playbooks"` if available.
  - Audit: Review should challenge whether native adapters still point at the old missing path.

- ACC-004: Package inclusion and repository guidance are aligned with the relocated corpus.
  - Evidence: `npm --prefix loom-playbooks run pack:check`, source inspection of `AGENTS.md`, and targeted grep for stale active package-shape references to `loom-playbooks/skills/` outside historical Loom records.
  - Audit: Review should challenge whether future agents would reintroduce top-level `skills/` from stale guidance.

- ACC-005: The move stays behavior-preserving for Playbook bodies and does not implement Gemini commands, broad docs/tests, or unrelated package changes.
  - Evidence: Git diff/source inspection showing path move plus required references only; `git diff --check`.
  - Audit: Review should challenge scope creep and product-surface leakage.

## Current State

Closed. Ralph packet `packet:20260515T230227Z-playbook-skill-corpus-relocation` returned `continue`: the shared Playbook corpus moved to `loom-playbooks/playbooks/`, top-level `loom-playbooks/skills/` is absent, OpenCode catalog loading, package files, native plugin manifests, and `AGENTS.md` now point at the relocated corpus, and scoped verification passed.

Follow-up Ralph packet `packet:20260515T231048Z-playbook-relocation-doc-paths` returned `stop`: active documentation path/package-shape references in `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md` now point at `loom-playbooks/playbooks/` where they describe the relocated Playbooks corpus, while Core `loom-core/skills/` references remain intact. Targeted stale-path grep outside `.loom/` and `git diff --check` passed.

Audit `audit:20260515-playbook-skill-corpus-relocation` returned `clear` with no material findings. ACC-001 through ACC-005 are satisfied for the relocation closure claim. Residual limits are explicit: no live runtime invocation was performed, Gemini command validation remains downstream, and Cursor/Codex validator coverage was not available.

## Journal

- 2026-05-15: Created ticket from operator-selected `decision:0001` route after Gemini research showed top-level extension `skills/` blocks command-only Playbooks.
- 2026-05-15: Set status to active and launched `packet:20260515T230227Z-playbook-skill-corpus-relocation`.
- 2026-05-15: `packet:20260515T230227Z-playbook-skill-corpus-relocation` returned `continue`: moved the corpus to `loom-playbooks/playbooks/`, updated package/native/OpenCode/AGENTS references, preserved all 25 `SKILL.md` files plus 25 Codex policies and explicit-only frontmatter entries, and passed smoke, pack dry-run, Claude plugin validation, metadata counts, stale-path grep, and `git diff --check`. Active docs outside packet write scope still reference the old Playbooks path and need disposition before closure.
- 2026-05-15: Launched follow-up `packet:20260515T231048Z-playbook-relocation-doc-paths` for narrow path-only doc alignment needed by ACC-004.
- 2026-05-15: `packet:20260515T231048Z-playbook-relocation-doc-paths` returned `stop`: aligned active docs in `INSTALL.md`, `README.md`, `ARCHITECTURE.md`, and `loom-playbooks/README.md` with `loom-playbooks/playbooks/`; targeted stale-path grep outside `.loom/` returned no matches; relocated-path grep showed the updated doc references; `git diff --check` passed. Moved ticket to review for Ralph audit before closure.
- 2026-05-15: Recorded clear Ralph-backed audit in `audit:20260515-playbook-skill-corpus-relocation` and closed the ticket. Gemini command implementation is unblocked.
