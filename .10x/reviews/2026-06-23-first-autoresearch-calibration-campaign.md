Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: .10x/research/2026-06-23-first-autoresearch-calibration-campaign.md
Verdict: concerns

# First Autoresearch Calibration Campaign Review

## Target

Campaign research, evidence, raw artifacts, score artifacts, and report:

- `.10x/research/2026-06-23-first-autoresearch-calibration-campaign.md`
- `.10x/evidence/2026-06-23-first-autoresearch-calibration-campaign.md`
- `.10x/evidence/.storage/2026-06-23-first-autoresearch-calibration-campaign/`

## Findings

Significant: the candidate arm is not a real candidate.

The campaign registers `candidate-variant` as a placeholder using current
`SKILL.md` and the same pass fixtures as current-10x. Any apparent candidate
parity or improvement is null/confounded. The research and evidence records
state this correctly, so the finding blocks promotion claims rather than the
calibration artifact itself.

Significant: scorer trust remains low.

All score artifacts are produced by `offline-coverage-v1` at Trust Level 1 with
low confidence and `manual_inspection_required: true`. Manual inspection notes
exist in the research/evidence records, but the generated score artifacts still
say `required-not-done`. The score artifacts should not be read independently as
reviewed or promotion-ready.

Significant: FULL fixture-smoke does not prove live Codex behavior.

The FULL run wrote Codex-shaped raw artifacts and workspace manifests, but
`live_codex_calls` was 0 for every sample. Planned no-10x argv includes
`--disable plugins` and `--ignore-user-config`, and prior evidence supports a
narrow smoke, but this campaign does not prove benchmark-scale live isolation or
hidden-context absence.

Minor: campaign-level null/confounded status is outside the generated report.

The generated report says no result statuses were present because score artifacts
do not carry null/confounded fields. The campaign verdict is preserved in
research/evidence, but a future reader who opens only `report.md` could miss the
null/confounded interpretation.

## Verdict

Concerns raised.

The campaign is acceptable as a first calibration artifact because it registered
the experiment before runs, produced raw and score artifacts, generated a report,
preserved manual inspection notes, recorded null/confounded findings, and opened
follow-up tickets. It is not acceptable as a promotion basis.

## Residual Risk

- Fixture-backed results may overstate scenario quality because all behavior is
  represented by canned JSON fixtures.
- The no-10x control failure is selected by fixture, not elicited from a live
  model.
- The candidate arm cannot inform instruction quality until a real candidate is
  designed and evaluated.
- Trust Level 1 scorer keyword/path heuristics may reward superficial wording or
  miss terse correct behavior.
- Broader live Codex isolation remains unproven.
