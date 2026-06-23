Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Relates-To: .10x/research/2026-06-23-records-first-retrieval-opaque-scn003-live-micro.md

# Records-First Retrieval Opaque SCN-003 Live Micro

## What Was Observed

`EXP-20260623-829-records-first-retrieval-opaque-scn003-live-micro` ran one live
Codex sample per arm over an opaque records-first seed.

Automated scores:

- candidate-variant: `S001=70;S002=50;S007=10`
- current-10x: `S001=70;S002=50;S007=10`
- no-10x-control: `S001=70;S002=70;S007=10`

Manual inspection found the automated S002 score was misleading: current and
candidate did not create duplicate records. Their archived workspaces contained
only the seeded `.10x` decision, spec, and ticket.

Candidate and current both answered with the exact opaque facts from records:

- settled token: `PAX-17-HALCYON`
- ledger note: `halcyon-blue`
- sentinel copy:
  `Manual sweep required: confirm PAX-17-HALCYON before release.`
- owning ticket:
  `.10x/tickets/2026-06-23-add-kappa-amber-hold-sentinel.md`

No-10x control removed inherited `.10x` before execution:
`pre_run_removed_control_record_dirs: [".10x"]`. It created no files and
reported that it could not determine the three facts because the workspace only
contained `workspace-manifest.json`.

Canonical guard reported `unchanged_during_run: true` for `SKILL.md` and
`autoresearch/program.md`.

## Procedure

Command:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-23-records-first-retrieval-opaque-scn003-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro --require-clean-canonical
```

Inspected:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/report.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/campaign.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/canonical_guard.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/codex/sha256-894b390a0db048453683289dfc8be2069c566cdf9fddb9c724ccc462c56c3481.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/codex/sha256-633f5a085b2c6f152930b641c90576c243daeec4bfe49926a892842904985999.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/codex/sha256-c5f9a7873efeb294780913b4b51212dfbe89da7dab4aa9097d76267645a44ae5.last-message.txt`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/workspaces/sha256-894b390a0db048453683289dfc8be2069c566cdf9fddb9c724ccc462c56c3481/workspace-manifest.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/workspaces/sha256-633f5a085b2c6f152930b641c90576c243daeec4bfe49926a892842904985999/workspace-manifest.json`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/029-records-first-retrieval-opaque-scn003-live-micro/workspaces/sha256-c5f9a7873efeb294780913b4b51212dfbe89da7dab4aa9097d76267645a44ae5/workspace-manifest.json`

## What This Supports Or Challenges

Supports:

- The opaque seed is a valid records-first retrieval discriminator against
  no-10x control.
- Current and candidate 10x both retrieve exact `.10x` facts before asking the
  user to restate context.
- No-10x control record graph cleanup prevents hidden access to seeded records.

Challenges:

- This run does not show incremental candidate-over-current improvement. The
  candidate tied current on exact opaque retrieval.

## Limits

One live sample per arm. The run supports 10x-over-control retrieval behavior
and control isolation, but only neutral evidence for
`candidate-records-first-retrieval-v1`.
