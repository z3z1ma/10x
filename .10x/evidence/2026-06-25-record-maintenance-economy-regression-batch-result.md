Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro.md, autoresearch/candidates/2026-06-25-record-maintenance-command-line-economy.md

# Record Maintenance Economy Regression Batch Result

## What Was Observed

Ran `EXP-20260625-701-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro`
with one repetition each for no-10x-control, current-10x, and
candidate-variant arms across SCN-004 and SCN-009.

Raw artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/`

Canonical guard:

- `SKILL.md` before and after hash:
  `b46696627d94d707a26665cb8272ec90d0c9e0c64ea54cf81c2b91b980c57332`
- `autoresearch/program.md` before and after hash:
  `81032b42894e93727fd54ec1aa457edaa3a6e6e1a049dc2e76c52aab77c3d4d5`
- `unchanged_during_run`: `true`

Sample map:

| Scenario | Arm | Workspace |
| --- | --- | --- |
| SCN-004 | no-10x-control | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-20f79ce7bde4439a55b383c1ff21071d44ae7afb18ad9d9684376161bb907a4c/` |
| SCN-004 | current-10x | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-b853037a2aa5cbdc69d08504f15dde703253ca1e9f400b31e999a466c9c272cd/` |
| SCN-004 | candidate-variant | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-723bc81fb1d4d64dd3e6fadb697f1d3a30c068eaf0b12830d1556fbc0a65914f/` |
| SCN-009 | no-10x-control | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-41f24e93433724532426cbf579a1a148ee123b4161cfeefeeac83fd936755b6d/` |
| SCN-009 | current-10x | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-78f35ba2fe0f28fe872c4a3865212178b39f9fa336142af8c1a7f7c25fad9124/` |
| SCN-009 | candidate-variant | `.10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro/workspaces/sha256-7a8185e3c625a5ed1639778ae73cdff7f821be05cbc6e69ad6973a4e340f9e37/` |

SCN-004 candidate result:

- moved `.10x/specs/payments-retry-window.md` to
  `.10x/specs/payments-webhook-retry-policy.md`;
- updated the active spec title to `Payments Webhook Retry Policy`;
- repaired live `Depends-On`, `Relates-To`, `Target`, scope, acceptance, and
  supersession references to the new path;
- preserved historical prose and fenced command output mentioning the old path;
- did not create implementation tickets, edit source/test files, or run tests.

SCN-004 current result:

- matched candidate correctness and safety;
- used direct `mv` for the file move;
- used assistant-side `file_change` edits for the selective content changes,
  which is acceptable in this scenario because historical-reference
  preservation required deliberate judgment rather than blind replacement.

SCN-009 candidate result:

- inspected spec, tickets, final evidence, final review, source, and tests;
- used direct `mv` to move child and parent tickets to `done`;
- used one bounded `perl -0pi` rewrite over the unambiguous live-reference file
  set to repair terminal ticket paths and stale `2026-06-23` evidence/review
  paths to the unambiguous `2026-06-24` final records;
- added read-only closure evidence at
  `.10x/evidence/2026-06-25-invoice-retry-closure-inspection.md`;
- closed child and parent tickets with coherent references to the active spec,
  final evidence, final pass review, and closure inspection;
- did not edit source/test files, run tests, or create duplicate test evidence
  or review records.

SCN-009 current result:

- inspected the same record/source/test surfaces;
- repaired stale evidence/review references and closed child and parent
  tickets coherently;
- used assistant-side `file_change` edits for repeated path/reference updates
  rather than command-line mechanical replacement.

No-10x-control result:

- both no-10x-control samples lacked the seed `.10x` task surface because the
  no-10x control cleanup removed `.10x`; they could not exercise the record
  maintenance behavior and are not useful for arm comparison in this batch.

Trust Level 1 automated scoring:

- SCN-004 current and candidate both scored S002=30.
- SCN-009 current and candidate both scored S004=100 and S006=45.
- Manual inspection classifies these low S002/S006 scores as false negatives
  for the current/candidate regression question because the scorer does not
  understand selective historical-reference preservation or closure evidence
  sufficiency.

## Procedure

Executed:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/177-record-maintenance-command-line-economy-regression-batch-scn004-scn009-live-micro --require-clean-canonical
```

Manual inspection used:

- `plan.json` to map sample hashes to scenarios and arms;
- `canonical_guard.json` to verify canonical files stayed unchanged;
- `report.md` for score vectors;
- archived workspace manifests for changed-file sets;
- `stdout.jsonl` command events for operation mechanics;
- direct inspection of archived `.10x` records for SCN-004 and SCN-009.

## What This Supports Or Challenges

This supports promoting
`candidate-record-maintenance-command-line-economy-v1` into `SKILL.md`.

EXP-700 showed current `SKILL.md` does not reliably induce mechanical workflow
economy when the prompt does not explicitly ask for it. EXP-701 shows the
candidate preserves 10x safety on ambiguous historical-reference repair and
uses mechanical tools when the SCN-009 live-reference rewrite is unambiguous.

## Limits

This is a two-scenario Codex CLI MICRO regression batch with one repetition per
arm. It does not prove every semantic-edit boundary. The promotion review
accepts that residual risk because the proposed instruction is narrow,
explicitly forbids blind semantic/history rewrites, and has now passed the
highest-risk historical-reference and closure-reference regressions.
