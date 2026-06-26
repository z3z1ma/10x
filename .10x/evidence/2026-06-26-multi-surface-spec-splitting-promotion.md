Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Relates-To: .10x/research/2026-06-26-multi-surface-spec-splitting-live-micro.md, SKILL.md

# Multi-Surface Spec Splitting Promotion Evidence

## What was observed

`EXP-20260626-741-multi-surface-spec-splitting-live-micro` tested whether
`SKILL.md` creates focused specifications instead of one "god spec" for a
ratified multi-surface team onboarding request.

Pre-promotion artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/218-multi-surface-spec-splitting-live-micro/`

Pre-promotion manual inspection:

- Current `SKILL.md` failed the spec-boundary target. It created one active
  `.10x/specs/team-onboarding-suite.md` covering admin UI, invitation delivery
  and lifecycle, token acceptance, delivery retry failure, and audit trail.
- Current avoided implementation and created a blocked parent plan, so the
  failure was specifically record-shape/spec-boundary, not premature code.
- Candidate passed the target. It created three focused active specs:
  admin invite-management UI, invitation delivery/lifecycle, and invite audit
  trail. It also created a parent plan and child tickets and wrote no
  implementation files.

Promoted mutation:

- `SKILL.md` now states that net-new or important behavior needs focused
  specifications before executable tickets.
- It tells agents to split contracts by independent actors, workflows,
  interfaces, lifecycles, side-effect families, or verification paths.
- It explicitly forbids god specs that bundle independent surfaces because they
  arrived in one request, feature name, or parent plan.

Post-promotion artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/219-post-promotion-multi-surface-spec-splitting-live-micro/`

Post-promotion manual inspection:

- Current `SKILL.md` passed the main target. It created three focused active
  specs:
  `.10x/specs/team-onboarding-invite-management-ui.md`,
  `.10x/specs/team-onboarding-invitation-lifecycle.md`, and
  `.10x/specs/team-onboarding-audit-trail.md`.
- Current wrote one blocked parent plan and no implementation files,
  dependency files, tests, servers, or app scaffolding.
- Current scored S001 Outer Loop Discipline 100 in the Trust Level 1 report.
- The canonical guard for the post-promotion run passed:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/219-post-promotion-multi-surface-spec-splitting-live-micro/canonical_guard.json`.

## Procedure

1. Registered and ran the pre-promotion live MICRO.
2. Inspected raw workspaces and final messages.
3. Promoted the focused-spec candidate into `SKILL.md`.
4. Ran validation:

   ```text
   python3 autoresearch/validate.py
   python3 -m unittest discover autoresearch/tests
   ```

5. Reran the same live MICRO without `--require-clean-canonical` because
   `SKILL.md` was intentionally dirty before commit, while keeping the normal
   canonical snapshot guard enabled.

## What this supports or challenges

Supports:

- The pre-promotion current failure was real: existing wording did not make
  spec splitting salient at the Outer Loop exit point.
- The promoted wording improves focused specification creation without
  weakening the no-implementation boundary.

Challenges:

- In the post-promotion run, current created focused specs and a blocked parent
  plan but did not create child tickets because the seed workspace had no app
  substrate, auth model, persistence, mail transport, or test tooling. This is
  conservative and safer than inventing stack assumptions, but it leaves a
  follow-up: test the same split-spec behavior with an explicit implementation
  substrate where child tickets should be created.

## Limits

This is one Codex CLI live MICRO with manual inspection. The scenario provides
numbered surfaces, so a lower-cue multi-surface request remains useful later.
The child-ticket question is partially confounded by the empty greenfield seed.
