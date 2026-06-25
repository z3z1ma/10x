Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-source-inspection-decoy-pressure-live-micro.md

# Source-Inspection Decoy Pressure Result

## What Was Observed

EXP-20260625-711 ran 6 live Codex subject calls:

- 1 scenario: SCN-003 source-inspection decoy pressure;
- 3 arms: no-10x-control, current-10x, and candidate-variant with a no-op
  overlay;
- 2 repetitions per arm.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/188-source-inspection-decoy-pressure-live-micro/`

Current-10x answered correctly in both repetitions:

- identified `src/risk/refundRiskSummary.js` as the summary surface;
- identified `src/risk/refundRiskScore.js` as the risk pipeline authority;
- listed risk levels `critical`, `high`, `medium`, `low`, and `unknown`;
- cited `src/risk/rules/escalationRules.js` for escalation semantics;
- cited `src/risk/rules/refundThresholds.js` for threshold semantics;
- treated UI labels, analytics dashboard buckets, legacy risk source, tests,
  fixtures, routes, and jobs as non-authoritative behavior sources.

Current-10x produced no `file_outputs`. Current workspace manifests recorded
`changed_files: []`, `workspace_contamination_present: false`, and `timed_out:
false`.

Current-10x failed the operation-quality precision floor. Both current
repetitions used shell-native commands, but after records and imports had
already identified authoritative files, they still read most decoy files in
full.

Current rep 0 command pattern:

```text
rg --files .10x . 2>/dev/null | ... | sort | head -300
rg -n "refund|risk|summary|escalat|threshold" .10x .
sed -n ... src/risk/refundRiskSummary.js
sed -n ... .10x/specs/refund-risk-summary.md
sed -n ... src/risk/rules/escalationRules.js
sed -n ... src/risk/rules/refundThresholds.js
sed -n ... .10x/knowledge/refund-risk-vocabulary.md
sed -n ... src/risk/refundRiskScore.js
sed -n ... src/analytics/refundRiskDashboard.js
sed -n ... src/risk/fixtures/refunds.js
sed -n ... src/ui/refundRiskLabels.js
sed -n ... src/risk/refundRiskSummary.test.js
sed -n ... src/legacy/refundRiskOld.js
sed -n ... src/jobs/refundRiskBackfill.js && sed -n ... src/api/refundRoutes.js
```

Current rep 1 additionally read `src/support/refundTags.js`,
`src/api/refundRoutes.js`, `src/analytics/refundRiskDashboard.js`, and
`src/legacy/refundRiskOld.js`, then re-read several authoritative files with
`nl`.

The no-10x-control and no-op candidate arms also showed decoy over-reading
patterns. This appears to be a model/harness tendency under decoy pressure, not
a one-off current-only anomaly.

Trust Level 1 automated scores under-scored S001 for every arm and did not
measure source-inspection precision. Manual inspection is authoritative.

## Procedure

Command run:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-source-inspection-decoy-pressure-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/188-source-inspection-decoy-pressure-live-micro --require-clean-canonical
```

Manual inspection used:

- `report.md`
- `plan.json`
- per-sample raw JSON artifacts
- per-sample command events
- per-sample last messages
- current-10x workspace manifests

## What This Supports Or Challenges

This challenges the sufficiency of the current Mechanical Tool Economy wording
for read-only source-authority questions in decoy-heavy workspaces.

The result does not challenge correctness, write-boundary discipline, or the
general shell-native workflow preference. The gap is narrower: after active
records or imports identify source authority, the agent needs a stronger bias
toward targeted source inspection instead of full decoy browsing.

## Limits

This is one Codex CLI MICRO batch with two current repetitions. The workspace
is still small compared with a production repository, and the offline scorer
does not measure tool precision.
