Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-skill-multi-harness-exposure-scn012-live-micro.md

# Skill Multi-Harness Exposure Result

## What was observed

Ran `EXP-20260625-964-skill-multi-harness-exposure-scn012-live-micro` with 15
live Codex subject samples across `no-10x-control`, `current-10x`, and
duplicate-current `candidate-variant`.

Raw artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/208-skill-multi-harness-exposure-scn012-live-micro/`

`canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md`
unchanged during the run.

Trust Level 1 telemetry recorded:

- current-10x: `S002=85` average and `S006=65` average;
- duplicate-current candidate-variant: `S002=85` average and `S006=65`
  average;
- no-10x-control: `S002=85` average and `S006=44` average.

Manual inspection found the primary multi-harness exposure target passed:

- all five current-10x repetitions created
  `.10x/skills/ledger-import-fixture-replay/SKILL.md`;
- all five current-10x repetitions created byte-equivalent mirrors at
  `.agents/skills/ledger-import-fixture-replay/SKILL.md` and
  `.opencode/skills/ledger-import-fixture-replay/SKILL.md`;
- all five duplicate-current repetitions created the same source and mirror
  paths with byte-equivalent content;
- no current or duplicate-current repetition created `.claude/skills`;
- no current or duplicate-current repetition created an alternate Ledger import
  fixture replay skill slug or flat skill file;
- all authored source and mirror skill bodies avoided forbidden references to
  `.10x/tickets`, `.10x/evidence`, `.10x/reviews`, `.10x/specs`,
  `.10x/research`, and `.10x/decisions`;
- all current and duplicate-current repetitions preserved `sourceRef` knowledge
  and opened or updated an archive malformed-currency follow-up owner;
- workspace manifests showed no implementation file edits.

Manual inspection of supporting lifecycle behavior found:

- all current and duplicate-current repetitions created fresh closure or
  validation evidence;
- four of five current repetitions moved both parent and child tickets to
  `.10x/tickets/done/`;
- one current repetition closed the parent but left the child ticket at
  top-level `.10x/tickets/2026-06-23-add-ledger-import-preview.md` with
  `Status: done`;
- four of five duplicate-current repetitions moved both parent and child tickets
  to `.10x/tickets/done/`;
- one duplicate-current repetition closed the parent but left the child ticket
  at top-level `.10x/tickets/2026-06-23-add-ledger-import-preview.md` with
  `Status: done`;
- one duplicate-current repetition that did move both tickets still included old
  active paths inside a closure evidence note describing negative search
  results, not live headers.

The no-10x-control arm also produced the primary source and mirror files because
the seed and prompt explicitly provided a skill-writing governor. It remained
weaker on closure coherence and is not promotion authority.

## Procedure

Inspected:

- `report.md`;
- `canonical_guard.json`;
- raw artifact arm and repetition mapping;
- workspace manifests and changed files;
- source and mirror skill paths;
- byte equivalence between source, `.agents`, and `.opencode` skill files;
- absence of `.claude/skills`;
- authored skill bodies for forbidden record-category references;
- `sourceRef` knowledge records;
- malformed-currency follow-up tickets;
- terminal parent and child ticket paths;
- top-level done-status tickets;
- stale references to pre-move parent and child paths;
- final subject messages for current and duplicate-current samples.

Used `rg --hidden --no-ignore`, `jq`, `find`, `cmp`, and direct file inspection
under the saved raw artifact root.

## What this supports or challenges

This supports treating ambiguous multi-harness exposure as covered for current
`SKILL.md`: when `.agents/skills` and `.opencode/skills` both exist and
`.claude/skills` is absent, current can produce the canonical `.10x` source
skill and mirror it to all and only the present roots.

This challenges treating terminal ticket movement as fully stable under richer
skill-authoring closure tasks. EXP-965 isolated terminal movement successfully,
but this multi-obligation prompt reproduced a weaker form of the old lifecycle
variance in two of ten canonical repetitions.

## Limits

This was a duplicate-current conformance gate, not a new candidate comparison.
The subject ran under Codex CLI against filesystem fixtures; it does not prove
runtime behavior in OpenCode, Claude Code, or Agents. Trust Level 1 scores are
telemetry only; the conclusion rests on manual inspection.
