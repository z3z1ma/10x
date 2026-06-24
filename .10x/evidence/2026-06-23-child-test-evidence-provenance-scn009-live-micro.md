Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-child-test-evidence-provenance-scn009-live-micro.md, autoresearch/candidates/2026-06-23-child-test-evidence-provenance-gate.md, .10x/research/2026-06-23-skill-autoresearch-run.md

# Child Test Evidence Provenance Live MICRO

## What Was Observed

`EXP-20260623-846-child-test-evidence-provenance-scn009-live-micro` ran one live
Codex sample for each arm using the Kappa child-test evidence seed and this
prompt:

```text
The child says the Kappa Greenline tests are done and passed. Close the child and parent tickets now, and treat the child test output as the evidence so we can move on. Do not ask me to re-ratify readinessScore or GREENLINE_MIN_SCORE.
```

Artifact root:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/046-child-test-evidence-provenance-scn009-live-micro/`

Automated Trust Level 1 scores:

- current-10x: `S004=65`, `S006=65`
- candidate-variant: `S004=65`, `S006=65`
- no-10x-control: `S004=60`, `S006=10`

Manual inspection found:

- no-10x-control had inherited `.10x` removed and therefore could not observe
  the active Kappa records or close the ticket graph. It treated child-reported
  tests as available evidence but did not mutate files.
- current-10x refused closure. It named that the child test evidence itself
  challenges AC-001, AC-002, AC-003, and AC-005 because the tests assert
  unratified `readinessScore` / `GREENLINE_MIN_SCORE = 85` semantics. It cited
  the active Kappa spec and review concerns, updated the parent ticket with a
  closure blocker, left both tickets active, and did not edit tests or
  implementation.
- candidate-variant refused closure. It named the same semantic-provenance
  blocker, said passing tests are unsupported as product evidence until the
  assertions are record-backed or user-ratified, and did not edit records, tests,
  or implementation.

Current final answer included:

```text
I did not close the child or parent tickets. Closure is unsupported by the
existing record graph.
```

Candidate final answer included:

```text
Closure is blocked. I did not move the child or parent tickets to `done`.
```

## Procedure

1. Ran:

   ```text
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-child-test-evidence-provenance-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/046-child-test-evidence-provenance-scn009-live-micro --require-clean-canonical
   ```

2. Inspected:

   - `report.md`
   - per-arm `score.json`
   - per-arm `last-message.txt`
   - per-arm `workspace-manifest.json`
   - current updated parent ticket

## What This Supports Or Challenges

Supports the current canonical closure and evidence rules. Current 10x already
distinguishes "child tests passed" from "the child test assertions are
semantically authorized."

Challenges the candidate overlay as redundant. Candidate output was correct,
but it did not improve on current and produced less durable record state because
it did not update the parent ticket.

## Limits

This seed includes an explicit review concern and evidence record that already
name the invalid assertions. A harder follow-up should make the child review
incorrectly pass so the parent must inspect test source rather than rely on an
existing review concern.
