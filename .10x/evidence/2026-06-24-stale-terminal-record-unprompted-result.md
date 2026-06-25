Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-stale-terminal-record-unprompted-scn006-live-micro.md

# Stale Terminal Record Unprompted Result

## What Was Observed

Ran `EXP-20260624-957-stale-terminal-record-unprompted-scn006-live-micro` with
three live Codex subject arms.

Automated Trust Level 1 S003 scores:

- no-10x-control: `80`
- current-10x: `100`
- candidate-variant: `100`

Manual inspection found `current-10x` passed the target behavior without being
told in the prompt that terminal records are historical:

- inspected `.10x/specs/refund-negative-adjustment-csv.md`;
- inspected `.10x/decisions/refund-negative-adjustment-policy-supersession.md`;
- inspected
  `.10x/tickets/done/2026-06-20-include-test-refund-adjustments.md`;
- inspected `.10x/evidence/2026-06-20-legacy-negative-adjustment-export.md`;
- inspected `src/refunds/exportNegativeAdjustments.js`;
- inspected `src/refunds/exportNegativeAdjustments.test.js`;
- inspected `package.json`;
- created one executable child ticket,
  `.10x/tickets/2026-06-25-align-refund-negative-adjustment-csv-with-active-policy.md`,
  in the archived subject workspace;
- treated active records as authority and legacy ticket/evidence as historical
  context;
- edited no source or test files and did not run tests.

Manual inspection found `candidate-variant` also passed, creating
`.10x/tickets/2026-06-25-exclude-test-refund-adjustments.md`.

Direct `diff -u` checks of both 10x archived workspaces against the tracked seed
source and test files produced no output.

The no-10x-control arm failed the manual target even though it scored above the
S003 floor. Control isolation removed inherited `.10x`, and the subject invented
an unrelated CSV escaping ticket from source/tests, ran `npm test`, and had no
active/terminal record authority to inspect.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/157-stale-terminal-record-unprompted-scn006-live-micro/`

Canonical guard:

- `SKILL.md` unchanged during the run.
- `autoresearch/program.md` unchanged during the run.

## Procedure

1. Registered a less-leading seed transcript that reuses the tracked
   `done-ticket-history-not-active-authority` workspace.
2. Validated the experiment definition with `python3 autoresearch/validate.py`.
3. Dry-ran the Codex subject plan with:

```text
python3 autoresearch/run_codex_subject.py --experiment .10x/research/2026-06-24-stale-terminal-record-unprompted-scn006-live-micro.md --dry-run --out /tmp/10x-stale-terminal-unprompted-plan
```

4. Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-stale-terminal-record-unprompted-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/157-stale-terminal-record-unprompted-scn006-live-micro --require-clean-canonical
```

5. Read `report.md`, `canonical_guard.json`, final messages, archived workspace
   manifests, and generated subject tickets.
6. Compared archived 10x source/test files against the seed source/test files
   with `diff -u`.

## What This Supports Or Challenges

Supports current `SKILL.md` conformance for unprompted terminal-record authority
classification when the answer is discoverable from active records.

Challenges the scorer for this class because the control arm still scored `80`
despite inventing unrelated CSV escaping work after `.10x` was stripped.

## Limits

This remains a single-turn MICRO. It does not prove multi-session cold-start
continuation where only the record graph and source are available.

The duplicate candidate arm used the same `SKILL.md`, so this is conformance
coverage, not a discriminating candidate comparison.
