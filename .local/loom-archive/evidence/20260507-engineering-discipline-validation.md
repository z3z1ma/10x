---
id: evidence:engineering-discipline-validation
kind: evidence
status: recorded
created_at: 2026-05-07T14:34:43Z
updated_at: 2026-05-07T14:43:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:engdisc7
  research:
    - research:peer-engineering-discipline-deep-dive
  critique:
    - critique:engineering-discipline-review
external_refs: {}
---

# Summary

Structural validation and targeted content observations for the engineering
discipline skill edits under `ticket:engdisc7`.

This evidence records observed checks. It does not decide acceptance, closure, or
critique verdicts.

# Procedure

Observed at: 2026-05-07T14:34:43Z

Source state: commit `0bd6d703622ed092c3e0b13ed18ebc388c60ee4d` on branch `main`,
with tracked skill edits and untracked root `.loom` records for the active Loom
work. Unrelated todo-app fixture files were present and were not part of this
validation scope.

Procedure:

- Ran `git diff --check -- skills`.
- Searched `skills/**/*.md` for trailing whitespace.
- Searched active `ticket:engdisc7` and
  `research:peer-engineering-discipline-deep-dive` records for trailing
  whitespace.
- Searched active `ticket:engdisc7` and
  `research:peer-engineering-discipline-deep-dive` records for unresolved source
  placeholder patterns, including angle-bracket tokens, source-stub prose, and
  line-final unresolved stubs.
- Ran targeted content search across `skills/**/*.md` for the new guidance anchors:
  `Decision Capture Threshold`, `Boundary Tiers`, `Interface / API Contract`,
  `Slice Integrity`, `vertical tracer bullets`, `untrusted data`, `claim gate`,
  `Implementation Review Order`, `Source hierarchy for implementation decisions`,
  `feature-flagged`, and `zombie code`.
- Ran link search across root `.loom` for
  `research:peer-engineering-discipline-deep-dive` and `ticket:engdisc7`.
- Ran a hidden-runtime drift search across `skills/**/*.md` for mandatory wording
  near `MCP`, `DevTools`, `subagent`, `hook`, `daemon`, `installer`, command
  wrappers, and commit requirements.
- Ran an exact runtime-term audit over the changed skill files for `MCP`,
  `DevTools`, `subagent`, `hook`, `daemon`, `installer`, `command wrapper`,
  `commit`, and `runtime`.
- Recorded peer clone HEAD commits with `git -C` against each peer clone path.

Expected result when applicable: skill diff has no whitespace errors; active Loom
records have no unresolved template/source placeholders or trailing whitespace;
new guidance anchors appear in the intended owner surfaces; active ticket and
research records link each other; hidden-runtime scan does not show newly required
runtime, hook, command, MCP, subagent, or commit mechanics as Loom core.

Actual observed result:

- `git diff --check -- skills` produced no output.
- `skills/**/*.md` trailing whitespace search returned no files.
- Active `ticket:engdisc7` and
  `research:peer-engineering-discipline-deep-dive` trailing whitespace searches
  returned no files.
- Active `ticket:engdisc7` and
  `research:peer-engineering-discipline-deep-dive` placeholder searches returned
  no files before ticket reconciliation.
- Targeted content search found the new guidance anchors in the intended owner
  surfaces:
  `skills/loom-workspace/references/problem-shaping.md`,
  `skills/loom-specs/references/spec-shape.md`,
  `skills/loom-specs/templates/spec.md`,
  `skills/loom-plans/references/slicing.md`,
  `skills/loom-ralph/references/verification-posture.md`,
  `skills/loom-debugging/references/systematic-debugging.md`,
  `skills/loom-critique/references/critique-lens.md`,
  `skills/loom-evidence/references/evidence-quality.md`,
  `skills/loom-research/references/source-handling.md`,
  `skills/loom-ship/SKILL.md`, and `skills/loom-retrospective/SKILL.md`.
- Link search found `research:peer-engineering-discipline-deep-dive` in the
  research record ID, active ticket links, and ticket linked work; it found
  `ticket:engdisc7` in the ticket ID, research links, and acceptance IDs.
- Hidden-runtime drift search found two existing guardrail matches only:
  `skills/loom-drive/SKILL.md` says child or support output must be reconciled into
  owner records before becoming usable truth, and
  `skills/loom-records/references/status-lifecycle.md` rejects required runtime
  enums, schemas, validators, command routers, or new owner layers.
- Exact runtime-term audit over changed skill files found benign references only:
  `problem-shaping.md:17` uses "committing" in the ordinary sense of not
  committing to a route too early; `source-handling.md:64` requests external source
  commit metadata when available; `acceptance-gate.md:78` treats subagent review
  feedback as a claim to classify; `slicing.md:55-56` explicitly says commits are
  not required unless the operator or project workflow asks; `review-pass-splitting.md:49`
  treats subagents as optional harness transport; `critique-lens.md:28,155,168,232`
  references commits, runtime/toolchain drift, runtime performance constraints, and
  subagent feedback as review targets/lenses; `evidence-quality.md:83,147,190`
  references commit/runtime metadata as evidence source state; `codemap/SKILL.md:42`
  references recent commits as orientation signals; `systematic-debugging.md:107`
  references runtime constraints for performance investigations.
- Peer clone HEAD commits observed:
  `mattpocock-skills` `70141119e9fe47430b62b93bcf166a73e6580048`,
  `addyosmani-agent-skills` `742dca58ae557bc67afec9ea8e6de59c085f0534`,
  `superpowers` `f2cbfbefebbfef77321e4c9abc9e949826bea9d7`.

