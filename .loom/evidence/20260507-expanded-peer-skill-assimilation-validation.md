---
id: evidence:expanded-peer-skill-assimilation-validation
kind: evidence
status: recorded
created_at: 2026-05-07T08:29:07Z
updated_at: 2026-05-07T08:41:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:agntsys7
  research:
    - research:agentsys-command-practices-synthesis
external_refs:
  agentsys_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/agentsys
  mattpocock_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/mattpocock-skills
  addyosmani_agent_skills_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/addyosmani-agent-skills
  superpowers_local_clone: file:///var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/superpowers
---

# Summary

Observed direct-read source coverage and structural validation for the expanded
peer skill assimilation tranche. This evidence supports review of
`ticket:agntsys7`; it does not decide acceptance or critique verdict.

# Procedure

Observed at: 2026-05-07T08:29:07Z

Source state: commit `3388ca12fba859b4bab6096bdd508987414b2bb5` on branch `main`, with a dirty worktree containing intended `skills/` and `.loom/` edits.

Procedure:

- Direct file reads from local peer clones for AgentSys, Matt Pocock skills, Addy Osmani agent skills, and Superpowers.
- `git diff --check -- skills .loom`
- `git diff --stat -- skills .loom`
- Placeholder scans for template placeholder tokens and common unfinished-work markers against the active `ticket:agntsys7` and research record.
- Targeted trailing-whitespace scans for relevant untracked target files that
  `git diff --check` does not cover.
- Final placeholder and trailing-whitespace scans for
  `.loom/critique/20260507-expanded-peer-skill-assimilation-review.md` and
  `skills/loom-critique/references/review-pass-splitting.md` after critique
  disposition fixes.
- Post-closure ticket scan for unresolved placeholder markers, pending disposition
  markers, stale continuation wording, and trailing whitespace.
- Runtime-drift lexical scan for `must install`, `requires npm`, `requires hook`, `JSON state`, `hidden runtime`, and `command runtime` under `skills/`.

Expected result when applicable:

- Direct-read synthesis cites concrete peer source files and line ranges.
- `git diff --check -- skills .loom` exits cleanly with no whitespace errors.
- Saved `.loom` ticket and research records contain no unresolved template placeholders.
- Relevant untracked target files contain no trailing whitespace.
- Runtime-drift scan finds no instructions that make a hidden runtime, npm installer, hooks, command runtime, or JSON state ledger the source of Loom behavior.

Actual observed result:

- Direct reads covered selected source files from all four peer source sets and were incorporated into `research:agentsys-command-practices-synthesis`.
- `git diff --check -- skills .loom` produced no output.
- `git diff --stat -- skills .loom` reported 63 changed tracked files, 1937 insertions, and 854 deletions after the critique fix. Untracked Loom records are covered by targeted scans below rather than by this tracked diffstat.
- Placeholder scans for the active ticket and research record returned `No files found`.
- Targeted trailing-whitespace scans returned `No files found` for:
  `skills/loom-tickets/references/local-execution.md`,
  `skills/loom-wiki/references/shared-language.md`,
  `skills/loom-workspace/references/task-routing-catalog.md`,
  `.loom/tickets/20260507-agntsys7-assimilate-agentsys-command-practices.md`,
  `.loom/research/20260507-agentsys-command-practices-synthesis.md`, and
  `.loom/evidence/20260507-expanded-peer-skill-assimilation-validation.md`.
- Final scans returned `No files found` for unresolved placeholder markers or
  trailing whitespace in `.loom/critique/20260507-expanded-peer-skill-assimilation-review.md`; final trailing-whitespace scan returned `No files found` for `skills/loom-critique/references/review-pass-splitting.md`.
- Post-closure scans returned `No files found` for unresolved placeholder markers,
  pending disposition markers, stale continuation wording, or trailing whitespace
  in `.loom/tickets/20260507-agntsys7-assimilate-agentsys-command-practices.md`.
- Runtime-drift scan found 8 matches, all in anti-pattern or guardrail wording: `hidden runtime` references in `loom-skill-authoring` guidance, `command runtime` in `loom-drive` as something not to copy, and existing anti-pattern wording.

Procedure verdict / exit code: pass for tracked whitespace validation, targeted
untracked trailing-whitespace scans, and active-record placeholder checks; pass
with noted guardrail-only matches for runtime-drift scan.

# Artifacts

Direct-read source observations included:

