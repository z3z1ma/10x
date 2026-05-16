# Playbook Explicit Macros

ID: plan:20260515-playbook-explicit-macros
Type: Plan
Status: open
Created: 2026-05-15
Updated: 2026-05-15
Risk: medium - changes shipped package surfaces, adapter manifests, and activation expectations across supported harnesses.

## Summary

Convert Loom Playbooks from broad auto-activated workflow skills into explicit user-invoked workflow macros or explicit-only skills, preserving Core record-skill routing as the natural-language activation owner.

This needs more than one ticket because the work spans a shared Playbook content source, OpenCode command config, native Claude/Cursor/Codex explicit-only behavior, Gemini command files, docs, smoke checks, and activation tests. The completed plan should leave Playbooks installable and discoverable without causing natural prompts to auto-load workflow lenses.

## Related Records

- `spec:playbook-explicit-macros` - defines the intended behavior, requirements, scenarios, and harness-specific limits this plan implements.
- `research:20260515-playbook-command-surfaces` - identifies each supported harness's command or explicit-only skill surface and the Codex limiting case.
- `research:20260515-playbooks-core-activation-pressure` - explains why broad automatic Playbook activation should be replaced.
- `evidence:20260515-playbook-activation-stacking` - preserves observed Playbook stacking and current test gaps.
- `loom-playbooks/` - current package surface to convert.
- `CLAUDE.md` and `tests/skill-triggering/` - current stale natural-prompt activation assumptions that must be revised.

## Strategy

Use a contract-first route. First create a canonical Playbook macro catalog or generation seam so later adapter tickets do not copy and drift 25 workflow bodies by hand. Then update each adapter family using the strongest explicit surface it supports: OpenCode command config, Claude/Cursor/Codex explicit-only native surfaces, and Gemini TOML commands. Finish by rewriting docs and tests so validation rewards Core-first natural prompts and explicit Playbook invocation instead of automatic Playbook triggering.

The work deliberately leaves individual Playbook workflow redesign out of scope. Macro bodies may adjust headers, descriptions, and invocation framing to satisfy explicit macro behavior, but the purpose is not to rewrite each workflow lens.

OpenCode and Gemini work can proceed independently after the catalog exists. Claude, Cursor, and Codex share enough explicit-only skill mechanics that they should be handled together, with Codex kept honest: no custom slash-command claim unless newer source-backed research changes the constraint.

Replan if implementation shows a harness cannot expose the intended explicit behavior, if a canonical source would require broader content migration than expected, or if validation cannot distinguish natural Core activation from Playbook macro invocation.

## Execution Units

### Unit: Canonical Playbook Macro Catalog

Ticket: ticket:20260515-playbook-macro-catalog

Create the shared Playbook macro source or generation seam that downstream adapter tickets consume. The ticket should preserve the existing Playbook workflow value while reframing each Playbook as an explicit optional lens and preventing adapter-specific body drift.

This must run first. Evidence should be source inspection and smokeable package introspection showing all Playbooks are represented and product-visible macro content avoids contributor-only leakage.

### Unit: OpenCode Command Surface

Ticket: ticket:20260515-opencode-playbook-commands

Convert the OpenCode Playbooks package from `config.skills.paths` registration to explicit command registration through `loom-playbooks.mjs`, using the catalog from the first ticket. The ticket's single closure claim is that OpenCode installs Playbooks as commands and no longer exposes them as implicit model skills.

This depends on `ticket:20260515-playbook-macro-catalog`. Evidence should include source inspection plus `npm --prefix loom-playbooks run smoke`, `npm --prefix loom-playbooks run pack:check`, and `git diff --check` or a documented narrower equivalent if later package changes alter the command set.

### Unit: Claude Cursor Codex Explicit-Only Surfaces

Ticket: ticket:20260515-native-playbook-explicit-surfaces

Update Claude, Cursor, and Codex native plugin surfaces so Playbooks are available only through explicit commands or explicit-only skills. Claude and Cursor may use command files or skills with `disable-model-invocation: true`; Codex must use explicit-only skills with `policy.allow_implicit_invocation: false` unless newer source-backed research changes the Codex constraint.

This depends on `ticket:20260515-playbook-macro-catalog`. Evidence should include source inspection of manifests and explicit-only metadata, plus native plugin validation commands where available and applicable.

### Unit: Relocate Playbook Skill Corpus

Ticket: ticket:20260515-playbook-skill-corpus-relocation

