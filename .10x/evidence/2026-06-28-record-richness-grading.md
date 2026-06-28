Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Relates-To: .10x/tickets/done/2026-06-28-add-record-richness-grading.md, .10x/specs/10x-autoresearch-loop.md, autoresearch/catalogs/scores.json

# Record Richness Grading Evidence

## What Was Observed

The autoresearch rubric now includes `S010` / Record Regeneration Quality for
judging whether created or materially updated `.10x` records are rich enough
for a cold-start agent to reconstruct the goal, constraints, edge cases,
provenance, blockers, and next action without chat archaeology.

`S010` is quality-gated with an active floor of 80 and a 100-point manual
sub-score split:

- Cold-start completeness: 20.
- Behavior and edge-case coverage: 15.
- Provenance and evidence grounding: 15.
- Ambiguity and blocker preservation: 15.
- Operational actionability: 15.
- Cross-record coherence: 10.
- Economy without thinness: 10.

Hard floors cap under-specified executable records, blurred semantic authority,
record bloat that still leaves future agents guessing, and unnecessary
preservation of secrets or sensitive data.

## Procedure

Updated:

- `.10x/specs/10x-autoresearch-loop.md` with `REQ-023` and the active `S001`
  through `S010` rubric list.
- `autoresearch/catalogs/scores.json` with the `S010` rubric entry and a
  `S009` cost false positive for terse records that shift reconstruction cost to
  future agents.
- `autoresearch/catalogs/scenarios.json` so record-producing scenarios target
  `S010` where richness is materially observable.
- `autoresearch/program.md` and `autoresearch/README.md` so scientists see
  record richness as part of the active evaluation surface.
- `autoresearch/validate.py` so `S010` and `REQ-023` are part of the checked
  contract.

Regenerated the seed index:

```bash
python3 autoresearch/build_trial_seed_index.py
```

Observed:

```text
wrote autoresearch/trial-seeds/index.json (129 seeds)
```

Seed inventory after regeneration:

```text
seed count: 129
S010 seed count: 80
S010 scenarios: SCN-004=13, SCN-005=2, SCN-006=29, SCN-007=1, SCN-008=1, SCN-009=18, SCN-012=15, SCN-015=1
```

## Validation

Commands run after the final edits:

```bash
python3 autoresearch/validate.py
python3 -m unittest discover -s autoresearch/tests
git diff --check
```

Observed:

- `python3 autoresearch/validate.py`: `autoresearch contracts valid`.
- `python3 -m unittest discover -s autoresearch/tests`: 60 tests passed.
- `git diff --check`: no whitespace or conflict-marker issues.

## What This Supports Or Challenges

Supports:

- Existing seed workspaces are sufficient for this new quality vector; no new
  seed suite was needed.
- Record richness is now explicit in the scientist-facing program, the normative
  spec, the score catalog, the scenario catalog, validation, and the seed
  selection index.
- The new score rewards concise complete records and penalizes both thin tickets
  and verbose records that still omit material context.

Challenges:

- `S010` remains a judgment-based score. That is intentional: record richness is
  about whether available context was preserved well enough for a future agent,
  and that comparison requires scientist inspection of transcripts, artifacts,
  source, and created records.

## Limits

No live subject trial was run for this record-only tooling change. The evidence
proves the static autoresearch contracts, docs, catalogs, and seed index are
coherent and validated; actual score calibration will come from future
experiments that create or update records.
