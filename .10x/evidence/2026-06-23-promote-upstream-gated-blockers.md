Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/tickets/done/2026-06-23-promote-upstream-gated-blockers.md, autoresearch/candidates/2026-06-23-upstream-gated-blockers.md, .10x/research/2026-06-23-skill-autoresearch-run.md

## What was observed

`candidate-upstream-gated-blockers-v1` was promoted into canonical `SKILL.md`.
The promoted rule adds dependency-gated ambiguity blockers to the Outer Loop:
name the ambiguity directly, ask upstream blockers before downstream details,
ask only current blockers, preserve multi-question interviews when independent
answers change the next safe action, and avoid invented business rules.

Candidate metadata was updated:

- `autoresearch/candidates/2026-06-23-upstream-gated-blockers.md` status:
  `promoted`
- `autoresearch/candidates/candidates.json` status:
  `promoted`

Validation commands after the edit:

```text
$ python3 autoresearch/validate.py
autoresearch contracts valid
```

```text
$ python3 -m unittest discover -s autoresearch/tests
Ran 46 tests in 13.001s

OK
```

```text
$ git diff --check
```

`git diff --check` exited 0 with no output.

## Procedure

1. Reviewed the leading candidate and live evidence records from SCN-001,
   SCN-002, SCN-001 continuation, and SCN-003 retrieval.
2. Edited `SKILL.md` to add the candidate behavior in the existing Outer Loop
   ambiguity-resolution section.
3. Updated candidate metadata to mark the candidate promoted.
4. Ran contract validation, unit tests, and whitespace checks.

## What this supports or challenges

Supports closing
`.10x/tickets/done/2026-06-23-promote-upstream-gated-blockers.md` and treating
the upstream-gated blocker rule as canonical 10x behavior.

Challenges the prior run-log conclusion that no canonical promotion was
currently supported; that conclusion was true before the later upstream-gated
live runs and user promotion authorization.

## Limits

This evidence proves the canonical edit was made and local validation passed. It
does not prove long-run effect size, cross-harness behavior, or that the
promoted instruction cannot under-question in a nearly executable ticket-boundary
scenario. Those remain autoresearch targets.
