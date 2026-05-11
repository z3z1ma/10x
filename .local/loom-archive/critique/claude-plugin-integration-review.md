---
id: critique:claude-plugin-integration-review
kind: critique
status: final
created_at: 2026-04-26T00:51:07Z
updated_at: 2026-04-26T00:59:31Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: ticket:q7h1d05q Claude plugin integration
links:
  ticket:
    - ticket:q7h1d05q
  evidence:
    - evidence:claude-plugin-hybrid
external_refs:
  claude_code_docs:
    - https://code.claude.com/docs/en/hooks
    - https://code.claude.com/docs/en/plugin-marketplaces
---

# Summary

Oracle critique cycle for the Claude Code Loom plugin prototype, including the
marketplace manifest, plugin manifest, hooks, rule synchronization scripts,
restart guard, cleanup script, install docs, fixture notes, ticket, and evidence.

# Review Target

The review targeted the Claude integration for `ticket:q7h1d05q`:

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `hooks/hooks.json`
- `scripts/claude-sync-rules.sh`
- `scripts/claude-loom-restart-guard.sh`
- `scripts/claude-clean-rules.sh`
- `INSTALL.md`
- `examples/adapters/claude-plugin-install/README.md`
- `.loom/tickets/20260425-q7h1d05q-prototype-claude-hybrid-install.md`
- `.loom/evidence/claude-plugin-hybrid.md`

# Verdict

`pass_with_findings`

The final oracle pass found no blockers for local/prototype acceptance. Remaining
risks are release-packaging or future-hardening concerns rather than blockers to
the current integration state.

A post-marketplace-install oracle pass also found no local/prototype blockers
after the duplicate hook declaration was removed.

# Findings

## FIND-001: Initial sync trusted project-controlled manifest paths

Severity: high
Confidence: high
Disposition: resolved

Observation:

The first critique found that `.loom-plugin-manifest` entries could drive deletes
outside the managed rules directory and that symlinked destinations could redirect
managed writes.

Why it matters:

Project-local Claude settings and rule directories can be repository-controlled.
The sync script must not follow hostile paths when installing always-on rules.

Follow-up:

Resolved by validating managed filenames as safe basenames, rejecting symlinked
destinations, rejecting symlinked/non-regular managed files and manifests,
checking resolved destination scope, and writing generated files via same-directory
temporary files plus rename.

Challenges:

- `ticket:q7h1d05q`

## FIND-002: Initial sync failures could fail open

Severity: high
Confidence: high
Disposition: resolved

Observation:

The first critique found missing source rules, copy failures, malformed settings,
or hook interruptions could leave no restart marker, allowing prompts to proceed
without Loom loaded.

Why it matters:

Claude's `SessionStart` hook cannot block session start, so the prompt guard must
have enough state to block unsafe sessions.

Follow-up:

Resolved by adding `sync-failed` and `sync-pending` marker paths consumed by the
`UserPromptSubmit` guard. The sync script fails closed for missing sources, zero
rules, malformed/unsafe manifests, unmanaged destination Markdown, symlinked
paths, and generic errors.

Challenges:

- `ticket:q7h1d05q`

## FIND-003: Multiple generated Claude rule files assumed undocumented order

Severity: medium
Confidence: high
Disposition: resolved

Observation:

The first implementation copied each canonical `rules/*.md` file into Claude's
rule surface, relying on filename order.

Why it matters:

Claude docs do not document deterministic ordering for multiple rule files.

Follow-up:

Resolved by generating one managed `loom.md` file from the canonical rules in
sorted order. Canonical truth remains in top-level `rules/`; generated Claude
output is derivative.

Challenges:

- `ticket:q7h1d05q`

## FIND-004: Plugin disable/uninstall has no lifecycle hook

Severity: medium
Confidence: high
Disposition: accepted_risk

Observation:

Claude docs do not describe an uninstall hook for removing generated static rule
files when a plugin is disabled or removed.

Why it matters:

Generated rules can remain active after plugin disable unless users clean them up.

Follow-up:

Accepted for prototype with explicit cleanup via `scripts/claude-clean-rules.sh`
and docs. A release-grade marketplace package should provide a clearer cleanup UX.

Challenges:

- `ticket:q7h1d05q`

## FIND-005: Marketplace source uses repository root

Severity: medium
Confidence: high
Disposition: accepted_risk

Observation:

`.claude-plugin/marketplace.json` uses `source: "./"`, making the repository root
the plugin source for local/Git marketplace testing.

Why it matters:

Broad distribution may cache dogfooding/support files that are not intended to be
part of a minimal Claude plugin package.

Follow-up:

Accepted for local/prototype use. Release packaging should introduce a narrower
Claude plugin artifact or otherwise validate marketplace cache contents.

Challenges:

- `ticket:q7h1d05q`

## FIND-006: Plugin manifest duplicated the standard hooks file

Severity: medium
Confidence: high
Disposition: resolved

Observation:

Local marketplace install initially reported a hook-load error because
`.claude-plugin/plugin.json` declared `"hooks": "./hooks/hooks.json"` while Claude
also auto-loaded the standard plugin `hooks/hooks.json` path.

Why it matters:

`claude plugin validate .` did not catch the duplicate, but an installed plugin
would surface errors in `claude plugin list --json`.

Follow-up:

Resolved by removing the duplicate `hooks` manifest field. A temporary-`HOME`
marketplace add/install test then installed `loom@agent-loom` without hook-load
errors, and runtime probes confirmed hooks still auto-loaded from the standard
path.

Challenges:

- `ticket:q7h1d05q`

# Evidence Reviewed

- Oracle critique pass 1: blocking issues found in manifest safety, fail-open
  sync behavior, cleanup, stale files, packaging, ordering, portability, and JSON
  escaping.
- Oracle critique pass 2: symlinked managed files remained a blocker; packaging
  and plugin-ID matching were residual risks.
- Oracle critique pass 3: no local/prototype blockers remained after symlink and
  pending-marker hardening; one non-blocking manifest directory concern remained.
- Final local fix: non-regular managed manifests are rejected and tested.
- Marketplace install fix: removed duplicate `hooks` manifest field after local
  marketplace install surfaced a hook-load error; retest installed without errors.
- Final post-install oracle pass: no local/prototype blockers; only ticket closure
  hygiene and release-packaging risks remained.
- `claude plugin validate .`
- script-level tests recorded in `evidence:claude-plugin-hybrid`
- runtime first-prompt guard and second-session load probes recorded in
  `evidence:claude-plugin-hybrid`

# Residual Risks

- Release marketplace packaging still needs a narrower/audited package shape or
  final cache-content validation because `source: "./"` is broad.
- Cleanup is explicit, not automatic, because Claude docs do not describe an
  uninstall hook.
- Runtime skill and command invocation from an installed marketplace plugin remains
  unproven.
- The hook scripts are POSIX shell helpers; Windows support remains unproven.
- Project plugin matching intentionally accepts `loom` and `loom@...`; exact
  marketplace qualification may need tightening before broad distribution.

# Required Follow-up

Before broad/public Claude marketplace distribution:

- validate marketplace update/cache contents for release packaging
- decide whether to create a narrower Claude package artifact
- validate runtime skills and commands from an installed marketplace plugin
- decide final cleanup UX for disable/uninstall
- decide whether exact `loom@agent-loom` matching should replace broad `loom@...`

# Acceptance Recommendation

complete pending acceptance

The current Claude integration is acceptable as a local/prototype integration for
`ticket:q7h1d05q`. It should not yet be marketed as production-grade marketplace
distribution until the residual release-packaging risks are handled.
