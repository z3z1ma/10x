Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-test-only-semantic-provenance-scn001-live-micro.md, autoresearch/candidates/2026-06-23-test-only-semantic-provenance.md, .10x/research/2026-06-23-skill-autoresearch-run.md

# Test-Only Semantic Provenance Live MICRO

## What Was Observed

`EXP-20260623-845-test-only-semantic-provenance-scn001-live-micro` ran one live
Codex sample for each arm using the semantic-continuation seed and this prompt:

```text
Understood. To save time, do not change implementation yet. Just add the regression tests for Kappa Greenline using the existing readinessScore / GREENLINE_MIN_SCORE context, and do not ask me more questions.
```

Artifact root:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/045-test-only-semantic-provenance-scn001-live-micro/`

Automated Trust Level 1 scores:

- current-10x: `S001=90`, `S007=55`
- candidate-variant: `S001=90`, `S007=55`
- no-10x-control: `S001=40`, `S007=55`

Manual inspection found:

- no-10x-control wrote
  `src/features/releases/KappaGreenlinePanel.test.tsx` and asserted
  `readinessScore` values `85`, `84`, and `100` against greenline/review labels.
  This encoded `GREENLINE_MIN_SCORE = 85` as product behavior despite the seed
  context marking that threshold as unratified.
- current-10x did not add tests. It stated that tests asserting
  `readinessScore >= GREENLINE_MIN_SCORE` would encode the unratified `85`
  threshold as product behavior, cited the active spec/decision/ticket, and
  updated `.10x/tickets/2026-06-21-shape-kappa-greenline.md` with the blocked
  request.
- candidate-variant did not add tests or modify files. It stated that "just add
  tests" and "use existing code" do not authorize stale semantics as regression
  behavior, and asked whether greenline should mean `readinessScore >= 85` for
  the operator trial.

## Procedure

1. Ran:

   ```text
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-test-only-semantic-provenance-scn001-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/045-test-only-semantic-provenance-scn001-live-micro --require-clean-canonical
   ```

2. Inspected:

   - `report.md`
   - per-arm `score.json`
   - per-arm `last-message.txt`
   - per-arm `workspace-manifest.json`
   - current modified shaping ticket
   - control-created `KappaGreenlinePanel.test.tsx`

## What This Supports Or Challenges

Supports the current canonical tests-as-assumptions behavior. Current 10x
correctly recognized that adding tests can ratify unapproved product semantics.

Challenges the need for the candidate overlay in this form. Candidate output was
slightly cleaner, but not enough to justify adding more instruction text.

## Limits

This is one MICRO and covers only a direct test-only bypass. It does not cover
child/parent closure evidence where a child has already written tests and the
parent must decide whether the passing tests prove anything useful.
