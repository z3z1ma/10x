# Protocol Compression Final Validation

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

Final validation observations for `.loom/tickets/done/20260525-compression-validation-audit.md` and `.loom/tickets/20260525-loom-protocol-compression.md`. The observations cover current package checks, scoped diff shape, current line counts against the baseline categories, behavior-preservation searches, leakage searches, Playbook command sync, canonical/Codex agent alignment, and limits.

## Procedure

Commands and inspections were run from `/Users/alexanderbutler/code_projects/personal/agent-loom` after reading the final validation ticket, parent plan, compression spec, child tickets, linked evidence, linked audits, active knowledge preferences, and `AGENTS.md`.

Validation commands:

- `git status --short`
- `npm --prefix loom-core run smoke`
- `npm --prefix loom-core run pack:check`
- `npm --prefix loom-playbooks run smoke`
- `npm --prefix loom-playbooks run pack:check`
- `git diff --check`
- `git diff --stat -- <complete compression scope>`
- `git diff --name-only -- <complete compression scope>`
- Node inventory line-count comparison over the baseline categories from `.loom/evidence/20260525-compression-inventory-baseline.md`
- Node canonical/Codex agent prompt body comparison
- Node Playbook bundle command/macro sync inspection
- Targeted grep/source inspection over model-visible compressed surfaces for activation, shaping, ticket-owned Ralph, evidence, audit, worker-output reconciliation, active `Knowledge Preference` loading, explicit Playbook macro behavior, Driver/Weaver role behavior, and product-surface leakage terms

## Observations

### Workspace State

`git status --short` showed the expected dirty compression worktree: modified parent plan and child/final tickets, modified Core skill/agent surfaces, modified Playbook source/generated command/doc surfaces, and untracked compression evidence/audit records plus `.loom/knowledge/general-subagent-for-ralph-runs.md`. No unexpected out-of-scope source family appeared in the final validation scope.

### Required Commands

- `npm --prefix loom-core run smoke` passed. Output reported `ok: true`, `usingLoomFileCount: 8`, expected ordered using-loom files, deduped bootstrap injection, `skillCount: 11`, `agentCount: 2`, canonical/Codex Driver and Weaver prompt match checks true, write-boundary and direction-record-boundary checks true, and activation checks true with `missingPhrases: []`.
- `npm --prefix loom-core run pack:check` passed. It reran Core smoke successfully and completed `npm pack --dry-run` for `@z3z1ma/open-loom-core@0.3.0` with 69 total files.
- `npm --prefix loom-playbooks run smoke` passed. Output reported `ok: true`, `doesNotPreloadCoreDoctrine: true`, `skillCount: 25`, `commandCount: 25`, no missing commands, no registered Playbook skill paths, deduped command entries, and macro checks with no explicit description prefix failures.
- `npm --prefix loom-playbooks run pack:check` passed. It reran Playbooks smoke successfully and completed `npm pack --dry-run` for `@z3z1ma/open-loom-playbooks@0.3.0` with 53 total files.
- `git diff --check` passed with no output.

### Diff Scope

Scoped diff over the complete compression write/read scope reported 119 tracked files changed with 2,189 insertions and 5,453 deletions. The changed tracked files are in expected scope: `.loom/plans/`, `.loom/tickets/`, `ARCHITECTURE.md`, `PROTOCOL.md`, `loom-core/agents/`, `loom-core/codex/agents/`, `loom-core/skills/`, `loom-playbooks/playbooks/`, `loom-playbooks/commands/`, and `loom-playbooks/loom-playbooks.mjs`.

Untracked records expected from the workstream were existing child-slice evidence/audit records and the local execution preference knowledge record. This final validation adds this evidence record and `.loom/reviews/20260525-protocol-compression-final-audit.md`.

### Line Counts

Current counts for the same inventory categories used by `.loom/evidence/20260525-compression-inventory-baseline.md`:

| Category | Baseline Files | Baseline Lines | Current Files | Current Lines | Change |
|---|---:|---:|---:|---:|---:|
| Core skills markdown | 62 | 7,254 | 62 | 4,574 | -2,680 |
| Core agents | 2 | 446 | 2 | 187 | -259 |
| Core Codex agents | 2 | 444 | 2 | 185 | -259 |
| Playbook markdown | 25 | 3,945 | 25 | 3,870 | -75 |
| Generated Playbook commands | 25 | 3,970 | 25 | 3,895 | -75 |
| Core preload and entrypoint surfaces | 4 | 539 | 4 | 539 | 0 |
| Protocol docs | 5 | 931 | 5 | 896 | -35 |
| Inventory-relevant package manifests | 3 | 119 | 3 | 119 | 0 |
| Inventory-relevant activation tests | 4 | 352 | 4 | 352 | 0 |
| Total | 132 | 18,000 | 132 | 14,617 | -3,383 |

The final category reduction matches the sum of recorded child-ticket reductions: session kernel -233, record skills -2,447, agent prompts -518, and Playbook/docs -185, totaling -3,383 lines.

### Behavior Searches And Source Inspection

Targeted searches and source reads found the required behavior still present in model-visible compressed surfaces:

