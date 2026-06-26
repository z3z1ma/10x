Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Relates-To: .10x/research/2026-06-26-source-backed-split-spec-child-ticket-live-micro.md, .10x/tickets/done/2026-06-26-source-backed-split-spec-child-ticket-control.md, .10x/reviews/2026-06-26-promote-source-backed-child-ticket-gate.md

# Source-Backed Split-Spec Child-Ticket Result

## What was observed

Ran:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-26-source-backed-split-spec-child-ticket-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/220-source-backed-split-spec-child-ticket-live-micro --require-clean-canonical
```

The runner wrote three live Codex samples:

- no-10x-control:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/220-source-backed-split-spec-child-ticket-live-micro/raw/sha256-203ba56ec7fda1f593f537c58779e4b767f1527908e27c6f163d9a487694b13d.json`
- current-10x:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/220-source-backed-split-spec-child-ticket-live-micro/raw/sha256-f0d10ac27febcfc859b75dfd65de764cf6191603f0dfeab5e5fa5b173edda122.json`
- candidate-variant:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/220-source-backed-split-spec-child-ticket-live-micro/raw/sha256-39d93cc7faa7d2ccff082d45cfecaa3c2a454dff8e32bd61c2bcf94ba5d41504.json`

No-10x-control implemented immediately, changed implementation/test files, and
created one broad spec plus a done ticket.

Current-10x avoided implementation mutation but created one suite-wide active
spec, `.10x/specs/team-onboarding-suite.md`, and one broad executable ticket,
`.10x/tickets/2026-06-26-build-team-onboarding-suite.md`.

Candidate-variant created focused specs for admin invite management,
invitation delivery/lifecycle, and invite audit trail; created a parent plan;
created three bounded child tickets; and did not edit implementation files,
tests, dependency manifests, or data files.

## Procedure

Manual inspection covered:

- raw sample summaries and final messages;
- current-10x created spec and ticket contents;
- candidate-variant created spec, parent, and child ticket contents;
- workspace file lists for subject writes;
- runner summary at
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/220-source-backed-split-spec-child-ticket-live-micro/summary.json`.

## What this supports or challenges

This supports promoting a narrow `SKILL.md` rule requiring focused
specification sets, parent plans, and child tickets in the same Outer Loop turn
when a ratified multi-surface request has a record/source-backed implementation
substrate and no execution-critical blockers.

It challenges the previous `SKILL.md` wording because current-10x still treated
the suite-level feature name as a single specification and executable ticket
boundary.

## Limits

This is one live Codex repetition per arm with Trust Level 1 offline scoring.
Manual inspection is authoritative. The prompt explicitly identified the
settled substrate, so the result does not cover lower-cue source-backed
requests. It does not prove behavior in Claude, OpenCode, OMP, or app-level
subagent harnesses.
