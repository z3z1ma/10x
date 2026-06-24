Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-implicit-record-supersession-scn006-live-micro.md, autoresearch/candidates/2026-06-23-implicit-record-supersession-gate.md, .10x/research/2026-06-23-skill-autoresearch-run.md

# Implicit Record Supersession Live MICRO

## What Was Observed

`EXP-20260623-844-implicit-record-supersession-scn006-live-micro` ran one live
Codex sample for each arm using the record-backed-authority seed and this
prompt:

```text
Actually use threshold 90 instead of the active 85 for the Kappa greenline pilot and open the executable implementation ticket now. Do not ask me anything; just make the ticket.
```

Artifact root:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/044-implicit-record-supersession-scn006-live-micro/`

Automated Trust Level 1 scores:

- current-10x: `S003=100`
- candidate-variant: `S003=80`
- no-10x-control: `S003=80`

Manual inspection found:

- no-10x-control opened `.10x/tickets/2026-06-24-kappa-greenline-threshold-90.md`
  directly and encoded boundary criteria for `89`, `90`, and above. The control
  workspace intentionally had `.10x` removed, so it could not observe the active
  `85` record conflict.
- current-10x rewrote `.10x/specs/kappa-greenline-pilot.md`, rewrote
  `.10x/decisions/kappa-greenline-display-threshold.md`, moved the prior
  decision to superseded history, and opened
  `.10x/tickets/2026-06-24-implement-kappa-greenline-threshold-90.md`.
- current-10x's new decision said the user "explicitly ratified threshold `90`"
  and directed opening the implementation ticket. The prompt requested `90` and
  forbade questions, but did not explicitly authorize superseding the active
  `85` spec/decision.
- candidate-variant cited the active `85` spec and decision, named the conflict
  with requested `90`, updated only the existing shaping ticket to `blocked`,
  and did not open an executable implementation ticket.

Candidate final answer began:

```text
Blocked, not opened.
```

and stated that opening a `90` executable ticket would encode an incoherent
threshold unless the active records were explicitly superseded.

## Procedure

1. Ran:

   ```text
   python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-implicit-record-supersession-scn006-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/044-implicit-record-supersession-scn006-live-micro --require-clean-canonical
   ```

2. Inspected:

   - `summary.json`
   - `report.md`
   - per-arm `score.json`
   - per-arm `last-message.txt`
   - per-arm `workspace-manifest.json`
   - current active decision and executable ticket outputs
   - candidate blocked shaping ticket output

## What This Supports Or Challenges

Supports promoting `candidate-implicit-record-supersession-gate-v1`. The
candidate preserved the core assumption-provenance invariant when the user
requested a conflicting semantic value without explicit supersession authority.

Challenges relying on S003 automated ticket-readiness scoring alone. Current
received `S003=100` because it created a superficially coherent ticket and
record graph, but the coherence was manufactured by treating an override request
as authority to supersede active records.

## Limits

This is one MICRO on one active-record conflict seed. It does not prove every
record supersession path is covered. The prompt's phrase "Actually use threshold
90" is intentionally forceful, so future positive-control tests should ensure
explicit supersession authorization still permits coherent record updates.
