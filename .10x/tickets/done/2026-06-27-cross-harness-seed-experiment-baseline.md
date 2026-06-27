Status: done
Created: 2026-06-27
Updated: 2026-06-27

# Cross-Harness Seed Experiment Baseline

## Scope

Run the current canonical `SKILL.md` arm across every registered seed-backed
autoresearch experiment definition through both supported subject harnesses:
`codex-cli` and `opencode-cli`.

The baseline uses existing `.10x/research/*live*` subject-runner definitions as
the registered experiment source. For each source definition, extract only the
`current-10x` arm and preserve the source scenarios, prompts, seed
`prior_raw_path` values, workspace procedures, and scientific contract intent.

## Explicit Exclusions

- Do not replay historical `no-10x-control` or `candidate-variant` arms in this
  baseline. They are useful for historical experiments, but they are not the
  current canonical skill baseline.
- Do not mutate canonical `SKILL.md`, `autoresearch/program.md`, score catalogs,
  scenario catalogs, validators, or harness code.
- Do not treat missing ignored `.10x/evidence/.storage` continuation artifacts
  as successful coverage.
- Do not promote or change instructions from this run.

## Acceptance Criteria

- Inventory the registered live experiment definitions and identify the
  seed-backed current-skill subset.
- Generate reproducible current-only Codex and OpenCode runner definitions under
  the campaign artifact directory.
- Run the seed-backed subset with `autoresearch/run_once.py` and
  `--require-clean-canonical` for both harnesses.
- Preserve raw runner artifacts under `.10x/evidence/.storage/`.
- Produce a durable baseline evidence record with aggregate pass/border/fail
  counts, scenario coverage, harness comparison, artifact paths, exclusions, and
  limits.
- Record any non-runnable continuation definitions as a reproducibility gap with
  explicit evidence.

## Evidence Expectations

- Campaign manifest listing source definitions, generated definitions, run
  status, and artifact directories.
- Per-run `summary.json`, `plan.json`, `report.md`, `canonical_guard.json`, raw
  artifacts, command metadata, prompts, and archived workspaces.
- Scientist-side baseline verdict record under `.10x/evidence/`.
- Adversarial review under `.10x/reviews/`.

## Progress And Notes

- 2026-06-27: Inspected `.10x/research` live definitions. Found 256 registered
  definitions total, all with a `current-10x` arm.
- 2026-06-27: Found 212 definitions whose current arm is seed-backed and
  runnable from tracked seed workspaces. These cover all 129 indexed seeds and
  contain 261 current-skill subject samples per harness.
- 2026-06-27: Found 25 continuation definitions whose current-arm prior raw
  artifacts point into ignored `.10x/evidence/.storage` paths that are not
  present locally. These are excluded from the seed-backed baseline and must be
  recorded as a reproducibility gap.
- 2026-06-27: Found 19 older generated-workspace definitions without tracked
  seed `prior_raw_path` values for the current arm. These are excluded from the
  seed-backed baseline and recorded as replay-hygiene follow-up scope.
- 2026-06-27: Ran the full seed-backed baseline through Codex and OpenCode:
  424 `run_once.py` invocations, 522 live subject calls, 522 raw artifacts, 522
  workspace manifests, no timeouts, no nonzero subject exits, and no canonical
  guard drift.
- 2026-06-27: Recorded durable evidence:
  `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md`.
  Recorded adversarial review:
  `.10x/reviews/2026-06-27-cross-harness-seed-experiment-baseline-review.md`.
  Follow-up owners:
  `.10x/tickets/2026-06-27-harden-current-skill-baseline-regressions.md` and
  `.10x/tickets/2026-06-27-harden-autoresearch-baseline-replay-hygiene.md`.

## Blockers

None for the seed-backed baseline.

## Closure

Acceptance criteria met for the seed-backed baseline run and durable record.
The baseline is not a behavioral pass for canonical `SKILL.md`; it found
current-skill regressions that are owned by
`.10x/tickets/2026-06-27-harden-current-skill-baseline-regressions.md`.

## References

- `SKILL.md`
- `autoresearch/program.md`
- `autoresearch/README.md`
- `autoresearch/trial-seeds/index.json`
- `autoresearch/run_once.py`
- `autoresearch/run_subject.py`
