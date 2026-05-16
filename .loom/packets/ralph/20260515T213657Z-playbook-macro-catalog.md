# Playbook Macro Catalog Implementation

ID: packet:20260515T213657Z-playbook-macro-catalog
Type: Packet
Status: consumed
Created: 2026-05-15 21:36 UTC
Updated: 2026-05-15 21:43 UTC
Target: ticket:20260515-playbook-macro-catalog
Packet Kind: Ralph
Mode: execution
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: 1
Risk: medium - establishes shared Playbook content source used by later adapter packaging.
Verification Posture: observation-first
Change Class: Playbook package source/catalog seam

## Mission

Implement the first ticket slice for `ticket:20260515-playbook-macro-catalog`: create the smallest correct canonical Playbook macro catalog or generation seam that represents every existing Playbook as an explicit optional workflow macro source while preserving Loom loop order and avoiding adapter-specific body drift.

This run is ready because `spec:playbook-explicit-macros` defines the intended behavior, `research:20260515-playbook-command-surfaces` constrains downstream adapter surfaces, and the ticket acceptance criteria bound the catalog-only work.

## Context Bundle

Records:

- `ticket:20260515-playbook-macro-catalog` - owns this execution slice, acceptance criteria, scope, and current state.
- `plan:20260515-playbook-explicit-macros` - explains sequencing and why adapter tickets depend on this catalog.
- `spec:playbook-explicit-macros` - authoritative behavior contract for explicit Playbook macros.
- `research:20260515-playbook-command-surfaces` - source-backed harness constraints for command or explicit-only surfaces.
- `research:20260515-playbooks-core-activation-pressure` - explains why macro framing must avoid automatic activation pressure.
- `evidence:20260515-playbook-activation-stacking` - observed failure mode and stale validation assumptions.
- `AGENTS.md` - contributor constraints for product-surface leakage, package shape, and validation commands.

Evidence Or Artifacts:

- None yet. The worker should gather source-inspection observations and command output in this packet output or in the ticket journal if useful.

Files, Diffs, Or External References:

- `loom-playbooks/skills/` - current Playbook corpus and likely source for canonical macro content.
- `loom-playbooks/loom-playbooks.mjs` - current package helper/inspection functions; may host catalog reader helpers if that is the smallest correct seam.
- `loom-playbooks/package.json` - current package file list; may need inclusion updates if a new catalog directory is added.
- `loom-playbooks/README.md` - read-only for this packet unless a tiny package-local catalog note is required; broader docs belong to a later ticket.

## Read Scope

- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `.loom/research/20260515-playbooks-core-activation-pressure.md`
- `.loom/evidence/20260515-playbook-activation-stacking.md`
- `AGENTS.md`
- `loom-playbooks/skills/**`
- `loom-playbooks/loom-playbooks.mjs`
- `loom-playbooks/package.json`
- `loom-playbooks/README.md`

## Write Scope

Records Or Artifacts:

- `.loom/tickets/20260515-playbook-macro-catalog.md` - update Current State and Journal with progress, blockers, evidence, or completion disposition.
- this packet - fill `## Worker Output`, update `Status:`, and add follow-up notes when appropriate.

Source Paths:

- `loom-playbooks/` - only files needed for the canonical macro catalog or generation seam and package inclusion. Do not implement adapter-specific command surfaces in this packet.

## Source Snapshot

The current branch is `main` at worktree `/Users/alexanderbutler/code_projects/personal/agent-loom`. The working tree already contains untracked Loom records from the current shaping pass: `research:20260515-playbook-command-surfaces`, `spec:playbook-explicit-macros`, `plan:20260515-playbook-explicit-macros`, and the five child tickets. No Playbook package source files have been changed by this ticket yet.

Current implementation reality:

- `loom-playbooks/loom-playbooks.mjs` reads `loom-playbooks/skills/*/SKILL.md`, registers the skill root through `config.skills.paths`, and smoke-checks broad trigger description prefixes.
- `loom-playbooks/package.json` currently packs only `loom-playbooks.mjs` and `skills/`.
- The package has no canonical command or macro catalog separate from the current skill corpus.

## Task

Implement the smallest catalog/generation seam that satisfies `ticket:20260515-playbook-macro-catalog#ACC-001` through `ACC-005`.

Guidance:

