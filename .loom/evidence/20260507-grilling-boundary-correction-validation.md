---
id: evidence:grilling-boundary-correction-validation
kind: evidence
status: recorded
created_at: 2026-05-07T15:32:57Z
updated_at: 2026-05-07T15:36:24Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:grfix507
  ticket_related:
    - ticket:grill507
  critique:
    - critique:grilling-boundary-correction-review
external_refs:
  matt_grill_with_docs: https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md
---

# Summary

Structural validation and targeted content observations for the corrective grilling
boundary edits under `ticket:grfix507`.

This evidence records observations. It does not decide ticket acceptance, closure,
or critique verdicts.

# Procedure

Observed at: 2026-05-07T15:32:57Z

Source state: commit `d75d3a418936613dcfc8a7741953292589981d66` on branch `main`,
with tracked spec/plan skill edits plus untracked root `.loom` records for this
Loom work. Unrelated todo-app example files, unrelated `package.json`, and other
prior Loom tranche files were present in the worktree and were not part of this
validation scope.

Procedure:

- Read Matt Pocock's `grill-with-docs` source directly from the local peer clone.
- Read the edited `loom-specs` and `loom-plans` skill, reference, and template
  surfaces.
- Ran `git diff --check -- skills/loom-specs skills/loom-plans .loom/tickets/20260507-grfix507-correct-grilling-boundaries.md`.
- Searched `skills/loom-specs` for `implementation`, `code`, `codebase`, `source reality`, `current source`, and `current implementation`.
- Searched spec and plan templates for grilling-pass remnants such as spec/planning
  grilling headings and material-question rows.
- After critique follow-up wording, reran scoped structural and content checks.
- Searched spec and plan skill surfaces for procedure anchors: relentless
  interview, one material question at a time, recommended answer, concrete
  scenarios, behavior contract, and execution units.
- Searched spec guidance for the removed process-metadata phrase about material
  questions being asked and stored with recommended answers.
- Searched scoped skill files and active ticket for trailing whitespace.
- Searched active ticket for unresolved placeholder patterns.
- Listed changed scoped skill files with `git diff --name-only -- skills/loom-specs skills/loom-plans`.

Expected result: scoped diff has no whitespace errors; spec surfaces no longer
mention current implementation or code/source coupling; spec and plan templates no
longer contain grilling-pass sections; plan skill guidance contains the grilling
operator procedure; spec skill guidance contains behavior-contract grilling;
active ticket is placeholder-clean.

Actual observed result:

- `git diff --check` produced no output for the scoped paths.
- The spec coupling search returned no files for the searched terms.
- The spec and plan template grilling-remnant searches returned no files.
- Plan guidance anchor search found the procedure in `skills/loom-plans/SKILL.md`:
  relentless operator interview, one material question at a time, recommended
  answers, terminology challenge, concrete execution scenarios, dependent-branch
  walking, and preserving only resulting execution units / assumptions / loopbacks
  in the plan.
- Plan template and reference still expose `Execution Units / Ticket Slices` as the
  record shape for detailed ticket-ready decomposition.
- Spec guidance anchor search found behavior-contract grilling in
  `skills/loom-specs/SKILL.md` and `skills/loom-specs/references/spec-shape.md`:
  relentless interview, one material question at a time, recommended answers,
  terminology challenge, concrete scenarios, design-tree walking, and owner-layer
  routing.
- Post-critique search confirmed the process-metadata phrase about material
  questions being asked and stored with recommended answers was removed; spec
  guidance now asks for material decisions that were resolved, routed, or left
  blocking.
- Trailing-whitespace searches returned no files for scoped spec/plan skill files
  and the active ticket.
- Active ticket placeholder-pattern search returned no files.
- Changed scoped skill files were `skills/loom-plans/SKILL.md`,
  `skills/loom-plans/references/plan-shape.md`,
  `skills/loom-plans/references/slicing.md`, `skills/loom-plans/templates/plan.md`,
  `skills/loom-specs/SKILL.md`, `skills/loom-specs/references/spec-shape.md`, and
  `skills/loom-specs/templates/spec.md`.

Procedure verdict / exit code: pass for scoped structural checks. Mandatory
critique remains required before ticket closure.

# Raw Artifact Store

- Path: None - no raw artifacts were created for this validation.
- Captured artifacts: None - validation output is summarized directly in this
  evidence record.
- Key excerpts / index: N/A.
- Redaction / sensitivity: no sensitive values observed in scoped output.
- Retention / tracking: N/A.

# Supports Claims

- `ticket:grfix507#ACC-001` - template grilling-remnant searches returned no files,
  supporting that spec and plan templates no longer contain grilling sections.
- `ticket:grfix507#ACC-002` - plan skill procedure now carries the grilling loop as
  operator behavior.
- `ticket:grfix507#ACC-003` - plan template/reference still center execution units
  / ticket slices for detailed decomposition.
- `ticket:grfix507#ACC-004` - spec skill/reference now keep grilling focused on
  behavior-contract hardening, and the searched spec surfaces have no current-code
  or current-implementation coupling terms.
- `ticket:grfix507#ACC-005` - structural validation passed; critique remains a
  separate gate recorded as `critique:grilling-boundary-correction-review`.

# Challenges Claims

None from the scoped checks.

# Environment

Commit: `d75d3a418936613dcfc8a7741953292589981d66`

Branch: `main`

Runtime: ordinary Git and file-content checks; no project build or test suite exists
for the skills corpus.

OS: macOS / Darwin via current OpenCode environment.

Relevant config: `AGENTS.md` says verification is structural/manual and product
surface is `skills/`.

External service / harness / data source when applicable: local peer clone under
the OpenCode temp directory was used for Matt's `grill-with-docs` source.

# Validity

Valid for: scoped spec/plan grilling boundary edits at the observed worktree state.

Fresh enough for: structural validation and critique preparation for
`ticket:grfix507`.

Recheck when: spec/plan skill files, active ticket, evidence record, or critique
record changes.

Invalidated by: source or record changes after this observation, reintroduced
template grilling sections, reintroduced spec current-code coupling, or critique
findings that challenge this validation.

Supersedes / superseded by: None.

# Limitations

- This is structural and content-anchor evidence, not proof that future agents will
  apply grilling well.
- The checks are scoped to spec and plan skill surfaces plus the active ticket.
- The evidence does not validate unrelated todo-app example files or unrelated
  worktree modifications.

# Result

The scoped validation observed clean whitespace checks, no spec current-code/source
coupling term hits, no grilling-remnant hits in spec or plan templates, and the
expected grilling procedure anchors in spec/plan skill guidance.

# Interpretation

The observations support mandatory critique review for `ticket:grfix507`. They do
not by themselves close the ticket or prove future operator behavior.

# Related Records

- `ticket:grfix507`
- `ticket:grill507`
- `critique:grilling-boundary-correction-review`