Move the shared Playbook skill corpus out of top-level `loom-playbooks/skills/` and update OpenCode, Claude, Cursor, Codex, package files, and contributor guidance to the relocated path. This preserves the existing `loom-playbooks/` Gemini extension root while removing Gemini's automatic extension skill discovery surface.

This unit was added after `research:20260515-gemini-playbooks-skills-root` and `decision:0001`. It must complete before Gemini command TOML work starts. Evidence should include Playbook count/path inspection, OpenCode smoke/pack checks, Claude plugin validation, stale-path grep, and `git diff --check`.

### Unit: Gemini Command Surface

Ticket: ticket:20260515-gemini-playbook-commands

Update the Gemini Playbooks extension to expose Playbooks through `commands/*.toml` prompt macros and stop relying on Gemini model-activated skills for Playbooks.

This depends on `ticket:20260515-playbook-skill-corpus-relocation`. Evidence should include source inspection of command TOML files, confirmation that top-level `loom-playbooks/skills/` is absent, `gemini extensions validate "$PWD/loom-playbooks"`, root validation if root manifests are touched, and `git diff --check`.

### Unit: Documentation Tests And Final Validation

Ticket: ticket:20260515-playbook-explicit-macro-docs-tests

Update human-facing docs, stale acceptance guidance, package smoke checks, and activation tests so they verify Core-first natural routing and explicit Playbook invocation. Remove or rewrite tests that expect natural prompts like `Let's make a react todo list` to auto-trigger Playbooks.

This depends on the adapter implementation tickets. Evidence should include updated test fixtures, negative activation checks for natural prompts, positive explicit-invocation checks where feasible, package smoke and pack checks, `git diff --check`, and a final audit or explicit audit waiver for the activation behavior claim.

## Milestones

### Milestone: Shared Macro Contract Exists

Child tickets: ticket:20260515-playbook-macro-catalog

All Playbooks have a canonical explicit macro representation that adapter tickets can consume without redefining the behavior.

### Milestone: Adapter Surfaces Are Explicit

Child tickets: ticket:20260515-opencode-playbook-commands, ticket:20260515-native-playbook-explicit-surfaces, ticket:20260515-playbook-skill-corpus-relocation, ticket:20260515-gemini-playbook-commands

Supported harness packages expose Playbooks through explicit command or explicit-only skill surfaces, and no supported package path intentionally keeps broad Playbook implicit activation.

### Milestone: Validation Story Reversed

Child tickets: ticket:20260515-playbook-explicit-macro-docs-tests

Docs and tests no longer treat natural Playbook autoactivation as success. The validation story proves natural prompts stay Core-first while explicit Playbook invocations still work.

## Current State

Open with Gemini commands next. The shared macro contract, OpenCode command, native explicit-only, and skill-corpus relocation milestones are complete with clear audits. `ticket:20260515-gemini-playbook-commands` is now open because top-level `loom-playbooks/skills/` is absent from the Gemini extension root. The final docs/tests ticket remains blocked until Gemini commands close.

## Journal

- 2026-05-15: Created plan from `spec:playbook-explicit-macros` and `research:20260515-playbook-command-surfaces` with five child execution units.
- 2026-05-15: Closed `ticket:20260515-playbook-macro-catalog` after implementation and clear Ralph audit; adapter command and explicit-only surface tickets are now unblocked.
- 2026-05-15: Closed `ticket:20260515-opencode-playbook-commands` after implementation and clear Ralph audit. OpenCode Playbooks now register explicit commands from the macro catalog instead of a Playbook skill path.
- 2026-05-15: Closed `ticket:20260515-native-playbook-explicit-surfaces` after implementation and clear Ralph audit. Claude/Cursor Playbooks are explicit-only skills, and Codex Playbooks have per-skill implicit-invocation disabled.
- 2026-05-15: Blocked `ticket:20260515-gemini-playbook-commands` after Gemini docs confirmed extension roots auto-discover top-level `skills/`. Need operator/package architecture decision: move shared skill corpus out of top-level `skills/`, or create a Gemini-specific command-only extension root.
- 2026-05-15: Operator selected the corpus-move route. Recorded `decision:0001`, added `ticket:20260515-playbook-skill-corpus-relocation`, and made it the hard prerequisite for Gemini command implementation.
- 2026-05-15: Closed `ticket:20260515-playbook-skill-corpus-relocation` after implementation, path-doc follow-up, and clear Ralph audit. Gemini command implementation is unblocked.