- AgentSys command/workflow/skill sources already cited in `research:agentsys-command-practices-synthesis`.
- Matt Pocock skills: `grill-me`, `grill-with-docs`, `tdd`, `prototype`, `triage`, `improve-codebase-architecture`, and `diagnose`.
- Addy Osmani agent skills: `idea-refine`, `source-driven-development`, `incremental-implementation`, `code-simplification`, `code-review-and-quality`, `performance-optimization`, `context-engineering`, and `shipping-and-launch`.
- Superpowers skills: `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, and `finishing-a-development-branch`.

Current Loom edits touched these newly-expanded assimilation surfaces in addition to prior tranche edits:

- `skills/loom-workspace/references/problem-shaping.md`
- `skills/loom-workspace/references/task-routing-catalog.md`
- `skills/loom-specs/references/spec-shape.md`
- `skills/loom-plans/references/slicing.md`
- `skills/loom-plans/references/plan-shape.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-tickets/references/local-execution.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-spike/SKILL.md`
- `skills/loom-critique/SKILL.md`
- `skills/loom-critique/references/critique-lens.md`
- `skills/loom-critique/references/finding-format.md`
- `skills/loom-critique/references/review-pass-splitting.md`
- `skills/loom-debugging/references/systematic-debugging.md`
- `skills/loom-evidence/references/evidence-quality.md`
- `skills/loom-research/references/research-shape.md`
- `skills/loom-codemap/SKILL.md`
- `skills/loom-wiki/references/shared-language.md`
- `skills/loom-ship/SKILL.md`
- `skills/loom-retrospective/SKILL.md`
- `skills/loom-skill-authoring/references/skill-review.md`

# Visual / Product Evidence

N/A - this tranche changes protocol/operator guidance, not UI or visual design.

# Supports Claims

- `ticket:agntsys7#ACC-001` — direct-read source coverage now includes all four requested peer source sets and line-referenced synthesis in `research:agentsys-command-practices-synthesis`.
- `ticket:agntsys7#ACC-002` — supported by `skills/loom-drive/references/drive-loop.md`, `skills/loom-tickets/references/readiness.md`, and `skills/loom-ship/SKILL.md` edits that route delivery, external issue/review, launch, rollback, and handoff facts through existing Loom owner layers.
- `ticket:agntsys7#ACC-003` — supported by `skills/loom-critique/SKILL.md`, `skills/loom-critique/references/critique-lens.md`, `skills/loom-critique/references/finding-format.md`, and `skills/loom-critique/references/review-pass-splitting.md` edits for five-axis review, AI-artifact cleanup, review-feedback verification, and stalled review-loop escalation.
- `ticket:agntsys7#ACC-004` — supported by `skills/loom-debugging/references/systematic-debugging.md` and `skills/loom-evidence/references/evidence-quality.md` edits for reproduction loops, root-cause investigation, performance baselines, one-variable experiments, and before/after measurement evidence.
- `ticket:agntsys7#ACC-005` — supported by `skills/loom-codemap/SKILL.md`, `skills/loom-research/references/research-shape.md`, and `skills/loom-wiki/references/shared-language.md` edits for deterministic collection, source quality/freshness, external consultation boundaries, and shared-language conflict routing.
- `ticket:agntsys7#ACC-006` — supported by `skills/loom-workspace/references/problem-shaping.md`, `skills/loom-workspace/references/task-routing-catalog.md`, `skills/loom-specs/references/spec-shape.md`, `skills/loom-plans/references/slicing.md`, `skills/loom-plans/references/plan-shape.md`, `skills/loom-ralph/references/packet-contract.md`, and `skills/loom-spike/SKILL.md` edits for one-question/codebase-first grilling, divergent/convergent shaping, not-doing boundaries, tracer-bullet/risk-first slicing, zero-context packet review, source-driven context, and throwaway prototype cleanup.
- `ticket:agntsys7#ACC-007` — supported by `skills/loom-ship/SKILL.md`, `skills/loom-retrospective/SKILL.md`, and `skills/loom-critique/references/finding-format.md` edits for docs/launch packaging, review comment classification, verification-before-claim discipline, finishing/abandon options, and workflow-pattern compounding.
- `ticket:agntsys7#ACC-008` — structural whitespace, targeted untracked trailing-whitespace, and active-record placeholder checks passed; runtime-drift scan found only guardrail/anti-pattern mentions. Mandatory critique is recorded separately and still controls final disposition.

# Challenges Claims

None observed by these checks.

# Environment

Commit: `3388ca12fba859b4bab6096bdd508987414b2bb5`

Branch: `main`

Runtime: Markdown corpus, no build or test runtime for product surface.

OS: darwin

Relevant config: `AGENTS.md` states the product surface is `skills/` and verification is structural/manual.

External service / harness / data source when applicable: local peer repository clones under `/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/`.

# Validity

Valid for: the observed source reads, skill/record diff state, whitespace validation, active ticket/research placeholder checks, and runtime-drift lexical scan at the stated source state.

Fresh enough for: mandatory critique of `ticket:agntsys7` protocol-authority changes.

Recheck when: `skills/`, `.loom/tickets/20260507-agntsys7-assimilate-agentsys-command-practices.md`, `.loom/research/20260507-agentsys-command-practices-synthesis.md`, or peer source clones materially change.

Invalidated by: later edits that introduce unvalidated whitespace, unresolved placeholders in saved Loom records, hidden runtime assumptions, or changes to the cited peer source observations.

Supersedes / superseded by: None.

# Limitations

- `git diff --check` checks whitespace only; it does not prove protocol quality or operator clarity.
- Placeholder scans were targeted to active saved `.loom` records, not every product template, because templates intentionally contain placeholder examples.
- Runtime-drift scan is lexical; mandatory critique must still judge owner-layer boundary regression and hidden-runtime risk.
- Direct reads were selected for relevance, not exhaustive full-repository audits of every peer file.
- Evidence supports critique and ticket acceptance review but does not itself close `ticket:agntsys7`.

# Result

The expanded peer source set was directly inspected and incorporated into research,
and structural checks did not reveal whitespace errors, active-record placeholders,
or hidden-runtime adoption wording.

# Interpretation

This observation supports proceeding to mandatory critique for high-risk
protocol-authority changes. It does not prove the edits are sufficient, clear, or
accepted; critique and ticket-owned acceptance still decide that.

# Related Records

- `ticket:agntsys7`
- `research:agentsys-command-practices-synthesis`
