Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-deletion-before-accommodation-scn010-live-micro.md, autoresearch/candidates/2026-06-24-deletion-before-accommodation.md

# Deletion Before Accommodation Live MICRO

## What Was Observed

`EXP-20260624-883-deletion-before-accommodation-scn010-live-micro` ran one live
Codex subject sample for each arm against the deletion-before-accommodation
seed:

- `candidate-variant`
- `current-10x`
- `no-10x-control`

The canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

Automated Trust Level 1 scores tied all arms:

| Arm | Score vector |
| --- | --- |
| candidate-variant | `S005=85`, `S007=10` |
| current-10x | `S005=85`, `S007=10` |
| no-10x-control | `S005=85`, `S007=10` |

Manual inspection found:

- candidate-variant removed the `sendLegacyEmailBridge` import and invocation
  from `src/alerts/incidentDispatcher.js`, preserved the missing `id` or
  `severity` validation guard, added no dependencies, added no feature flag,
  added no deduplication store, added no adapter, ran `npm test`, wrote evidence
  and review records, and moved the ticket to `done`.
- current-10x made the same source change, preserved validation, added no
  accommodation complexity, ran `npm test`, wrote evidence and review records,
  and moved the ticket to `done`.
- no-10x-control also removed the legacy bridge call and passed tests, but its
  inherited `.10x/` graph was removed by the control harness, so it did not
  produce durable 10x records.

All three archived workspaces passed `npm test` when manually rerun after the
experiment.

## Procedure

1. Ran:

   ```sh
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-deletion-before-accommodation-scn010-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/083-deletion-before-accommodation-scn010-live-micro --require-clean-canonical
   ```

2. Read the generated report, summary, canonical guard, raw artifacts, last
   messages, workspace manifests, changed source files, and score artifacts.
3. Reran `npm test` in each archived workspace.
4. Compared candidate and current behavior against the manual inspection
   requirements in the research record.

## What This Supports Or Challenges

This challenges promotion of
`candidate-deletion-before-accommodation-v1`: current canonical `SKILL.md`
already chooses deletion before accommodation for this seeded duplicate-path
bug.

It supports the current skill's operational minimalism in this scenario: current
10x removed the retired bridge instead of adding coordination state, while still
preserving validation and closure evidence.

## Limits

This is one MICRO fixture with strong active records and tests. It does not
prove current 10x will choose deletion before accommodation when records are
weaker, when the obsolete path is harder to identify, or when the user more
strongly demands compatibility preservation.
