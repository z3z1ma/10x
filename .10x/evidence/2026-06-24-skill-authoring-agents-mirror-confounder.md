Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-skill-authoring-agents-mirror-scn012-live-micro.md

# Skill Authoring Agents Mirror Confounder

## What Was Observed

The live run for
`EXP-20260624-936-skill-authoring-agents-mirror-scn012-live-micro` was stopped
after the no-10x-control sample because the subject harness blocked writes to
the target `.agents/skills` mirror path.

The completed no-10x-control raw artifact is:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/136-skill-authoring-agents-mirror-scn012-live-micro/raw/sha256-344e18540f674f4fba86b892e314da1cd7de82e7da9522bc31f4a085df76cfd8.json`

Observed behavior:

- The subject read `.agents/skills/skill-writing-governor/SKILL.md`.
- The control workspace had `.10x` removed before execution, as expected.
- The subject created `.10x/skills/ledger-import-fixture-replay/SKILL.md`.
- The subject attempted to create
  `.agents/skills/ledger-import-fixture-replay/`.
- Shell `mkdir -p .10x/skills/ledger-import-fixture-replay .agents/skills/ledger-import-fixture-replay`
  failed with `mkdir: cannot create directory '.agents/skills/ledger-import-fixture-replay': Operation not permitted`.
- A patch attempt also failed with `patch rejected: writing outside of the project; rejected by user approval settings`.
- The archived workspace manifest reports `.agents/skills` as a suppressed
  instruction path present before and after the run.

The run was interrupted with Ctrl-C while the second sample was executing, so no
complete current-10x or candidate-variant result exists.

## Procedure

Command started:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-skill-authoring-agents-mirror-scn012-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/136-skill-authoring-agents-mirror-scn012-live-micro --require-clean-canonical
```

After inspecting the first raw artifact and identifying the write-boundary
confounder, the command was interrupted with Ctrl-C. A subsequent process check
found no remaining `10x-autoresearch`, `run_once`, or matching Codex subject
processes.

## What This Supports Or Challenges

This supports marking
`.10x/research/2026-06-24-skill-authoring-agents-mirror-scn012-live-micro.md`
as inconclusive and avoiding any `SKILL.md` promotion from this run.

It also supports routing the next non-`.claude` harness mirroring test to a
non-suppressed fixture path such as `.opencode/skills/`, or explicitly changing
the runner before testing `.agents/skills`.

## Limits

This evidence does not prove current 10x fails `.agents` mirroring. It only
proves this Codex CLI subject harness cannot fairly test creation of new
`.agents/skills` entries under the current isolation settings.

The completed sample was the no-10x-control arm, not the current-10x arm.
