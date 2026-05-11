---
id: evidence:artifact-store-validation
kind: evidence
status: recorded
created_at: 2026-05-07T15:11:00Z
updated_at: 2026-05-07T15:37:30Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:artf507
  critique:
    - critique:artifact-store-review
external_refs: {}
---

# Summary

Structural validation and targeted content observations for the optional raw
artifact store guidance under `ticket:artf507`.

This evidence records observations. It does not decide ticket acceptance, closure,
or critique verdicts.

# Procedure

Observed at: 2026-05-07T15:11:00Z

Source state: branch `main`, with tracked skill and `.gitignore` edits plus
untracked root `.loom` records for this Loom work. Unrelated todo-app example files
and an unrelated `package.json` modification were present in the worktree and were
not part of this validation scope.

Procedure:

- Ran `git diff --check -- .gitignore skills/loom-evidence skills/loom-research skills/loom-records/references/naming-and-ids.md .loom/tickets/20260507-artf507-add-artifact-stores.md`.
- Searched scoped evidence, research, and records Markdown files plus the active
  ticket for trailing whitespace.
- Searched changed skill files for guidance anchors covering the evidence and
  research artifact-store paths, `Raw Artifact Store`, `Source Material Store`,
  `support cache`, `usually gitignored`, and `primary understanding`.
- Ran `git check-ignore -v` against representative artifact paths under
  `.loom/evidence/artifacts/` and `.loom/research/artifacts/`.
- Searched scoped evidence, research, and naming guidance for hidden-runtime drift
  terms including `MCP`, `DevTools`, `subagent`, `hook`, `daemon`, `installer`,
  `command wrapper`, `validator`, `schema`, `database`, and `runtime`.
- Listed scoped changed files with `git diff --name-only -- .gitignore skills/loom-evidence skills/loom-research skills/loom-records/references/naming-and-ids.md`.

Expected result: no whitespace errors; no trailing whitespace in scoped files; new
artifact-store guidance appears in the intended evidence, research, template, and
record-grammar surfaces; representative artifact paths are ignored by `.gitignore`;
hidden-runtime scan does not show a new required runtime, database, validator,
command wrapper, hook, MCP, or schema system.

Actual observed result:

- `git diff --check` produced no output for the scoped paths.
- Trailing-whitespace searches returned no files for scoped evidence, research,
  naming guidance, and active ticket files.
- Anchor search found artifact-store guidance in `skills/loom-evidence/SKILL.md`,
  `skills/loom-evidence/references/evidence-quality.md`,
  `skills/loom-evidence/templates/evidence.md`, `skills/loom-research/SKILL.md`,
  `skills/loom-research/references/source-handling.md`,
  `skills/loom-research/templates/research.md`, and
  `skills/loom-records/references/naming-and-ids.md`.
- `git check-ignore -v` reported `.gitignore:2:/.loom/evidence/artifacts/` for
  `.loom/evidence/artifacts/example/output.log` and
  `.gitignore:3:/.loom/research/artifacts/` for
  `.loom/research/artifacts/example/source.pdf`.
- Hidden-runtime scan found benign matches only: `evidence-quality.md` explicitly
  says not to turn the artifact store into a hidden validator, dashboard, queue,
  database, or canonical truth layer; existing performance evidence guidance uses
  `device/runtime`; `naming-and-ids.md` uses `validators` only in existing memory
  metadata discussion.
- Changed scoped files were `.gitignore`, `skills/loom-evidence/SKILL.md`,
  `skills/loom-evidence/references/evidence-quality.md`,
  `skills/loom-evidence/templates/evidence.md`,
  `skills/loom-records/references/naming-and-ids.md`,
  `skills/loom-research/SKILL.md`,
  `skills/loom-research/references/source-handling.md`, and
  `skills/loom-research/templates/research.md`.

Procedure verdict / exit code: pass for scoped structural checks. Mandatory
critique is recorded as `critique:artifact-store-review`.

# Raw Artifact Store

- Path: `None - no raw artifacts were created for this validation`
- Captured artifacts: None - validation output is summarized directly in this
  evidence record.
- Key excerpts / index: `git check-ignore -v` output is quoted in the procedure
  result above.
- Redaction / sensitivity: no sensitive values observed in scoped output.
- Retention / tracking: N/A.

# Supports Claims

- `ticket:artf507#ACC-001` - evidence guidance defines the optional slugged raw
  artifact store under `.loom/evidence/artifacts/`.
- `ticket:artf507#ACC-002` - research guidance defines the optional slugged
  source-material store under `.loom/research/artifacts/`.
- `ticket:artf507#ACC-003` - guidance says the stores are usually gitignored,
  may be absent, useful to inspect when named, and secondary to the Markdown
  evidence or research record.
- `ticket:artf507#ACC-004` - templates and naming guidance include artifact-store
  citation, redaction, retention/tracking, and support-cache boundaries.
- `ticket:artf507#ACC-005` - scoped structural checks, `.gitignore` check, and
  hidden-runtime scan found no whitespace, ignore, or hidden-runtime drift issue;
  mandatory critique found no high/medium blockers.

# Challenges Claims

None from the scoped checks.

# Environment

Commit: not recorded; validation was performed in a dirty worktree on branch `main`.

Branch: `main`

Runtime: ordinary Git and file-content checks; no project build or test suite exists
for the skills corpus.

OS: macOS / Darwin via current OpenCode environment.

Relevant config: `.gitignore` now ignores `/.loom/evidence/artifacts/` and
`/.loom/research/artifacts/`.

External service / harness / data source when applicable: N/A.

# Validity

Valid for: scoped artifact-store guidance and `.gitignore` changes at the observed
worktree state.

Fresh enough for: structural validation and critique preparation for
`ticket:artf507`.

Recheck when: `.gitignore`, evidence/research guidance, naming guidance, active
ticket, evidence record, or critique record changes.

Invalidated by: source or record changes after this observation, new artifact-store
paths, hidden runtime requirements introduced later, or critique findings that
challenge this validation.

Supersedes / superseded by: None.

# Limitations

- This is structural and content-anchor evidence, not proof that future agents will
  capture raw artifacts well.
- No actual raw artifact directory was created; `git check-ignore` used
  representative paths to verify ignore behavior.
- It does not validate unrelated todo-app example files or unrelated `package.json`
  changes.

# Result

The scoped validation observed clean whitespace checks, intended artifact-store
guidance anchors in evidence/research/record-grammar surfaces, `.gitignore` coverage
for representative artifact paths, and no hidden runtime requirement drift in the
searched scoped guidance.

# Interpretation

The observations support mandatory critique review for `ticket:artf507`. They do
not by themselves close the ticket or prove future artifact-store usage quality.

# Related Records

- `ticket:artf507`
- `critique:artifact-store-review`
