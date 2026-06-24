Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: SKILL.md, autoresearch/candidates/2026-06-23-implicit-record-supersession-gate.md
Verdict: pass

# Promote Implicit Record Supersession Review

## Target

Canonical promotion of `candidate-implicit-record-supersession-gate-v1` into
`SKILL.md`.

## Findings

- **Pass:** The promoted rule targets a real observed failure: current 10x
  converted a conflicting user value into active-record authority without
  explicit supersession authorization.
- **Pass:** The rule is narrow. It applies only when a new semantic value
  conflicts with an active specification, active decision, or active knowledge
  record.
- **Pass:** The rule preserves positive-control behavior from
  `EXP-20260623-843-active-record-conflict-scn006-live-micro`: when the user
  explicitly authorizes updating records, coherent supersession remains allowed.
- **Pass:** The candidate improved the intended safety property by keeping
  threshold `90` out of active behavior and executable acceptance criteria until
  supersession authority is explicit.
- **Concern accepted:** The rule may overblock if an agent interprets any
  conflict as requiring formulaic wording. The intended bar is explicit
  supersession authority, not a magic phrase.

## Verdict

Pass. Promote the implicit-supersession clarification near Assumption
Provenance and continue with tests-as-assumptions experiments.

## Residual Risk

The main residual risk is overblocking legitimate user corrections. The prior
explicit-record-update MICRO mitigates this risk but does not exhaust it.
Future positive controls should verify that clear supersession authorization
allows record repair without extra ceremony.
