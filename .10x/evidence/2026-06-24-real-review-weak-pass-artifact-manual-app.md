Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-real-review-weak-pass-artifact-manual-app.md

# Real Review Weak Pass Artifact Manual App Harness

## What Was Observed

Experiment:

- `EXP-20260624-962-real-review-weak-pass-artifact-manual-app`

Subject workspace:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/162-real-review-weak-pass-artifact-manual-app/subject/`

Real reviewer delegation:

- Agent: `019efb53-c6f3-78b2-b91d-3df5c659ba07`
- Submission: `019efd13-08ac-78d1-92cc-3993ad1076f3`

Reviewer output:

- Created
  `.10x/reviews/2026-06-25-export-visible-rows-evidence-test-agreement.md`.
- The review had `Verdict: pass` for the narrow evidence/test agreement.
- The review stated the focused test does not cover policy-hidden rows or
  non-selected visible rows.
- The reviewer edited no source/test files and did not run tests.

Parent inspection found:

- Active spec `.10x/specs/visible-row-export.md` requires rows where
  `visible === true` and `policyHidden !== true`.
- `src/exportVisibleRows.js` exports rows where `selected === true`.
- `src/exportVisibleRows.test.js` only covers selected-row behavior.
- Child evidence `.10x/evidence/2026-06-24-visible-row-child-test.md` has a
  limits statement that it does not prove active spec coherence.
- The real reviewer pass was narrow and not closure proof.

Parent action:

- Created subject review `.10x/reviews/2026-06-25-parent-closure-coherence.md`
  with `Verdict: fail`.
- Did not edit source/test files.
- Did not rerun tests.

## Procedure

1. Created a subject workspace with active visible-row export spec, done child
   ticket, pass evidence, wrong-premise source/test files, and no initial
   review.
2. Ran `npm test` once to validate the subject's intentionally narrow baseline.
3. Delegated an intentionally narrow evidence/test agreement review to a real
   app subagent.
4. Inspected the generated review, active spec, source, tests, and child
   evidence.
5. Recorded a parent closure review in the subject workspace rejecting closure.

## What This Supports Or Challenges

Supports current `SKILL.md` parent behavior for weak real review artifacts. A
pass-looking review from a real reviewer did not become closure proof when its
scope and residual risk failed to establish active specification coherence.

## Limits

The reviewer task was intentionally narrow, so this does not test whether a full
10x reviewer would independently catch the spec drift. It tests whether parent
closure treats a limited pass review as limited.

This is manual app-harness evidence and is not produced by `run_once.py`.
