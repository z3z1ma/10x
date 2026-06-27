Status: open
Created: 2026-06-27
Updated: 2026-06-27
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

## Blockers

None.

## References

- `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md`
- `SKILL.md`
- `autoresearch/catalogs/scenarios.json`
- `autoresearch/catalogs/scores.json`
- `autoresearch/trial-seeds/accessibility-safety-rail/raw.json`
- `autoresearch/trial-seeds/false-pass-child-test-provenance/raw.json`
