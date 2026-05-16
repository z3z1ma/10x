# Native Playbook Explicit Surfaces Audit

ID: packet:20260515T221555Z-native-playbook-explicit-surfaces-audit
Type: Packet
Status: consumed
Created: 2026-05-15 22:15 UTC
Updated: 2026-05-15 22:18 UTC
Target: ticket:20260515-native-playbook-explicit-surfaces
Packet Kind: Ralph
Mode: review
Context Style: live-reference
Worker: subagent
Branch: main
Worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
Iteration: audit-1
Risk: medium - native explicit-only behavior depends on harness metadata semantics and broad per-skill updates.
Review Lens: audit, acceptance, scope, explicit-only semantics, product-surface leakage
Change Class: Native plugin explicit-only surface review

## Mission

Perform a bounded adversarial audit of `ticket:20260515-native-playbook-explicit-surfaces` against ACC-001 through ACC-005. Determine whether the Claude, Cursor, and Codex native Playbook surfaces can honestly close as explicit-only, or whether changes are needed before downstream docs/tests rely on them.

## Context Bundle

Records:

- `ticket:20260515-native-playbook-explicit-surfaces` - target ticket, acceptance, current state, and implementation summary.
- `packet:20260515T220601Z-native-playbook-explicit-surfaces` - implementation packet and worker output.
- `ticket:20260515-playbook-macro-catalog` - closed catalog prerequisite.
- `audit:20260515-playbook-macro-catalog` - clear audit of catalog seam.
- `plan:20260515-playbook-explicit-macros` - sequencing and remaining work.
- `spec:playbook-explicit-macros` - behavior contract for explicit-only native surfaces.
- `research:20260515-playbook-command-surfaces` - support matrix for Claude, Cursor, and Codex.
- `AGENTS.md` - product-surface leakage and adapter constraints.

Evidence Or Artifacts:

- Worker output in `packet:20260515T220601Z-native-playbook-explicit-surfaces` reports 25 `disable-model-invocation` entries, 25 Codex policy files, Claude plugin validation, and `git diff --check`.

Files, Diffs, Or External References:

- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `loom-playbooks/skills/**/SKILL.md`
- `loom-playbooks/skills/**/agents/openai.yaml`
- Current git diff, including untracked Codex policy files.

## Read Scope

- `.loom/tickets/20260515-native-playbook-explicit-surfaces.md`
- `.loom/packets/ralph/20260515T220601Z-native-playbook-explicit-surfaces.md`
- `.loom/tickets/20260515-playbook-macro-catalog.md`
- `.loom/audit/20260515-playbook-macro-catalog.md`
- `.loom/plans/20260515-playbook-explicit-macros.md`
- `.loom/specs/playbook-explicit-macros.md`
- `.loom/research/20260515-playbook-command-surfaces.md`
- `AGENTS.md`
- `loom-playbooks/.claude-plugin/plugin.json`
- `loom-playbooks/.cursor-plugin/plugin.json`
- `loom-playbooks/.codex-plugin/plugin.json`
- `loom-playbooks/skills/**/SKILL.md`
- `loom-playbooks/skills/**/agents/openai.yaml`
- Current git status and diff for native ticket files.

## Write Scope

Records Or Artifacts:

- this packet - fill `## Worker Output`, update `Status:`, and include findings and verdict.

Source Paths:

- None - this is a review packet. Do not edit source or tickets. Return findings for the parent to record and disposition.

## Source Snapshot

Implementation summary to challenge:

- All 25 Playbook `SKILL.md` files now have `disable-model-invocation: true` in frontmatter.
- Each Playbook directory now has `agents/openai.yaml` with `policy.allow_implicit_invocation: false`.
- Claude, Cursor, and Codex plugin descriptions now describe explicit-only workflow lenses.
- Codex interface text now says Playbooks should be invoked explicitly and not treated as automatic natural-language routes.
- The implementation chose explicit-only skills rather than separate adapter command files, keeping shared Playbook bodies in `skills/**/SKILL.md`.

## Task

Review the target ticket, diff, and evidence. Focus on:

- ACC-001: Does Claude have explicit-only behavior for all Playbooks, and did `claude plugin validate` pass?
- ACC-002: Does Cursor have explicit-only behavior for all Playbooks through documented `disable-model-invocation: true`?
- ACC-003: Does Codex have `policy.allow_implicit_invocation: false` for all Playbooks, and does plugin metadata avoid custom slash-command claims?
- ACC-004: Is the chosen body-alignment strategy acceptable? Specifically, native adapters keep shared `SKILL.md` bodies plus explicit-only metadata rather than command files generated from `readPlaybookMacroCatalog().body`. Decide whether that still satisfies alignment with the canonical macro source for explicit-only skill adapters, or whether it is a finding.
- ACC-005: Does changed native adapter content avoid contributor-only package smoke, adapter mechanics, dogfood state, npm packaging, test harness details, and repository workflow commentary?
- Scope: Did implementation stay out of OpenCode, Gemini, broad docs, tests, and unrelated package metadata?
- Evidence: Are source inspection, Claude plugin validation, and `git diff --check` enough for this closure claim, with Cursor/Codex runtime validation explicitly unverified?

Do not fix issues. Return findings with file/line or record references when practical, plus a verdict.

## Launch

Launch transport: harness-native subagent. Thin wrapper: read this packet first, perform the bounded audit, update this packet output, and return the output contract.

## Evidence, Review, Or Verification Expectations

