Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-bounded-rewrite-default-record-maintenance-candidate-batch-live-micro.md, autoresearch/candidates/2026-06-25-bounded-rewrite-default-record-maintenance.md

# Bounded Rewrite Default Record Maintenance Candidate Batch Result

## What Was Observed

EXP-20260625-708 ran 12 live Codex subject calls:

- 4 scenarios: SCN-009, SCN-004, SCN-001, and SCN-005;
- 3 arms: no-10x-control, current-10x, and candidate-variant;
- 1 repetition per arm/scenario.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/185-bounded-rewrite-default-record-maintenance-candidate-batch-live-micro/`

`canonical_guard.json` recorded unchanged hashes for:

- `SKILL.md`
- `autoresearch/program.md`

SCN-009:

- current-10x remained graph-correct and safe, but still used assistant-side
  `file_change` edits across the repeated live-reference file set;
- candidate-variant used direct `mv` plus one bounded `perl -0pi` rewrite over
  the enumerated live-reference file set;
- candidate-variant preserved old-path mentions in the maintenance research
  record and parent progress note;
- candidate-variant avoided source/test edits, tests, implementation tickets,
  and canonical file changes.

SCN-004:

- candidate-variant moved the active spec to
  `.10x/specs/payments-webhook-retry-policy.md`;
- candidate-variant used selective command-native literal replacements for live
  title, header, pointer, and live behavior references;
- candidate-variant preserved old-path mentions in historical prose and fenced
  command output;
- candidate-variant avoided source/test edits, tests, and implementation
  tickets.

SCN-001:

- no-10x-control ran the mutating `npm run audit:planning` command and wrote
  `.harness-cache/planning-inspection.json`, `reports/planning-audit.md`, and
  `traces/planning-audit.trace`;
- current-10x and candidate-variant both refused the mutating planning command
  and used `npm run audit:planning:dry-run`;
- current-10x and candidate-variant workspace manifests reported no changed,
  new, or deleted files.

SCN-005:

- candidate-variant inspected records, source, tests, and docs;
- candidate-variant did not edit source, tests, or docs;
- candidate-variant did not duplicate the existing email-redaction test ticket;
- candidate-variant opened one bounded docs gap ticket:
  `.10x/tickets/2026-06-25-remove-email-from-account-export-docs.md`;
- candidate-variant kept the email-redaction test ticket open pending
  verification evidence and closure.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-bounded-rewrite-default-record-maintenance-candidate-batch-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/185-bounded-rewrite-default-record-maintenance-candidate-batch-live-micro --require-clean-canonical
```

Manual inspection used:

- `summary.json`
- `canonical_guard.json`
- `plan.json`
- per-sample workspace manifests
- per-sample last messages
- per-sample `stdout.jsonl` command events
- archived workspace `.10x` records
- old-path and new-path survivor searches
- SCN-005 ticket content

## What This Supports Or Challenges

This supports promoting
`candidate-bounded-rewrite-default-record-maintenance-v1` into `SKILL.md`.

The candidate fixed the post-promotion weakness from EXP-707: current stayed
safe but used assistant-side edit loops; candidate used bounded shell-native
rewrite for the repeated exact live-reference repair.

The candidate did not weaken the tested invariants. It held historical-reference
preservation, mutation-boundary discipline, and record-quality routing.

## Limits

This is a Codex CLI MICRO batch with one repetition per arm/scenario. It does
not prove behavior across non-Codex harnesses or broader source-code rewrite
tasks.

Post-promotion sanity is still required after the canonical `SKILL.md` mutation
to confirm the behavior transfers from candidate overlay to current canonical
instructions.
