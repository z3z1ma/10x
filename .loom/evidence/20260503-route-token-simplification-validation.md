---
id: evidence:route-token-simplification-validation
kind: evidence
status: recorded
created_at: 2026-05-03T19:42:50Z
updated_at: 2026-05-03T19:46:54Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  tickets:
    - ticket:rtfree53
  critique:
    - critique:route-token-simplification-review
external_refs: {}
---

# Summary

Observed structural validation for removing saved route-token mechanics from
current Loom product guidance while preserving packet contract boundaries.

# Procedure

Observed at: 2026-05-03T19:46:54Z

Source state: branch `main`, HEAD `8e304ebbf6901c856fdb3694995c32d10754c580`,
dirty working tree with route-token simplification edits, expected-flow example
renames, and new Loom ticket/evidence/critique records.

Procedure:

- Ran targeted product-surface searches for stale saved-route wording across
  `skills/`, `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `AGENTS.md`, and
  `examples/`.
- Confirmed `examples/**/expected-route.md` no longer exists and replacement
  `examples/**/expected-flow.md` files exist as untracked files paired with the
  tracked deletions.
- Ran adversarial critique and a follow-up review after repairing the critique
  findings.
- Ran whitespace validation with `git diff --check`.
- Parsed frontmatter for the new ticket, evidence, and critique records.
- Searched the new records for unresolved placeholder leakage.

Expected result when applicable: current product surfaces do not instruct owners
to save next-route, Route, route-readiness, route-token, or `acceptance_review`
workflow-token fields; ticket template/readiness omit the old route sections;
packet guidance keeps bounded contract language; examples use expected-flow
fixtures; validation has no structural errors.

Actual observed result: targeted product searches found no stale current guidance
for expected-route fixtures, `acceptance_review`, Ralph saved route
authorization, or plan route fields. The remaining `next route` / `Route` /
route-readiness matches in `skills/` were four lines of prohibitory compatibility
text in `skills/loom-records/references/route-vocabulary.md`,
`skills/loom-tickets/references/readiness.md`, and
`skills/loom-workspace/references/routing.md`. `PROTOCOL.md` had one intentional
compatibility reference saying the old filename is not a saved route token
registry. Historical `.loom/` provenance was not treated as current product
guidance.

Procedure verdict / exit code: pass; `git diff --check` produced no output,
new-file whitespace scan printed `checked 9 untracked/new files`, frontmatter
parse printed `parsed 3 new Loom record frontmatter blocks`, placeholder scans
returned no files found, and final product/example searches had only intentional
compatibility/prohibition matches.

# Artifacts

- `skills/loom-records/references/route-vocabulary.md`
- `skills/loom-tickets/templates/ticket.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-workspace/references/routing.md`
- `skills/loom-drive/SKILL.md`
- `skills/loom-drive/references/checkpoint-resume-protocol.md`
- `skills/loom-drive/references/continuity-contract.md`
- `skills/loom-drive/references/tranche-decision-protocol.md`
- `skills/loom-ralph/templates/ralph-packet.md`
- `skills/loom-ship/SKILL.md`
- `skills/loom-ship/references/handoff-options.md`
- `skills/loom-plans/templates/plan.md`
- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `AGENTS.md`
- `examples/**/expected-flow.md`
- `git diff --check`: no output.
- New-file whitespace scan: `checked 9 untracked/new files`.
- New-record frontmatter parse: emitted local Ruby gem extension warnings, then
  printed `parsed 3 new Loom record frontmatter blocks`.
- New-record placeholder scans: no files found with the refined placeholder
  pattern.
- `glob examples/**/expected-route.md`: no files found.
- `glob examples/**/expected-flow.md`: six replacement fixture files found.
- Adversarial review task `ses_210a8b579ffeHPXuMd2JVF7laQ`: initial findings
  repaired; follow-up review reported no remaining findings.

# Supports Claims

- ticket:rtfree53#ACC-001: product guidance now frames workflow selection as
  reasoning from owner records, and the remaining forbidden field names occur as
  explicit prohibitions or compatibility notes.
- ticket:rtfree53#ACC-002: ticket template/readiness guidance no longer carries
  the old `# Next Move / Next Route` or `# Route Readiness` sections.
- ticket:rtfree53#ACC-003: packet guidance retains explicit bounded child
  contract fields while saying packets do not overrule ticket-owned truth.
- ticket:rtfree53#ACC-004: ship, drive, plan, workspace, Ralph, bootstrap, and
  package-framing docs use owner/workflow/acceptance-gate wording rather than
  saved route-token fields.
- ticket:rtfree53#ACC-005: examples use expected-flow files and wording.
- ticket:rtfree53#ACC-006: structural validation and mandatory critique completed.

# Challenges Claims

None - no final validation observation challenged the scoped acceptance criteria.

# Environment

Commit: `8e304ebbf6901c856fdb3694995c32d10754c580`

Branch: `main`

Runtime: Markdown/source validation with Git and ripgrep-backed searches through
the harness tools; no application runtime or automated test suite exists.

OS: macOS Darwin

Relevant config: repository product surface is the `skills/` corpus plus package
docs and internal examples for fixture consistency.

External service / harness / data source when applicable: oracle review task
`ses_210a8b579ffeHPXuMd2JVF7laQ` used as adversarial review support.

# Validity

Valid for: the route-token simplification diff at the observed source state.

Fresh enough for: structural acceptance of ticket:rtfree53 unless the changed
product surfaces or examples are edited materially.

Recheck when: ticket/readiness templates, route/workflow-selection guidance,
drive/ship/Ralph/plan/workspace surfaces, package docs, or example fixture names
change.

Invalidated by: later edits that reintroduce saved workflow-choice fields into
owner records or remove packet contract safeguards.

Supersedes / superseded by: none.

# Limitations

This evidence validates Markdown guidance and examples, not a runtime. It does
not migrate historical `.loom/` records that intentionally preserve prior route
vocabulary as provenance, and it does not stage or commit the untracked
`expected-flow.md` example files.

# Result

Current product guidance now teaches owner/workflow reasoning without saved
route-token fields, while packet contracts remain explicit bounded support
artifacts.

# Interpretation

The observations support accepting the route-token simplification when consumed
with `critique:route-token-simplification-review` and the ticket-owned finding
dispositions in `ticket:rtfree53`.

# Related Records

- ticket:rtfree53
- critique:route-token-simplification-review