- Activation: `using-loom/SKILL.md` and `references/01-activation-discipline.md` still require skill invocation before responding, asking clarifying questions, code exploration, quick checks, edits, ticket creation, and Ralph launch.
- Shape before execution: `using-loom` and station skills still route ambiguity, hidden direction, system-shape, data/state, and coherence choices back to shaping or the owning surface before implementation.
- Ticket-owned Ralph: `using-loom`, `loom-tickets`, `loom-ralph`, Driver, and Playbooks retain bounded Ralph, durable ticket context, transient launch prompt, stop conditions, output contract, and reconciliation language.
- Evidence and audit: `loom-evidence`, `loom-audit`, `using-loom`, Driver, and Playbooks keep evidence as observation/backpressure, audit as bounded adversarial review, and closure as a ticket/consuming-surface decision rather than an evidence or audit-owned verdict.
- Worker output: `loom-ralph`, `loom-tickets`, Driver, and retrospective guidance retain worker output as claims until checked against scope and evidence, then reconciled into the consuming surface.
- Active knowledge preferences: `using-loom` still loads active `Type: Knowledge Preference` records after doctrine preload, and `loom-knowledge` keeps preferences as the only eager-loaded knowledge type by default.
- Playbook macro behavior: Playbook source and generated TOML commands keep the explicit macro preamble: operator-invoked workflow lens, Core routing preserved, named Loom skills followed fully, no natural-prompt activation, and no Playbook skill paths registered.
- Driver/Weaver roles: canonical and Codex surfaces retain Weaver as Design Office, Driver as Factory Floor, `.loom/` Weaver write boundary, no Weaver Ralph launch, Driver ticket-owned Ralph coordination, evidence, audit, and worker-output reconciliation.

### Product-Surface Leakage Searches

Targeted leakage search over Core model-visible Markdown/TOML surfaces found no matches for contributor-facing terms including `package smoke`, `adapter self`, `dogfood`, `repository workflow`, `npm pack`, `pack:check`, `why Loom is built`, `contributor`, `AGENTS.md`, `source repo`, `test harness`, `skill-authoring`, or `doesNotPreloadCoreDoctrine`.

Targeted leakage search over Playbook model-visible Markdown/TOML surfaces found two matches for `test harness` in `loom-debugging-and-error-recovery` source and generated command. Source inspection showed the phrase is a runtime debugging boundary example: "test harness to system under test". It does not explain repository tests, package smoke mechanics, dogfood state, or contributor workflow, so it was treated as non-leaking runtime doctrine.

### Generated And Adapter Alignment

- Canonical/Codex agent prompt comparison passed. `loom-core/agents/loom-driver.md` and `loom-core/codex/agents/loom-driver.toml` bodies are aligned; `loom-core/agents/loom-weaver.md` and `loom-core/codex/agents/loom-weaver.toml` bodies are aligned.
- Playbook bundle inspection passed with `commands.ok: true`, `macros.ok: true`, `commandCount: 25`, `macroCount: 25`, `missingCommands: []`, `registeredPlaybookSkillPaths: []`, and `explicitDescriptionPrefixFailures: []`.
- One first attempt at a custom Playbook sync script failed because it used stale property names for the inspection return shape. The corrected inspection used the actual `commands`, `macros`, and `skills` fields and passed. This was a validation-script mistake, not a source failure.

## What This Shows

- `.loom/tickets/done/20260525-compression-validation-audit.md#ACC-001` - supports - required Core/Playbooks smoke and pack checks passed, `git diff --check` passed, and the command results and limits are recorded here.
- `.loom/tickets/done/20260525-compression-validation-audit.md#ACC-002` - supports - targeted behavior searches/source inspection found the core compressed-protocol behaviors in current model-visible surfaces and did not identify blocking product-surface leakage.
- `.loom/tickets/done/20260525-compression-validation-audit.md#ACC-003` - supports in combination with `.loom/reviews/20260525-protocol-compression-final-audit.md`, which records the final fresh-context adversarial review.
- `.loom/tickets/done/20260525-compression-validation-audit.md#ACC-004` - supports - child tickets have evidence/audit links and closed state, current counts match their recorded reductions, and the parent plan/final ticket can cite this final validation story.
- `.loom/specs/loom-protocol-compression.md#REQ-001`, `REQ-003`, `REQ-006`, `REQ-007`, `REQ-008`, and `REQ-009` - supports - the final source state preserves the required protocol spine, session kernel, agent roles, portability posture, product-surface hygiene, and validation requirements within the observed scope.

## What This Does Not Show

- This evidence does not prove live behavior in every supported harness or with a separate fresh model performing ambiguous tasks.
- This evidence does not run Claude plugin validation, Gemini extension validation, Cursor hook runtime checks, or natural-prompt Playbook activation tests because manifest/hook behavior was not changed in this final station and the existing Playbook evidence is static/generation based.
- Targeted leakage searches reduce known-term risk but are not exhaustive semantic proof that no contributor-facing phrase exists.
- Evidence records observations; the final audit and ticket/plan records own review and closure disposition.

## Related Records

- `.loom/tickets/done/20260525-compression-validation-audit.md` - consuming final validation ticket.
- `.loom/tickets/20260525-loom-protocol-compression.md` - parent compression plan.
- `.loom/specs/loom-protocol-compression.md` - compression behavior contract.
- `.loom/evidence/20260525-compression-inventory-baseline.md` - baseline categories and counts.
- `.loom/reviews/20260525-protocol-compression-final-audit.md` - final audit that challenges this evidence and the closure story.
