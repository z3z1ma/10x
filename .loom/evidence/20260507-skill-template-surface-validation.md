---
id: evidence:skill-template-surface-validation
kind: evidence
status: recorded
created_at: 2026-05-07T06:27:32Z
updated_at: 2026-05-07T06:35:03Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:tmplrs07
  research:
    - research:skill-template-benchmark-synthesis
external_refs: {}
---

# Summary

Structural validation for the skill/template reasoning-surface overhaul. The
observations support the ticket's template simplification, section-name
alignment, behavior-guard coverage, and no-hidden-runtime claims. This evidence
does not decide acceptance or replace the required critique.

# Procedure

Observed at: 2026-05-07T06:27:32Z

Source state: repo `main` at HEAD `3388ca12fba859b4bab6096bdd508987414b2bb5` with a dirty working tree containing the `skills/` edits and root Loom records for `ticket:tmplrs07`.

Procedure:

- `git diff --check`
- `rg -n '# Coverage|# Critique Disposition|# Retrospective / Promotion Disposition|# Acceptance Criteria' skills`
- `rg -n '<TBD|PLACEHOLDER|TODO' .loom/research .loom/tickets`
- `rg -n '<TBD|PLACEHOLDER|TODO' .loom/research/20260507-skill-template-benchmark-synthesis.md .loom/tickets/20260507-tmplrs07-simplify-template-reasoning-surfaces.md`
- `rg -n '^## Common Rationalizations$|^## Red Flags$|^## Verification$' skills/*/SKILL.md`
- `git diff --unified=0 -- skills | rg '^\+.*(script|runtime|daemon|MCP|CLI|validator|schema)'`
- `rg -n 'ticket:<token>#ACC-001|spec:<slug>#ACC-001|initiative:<slug>#OBJ-001|# Review And Follow-Through|# Acceptance' skills/loom-records/references/claim-coverage.md skills/loom-records/references/semantic-link-usage.md skills/loom-tickets/references/acceptance-gate.md skills/loom-tickets/references/readiness.md skills/loom-tickets/templates/ticket.md`
- `git diff --stat -- skills .loom/research .loom/tickets`

Expected result when applicable: no whitespace errors; no stale old ticket
section names in `skills/`; no unresolved placeholders in the active root ticket
or research record; behavior-guard sections present in the SKILL files where
added; no added hidden-runtime requirement; references align on `# Acceptance`
and `# Review And Follow-Through`.

Actual observed result: checks matched expectations with limitations noted below.

Procedure verdict / exit code: mixed pass. `git diff --check`, stale-heading scan,
and active-record placeholder scan produced no output. The broad root `.loom`
placeholder scan found older historical placeholder-validation tickets unrelated
to this pass. The added-line runtime-drift scan found lexical false positives but
no newly required hidden runtime.

# Artifacts

`git diff --check` output:

```text
<no output>
```

Stale ticket-heading scan against `skills/` output:

```text
<no output>
```

Active-record placeholder scan output:

```text
<no output>
```

Broad root `.loom` placeholder scan output, limited to historical tickets about
placeholder handling:

```text
.loom/tickets/20260502-tmplph8x-harden-template-placeholders.md:48:- Replace dangerous placeholder prose with explicit `<TBD: replace before saving>`
.loom/tickets/20260503-phvalid16-add-placeholder-validation.md:34:Templates intentionally use `<TBD: ...>` placeholders, but saved `.loom` records
.loom/tickets/20260503-phvalid16-add-placeholder-validation.md:57:  placeholders, example IDs, or generic TODO/TBD tokens unless explicitly
.loom/tickets/20260503-critph28-quote-critique-packet-placeholders.md:34:The critique packet template uses quoted `<TBD: ...>` form for many fields but
.loom/tickets/20260503-critph28-quote-critique-packet-placeholders.md:45:- Prefer `<TBD: ...>` placeholders with explicit replacement instructions.
.loom/tickets/20260503-critph28-quote-critique-packet-placeholders.md:55:  `<TBD: ...>` form consistently where YAML scalar safety matters.
.loom/tickets/20260503-critph28-quote-critique-packet-placeholders.md:114:Expected: targeted searches for unquoted placeholders, `<TBD:`, critique packet
.loom/tickets/20260503-critph28-quote-critique-packet-placeholders.md:172:Residual risks: Copied packets still depend on operators replacing `<TBD: ...>`
```

Behavior-guard scan output: `Common Rationalizations`, `Red Flags`, and
`Verification` sections are present in the changed core SKILL files including
tickets, specs, Ralph, critique, evidence, plans, research, debugging, spike,
wiki, skill-authoring, drive, records, workspace, retrospective, ship,
initiatives, constitution, memory, codemap, and git. `loom-bootstrap` remains
doctrine-index focused and was not given the repeated guard-section shape.

Runtime-drift added-line scan output:

