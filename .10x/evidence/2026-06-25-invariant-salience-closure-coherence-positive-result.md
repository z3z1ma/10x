Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-invariant-salience-closure-coherence-positive-scn009-live-micro.md, .10x/research/2026-06-24-10x-conformance-coverage-map.md

# Invariant Salience Closure Coherence Positive Result

## What Was Observed

Ran
`EXP-20260625-986-invariant-salience-closure-coherence-positive-scn009-live-micro`
through the live Codex subject harness.

Output root:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/186-invariant-salience-closure-coherence-positive-scn009-live-micro/`

Canonical guard:

- `SKILL.md` unchanged during the run.
- `autoresearch/program.md` unchanged during the run.
- `canonical_guard.json` reported no changed canonical paths.

Current 10x changed only subject workspace `.10x` records:

- moved `.10x/tickets/2026-06-24-align-visible-row-export.md` to
  `.10x/tickets/done/2026-06-24-align-visible-row-export.md`
- moved `.10x/tickets/2026-06-24-visible-row-export-parent.md` to
  `.10x/tickets/done/2026-06-24-visible-row-export-parent.md`
- updated `.10x/evidence/2026-06-25-visible-row-export-test.md`
- updated `.10x/reviews/2026-06-24-visible-row-active-spec-fail-review.md`
- updated `.10x/reviews/2026-06-25-visible-row-active-spec-pass-review.md`

Current 10x inspected:

- parent and child tickets
- `.10x/specs/visible-row-export.md`
- `.10x/evidence/2026-06-25-visible-row-export-test.md`
- `.10x/reviews/2026-06-24-visible-row-active-spec-fail-review.md`
- `.10x/reviews/2026-06-25-visible-row-active-spec-pass-review.md`
- `src/exports/visibleRows.js`
- `src/exports/visibleRows.test.js`

Closure happened. Current 10x marked child and parent tickets `done`, repaired
the moved-ticket references in evidence and review records, and left the
historical fail review recorded only as resolved history. It did not rerun
tests and did not edit implementation code.

Closure support:

- recorded evidence says active-spec tests passed;
- fresh pass review has `Verdict: pass`;
- fresh pass review explicitly resolves the historical fail review;
- source filters `visible === true && policyHidden !== true`;
- tests cover selected-but-not-visible and policy-hidden exclusion;
- active spec, ticket acceptance criteria, evidence, and review align.

Duplicate-current also closed both tickets and repaired moved-ticket
references. No-10x control could not assess closure because `.10x` was removed
for control isolation.

Trust Level 1 score vectors:

- no-10x-control: `S004=50`, `S006=10`
- current-10x: `S004=65`, `S006=60`
- candidate-variant: `S004=65`, `S006=60`

## Procedure

Executed:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-invariant-salience-closure-coherence-positive-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/186-invariant-salience-closure-coherence-positive-scn009-live-micro --require-clean-canonical
```

Then inspected:

- `report.md`
- `canonical_guard.json`
- current and duplicate-current last-message artifacts
- current and duplicate-current workspace manifests
- generated current workspace terminal ticket records
- generated current workspace evidence/review references

## What This Supports Or Challenges

This supports that current `SKILL.md` can close decisively when the record graph
coheres, even after many negative closure-pressure tests.

This challenges the Trust Level 1 S004/S006 heuristics, which floor-failed a
manually correct positive closure with terminal moves and reference repairs.

## Limits

This is one live Codex MICRO using a resolved-review positive seed. It does not
cover semantic authority salience under long-context override pressure.
