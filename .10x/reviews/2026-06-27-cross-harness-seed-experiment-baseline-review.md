Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Target: .10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md
Verdict: concerns

# Cross-Harness Seed Experiment Baseline Review

## Target

Review of `.10x/evidence/2026-06-27-cross-harness-seed-experiment-baseline.md`
and its raw campaign artifacts under
`.10x/evidence/.storage/2026-06-27-cross-harness-seed-experiment-baseline/`.

## Findings

- Significant: The baseline evidence cleanly proves infrastructure health, but
  it also proves current-skill behavioral regressions. The evidence record must
  not be used as a blanket pass for canonical `SKILL.md`; SCN-011 and SCN-009
  have hard-floor failures with raw artifact references.
- Significant: The 44 excluded registered definitions mean this is a full
  seed-backed baseline, not a full historical-definition replay. The evidence
  states this plainly and a follow-up owner exists.
- Minor: Large OpenCode changed-file manifests from `.opencode/node_modules`
  create inspection noise. This does not invalidate the campaign because raw
  transcripts and manifests remain available, but it can slow future scientist
  inspection.
- Minor: Direct OpenCode reruns required an explicit PATH prefix in this shell.
  The full campaign completed, but ad hoc ergonomics are not yet foolproof.

## Verdict

Concerns raised.

The experiment execution and artifact capture are strong enough to serve as a
persistent baseline. The behavioral result is not a pass for current
`SKILL.md`; it is a useful failing baseline that should drive targeted
hardening.

## Residual Risk

- Manual scoring did not inspect every transcript line-by-line. The strongest
  conclusions are the infrastructure verdict and the two red-flag families with
  direct raw evidence.
- Future reruns may shift individual pass/fail counts because the live subjects
  are nondeterministic. The failure families are still material because they
  reproduced across harnesses and repeats.