- Prefer minimal changes. A correct solution may derive macro entries from the existing `skills/*/SKILL.md` corpus if it can reframe them as explicit macros and prevent downstream adapter drift without duplicating all bodies.
- Preserve all current Playbook names unless a rename is unavoidable; if unavoidable, record the reason in the ticket.
- Expose enough helper data or functions for later adapter tickets to generate OpenCode commands, native explicit-only surfaces, and Gemini commands from one source.
- Replace broad implicit activation wording in catalog-facing metadata with explicit optional macro wording where needed.
- Do not implement OpenCode command registration, native plugin explicit-only flags, Gemini TOML files, broad docs, or activation tests in this packet.
- Do not move contributor-only package, smoke, test harness, dogfood, or repository workflow commentary into model-visible Playbook content.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, stay inside its read/write scope, update the ticket and this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Source-inspection observation showing every current Playbook is represented by the catalog or generation seam.
- Source-inspection observation showing catalog metadata frames Playbooks as explicit optional macros rather than automatic trigger skills.
- Source-inspection observation showing the chosen seam can be consumed by downstream adapter tickets without manually duplicating all Playbook bodies.
- Run `npm --prefix loom-playbooks run smoke` if the package inspection code changes.
- Run `git diff --check` after edits.
- If any expected command is unavailable or not applicable, record the reason in Worker Output and ticket Current State.

## Stop Conditions

- Stop and return `blocked` if representing all Playbooks requires a product decision about command names or grouping that is not settled by the spec.
- Stop and return `escalate` if preserving existing Playbook bodies would require rewriting workflow behavior beyond explicit macro framing.
- Stop and return `blocked` if the write scope is too narrow to update required package inclusion files.
- Stop instead of editing adapter manifests, Gemini commands, global docs, or activation tests.
- Stop if the packet context no longer matches the current ticket, spec, or package source state.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

If this run supports closure, acceptance, evidence, audit, research, knowledge, or future recovery, preserve this output in the packet or in a cited durable record; do not leave it only in transient launch output.

## Worker Output

Outcome: stop

Files changed:

- `loom-playbooks/loom-playbooks.mjs`

Records changed:

- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/packets/ralph/20260515T213657Z-playbook-macro-catalog.md`

Evidence, review findings, validation output, or observations gathered:

- Implemented `readPlaybookMacroCatalog(options)` as the shared catalog seam. It derives each macro from the existing `skills/*/SKILL.md` corpus, preserving stable Playbook names and source paths while wrapping body content with explicit optional workflow macro framing.
- Implemented `inspectPlaybookMacroCatalog(options)` and wired it into `inspectLoomPlaybooksBundle()` and the smoke output. The smoke check now fails if a Playbook skill is missing from the derived macro catalog or if generated catalog descriptions retain `Use when`, `Use before`, or `Use after` trigger framing.
- `npm --prefix loom-playbooks run smoke` passed. Relevant output: `"skillCount": 25`, `"macroCount": 25`, `"macrosResult": "derived from skills as explicit optional workflow macros"`, `"macroChecks": { "ok": true, "missingMacros": [], "automaticDescriptionFailures": [] }`.
- Package introspection command comparing `readSkillFiles()` and `readPlaybookMacroCatalog()` passed with `skillCount: 25`, `macroCount: 25`, `sameSet: true`; the macro names were the full current Playbook set.
- Representative macro inspection for `loom-idea-refine`, `loom-debugging-and-error-recovery`, `loom-frontend-ui-engineering`, `loom-source-driven-development`, `loom-incremental-implementation`, `loom-security-and-hardening`, and `loom-shipping-and-launch` showed descriptions start with `Explicit optional workflow macro for ...` and generated bodies start with the explicit invocation preamble.
- Targeted product-surface leakage grep over `loom-playbooks/*.mjs` for `package smoke|adapter mechanics|test harness|dogfood|repository workflow|npm packaging` returned no matches.
- `git diff --check` passed with no output.

What was not verified or reviewed:

- No adapter-specific command, native explicit-only skill, Gemini TOML, manifest, docs, or activation test behavior was implemented or verified; those are later tickets.
- No independent audit was run in this packet. The ticket is in review for ACC-001 through ACC-005 challenge before closure.
- The derived macro body still includes the current Playbook body after the explicit macro preamble; this packet did not rewrite individual Playbook workflows beyond catalog-facing framing.

Blockers, risks, or assumptions discovered:

- No blocker encountered.
- Assumption: using existing Playbook names as macro names is the stable catalog identity for this first seam; downstream adapter tickets may still choose harness-specific command aliases without changing the canonical macro source.
- Risk: downstream adapter generators must consume `body` from `readPlaybookMacroCatalog()` rather than copying raw `SKILL.md` bodies, or they could lose the explicit macro preamble.

Recommended next move for the consuming surface:

- Run a narrow audit/review of `ticket:20260515-playbook-macro-catalog` against ACC-001 through ACC-005. If accepted, close this ticket and unblock `ticket:20260515-opencode-playbook-commands`, `ticket:20260515-native-playbook-explicit-surfaces`, and `ticket:20260515-gemini-playbook-commands` to consume `readPlaybookMacroCatalog()` as the shared source.
