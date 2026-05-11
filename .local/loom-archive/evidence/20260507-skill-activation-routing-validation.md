---
id: evidence:skill-activation-routing-validation
kind: evidence
status: recorded
created_at: 2026-05-07T07:46:15Z
updated_at: 2026-05-07T07:52:52Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:actvskill
  research:
    - research:external-skill-activation-deep-dive
external_refs: {}
---

# Summary

Structural validation for the skill activation and common-task routing pass. The
observations support the claims that skill descriptions now carry broader trigger
language, new routing/local-execution/shared-language references are linked, new
change classes are visible, and stale old ticket headings did not reappear.

# Procedure

Observed at: 2026-05-07T07:46:15Z

Source state: repo `main` at current dirty workspace state after the activation
and routing edits.

Procedure:

- `git diff --check`
- `rg -n '^description: ".*Use (when|for|first|after)' skills/*/SKILL.md`
- `rg -n 'task-routing-catalog|local-execution|shared-language|code-structure|validation-instrumentation|dependency-tooling|performance-sensitive|ui-product' skills README.md .loom/tickets/20260507-actvskill-broaden-skill-activation.md .loom/research/20260507-external-skill-activation-deep-dive.md`
- `rg -n '# Coverage|# Critique Disposition|# Retrospective / Promotion Disposition|# Acceptance Criteria' skills`
- `rg -n '<TBD|PLACEHOLDER|TODO' .loom/research/20260507-external-skill-activation-deep-dive.md .loom/tickets/20260507-actvskill-broaden-skill-activation.md`
- `git diff --unified=0 -- README.md skills .loom/research/20260507-external-skill-activation-deep-dive.md .loom/tickets/20260507-actvskill-broaden-skill-activation.md | rg '^\+.*(script|runtime|daemon|MCP|CLI|validator|schema|command wrapper|issue tracker)'`
- `git diff --stat -- README.md skills .loom/research/20260507-external-skill-activation-deep-dive.md .loom/tickets/20260507-actvskill-broaden-skill-activation.md`

Expected result when applicable: no whitespace errors; all core `SKILL.md`
frontmatter descriptions include `Use when`, `Use for`, `Use first`, or `Use
after`; new references and change classes are discoverable; stale ticket section
names do not return; active new records have no unresolved placeholders; runtime
drift scan shows no new hidden runtime requirement.

Actual observed result: checks matched expectations with limitations noted below.

Procedure verdict / exit code: mixed pass. `git diff --check`, stale-heading
scan, and active-record placeholder scan produced no output. Description and new
reference scans returned the expected matches. The runtime-drift scan returned
lexical false positives but no added requirement for a hidden runtime, daemon,
MCP, validator, command wrapper, or issue tracker.

# Artifacts

`git diff --check` output:

```text
<no output>
```

Stale ticket-heading scan output:

```text
<no output>
```

Active new record placeholder scan output:

```text
<no output>
```

Activation-description scan found all 22 top-level `skills/*/SKILL.md`
frontmatter descriptions with broad `Use ...` trigger language.

New routing/classification scan found:

- `skills/loom-workspace/references/task-routing-catalog.md`
- `skills/loom-tickets/references/local-execution.md`
- `skills/loom-wiki/references/shared-language.md`
- `skills/loom-records/references/change-class.md` entries for `code-structure`, `validation-instrumentation`, `dependency-tooling`, `performance-sensitive`, and `ui-product`
- references from `README.md`, workspace/ticket/wiki read orders, routing vocabulary, and the active ticket/research records

Runtime-drift scan interpretation:

- Matches included ordinary words such as `runtime`, `CLI`, `schema`, `script`,
  and `MCP` inside descriptions, negative boundaries, debugging examples, or
  dependency/tooling categories.
- No added line made a script, CLI, daemon, MCP, validator, schema, command
  wrapper, issue tracker, or hidden runtime the source of Loom behavior.

Scoped diff stat:

```text
55 files changed, 1354 insertions(+), 823 deletions(-)
```

# Visual / Product Evidence

N/A. This pass changed Markdown protocol and activation surfaces rather than a rendered UI.

# Supports Claims

- ticket:actvskill#ACC-001 - support. All core skill descriptions now include ordinary trigger language while preserving owner boundaries.
- ticket:actvskill#ACC-002 - support. `task-routing-catalog.md` covers the named common coding task families and is linked from workspace routing/read order.
- ticket:actvskill#ACC-003 - support. `local-execution.md` defines the ticket-local loop and is linked from ticket read order and readiness/routing guidance.
- ticket:actvskill#ACC-004 - support. `change-class.md` includes first-class common coding classes and evidence/critique defaults; evidence and critique references were updated.
- ticket:actvskill#ACC-005 - support. Skill-authoring principles, review guidance, and templates now require activation-rich descriptions with broad triggers and aliases.
- ticket:actvskill#ACC-006 - partial support. Structural validation passed; mandatory critique still needs to be recorded.

# Challenges Claims

None from these structural checks.

# Environment

Commit: not re-read during this observation; workspace is the dirty current `main` checkout.

Branch: `main`

Runtime: ordinary Git and ripgrep-based structural queries through the active harness.

OS: macOS / Darwin

Relevant config: no automated project test suite; structural/manual verification per `AGENTS.md`.

External service / harness / data source when applicable: none for validation commands.

# Validity

Valid for: current dirty workspace state after the activation/routing edits and before mandatory critique.

Fresh enough for: structural claims about descriptions, routing references,
change-class visibility, stale heading absence, active record placeholders, and
absence of newly required hidden runtime in added lines.

Recheck when: any `skills/`, `README.md`, or linked `ticket:actvskill` records
change materially.

Invalidated by: later edits, critique findings requiring changes, or package framing changes.

Supersedes / superseded by: none.

# Limitations

- Structural scans do not prove future harness autoactivation quality.
- Runtime-drift scan is lexical and may miss conceptual drift.
- Mandatory critique had not yet been recorded at observation time.
- No package/install distribution check was run.

# Result

The activation/routing edits are structurally coherent enough for mandatory
critique. Evidence supports the ticket's implementation claims except for the
critique gate.

Supplemental observation at 2026-05-07T07:52:52Z after critique-requested fixes:

- `git diff --check` produced no output.
- `rg -n 'local_edit|local-edit-ready|ticket-local fix|local edit' skills` produced no output.
- `rg -n 'code-structure.*code-structure|dependency-tooling.*dependency-tooling' skills/loom-records/references/change-class.md` confirmed default critique guidance now routes `code-structure` to the `code-structure` profile and `dependency-tooling` to the `dependency-tooling` profile.

# Interpretation

The changes improve Loom's activation discoverability without adding new owner
layers or hidden runtime dependencies. They preserve Loom's paper-process premise
by routing ordinary coding prompts into existing owner layers and ticket-owned
execution truth.

# Related Records

- `ticket:actvskill`
- `research:external-skill-activation-deep-dive`
