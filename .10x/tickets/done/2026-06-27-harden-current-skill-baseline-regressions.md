Status: done
Created: 2026-06-27
Updated: 2026-06-28
Depends-On: .10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md

# Harden Current Skill Baseline Regressions

## Scope

Improve canonical `SKILL.md` only after analyzing the cross-harness baseline
regressions without overfitting to one transcript.

Included:

- Reproduce and inspect the SCN-011 accessibility-safety-rail failures.
- Reproduce and inspect the SCN-009 false-pass child-test provenance failures.
- Identify the smallest instruction change that makes the governing invariant
  harder to miss while preserving existing passes and operational minimalism.
- Validate through both `codex-cli` and `opencode-cli`.

Excluded:

- Changing the autoresearch runner, scenario catalog, score catalog, or seed
  data as a substitute for fixing skill behavior.
- Weakening closure, minimalism, or safety-rail rules to make the baseline look
  better.
- Promoting a change from one lucky rerun.

## Acceptance Criteria

- AC-001: The raw failure artifacts in
  `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md` are
  inspected and summarized before editing `SKILL.md`.
- AC-002: Any `SKILL.md` change names the exact invariant it strengthens and the
  behavior it must not accidentally permit.
- AC-003: Targeted repeats pass the accessibility-safety-rail seed through both
  Codex and OpenCode with at least three direct samples per harness.
- AC-004: Targeted repeats pass the false-pass child-test provenance seed
  through both Codex and OpenCode with at least three direct samples per
  harness.
- AC-005: Regression controls include the passing `minimalism-safety-rail` seed,
  a valid closure-positive seed, and at least one authorized-record-hardening or
  ticket-readiness seed.
- AC-006: Evidence and adversarial review are recorded before any claim that the
  current skill is baseline-clean.

## Progress And Notes

- 2026-06-27: Opened from the cross-harness seed baseline. The baseline found
  nondeterministic SCN-011 accessibility safety-rail failures and repeated
  SCN-009 false-pass closure failures.
- 2026-06-28: Inspected raw failure artifacts before editing. SCN-011 failures
  obeyed pointer-only/visual-test pressure and removed native button,
  accessible-name, disabled, or ARIA semantics. SCN-009 failures treated passing
  child evidence and pass review as enough to close even though active records
  kept `readinessScore` / `GREENLINE_MIN_SCORE = 85` semantics unratified.
- 2026-06-28: Hardened `SKILL.md` with the smallest targeted invariants:
  passing tests/reviews prove only their actual assertions and do not ratify
  blocked semantics; parent/child closure must inspect child-test assertions
  when semantic authority is in question; visual or pointer-only coverage does
  not make baseline accessibility disposable. Intended not to permit generic
  distrust of all tests, broad closure refusal, or refusal of simplifications
  that preserve equivalent accessibility.
- 2026-06-28: First candidate repeats fixed the accessibility-safety-rail
  target across both harnesses but still found false-pass closure laundering via
  "preview-only / not product ratification" language and an OpenCode regression
  where a simplification prompt deleted validation plus its tests. Added the
  missing invariants: closure cannot be achieved by narrowing active acceptance
  criteria after the fact, and safety-rail simplification cannot proceed by
  deleting the rail or the tests that protect it. Intended not to block valid
  closure records already scoped to narrow regression evidence or valid
  simplifications that preserve the same protection.
- 2026-06-28: Second candidate matrix passed accessibility and all OpenCode
  false-pass repeats, but one Codex false-pass repeat still moved tickets to
  `done` from child evidence relying on unratified field/threshold semantics.
  Added the explicit parent/child closure outcome: leave tickets open or blocked
  when child evidence relies on unratified fields or thresholds, even if the user
  says to close now or not re-ratify.
- 2026-06-28: Final v3 candidate matrix passed all targeted repeats and
  controls across Codex and OpenCode. Recorded evidence in
  `.10x/evidence/2026-06-28-current-skill-baseline-regression-hardening.md` and
  pass review in
  `.10x/reviews/2026-06-28-current-skill-baseline-regression-hardening-review.md`.
  Closed this ticket.

## Blockers

None.

## References

- `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md`
- `.10x/evidence/2026-06-28-current-skill-baseline-regression-hardening.md`
- `.10x/reviews/2026-06-28-current-skill-baseline-regression-hardening-review.md`
- `SKILL.md`
- `autoresearch/catalogs/scenarios.json`
- `autoresearch/catalogs/scores.json`
- `autoresearch/trial-seeds/accessibility-safety-rail/raw.json`
- `autoresearch/trial-seeds/false-pass-child-test-provenance/raw.json`
