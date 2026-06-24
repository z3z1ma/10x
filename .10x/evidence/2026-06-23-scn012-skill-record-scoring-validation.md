Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/tickets/done/2026-06-23-improve-scn012-skill-record-scoring.md, .10x/evidence/2026-06-23-retrospective-extraction-type-gate-scn012-live-micro.md

# SCN-012 Skill Record Scoring Validation

## What Was Observed

The SCN-012 retrospective scorer was updated so valid `.10x/skills/<slug>/SKILL.md`
records count as repeatable procedure capture and use skill YAML frontmatter
instead of common record headers.

Validation commands:

```text
$ python3 autoresearch/validate.py
autoresearch contracts valid

$ python3 -m unittest discover autoresearch/tests
....................................................
----------------------------------------------------------------------
Ran 52 tests in 9.231s

OK

$ git diff --check
```

Direct rescore of the EXP-850 candidate artifact:

```text
$ python3 autoresearch/offline_score.py --fixtures .10x/evidence/.storage/2026-06-23-skill-autoresearch/050-retrospective-extraction-type-gate-scn012-live-micro/raw/sha256-f3365848bf004c796be5852432a721f4533b7d18ba625a4368a4d9abab3e94b5.json --out /tmp/10x-scn012-rescore
wrote /tmp/10x-scn012-rescore/sha256-f3365848bf004c796be5852432a721f4533b7d18ba625a4368a4d9abab3e94b5.score.json
```

The rescored candidate artifact now reports:

- `S002=85`, `floor_triggered=false`
- `S006=85`, `floor_triggered=false`

## Procedure

1. Inspected the scorer patch in `autoresearch/offline_score.py`.
2. Inspected new tests in `autoresearch/tests/test_offline_score.py`.
3. Ran the validation commands above.
4. Rescored the saved EXP-850 candidate raw artifact into `/tmp`.

## What This Supports Or Challenges

Supports closure of `.10x/tickets/done/2026-06-23-improve-scn012-skill-record-scoring.md`.
The change satisfies the ticket's acceptance criteria:

- valid skill records count as retrospective procedure capture;
- skill records do not require common record headers;
- tests cover valid skill records and invalid path-only skill records.

## Limits

This is still Trust Level 1 heuristic scoring. The change fixes the observed
SCN-012 false negative for skill records but does not remove the need for manual
inspection before promotion decisions.
