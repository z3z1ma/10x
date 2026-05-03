---
id: packet:ralph-ticket-trustbd2-20260503T042817Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:trustbd2
mode: execution
change_class: protocol-authority
risk_class: high
style: reference-first
verification_posture: observation-first
iteration: 2
created_at: 2026-05-03T04:28:17Z
updated_at: 2026-05-03T04:32:22Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - decision:0005
  paths:
    - INSTALL.md
    - gemini-bootstrap.md
    - .loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md
    - skills/loom-records/references/frontmatter.md
parent_merge_scope:
  records:
    - ticket:trustbd2
  paths:
    - .loom/tickets/20260503-trustbd2-add-trust-boundary-doctrine.md
    - .loom/evidence/20260503-trust-boundary-doctrine-validation.md
    - .loom/critique/trust-boundary-doctrine-review.md
    - .loom/packets/ralph/20260503T042019Z-ticket-trustbd2-iter-01.md
    - .loom/packets/ralph/20260503T042817Z-ticket-trustbd2-iter-02.md
source_fingerprint:
  git_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: fc29933b16d483abd6d376f0ea8563b7e3e62cba
  git_status_summary: dirty
  git_status_detail: dirty with trustbd2 iteration 1 product edits, ticket, packet, and evidence pending critique repair
  compiled_from:
    - ticket:trustbd2
    - critique finding TRUSTBD2-ORC-001
    - critique finding TRUSTBD2-ORC-003
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: tight
  max_source_files: 6
  max_excerpt_lines_per_file: 80
  avoid_full_file_reads: true
sources:
  ticket:
    - ticket:trustbd2
  critique_findings:
    - TRUSTBD2-ORC-001
    - TRUSTBD2-ORC-003
  files:
    - INSTALL.md
    - gemini-bootstrap.md
    - .loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md
    - skills/loom-records/references/frontmatter.md
links: {}
---

# Mission

Repair `ticket:trustbd2` critique findings `TRUSTBD2-ORC-001` and
`TRUSTBD2-ORC-003`.

# Bound Context

Iteration 1 added `skills/loom-bootstrap/references/08-trust-boundaries.md` to
mandatory bootstrap. Critique found the install/preload/constitutional surfaces
that enumerate bootstrap references still listed only `01` through `07`.
Critique also found one dropped code span around `external_refs`.

# Verification Targets

- `ticket:trustbd2#ACC-001`
- `ticket:trustbd2#ACC-002`
- `ticket:trustbd2#ACC-003`
- `ticket:trustbd2#ACC-004`

# Task For This Iteration

Make the smallest repair:

1. Update `INSTALL.md` bootstrap reference list to include
   `skills/loom-bootstrap/references/08-trust-boundaries.md`.
2. Update `gemini-bootstrap.md` to preload the new trust-boundaries reference.
3. Update `decision:0005` to say the ordered bootstrap references now run from
   `01` through `08`, with the original decision intact.
4. Restore code formatting around `external_refs` in
   `skills/loom-records/references/frontmatter.md`.

Do not edit evidence, ticket, critique, or packet records. The parent will refresh
evidence for `TRUSTBD2-ORC-002` after this child returns.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- `01` through `07` versus `01` through `08` bootstrap enumerations;
- presence of `08-trust-boundaries.md` in Gemini preload;
- `external_refs` code formatting;
- `git diff --check`.

# Stop Conditions

Stop if the repair would require changing the trust-boundary doctrine itself,
creating a new constitutional decision, or changing adapter mechanics beyond the
explicit reference lists.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled this repair packet after initial critique returned
`changes_requested`.

# Child Output

Outcome: stop - requested critique repairs were completed.

Files changed:

- `INSTALL.md`
- `gemini-bootstrap.md`
- `.loom/constitution/decisions/decision-0005-skill-packaged-bootstrap-doctrine.md`
- `skills/loom-records/references/frontmatter.md`

Records changed:

- `decision:0005`

Before observations:

- `INSTALL.md` listed bootstrap references `01` through `07` only.
- `gemini-bootstrap.md` preloaded `01` through `07` only.
- `decision:0005` said ordered references ran from `01-*.md` through `07-*.md`.
- The affected frontmatter prose had plain `external_refs` without code formatting.

After observations:

- `INSTALL.md` lists `01` through `08`, including
  `skills/loom-bootstrap/references/08-trust-boundaries.md`.
- `gemini-bootstrap.md` imports
  `@./skills/loom-bootstrap/references/08-trust-boundaries.md`.
- `decision:0005` says ordered references run from `01-*.md` through
  `08-*.md`.
- Frontmatter guidance restores code formatting around `external_refs`.

Validation: `git diff --check` passed with no output after child edits.

Self-review: edits stayed within the strict child write scope. Child noted that
pre-edit `git diff --check` was not captured, so only after-state whitespace was
directly observed.

Blockers/residual risks: no child-scope blockers. Parent still needed evidence
repair and ticket/critique reconciliation.

Recommendation: move to `review_required` after parent evidence refresh, then run
critique/acceptance follow-up.

# Parent Merge Notes

Accepted child output as in scope. Parent spot-check found one remaining stale
`decision:0005` consequence bullet that still said "seven former rule files" and
repaired it to avoid contradicting the new `01` through `08` bootstrap range.
Parent refreshed `evidence:trust-boundary-doctrine-validation`; next route is
mandatory critique.