```text
+- CLI or HTTP reproduction script
+| "The PR description can explain what is true." | PRs mirror Loom truth. They do not own acceptance, evidence, or risk. |
+description: "Routes <specific family of work>. Use when <specific trigger> needs a choice among <nearby owner layers or workflows>."
+description: "Does <specific capability>. Use when <specific trigger or situation>; <owner boundary if needed>."
+| "We should promote every useful note." | Promote repeated, reusable, or accepted understanding. Do not turn wiki into transcript residue. |
+- sources are missing or point only to chat/transcript memory
+| "Chat history is enough to resume." | Recovery must come from owner records, not transcript memory. |
+- [ ] The next skill is chosen from owner-layer truth, not habit or transcript context.
```

Interpretation of runtime-drift scan: these are false positives for forbidden
runtime drift. They refer to optional reproduction scripts, PR mirror boundaries,
template descriptions, memory as transcript context, and owner-layer routing. No
added line requires a shipped script, CLI, daemon, MCP, validator, schema, hidden
runtime, or new owner layer.

Diff stat for scoped product-surface and root Loom changes:

```text
49 files changed, 1183 insertions(+), 753 deletions(-)
```

# Visual / Product Evidence

N/A. This validation concerns Markdown protocol surfaces rather than a rendered
UI. Product/UX review guidance was added, but no visual artifact was produced.

# Supports Claims

- ticket:tmplrs07#ACC-001 — partial support. `skills/loom-tickets/templates/ticket.md` was shortened and stale section-name scans show related references now use the new compact sections; acceptance gate preservation still needs critique review.
- ticket:tmplrs07#ACC-002 — support. Claim matrix guidance is optional in `skills/loom-tickets/templates/ticket.md`, `skills/loom-records/references/claim-coverage.md`, and `skills/loom-tickets/references/acceptance-gate.md`.
- ticket:tmplrs07#ACC-003 — support. Spec template and guidance now include quality bar, examples/non-examples, assumptions/decision points, and evidence plan.
- ticket:tmplrs07#ACC-004 — partial support. Ralph, critique, wiki, drive handoff, plan, research, and evidence templates were edited and pass structural scans; critique still needs to judge whether safety fields were preserved sufficiently.
- ticket:tmplrs07#ACC-005 — support. Behavior-guard sections are present in the target core SKILL files and additional coordinator/support skills.
- ticket:tmplrs07#ACC-006 — support. Product/UX/visual critique profiles, UI/product evidence shape, spike variant guidance, debugging hypothesis guidance, and external skill benchmark lessons are reflected in product-surface files.
- ticket:tmplrs07#ACC-007 — support. Skill-authoring templates and references include process-over-knowledge, rationalizations, red flags, and evidence-backed verification guidance.
- ticket:tmplrs07#ACC-008 — partial support. Structural validation passed, but adversarial critique has not yet been recorded.

# Challenges Claims

None from these structural checks. The broad placeholder scan surfaced unrelated
historical placeholder examples in earlier tickets; it does not challenge the
active records for this pass.

# Environment

Commit: `3388ca12fba859b4bab6096bdd508987414b2bb5`

Branch: `main`

Runtime: ordinary Git and ripgrep-based structural queries through the active harness.

OS: macOS / Darwin

Relevant config: no project test suite; verification is structural/manual per `AGENTS.md`.

External service / harness / data source when applicable: none for validation commands.

# Validity

Valid for: the current dirty workspace state after the skill/template edits and before mandatory critique.

Fresh enough for: structural claims about section alignment, whitespace, active-record placeholders, behavior-guard coverage, and absence of newly required hidden runtime in added skill lines.

Recheck when: any `skills/` file, `.loom/research/20260507-skill-template-benchmark-synthesis.md`, or `.loom/tickets/20260507-tmplrs07-simplify-template-reasoning-surfaces.md` changes materially.

Invalidated by: further template/reference edits, ticket acceptance changes, or critique findings requiring edits.

Supersedes / superseded by: none.

# Limitations

- Structural scans do not prove the new guidance is the best protocol shape.
- Runtime-drift scan is lexical and can miss conceptual runtime drift or produce false positives.
- No adversarial critique had been recorded at observation time.
- No installed-package build or distribution packaging check was run.

# Result

The edited skill corpus passes the structural checks run so far. The evidence is
sufficient to route into mandatory critique, not sufficient by itself to close
`ticket:tmplrs07`.

Supplemental observation at 2026-05-07T06:35:03Z after critique-requested fixes:

- `git diff --check` produced no output.
- The stale ticket-heading scan against `skills/` produced no output.
- Targeted scan confirmed `Critique rationale:` and `Promotion / deferral rationale:` in `skills/loom-tickets/templates/ticket.md`.
- Targeted scan confirmed conditional risk restatement wording in `skills/loom-records/references/change-class.md`.
- Follow-up adversarial review verified the medium blocker and low wording drift as resolved, with no new high/medium blockers.

# Interpretation

The changes are structurally coherent enough for adversarial review: stale ticket
section references were removed from `skills/`, active Loom records have no
unresolved placeholders, behavior-guard sections were added broadly, and no new
hidden runtime requirement was observed in added skill lines.

# Related Records

- `ticket:tmplrs07`
- `research:skill-template-benchmark-synthesis`
