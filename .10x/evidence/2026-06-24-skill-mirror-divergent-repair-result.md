Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-skill-mirror-divergent-repair-scn012-live-micro.md

# Skill Mirror Divergent Repair Result

## What Was Observed

Ran `EXP-20260624-952-skill-mirror-divergent-repair-scn012-live-micro` with
three live Codex subject arms.

Automated Trust Level 1 scores:

- no-10x-control: `S002=15`, `S006=10`
- current-10x: `S002=45`, `S006=30`
- candidate-variant: `S002=45`, `S006=30`

Manual inspection found the scores are not reliable for this scenario because
SCN-012 scoring expects broad retrospective extraction, while this MICRO tests
one narrow source/mirror repair behavior.

Current `SKILL.md` satisfied the target behavior:

- read `.opencode/skills/skill-writing-governor/SKILL.md`;
- read `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- read `.opencode/skills/ledger-import-fixture-replay/SKILL.md`;
- identified the OpenCode exposure copy as stale;
- replaced only `.opencode/skills/ledger-import-fixture-replay/SKILL.md` with
  canonical `.10x` source content;
- left `.10x/skills/ledger-import-fixture-replay/SKILL.md` byte-identical to
  the seed source;
- created subject evidence at
  `.10x/evidence/2026-06-24-ledger-import-skill-exposure-repair.md`;
- changed no implementation files and created no `.claude` or `.agents`
  mirrors.

The duplicate-current arm did the same and recorded subject evidence at
`.10x/evidence/2026-06-25-ledger-import-fixture-replay-exposure-sync.md`.

The archived current workspace manifest reports these changed files:

- `.10x/evidence/2026-06-24-ledger-import-skill-exposure-repair.md`
- `.opencode/skills/ledger-import-fixture-replay/SKILL.md`

The archived duplicate-current workspace manifest reports these changed files:

- `.10x/evidence/2026-06-25-ledger-import-fixture-replay-exposure-sync.md`
- `.opencode/skills/ledger-import-fixture-replay/SKILL.md`

The no-10x-control workspace had inherited `.10x` removed by runner isolation.
It found no canonical source, made no repair, and created no speculative source
or mirror.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/152-skill-mirror-divergent-repair-scn012-live-micro/`

Canonical guard:

- `SKILL.md` unchanged during the run.
- `autoresearch/program.md` unchanged during the run.

## Procedure

1. Registered the fixture and research record.
2. Ran:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-skill-mirror-divergent-repair-scn012-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/152-skill-mirror-divergent-repair-scn012-live-micro --require-clean-canonical
```

3. Read `report.md`, `summary.json`, `canonical_guard.json`, workspace
   manifests, final messages, subject evidence records, and raw artifacts.
4. Ran manual checks over archived workspaces:

```bash
cmp -s .10x/skills/ledger-import-fixture-replay/SKILL.md .opencode/skills/ledger-import-fixture-replay/SKILL.md
rg '\.10x/(tickets|evidence|reviews|research|specs|decisions)' .10x/skills/ledger-import-fixture-replay/SKILL.md .opencode/skills/ledger-import-fixture-replay/SKILL.md
cmp -s <seed-source-skill> <current-arm-source-skill>
```

Current and duplicate-current returned `cmp=0` for source/mirror equivalence.
The forbidden-reference search returned no matches. The seed/current source
comparison returned `0`, proving the source skill was not rewritten.

## What This Supports Or Challenges

Supports marking current `SKILL.md` as passing divergent `.opencode` skill
mirror repair in a subject workspace where the `.10x` source skill is canonical
and the harness-native copy has drifted.

Supports treating the low automated scores as scorer false negatives for this
targeted mirror-repair MICRO.

## Limits

This was not a behavioral candidate comparison; `candidate-variant` duplicated
current `SKILL.md`.

The prompt explicitly named the canonical source path, so the run primarily
tests correct authority handling, mirror repair, and write boundaries rather
than spontaneous mirror discovery.

The run used Codex CLI subject workspaces and file-layout verification. It does
not prove OpenCode runtime ingestion behavior.

The duplicate-current subject wrote an evidence file dated `2026-06-25`, while
the outer repository date for this record is `2026-06-24`; that date mismatch
is preserved as archived subject output, not normalized.