- Review current diff and untracked files for native ticket scope.
- Count `disable-model-invocation: true` entries and Codex `allow_implicit_invocation: false` files.
- Run `claude plugin validate "$PWD/loom-playbooks"` if available.
- Run `git diff --check`.
- Run targeted leakage and unsupported Codex command-claim searches if useful.
- Findings should use `FIND-*` IDs for material issues, or say no material findings within scope.
- Verdict should be one of `clear`, `concerns`, `changes-needed`, or `inconclusive`, with limits.

## Stop Conditions

- Stop and return `inconclusive` if native source changes under review.
- Stop instead of modifying source or tickets.
- Stop and name missing context if exact explicit-only metadata semantics cannot be judged from the source-backed records and local files.

## Output Contract

The worker must update this packet or return output with:

- outcome: `continue`, `stop`, `blocked`, or `escalate`
- files changed
- records changed
- evidence, review findings, validation output, or observations gathered
- what was not verified or reviewed
- blockers, risks, or assumptions discovered
- recommended next move for the consuming surface

The review output must include any `FIND-*` findings and a bounded audit verdict that can be recorded under `.loom/audit/`.

## Worker Output

Outcome: stop

Files changed:

- None.

Records changed:

- `.loom/packets/ralph/20260515T221555Z-native-playbook-explicit-surfaces-audit.md` - filled Worker Output and marked the packet consumed.

Evidence, review findings, validation output, or observations gathered:

- Reviewed `ticket:20260515-native-playbook-explicit-surfaces`, the implementation packet, prerequisite catalog ticket and audit, plan, spec, research, `AGENTS.md`, native plugin manifests, representative Playbook bodies, scoped git status, and scoped diffs.
- `git status --short` shows the expected native manifest and 25 Playbook `SKILL.md` changes plus 25 untracked Codex policy files. It also shows pre-existing/out-of-scope Loom records and `loom-playbooks/loom-playbooks.mjs` changes from related catalog/OpenCode work; this audit did not attribute those to this native packet.
- Source inspection found 25 `disable-model-invocation: true` entries across 25 Playbook `SKILL.md` files, all at line 4, supporting Claude and Cursor explicit-only skill behavior when paired with the researched harness semantics.
- Source inspection found 25 `policy.allow_implicit_invocation: false` entries across 25 Playbook `agents/openai.yaml` files, with representative file `loom-playbooks/skills/loom-debugging-and-error-recovery/agents/openai.yaml` containing only that policy.
- `loom-playbooks/.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and `.codex-plugin/plugin.json` keep `skills: "./skills/"` and now describe Playbooks as explicit-only workflow lenses invoked deliberately after `loom-core` routing.
- `loom-playbooks/.codex-plugin/plugin.json` does not claim custom slash commands, custom prompt commands, or plugin-contributed command files. Its interface text says to invoke Playbooks explicitly and not treat them as automatic natural-language routes.
- Scoped diff shows native changes limited to the three native plugin manifests and Playbook skill metadata. The Codex policy files are untracked and therefore not present in `git diff`, but were inspected and counted directly.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `git diff --check` passed.
- Targeted leakage search over `loom-playbooks` Markdown, JSON, and YAML found only generic runtime terms such as `adapter`, `smoke`, and `test harness` inside Playbook guidance or package docs. Within the changed native product surfaces, no material contributor-only package smoke, adapter mechanics, dogfood state, npm packaging, repository workflow, or test-harness leakage was identified.

Review findings:

- None - no material findings within this bounded audit scope.

Verdict:

- `clear` - ACC-001 through ACC-005 are supported within the reviewed scope. Claude and Cursor explicit-only behavior is supported by `disable-model-invocation: true` on all 25 Playbooks plus successful Claude plugin validation. Codex explicit-only behavior is supported by one `agents/openai.yaml` policy file per Playbook with `allow_implicit_invocation: false` and Codex metadata that avoids unsupported slash-command claims. The shared-body strategy is acceptable for this native explicit-only skill route because the adapter surfaces reuse the canonical Playbook `SKILL.md` corpus directly and add explicit-only metadata rather than copying divergent command bodies; the macro catalog remains the generated command source for true command adapters. Changed native product-visible content does not show material contributor-only leakage.

What was not verified or reviewed:

- No live Claude, Cursor, or Codex runtime invocation was exercised.
- Cursor native plugin validation was not run; no Cursor validator command is listed in `AGENTS.md` or required by the packet.
- Codex native plugin validation was not run; no Codex validator command is listed in `AGENTS.md` or required by the packet.
- This audit did not perform exhaustive semantic review of every Playbook body beyond targeted metadata, representative body inspection, and leakage search.
- This audit did not review OpenCode, Gemini, broad docs, tests, package pack output, or final activation behavior outside the native ticket scope.

Blockers, risks, or assumptions discovered:

- No blockers.
- Residual risk: closure still depends on Claude, Cursor, and Codex honoring the researched metadata semantics at runtime; only Claude manifest validation and source inspection were observed here.
- Residual risk: using raw shared `SKILL.md` bodies for explicit-only skill adapters means these native surfaces do not include the generated macro preamble from `readPlaybookMacroCatalog().body`. This is acceptable for this ticket because explicit-only metadata carries the invocation constraint and avoids body duplication, but true command-surface tickets should continue consuming the macro catalog body.
- Residual risk: uncommitted related work is present in the workspace, including `loom-playbooks/loom-playbooks.mjs` and multiple Loom records. It appears tied to prerequisite/parallel tickets and was not modified by this audit.

Recommended next move for the consuming surface:

- Record a clear audit for `ticket:20260515-native-playbook-explicit-surfaces`, then let the ticket owner decide closure with the runtime-validation limits and residual risks stated explicitly.
