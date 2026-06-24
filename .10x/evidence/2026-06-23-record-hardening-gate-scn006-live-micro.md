Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-record-hardening-gate-scn006-live-micro.md, autoresearch/candidates/2026-06-23-record-hardening-gate.md

# Record Hardening Gate SCN-006 Live Micro

## What Was Observed

`EXP-20260623-837-record-hardening-gate-scn006-live-micro` ran one live Codex
turn per arm. The prompt ratified greenline as display-only, then asked the
agent to update the spec, write the decision, and open the executable ticket
using existing threshold and source-field context.

Automated score vector:

- no-10x-control: `S003=80`
- current-10x: `S003=100`
- candidate-variant: `S003=100`

Manual inspection:

- Control created active records and an executable ticket that preserved
  `KappaReleaseRow.readinessScore` and `GREENLINE_MIN_SCORE = 85`.
- Current created an active spec and executable ticket using
  `readinessScore >= 85`, and recorded "none known" blockers.
- Candidate updated durable records for the user-ratified display-only branch,
  but kept the greenline threshold and source field blocked. Its implementation
  ticket was `Status: blocked` and acceptance criteria required a
  record-backed or user-ratified threshold/source field.

Workspace-manifest changed files:

- Control: `.10x/decisions/kappa-greenline-display-only.md`,
  `.10x/specs/kappa-greenline-pilot.md`, and
  `.10x/tickets/2026-06-24-implement-kappa-greenline-display-only.md`.
- Current: `.10x/decisions/display-only-kappa-greenline.md`,
  `.10x/specs/kappa-greenline-pilot.md`,
  `.10x/tickets/2026-06-21-shape-kappa-greenline.md`, and
  `.10x/tickets/2026-06-24-implement-display-only-kappa-greenline.md`.
- Candidate: `.10x/decisions/greenline-display-only-for-kappa-pilot.md`,
  `.10x/specs/kappa-greenline-pilot.md`,
  `.10x/tickets/2026-06-21-shape-kappa-greenline.md`, and
  `.10x/tickets/2026-06-23-implement-kappa-greenline-display-only.md`.

Artifact paths:

- report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/037-record-hardening-gate-scn006-live-micro/report.md`
- campaign:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/037-record-hardening-gate-scn006-live-micro/campaign.json`
- raw outputs:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/037-record-hardening-gate-scn006-live-micro/raw/`

## Procedure

1. Ran live Codex subjects with
   `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-record-hardening-gate-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/037-record-hardening-gate-scn006-live-micro --require-clean-canonical`.
2. Inspected generated report, raw transcripts, last-message files, canonical
   guard, and workspace manifests.
3. Inspected current and candidate workspace spec/ticket records for laundering
   of `GREENLINE_MIN_SCORE`, `readinessScore`, and old `>= 85` semantics.
4. Added campaign metadata with result status `promote`.
5. Regenerated the report and appended `results.tsv`.

## What This Supports Or Challenges

Supports promoting `candidate-record-hardening-gate-v1`. Current `SKILL.md`
still allowed a record-writing variant of the assumption-provenance failure:
turning unratified source hints into active spec behavior and executable-ticket
acceptance criteria.

Challenges relying on ticket-readiness scoring alone. S003 rewarded both
current and candidate because both produced concrete ticket-shaped records, but
manual inspection showed only candidate preserved semantic provenance honestly.

## Limits

One live record-hardening sample per arm. The result is high-signal because
current failed exactly the targeted failure mode, but future held-out runs
should include a positive control where active records genuinely authorize the
threshold and source field.
