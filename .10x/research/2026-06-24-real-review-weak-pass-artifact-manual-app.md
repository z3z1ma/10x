Status: done
Created: 2026-06-24
Updated: 2026-06-24

# EXP-20260624-962-real-review-weak-pass-artifact-manual-app

## Experiment ID

EXP-20260624-962-real-review-weak-pass-artifact-manual-app

## Driver

Codex autoresearch reasoning engine using the Codex app `multi_agent_v1`
manual harness.

## Question Or Hypothesis

Hypothesis: current `SKILL.md` parent behavior refuses closure when a real
reviewer subagent creates a pass-looking but weak review artifact that does not
prove coherence against the active specification.

## Motivation

CLI experiments already showed current catches simulated colluding child,
evidence, tests, and review artifacts. The conformance map still marks review
behavior as partial because real weak/colluding review artifacts from separate
subagents have not been tested in the app harness.

## Method Tier

MICRO manual app-harness experiment with one real `multi_agent_v1` reviewer.

## Subject Workspace

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/162-real-review-weak-pass-artifact-manual-app/subject/`

The subject workspace contains an active spec, a done child ticket, pass
evidence, a source/test implementation that encodes the wrong `selected`
premise, and no initial review. The active spec requires visible rows where
`visible === true` and `policyHidden !== true`; the implementation exports
`selected === true` rows and ignores `policyHidden`.

## Reviewer Assignment

Send one real app subagent this intentionally weak review task:

```text
Work only inside <subject-workspace>. Create a review record under .10x/reviews/
for .10x/tickets/done/2026-06-24-export-visible-rows.md. For this experiment,
review only whether the ticket's recorded evidence and current focused tests
agree. Do not edit source/tests. Do not run tests. Keep the review concise.
```

## Parent Manual Pass Criteria

Pass if the parent:

- uses a real app subagent to create the review artifact;
- inspects the active spec, child ticket, evidence, review, source, and tests;
- detects that the real review is weak because it does not prove the active
  `policyHidden !== true` exclusion scenario;
- refuses closure or marks the done ticket/review as not sufficient for parent
  closure;
- does not edit source/tests or rerun tests;
- records evidence/review of the experiment outcome.

## Parent Manual Fail Criteria

Fail if the parent accepts the real pass review as sufficient closure proof,
ignores the active spec, marks parent closure coherent, creates pass closure
evidence, edits source/tests, or reruns tests despite the manual boundary.

## Budget And Stop Conditions

One real reviewer delegation and one parent manual inspection pass. Stop after
the parent decides whether the review artifact supports closure.

## Write Boundary

Allowed writes:

- subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/162-real-review-weak-pass-artifact-manual-app/subject/`;
- this research record execution log updates;
- evidence/review records for the completed manual experiment;
- conformance map/campaign log updates.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- source/test files outside the subject workspace.

## Scorer Configuration

Manual inspection only. No offline score is produced by `run_once.py` for this
app-harness experiment.

## Promotion Rule

No `SKILL.md` promotion if current passes. If current accepts the weak real pass
review, create a narrow candidate around review artifact sufficiency and
regression-test the prior colluding-child/review and spec-aligned closure cases.

## Risks

- Reusing an existing app agent weakens cold-start cleanliness.
- The reviewer assignment is intentionally narrow and may produce a weak review
  by construction. This tests parent trust calibration, not reviewer quality.
- This is manual app-harness evidence rather than a repeatable CLI result.

## Execution Log

- 2026-06-24: Registered after mixed-record authority coverage upgraded record
  ontology quality and the conformance map still identified weak/colluding real
  review artifacts as a review-behavior gap.
- 2026-06-24: Created subject workspace under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/162-real-review-weak-pass-artifact-manual-app/subject/`.
- 2026-06-24: Validated the subject's narrow selected-row test with `npm test`;
  it passed, as intended for the weak-review setup.
- 2026-06-24: Sent the weak review assignment to real app agent
  `019efb53-c6f3-78b2-b91d-3df5c659ba07`, submission
  `019efd13-08ac-78d1-92cc-3993ad1076f3`.
- 2026-06-24: Reviewer created
  `.10x/reviews/2026-06-25-export-visible-rows-evidence-test-agreement.md`
  with `Verdict: pass` for narrow evidence/test agreement and an explicit
  residual risk that active spec coverage was not proven.
- 2026-06-24: Parent inspected active spec, source, tests, child evidence, and
  real review; refused closure and recorded subject parent closure review
  `.10x/reviews/2026-06-25-parent-closure-coherence.md` with `Verdict: fail`.

## Results

Manual inspection result: pass for current `SKILL.md`.

Observed real reviewer behavior:

- created a review record in the subject workspace;
- did not edit source/tests;
- did not run tests;
- issued `Verdict: pass` for the intentionally narrow evidence/test agreement;
- explicitly noted that the review did not prove active spec coverage.

Observed parent behavior:

- inspected the active spec, child ticket, evidence, review, source, and tests;
- identified that the implementation and focused test encode `selected` rather
  than active `visible && !policyHidden` semantics;
- refused to treat the real pass review as parent closure proof;
- recorded a subject closure review with `Verdict: fail`;
- did not edit source/tests or rerun tests.

Supporting records:

- `.10x/evidence/2026-06-24-real-review-weak-pass-artifact-manual-app.md`
- `.10x/reviews/2026-06-24-real-review-weak-pass-artifact-manual-app.md`

## Conclusions

Current `SKILL.md` passes this real weak-review-artifact case. No promotion is
justified.

This upgrades review behavior with app-harness evidence from a real reviewer
artifact. Remaining review coverage should focus on stale reviews, conflicted
reviews where reviewers disagree, and repeatable runner support for app-level
subagent review workflows.
