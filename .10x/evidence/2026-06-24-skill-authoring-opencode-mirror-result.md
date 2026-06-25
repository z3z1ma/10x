Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-skill-authoring-opencode-mirror-scn012-live-micro.md

# Skill Authoring OpenCode Mirror Result

## What Was Observed

Ran `EXP-20260624-937-skill-authoring-opencode-mirror-scn012-live-micro` with
three live Codex subject arms.

Automated Trust Level 1 scores:

- no-10x-control: `S002=80`, `S006=20`
- current-10x: `S002=85`, `S006=85`
- candidate-variant: `S002=85`, `S006=85`

Manual inspection found current `SKILL.md` satisfied the `.opencode` skill
authoring target behavior:

- read `.opencode/skills/skill-writing-governor/SKILL.md`;
- created `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- created `.opencode/skills/ledger-import-fixture-replay/SKILL.md`;
- used the required skill frontmatter with `name`, `description`, and
  `metadata.created`/`metadata.updated`;
- made `description` begin with `Use when`;
- included `Objective`, `Prerequisites`, `Procedure`, and `Validation`;
- kept source and exposure copies byte-equivalent (`cmp=0`);
- referenced only the allowed knowledge record for shared vocabulary;
- recorded validation evidence at
  `.10x/evidence/2026-06-24-ledger-import-fixture-skill-validation.md`;
- updated the subject parent ticket to name `.opencode/skills/`;
- created no speculative `.claude/skills` or `.agents/skills` mirrors;
- edited no implementation files.

The archived current workspace manifest reports no suppressed instruction path
contamination and these changed files:

- `.10x/evidence/2026-06-24-ledger-import-fixture-skill-validation.md`
- `.10x/skills/ledger-import-fixture-replay/SKILL.md`
- `.10x/tickets/2026-06-23-ledger-import-parent.md`
- `.opencode/skills/ledger-import-fixture-replay/SKILL.md`

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/137-skill-authoring-opencode-mirror-scn012-live-micro/`

## Procedure

1. Registered the `.opencode` fixture and research record.
2. Ran:

```bash
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-24-skill-authoring-opencode-mirror-scn012-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/137-skill-authoring-opencode-mirror-scn012-live-micro --require-clean-canonical
```

3. Read `report.md`, raw artifacts, score artifacts, workspace manifests, final
   messages, and the current arm's generated skill, evidence, and parent ticket.
4. Ran manual checks over archived workspaces:

```bash
cmp -s .10x/skills/ledger-import-fixture-replay/SKILL.md .opencode/skills/ledger-import-fixture-replay/SKILL.md
rg -n '\.10x/(tickets|evidence|reviews|research|specs|decisions)|\.claude/skills|\.agents/skills' .10x/skills/ledger-import-fixture-replay/SKILL.md .opencode/skills/ledger-import-fixture-replay/SKILL.md
```

`cmp` returned `0` for every arm. The `rg` check returned no matches for every
arm.

## What This Supports Or Challenges

Supports marking current `SKILL.md` as passing a non-`.claude` harness-native
skill exposure path using `.opencode/skills/`.

Supports keeping the `.agents` probe classified as a harness confounder rather
than a product failure.

## Limits

This was not a behavioral candidate comparison; `candidate-variant` duplicated
current `SKILL.md`.

The run used Codex CLI subject workspaces and file-layout verification. It does
not prove OpenCode runtime ingestion behavior.

The prompt and seeded governor were explicit, so the run primarily tests
conformance to local skill-authoring governance and mirror placement, not
spontaneous discovery under weak prompting.
