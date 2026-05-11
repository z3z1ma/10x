---
id: evidence:peer-skill-practices-validation
kind: evidence
status: recorded
created_at: 2026-05-07T08:17:33Z
updated_at: 2026-05-07T08:20:29Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:peerpr07
  research:
    - research:external-peer-skill-practices-synthesis
external_refs: {}
---

# Summary

Structural validation for `ticket:peerpr07` after assimilating external peer skill
practices into existing Loom skill surfaces. This evidence records observed
checks; it does not decide acceptance, closure, or critique verdicts.

# Procedure

Observed at: 2026-05-07T08:17:33Z

Source state: branch `main`, commit `3388ca12fba859b4bab6096bdd508987414b2bb5`, with uncommitted changes under `skills/` and root `.loom/` records.

Procedure:

- Ran `git diff --check -- skills .loom` from the repository root.
- Ran `git rev-parse --abbrev-ref HEAD && git rev-parse HEAD` from the repository root.
- Searched root `ticket:peerpr07` and `research:external-peer-skill-practices-synthesis` records for `<TBD|TODO|FIXME`.
- Searched `skills/` for hidden-runtime drift language using `(required|mandatory|must|always)` near `runtime`, `script`, `helper`, `hook`, `plugin`, `mcp`, `command wrapper`, `validator`, or `daemon`.
- Searched `skills/` for current-tranche markers: `Problem Pressure Check`, `Pressure Check`, `Confidence Review`, `Evidence Before Claims`, `Claim Gate`, `pressure-scenario`, `Parent Reconciliation`, and `Child Output`.
- Searched `examples/` for `peerpr07` or `external-peer-skill-practices-synthesis`.
- Searched root `.loom/` for `id: ticket:peerpr07` and `id: research:external-peer-skill-practices-synthesis`.

Expected result when applicable:

- No whitespace errors in the changed `skills/` and root `.loom/` diff.
- Root peer-practice ticket and research records have no unresolved placeholder tokens.
- Hidden-runtime scan should not reveal new guidance that makes hooks, plugins,
  scripts, validators, command wrappers, MCPs, daemons, or other runtimes required
  Loom protocol surfaces.
- Current-tranche concepts should appear in the intended existing skill surfaces.
- Current peer-practice root records should not be duplicated under example fixtures.
- Root `.loom/` should contain exactly the peer-practice ticket and research IDs.

Actual observed result:

- `git diff --check -- skills .loom` returned no output.
- Branch and commit output was `main` and `3388ca12fba859b4bab6096bdd508987414b2bb5`.
- Placeholder scans on the root peer-practice ticket and research record returned `No files found`.
- Hidden-runtime drift scan returned five matches, all inspected as boundary-preserving or unrelated false positives:
  - `skills/loom-records/references/status-lifecycle.md` says not to turn vocabulary into a required runtime enum, schema, validator, command router, or new owner layer.
  - `skills/loom-bootstrap/references/06-filesystem-and-tooling.md` says query recipes are discovery aids, not mandatory runtime dependencies.
  - `skills/loom-records/references/query-and-linking.md` says recipes are not a mandatory runtime, generated index, schema validator, or proof.
  - `skills/loom-memory/SKILL.md` says validators must not require canonical record fields merely because memory exists.
  - `skills/loom-workspace/SKILL.md` includes a transcript-memory rationalization row unrelated to hidden runtime adoption.
- Marker scan returned expected current-tranche concepts in intended surfaces, including:
  - `skills/loom-workspace/references/problem-shaping.md`: `## Pressure Check`
  - `skills/loom-specs/references/spec-shape.md`: `Problem Pressure Check`
  - `skills/loom-specs/templates/spec.md`: `# Problem Pressure Check`
  - `skills/loom-plans/references/plan-shape.md`: `## Confidence Review`
  - `skills/loom-plans/templates/plan.md`: `# Confidence Review`
  - `skills/loom-evidence/references/evidence-quality.md`: `## Evidence Before Claims`
  - `skills/loom-tickets/references/local-execution.md`: `## Claim Gate`
  - `skills/loom-skill-authoring/SKILL.md` and `skills/loom-skill-authoring/references/skill-review.md`: pressure-scenario guidance
- Example-fixture search for `peerpr07` and `external-peer-skill-practices-synthesis` returned `No files found`.
- Root `.loom/` ID search returned exactly:
  - `.loom/research/20260507-external-peer-skill-practices-synthesis.md: id: research:external-peer-skill-practices-synthesis`
  - `.loom/tickets/20260507-peerpr07-assimilate-peer-skill-practices.md: id: ticket:peerpr07`

Procedure verdict / exit code: pass for structural checks; hidden-runtime scan pass after manual inspection of matches; critique still pending.

Follow-up revalidation at 2026-05-07T08:20:29Z after critique surfaced untracked-file whitespace and plan-template alignment concerns:

