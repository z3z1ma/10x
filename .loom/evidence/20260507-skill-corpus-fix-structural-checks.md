---
id: evidence:skill-corpus-fix-structural-checks
kind: evidence
status: recorded
created_at: 2026-05-07T18:43:58Z
updated_at: 2026-05-07T18:45:01Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:pkt7z924
external_refs: {}
---

# Summary

Structural validation for `ticket:pkt7z924` after skill-corpus consistency fixes and oracle review follow-ups.

# Procedure

Observed at: 2026-05-07T18:43:58Z

Source state: current working tree with uncommitted changes under `skills/`, `.loom/tickets/20260507-pkt7z924-address-skill-corpus-review-findings.md`, `.loom/evidence/20260507-skill-corpus-fix-structural-checks.md`, and `.loom/critique/20260507-skill-corpus-fix-review.md`.

Procedure: ran targeted checks for whitespace, frontmatter parseability, shared `change_class` vocabulary parity, and the specific contradiction patterns that triggered the fix.

Expected result when applicable: structural checks pass; canonical value lists match; removed contradiction patterns are absent; evidence disposition vocabulary appears in the owning ticket and record grammar surfaces.

Actual observed result: checks passed with the outputs below.

Procedure verdict / exit code: pass; commands returned exit code 0 except content searches whose successful expected result was “no files found”.

# Artifacts

- `git diff --check -- skills .loom/tickets/20260507-pkt7z924-address-skill-corpus-review-findings.md` produced no output, indicating no whitespace errors in the scoped diff.
- YAML frontmatter parse command over `skills/*/SKILL.md`, `skills/*/templates/*.md`, and the ticket parsed successfully when permitting YAML timestamp values. Ruby emitted local gem-extension warnings for `eventmachine`, `ffi`, and `http_parser.rb`; those warnings were unrelated to frontmatter parsing and did not cause failure.
- `change_class` parity script printed `missing=` and `extra=`, indicating the packet-frontmatter list matches `skills/loom-records/references/change-class.md`.
- Search for `git_status_summary:.*unknown with rationale` under `skills/` returned no files.
- Search for overbroad spike mutation phrases `mutates repository files|mutates the repository|mutated repository files|mutated repository` under `skills/loom-spike` returned no files.
- Search for evidence disposition vocabulary found aligned references in `skills/loom-tickets/SKILL.md`, `skills/loom-tickets/templates/ticket.md`, `skills/loom-tickets/references/acceptance-gate.md`, and `skills/loom-records/references/status-lifecycle.md`.
- After adding the evidence and critique records, final scoped whitespace and frontmatter parse checks were rerun over changed `skills/`, ticket, evidence, and critique records and passed.

# Raw Artifact Store

- Path: `None - command outputs are short and summarized directly in this evidence record`
- Captured artifacts: `None - no separate raw log retained`
- Key excerpts / index: See `# Artifacts`.
- Redaction / sensitivity: No sensitive values observed in the summarized outputs.
- Retention / tracking: This Markdown evidence record is sufficient.

# Visual / Product Evidence

N/A - this ticket changes Markdown protocol guidance and templates, not UI/product surfaces.

# Supports Claims

- ticket:pkt7z924#ACC-002 — structural checks verified the fixed vocabulary and placeholders no longer contradict the owning references targeted by this ticket.
- ticket:pkt7z924#ACC-003 — provides structural evidence used by the final critique record for review sufficiency.

# Challenges Claims

None - the observed checks did not produce failing structural output.

# Environment

Commit: current working tree, uncommitted.
Branch: not material to this structural record; git status was not clean because unrelated untracked example files preexisted.
Runtime: local shell, Ruby with YAML parser.
OS: macOS / Darwin.
Relevant config: no project test suite exists; validation is structural and manual per repository guidance.
External service / harness / data source when applicable: OpenCode local tool execution.

# Validity

Valid for: the scoped Markdown skill/template/reference/ticket edits present at observation time.
Fresh enough for: ticket:pkt7z924 structural acceptance and critique review of the current diff.
Recheck when: any changed `skills/` files, ticket, evidence, or critique records are edited again before closure.
Invalidated by: later edits that alter the checked vocabulary, templates, status lifecycle, spike wording, or ticket/critique/evidence records without rerunning relevant checks.
Supersedes / superseded by: None.

# Limitations

This evidence does not prove that future agents will follow the guidance correctly. It does not replace adversarial critique, semantic review of all skill text, or acceptance by the ticket owner. It also does not validate unrelated untracked `examples/00-todo-app` files.

# Result

The scoped structural validation passed and supports the claim that the targeted consistency fixes are structurally aligned.

# Interpretation

The checks support structural consistency for the edited surfaces. They do not by themselves decide ticket closure or critique verdict.

# Related Records

- ticket:pkt7z924
