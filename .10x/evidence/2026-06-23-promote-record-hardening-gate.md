Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/tickets/done/2026-06-23-promote-record-hardening-gate.md, autoresearch/candidates/2026-06-23-record-hardening-gate.md, .10x/research/2026-06-23-skill-autoresearch-run.md

# Promote Record Hardening Gate

## What Was Observed

`candidate-record-hardening-gate-v1` was promoted into canonical `SKILL.md`.

The promoted rule says:

- Record hardening does not ratify semantics.
- Before marking a spec active, writing an active decision, or opening an
  executable ticket, every behavioral claim and acceptance criterion must be
  classified as record-backed, user-ratified, or blocked.
- Unratified semantic values may appear only as blockers, candidate meanings, or
  draft notes.
- Active spec behavior, active decisions, and executable-ticket acceptance
  criteria must not encode guessed thresholds, source fields, lifecycle effects,
  permissions, notifications, approvers, failure behavior, or product
  acceptance criteria.

Live evidence:

- `.10x/evidence/2026-06-23-record-hardening-gate-scn006-live-micro.md`
- Candidate: `S003=100`
- Current: `S003=100`
- Control: `S003=80`
- Manual result: candidate pass; current fail for semantic laundering; control
  fail for semantic laundering.

Candidate metadata was updated:

- `autoresearch/candidates/2026-06-23-record-hardening-gate.md` status:
  `promoted`
- `autoresearch/candidates/candidates.json` status: `promoted`

## Procedure

1. Inspected the live record-hardening report, raw transcripts, last messages,
   canonical guard, and workspace manifests.
2. Edited `SKILL.md` to add the narrow record-hardening provenance rule inside
   the Assumption Provenance section.
3. Updated candidate metadata and the autoresearch run log.
4. Ran validation commands after the edit.

Validation results:

```text
$ python3 autoresearch/validate.py
autoresearch contracts valid
```

```text
$ python3 -m unittest discover autoresearch/tests
Ran 50 tests in 8.703s

OK
```

```text
$ git diff --check
```

`git diff --check` exited 0 with no output.

## What This Supports Or Challenges

Supports treating durable-record authoring as part of assumption provenance.
The protocol already blocked implementation from unratified assumptions, but
current behavior showed records can become the laundering path that makes a
future implementation look authorized.

Challenges the sufficiency of "by the time a ticket is executable, no unresolved
assumption may remain" without saying that record hardening itself cannot
resolve the assumption.

## Limits

This promotion is based on one high-signal MICRO plus manual inspection. It
does not prohibit active specs or executable tickets when active current records
or explicit user answers actually authorize the values.