- `git diff --check -- skills .loom` again returned no output.
- Targeted trailing-whitespace scans for the untracked peer-practice evidence, ticket, research, and `skills/loom-tickets/references/local-execution.md` returned `No files found`.
- `skills/loom-plans/templates/plan.md` contains `# Milestones` at line 30 after the plan-template alignment fix.

# Artifacts

Observed command and search outputs are summarized in `# Procedure`.

Relevant root records inspected:

- `.loom/tickets/20260507-peerpr07-assimilate-peer-skill-practices.md`
- `.loom/research/20260507-external-peer-skill-practices-synthesis.md`

Relevant changed skill surfaces checked by marker scan:

- `skills/loom-workspace/references/problem-shaping.md`
- `skills/loom-drive/SKILL.md`
- `skills/loom-drive/references/drive-loop.md`
- `skills/loom-specs/SKILL.md`
- `skills/loom-specs/references/spec-shape.md`
- `skills/loom-specs/templates/spec.md`
- `skills/loom-plans/SKILL.md`
- `skills/loom-plans/references/plan-shape.md`
- `skills/loom-plans/references/slicing.md`
- `skills/loom-plans/templates/plan.md`
- `skills/loom-records/references/validation.md`
- `skills/loom-evidence/references/evidence-quality.md`
- `skills/loom-tickets/references/local-execution.md`
- `skills/loom-ralph/references/packet-contract.md`
- `skills/loom-skill-authoring/references/principles.md`
- `skills/loom-skill-authoring/references/skill-review.md`
- `skills/loom-skill-authoring/references/anti-patterns.md`

# Visual / Product Evidence

N/A - protocol Markdown guidance and record-structure validation, not UI/product visual work.

# Supports Claims

- `ticket:peerpr07#ACC-001`: Supports the structural portion: root research exists, has the expected ID, has no unresolved placeholder tokens, and records direct-read synthesis with rejected command/plugin/runtime adoption.
- `ticket:peerpr07#ACC-002`: Supports the structural portion: pressure-check guidance appears in `loom-workspace`, `loom-drive`, and `loom-specs` surfaces.
- `ticket:peerpr07#ACC-003`: Supports the structural portion: evidence-before-claim and validation claim-gate guidance appears in `loom-evidence`, `loom-records`, and local execution guidance.
- `ticket:peerpr07#ACC-004`: Supports the structural portion: plan, ticket/local execution, and Ralph surfaces contain slice specificity, write-scope, and parent reconciliation guidance.
- `ticket:peerpr07#ACC-005`: Supports the structural portion: skill-authoring surfaces include pressure-scenario and prose-confidence-only validation guidance.
- `ticket:peerpr07#ACC-006`: Supports the structural-validation and hidden-runtime-scan portions only; mandatory critique remains a separate required input.

# Challenges Claims

None observed. This evidence does not test whether critique will find wording or boundary issues.

# Environment

Commit: `3388ca12fba859b4bab6096bdd508987414b2bb5`

Branch: `main`

Runtime: Markdown/filesystem validation with git, file reads, and content search tools.

OS: darwin

Relevant config: repository root `/Users/alexanderbutler/code_projects/personal/agent-loom`

External service / harness / data source when applicable: local filesystem only.

# Validity

Valid for: current structural state of the listed root `.loom` records and `skills/` guidance at the observed source state.

Fresh enough for: critique review and ticket evidence disposition for structural acceptance support on `ticket:peerpr07`.

Recheck when: any listed skill file, root peer-practice record, validation procedure, or acceptance criterion changes.

Invalidated by: new edits that add hidden runtime requirements, move peer-practice records under examples, introduce unresolved placeholders in saved root records, or alter the validated skill surfaces without rechecking.

Supersedes / superseded by: None.

# Limitations

- This evidence is structural and manual-inspection based; it does not prove the prose is optimal or that future agents will always follow it.
- This evidence does not satisfy the mandatory critique requirement by itself.
- The working tree contains earlier intended changes from prior closed tickets, so diff-stat breadth is not proof that every modified file belongs to `ticket:peerpr07`.
- Template files intentionally contain `<TBD>` placeholders; this evidence only scanned the saved root peer-practice ticket and research records for placeholders.

# Result

Fresh structural validation found no whitespace errors, no unresolved placeholders in the root peer-practice ticket or research record, no peer-practice record duplication under examples, and no inspected hidden-runtime scan match that makes a runtime, command, plugin, hook, script, validator, MCP, or daemon a required Loom protocol surface.

# Interpretation

The observations support moving `ticket:peerpr07` from evidence-pending toward critique review. They do not justify closure without the mandatory critique and ticket-owned acceptance decision.

# Related Records

- `ticket:peerpr07`
- `research:external-peer-skill-practices-synthesis`
