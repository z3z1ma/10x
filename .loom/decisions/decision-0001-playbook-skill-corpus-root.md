# Decision 0001: Move Playbook Skill Corpus Out Of Extension Root

Status: active
Created: 2026-05-15
Updated: 2026-05-15

## Summary

Agent Loom will keep `loom-playbooks/` as the Gemini Playbooks extension root and move the shared Playbook skill corpus out of the top-level `skills/` directory. Future adapter work should reference the relocated skill corpus explicitly instead of restoring top-level `loom-playbooks/skills/`.

## Context

The Playbooks conversion changes Playbooks from broad model-activated workflow skills into explicit user-invoked macros or explicit-only skills. OpenCode now consumes a macro catalog from package source, and Claude/Cursor/Codex can use explicit-only skill metadata.

Gemini is different. Gemini CLI extension docs say extension roots automatically contribute skills from a top-level `skills/` directory, and those skill names and descriptions are injected for model activation. `.loom/research/20260515-gemini-playbooks-skills-root.md` shows that adding `commands/*.toml` under the current `loom-playbooks/` root would still leave Playbook skills auto-discoverable because that root also contains `skills/`.

The operator selected the single-root route: keep the existing `loom-playbooks/` Gemini extension root and move the shared skill corpus away from the top-level path that Gemini discovers.

## Decision

Move the shared Playbook skill corpus out of `loom-playbooks/skills/` to a non-Gemini-discovered source path, and update OpenCode, Claude Code, Cursor, Codex, package files, docs, tests, and validation expectations to reference the new path.

The top-level `loom-playbooks/skills/` directory should not be restored as a product surface while Gemini Playbooks are intended to be command-only. Gemini Playbooks should use `loom-playbooks/commands/*.toml` under the existing `loom-playbooks/` extension root.

## Alternatives

- Add Gemini commands under the current root and leave `loom-playbooks/skills/` in place. Rejected because Gemini would still auto-discover Playbook skills from the same extension root, contradicting the explicit macro spec.
- Create a Gemini-specific command-only extension root. Rejected for now because it changes Gemini install and validation paths while leaving the root Playbooks package shape split by adapter.
- Accept Gemini model-activated Playbook skills as an exception. Rejected because it violates `.loom/specs/playbook-explicit-macros.md` and keeps the activation pressure failure mode in one supported harness.

## Consequences

Future agents should expect a broader package-layout change, not a local Gemini TOML-only patch.

Implementation must update every surface that assumed `loom-playbooks/skills/` was the shared corpus path, including OpenCode catalog loading, Claude/Cursor/Codex plugin manifests, Codex per-skill policy files, NPM package files, docs, tests, and repository guidance.

Closed tickets that added explicit-only native metadata remain valid in intent, but their file paths may need follow-up edits as part of the Gemini unblock work. Those edits should be recorded under the Gemini package-root execution path or a successor ticket, not treated as accidental cleanup.

The accepted cost is a larger cross-adapter file move to preserve one Gemini extension root and remove implicit Gemini Playbook skill discovery.

## Revisit Or Supersede If

- Gemini CLI adds a documented extension manifest field or skill metadata field that disables model invocation or excludes extension `skills/` discovery.
- Agent Loom chooses to split Playbooks into adapter-specific package roots as a broader product direction.
- Future evidence shows moving the skill corpus breaks a first-class adapter in a way that a Gemini-specific extension root would avoid with lower total complexity.

## Related

- `.loom/research/20260515-gemini-playbooks-skills-root.md` - source-backed reason this package-root decision is needed.
- `.loom/specs/playbook-explicit-macros.md` - intended behavior requiring Gemini command macros and no Playbook skill exposure.
- `.loom/tickets/20260515-playbook-explicit-macros.md` - execution plan now blocked on this package-layout decision.
- `.loom/tickets/done/20260515-gemini-playbook-commands.md` - blocked ticket that should consume this decision.
