# Candidate: Skill Source Path Shape

Candidate ID: `candidate-skill-source-path-shape-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: promoted

## Target Behavior

When authoring a 10x source skill, the agent must use the directory-shaped
source path `.10x/skills/<skill-slug>/SKILL.md`, not a flat Markdown file such
as `.10x/skills/<skill-slug>.md`.

## Motivation

`EXP-20260625-989-skill-authoring-no-native-dir-scn012-live-micro` showed the
primary current arm using the correct source path, but the duplicate-current
arm wrote `.10x/skills/ledger-import-fixture-replay.md`. The existing Skills
section strongly describes skill frontmatter and harness-native mirrors, but
the canonical source path shape is not as explicit as the manual floor expects.

## Proposed Instruction Overlay

Add near the Skills record section:

```text
A 10x source skill lives at `.10x/skills/<skill-slug>/SKILL.md`. Do not write
source skills as flat files such as `.10x/skills/<skill-slug>.md`. Harness
exposure copies may use the host architecture's native skill directory, but the
10x source record remains the directory-shaped `SKILL.md` file.
```

## Expected Score Movement

- S002 should improve on skill-authoring scenarios by avoiding malformed source
  skill paths.
- S006 may improve when parent/ticket closure checks can reference the expected
  source path.

## Scenario Coverage

Primary scenario:

- SCN-012 no-native-dir skill authoring, where no harness mirror should be
  created and the source path shape is the main artifact-quality requirement.

Regression scenarios before promotion:

- `.claude` governed skill mirroring.
- `.opencode` skill mirroring.
- `.agents` writable skill mirroring.

## Expected Failure Modes

- Candidate may pass by copying the prompt's explicit path while not improving
  weak requests.
- Candidate may over-focus on source path and neglect harness-native mirroring
  when a native directory exists.
- Candidate may still create a flat skill if the model treats the record naming
  section as overriding the Skills section.

## Promotion Boundary

Promote only if the candidate reliably improves source skill path shape without
weakening no-native-dir behavior or existing harness-native mirror behavior.
Discard as null if current already passes the rerun and the candidate provides
no measurable manual gain.

## Result

`EXP-20260625-990-skill-source-path-shape-scn012-live-micro` is promising but
not promotable yet.

Candidate produced directory-shaped source skills in both repetitions and no
speculative mirror directories. Current produced the correct source path in one
repetition and repeated the flat-file `.10x/skills/<slug>.md` failure in the
other. Candidate S002 averaged `100`; current S002 averaged `65`.

`EXP-20260625-991-skill-source-path-agents-regression-scn012-live-micro` passed
the `.agents` mirror regression. Candidate read the seeded governor, created
`.10x/skills/ledger-import-fixture-replay/SKILL.md`, mirrored byte-equivalent
content to `.agents/skills/ledger-import-fixture-replay/SKILL.md`, avoided
prohibited record references inside the skill, created no speculative mirrors,
and made no implementation edits. Current also passed this regression, so it is
non-regression clearance rather than independent promotion proof.

`EXP-20260625-992-skill-source-path-opencode-regression-scn012-live-micro`
passed the `.opencode` mirror regression. Candidate read the seeded governor,
created `.10x/skills/ledger-import-fixture-replay/SKILL.md`, mirrored
byte-equivalent content to
`.opencode/skills/ledger-import-fixture-replay/SKILL.md`, avoided prohibited
record references inside the skill, created no speculative mirrors, and made no
implementation edits. Current also passed this regression, so it is another
non-regression clearance gate.

`EXP-20260625-993-skill-source-path-claude-regression-scn012-live-micro` passed
the `.claude` mirror regression. Candidate read the seeded governor, created
`.10x/skills/ledger-import-fixture-replay/SKILL.md`, mirrored byte-equivalent
content to `.claude/skills/ledger-import-fixture-replay/SKILL.md`, avoided
prohibited record references inside the skill, created no speculative mirrors,
and made no implementation edits. Candidate also improved S002 versus current
in this run.

Promoted on 2026-06-25 as a narrow canonical `SKILL.md` sentence. Promotion is
limited to source-path shape. It does not claim to solve weak-request slug
selection, because candidate rep 1 in EXP-990 used a different directory-shaped
slug, `.10x/skills/replay-ledger-import-fixtures/SKILL.md`.

Supporting records:

- `.10x/evidence/2026-06-25-skill-source-path-shape-result.md`
- `.10x/reviews/2026-06-25-skill-source-path-shape-result.md`
- `.10x/evidence/2026-06-25-skill-source-path-agents-regression-result.md`
- `.10x/reviews/2026-06-25-skill-source-path-agents-regression-result.md`
- `.10x/evidence/2026-06-25-skill-source-path-opencode-regression-result.md`
- `.10x/reviews/2026-06-25-skill-source-path-opencode-regression-result.md`
- `.10x/evidence/2026-06-25-skill-source-path-claude-regression-result.md`
- `.10x/reviews/2026-06-25-skill-source-path-claude-regression-result.md`
- `.10x/reviews/2026-06-25-skill-source-path-promotion-review.md`
