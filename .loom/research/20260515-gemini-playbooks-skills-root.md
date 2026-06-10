# Gemini Playbooks Skills Root Conflict

Status: completed
Created: 2026-05-15
Updated: 2026-05-15

## Summary

Gemini CLI extension docs make the remaining Playbooks conversion non-local: an extension root with a top-level `skills/` directory automatically contributes model-activated skills. The current `loom-playbooks` root cannot honestly become Gemini commands-only while it still contains `skills/` for other adapters.

## Question

Can `.loom/tickets/done/20260515-gemini-playbook-commands.md` expose Gemini Playbooks as commands without moving or splitting the current `loom-playbooks/skills/` directory?

## Scope

Covered:

- Gemini CLI extension reference, extension writing guide, custom commands docs, and skills docs fetched on 2026-05-15.
- Current Agent Loom Playbooks package root shape: `loom-playbooks/gemini-extension.json`, `loom-playbooks/commands/` absent, and `loom-playbooks/skills/` present.
- The remaining Gemini ticket and plan/spec requirement that Gemini Playbooks stop relying on model-activated skills.

Excluded:

- Implementing a package restructure.
- Live Gemini extension validation.
- Revising the product spec or plan decomposition beyond blocker routing.

## Method And Sources

- Gemini extension reference, fetched 2026-05-15: extension roots can provide custom commands by placing TOML files in a `commands/` subdirectory; they can also bundle agent skills by placing skill definitions in a `skills/` directory.
- Gemini extension writing guide, fetched 2026-05-15: custom commands are invoked by the user, while agent skills are invoked by the model. The guide says Gemini CLI automatically discovers skills bundled with an extension and the model activates them when it identifies a relevant task.
- Gemini skills docs, fetched 2026-05-15: at session start, Gemini scans discovery tiers and injects the name and description of all enabled skills into the system prompt; extension skills are one of those discovery tiers; activation happens through `activate_skill` when the model matches a description.
- Gemini custom commands docs, fetched 2026-05-15: TOML commands are user-invoked prompt macros under `commands/`, with `prompt`, optional `description`, and argument/file/shell injection support.
- `.loom/research/20260515-playbook-command-surfaces.md` - earlier research that Gemini commands are the right explicit surface and Gemini skills are model-activated.
- `loom-playbooks/gemini-extension.json` and `loom-playbooks/skills/` - current source layout inspected during this plan.

## Findings

- Gemini command files and skills are separate extension features. Commands live under `commands/` and are invoked by the user. Skills live under `skills/` and are discovered by the model.

- Gemini extension skills are automatic discovery surfaces. The docs say extension skills are discovered at session start, names and descriptions are injected into the system prompt, and the model activates matching skills through `activate_skill`.

- Gemini docs fetched in this pass do not show a `disable-model-invocation` equivalent for Gemini skills, nor a manifest field that excludes an extension's `skills/` directory while keeping the same extension root active.

- The current Playbooks Gemini extension root is `loom-playbooks/` because it contains `loom-playbooks/gemini-extension.json`. That same root also contains `loom-playbooks/skills/`, which Gemini docs say is an extension skills directory.

- Adding `loom-playbooks/commands/*.toml` would create user-invoked commands, but it would not by itself remove the model-activated Playbook skill exposure from the same extension root.

## Tradeoffs

- Keep `loom-playbooks/` as the Gemini extension root and add commands only.
  Strength: smallest Gemini command change. Weakness: fails the spec because Gemini would still discover `skills/` from the same root.

- Move the shared Playbook skill corpus away from top-level `loom-playbooks/skills/` and update non-Gemini adapters to reference the new path.
  Strength: preserves one `loom-playbooks/` extension root for Gemini while removing Gemini auto-discovered skills. Weakness: broad package layout change across OpenCode, Claude, Cursor, Codex, NPM package files, docs, AGENTS guidance, and already-closed tickets.

- Create a Gemini-specific command-only extension root separate from the root that contains native skill surfaces.
  Strength: avoids moving the shared skill corpus and gives Gemini a clean `commands/` root with no `skills/`. Weakness: changes Gemini install and validation paths; the current repository guidance expects validating `$PWD/loom-playbooks`, not a sub-extension path.

- Accept Gemini skill activation as a temporary exception.
  Strength: avoids package restructure. Weakness: violates `.loom/specs/playbook-explicit-macros.md#REQ-006` and the research conclusion that Gemini skills remain model-activated.

## Rejected Paths And Null Results

- Adding Gemini command files under the current root is insufficient by itself because the root's `skills/` directory remains a Gemini extension skill source.

- Treating Claude/Cursor/Codex explicit-only metadata as portable to Gemini is unsupported by the fetched Gemini docs.

- Relying on docs alone to say "use commands, not skills" while leaving `skills/` under the Gemini extension root would make the product surface contradict its own installed behavior.

## Conclusions

- `.loom/tickets/done/20260515-gemini-playbook-commands.md` is blocked by package-root shape, not TOML syntax.

- The remaining Gemini work requires a package architecture decision before implementation: either move the shared Playbook skill corpus out of the Gemini extension root, or create a Gemini-specific command-only extension root and update install/validation guidance accordingly.

- The current spec remains directionally correct for Gemini: Playbooks should be commands, not Gemini skills. The open issue is which package surface should carry that behavior without breaking other adapters.

## Recommendations

- Do not implement Gemini commands in the current `loom-playbooks/` root while top-level `skills/` remains there; that would create commands and leave the auto-activated skills behind.

- Route the package-root choice back to the operator before changing source layout. This is a durable packaging/adapter decision that affects repository guidance and previously closed child-ticket assumptions.

- If preserving `loom-playbooks/` as the Gemini extension install path matters most, choose the corpus-move approach and update OpenCode/native adapters to reference the new skill source path.

- If minimizing disruption to OpenCode/Claude/Cursor/Codex matters most, choose the Gemini-specific extension root approach and update Gemini install/validation docs to use that root.

## Open Questions

- Should Agent Loom keep one Playbooks package root per adapter, even if that requires moving the shared skill corpus out of top-level `skills/`?
- Or should Gemini get a separate command-only extension root so other adapters can continue using `loom-playbooks/skills/`?

## Related Records

- `.loom/tickets/done/20260515-gemini-playbook-commands.md` - blocked consumer of this research.
- `.loom/tickets/20260515-playbook-explicit-macros.md` - broader conversion plan now blocked on the Gemini package-root decision.
- `.loom/specs/playbook-explicit-macros.md` - behavior contract requiring Gemini true commands and no Playbook skill exposure.
- `.loom/research/20260515-playbook-command-surfaces.md` - earlier harness command-surface research.