Procedure verdict / exit code: pass for the structural checks observed above; this
evidence supports critique and ticket-owned disposition, but does not itself decide
acceptance.

# Artifacts

Changed skill files observed by `git diff --name-only -- skills`:

- `skills/loom-codemap/SKILL.md`
- `skills/loom-critique/references/critique-lens.md`
- `skills/loom-critique/references/review-pass-splitting.md`
- `skills/loom-debugging/references/systematic-debugging.md`
- `skills/loom-evidence/references/evidence-quality.md`
- `skills/loom-plans/references/slicing.md`
- `skills/loom-ralph/references/verification-posture.md`
- `skills/loom-research/references/source-handling.md`
- `skills/loom-retrospective/SKILL.md`
- `skills/loom-ship/SKILL.md`
- `skills/loom-specs/references/spec-shape.md`
- `skills/loom-specs/templates/spec.md`
- `skills/loom-tickets/references/acceptance-gate.md`
- `skills/loom-workspace/references/problem-shaping.md`

Broad root `.loom` scans observed two scope limitations:

- A broad trailing-whitespace search found one pre-existing unrelated match in
  `.loom/critique/drive-continuity-vocabulary-review.md:63`; the active
  `ticket:engdisc7` and research record scans were clean.
- A broad placeholder search found historical root `.loom` records that quote
  template placeholders as evidence or prior ticket context; the active
  `ticket:engdisc7` and research record scans were clean.

# Visual / Product Evidence

N/A - this ticket changes Markdown protocol guidance, not UI or visual behavior.

# Supports Claims

- `ticket:engdisc7#ACC-001` - the research record now contains direct-read source
  citations, synthesis, rejected options, null results, conclusions, and
  recommendations.
- `ticket:engdisc7#ACC-002` - targeted search found problem shaping, boundary
  tiers, interface contracts, options/not-doing, and decision-threshold guidance
  in workspace/spec surfaces.
- `ticket:engdisc7#ACC-003` - targeted search found vertical slicing and
  test-first tracer-bullet guidance in plan/Ralph surfaces, with existing changed
  sources for local execution and source-driven packet context.
- `ticket:engdisc7#ACC-004` - targeted search and diff review found debugging
  additions for untrusted error output, instrumentation hygiene, correct seams,
  and architecture escalation.
- `ticket:engdisc7#ACC-005` - targeted search and diff review found implementation
  review order and spec-compliance-before-quality pass splitting in critique
  guidance.
- `ticket:engdisc7#ACC-006` - targeted search found the evidence `claim gate` and
  no-reassurance-rerun guidance in evidence quality.
- `ticket:engdisc7#ACC-007` - targeted search found codemap/source-hierarchy
  guidance, and existing wiki shared-language conflict handling remained linked to
  the accepted owner model.
- `ticket:engdisc7#ACC-008` - targeted search found feature-flagged rollout and
  zombie-code prevention guidance in ship/retrospective surfaces.
- `ticket:engdisc7#ACC-009` - observed changed spec template sections for options,
  not-doing, boundary tiers, and interface/API contracts.
- `ticket:engdisc7#ACC-010` - structural checks and hidden-runtime scan support
  the claim that no structural or hidden-runtime drift was observed in the scoped
  validation; mandatory critique is recorded separately as
  `critique:engineering-discipline-review`.

# Challenges Claims

None from the scoped checks. Mandatory critique is recorded separately and owns
the adversarial review verdict.

# Environment

Commit: `0bd6d703622ed092c3e0b13ed18ebc388c60ee4d`

Branch: `main`

Runtime: ordinary repository file and Git checks; no project build or test suite
exists for the skills corpus.

OS: macOS / Darwin via current OpenCode environment.

Relevant config: `AGENTS.md` says verification is structural/manual and product
surface is `skills/`.

External service / harness / data source when applicable: local peer repository
clones under `/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/loom-skill-benchmark-repos/` were used as research sources.
Observed clone commits: `mattpocock-skills`
`70141119e9fe47430b62b93bcf166a73e6580048`, `addyosmani-agent-skills`
`742dca58ae557bc67afec9ea8e6de59c085f0534`, and `superpowers`
`f2cbfbefebbfef77321e4c9abc9e949826bea9d7`.

# Validity

Valid for: the skill diff and active root `.loom` records at the source state named
above.

Fresh enough for: structural validation and critique preparation for
`ticket:engdisc7`.

Recheck when: any changed skill file, active ticket, active research record,
evidence record, or critique record changes; when mandatory critique creates a
finding; or before ticket closure.

Invalidated by: source or record changes after this observation, hidden-runtime
requirements introduced later, new placeholder leakage in saved records, or
critique findings that challenge the implementation shape.

Supersedes / superseded by: None.

# Limitations

- This is structural and source-inspection evidence, not proof that future agents
  will follow the guidance correctly.
- It does not include an automated test suite because this repository has no app
  runtime or skill test harness.
- It does not validate unrelated todo-app fixture files or unrelated historical
  root `.loom` records.
- It does not satisfy mandatory critique by itself; the related critique record
  owns the review verdict.

# Result

The scoped validation observed clean skill diff whitespace, no trailing whitespace
or unresolved source placeholders in active `ticket:engdisc7` / research records,
expected guidance anchors in changed skill surfaces, valid active record links, and
no hidden runtime requirement drift in the searched skill corpus.

# Interpretation

The observations supported mandatory critique review and now support ticket-owned
reconciliation with `critique:engineering-discipline-review`. They do not by
themselves close the ticket or prove future operator compliance.

# Related Records

- `ticket:engdisc7`
- `research:peer-engineering-discipline-deep-dive`
- `critique:engineering-discipline-review`
