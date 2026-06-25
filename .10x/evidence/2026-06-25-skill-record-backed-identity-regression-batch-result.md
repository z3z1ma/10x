Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-skill-record-backed-identity-no-native-source-path-regression-scn012-live-micro.md, .10x/research/2026-06-25-skill-record-backed-identity-agents-regression-scn012-live-micro.md, .10x/research/2026-06-25-skill-record-backed-identity-opencode-regression-scn012-live-micro.md, .10x/research/2026-06-25-skill-record-backed-identity-claude-regression-scn012-live-micro.md, autoresearch/candidates/2026-06-25-skill-record-backed-identity.md

# Skill Record-Backed Identity Regression Batch Result

## What was observed

Ran the remaining `candidate-skill-record-backed-identity-v1` promotion gates with live Codex subject samples:

- `EXP-20260625-999-skill-record-backed-identity-no-native-source-path-regression-scn012-live-micro`
- `EXP-20260625-967-skill-record-backed-identity-agents-regression-scn012-live-micro`
- `EXP-20260625-968-skill-record-backed-identity-opencode-regression-scn012-live-micro`
- `EXP-20260625-969-skill-record-backed-identity-claude-regression-scn012-live-micro`

Raw artifact roots:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/199-skill-record-backed-identity-no-native-source-path-regression-scn012-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/203-skill-record-backed-identity-agents-regression-scn012-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/204-skill-record-backed-identity-opencode-regression-scn012-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/205-skill-record-backed-identity-claude-regression-scn012-live-micro/`

Every corrected run's `canonical_guard.json` reported `SKILL.md` and `autoresearch/program.md` unchanged during the run.

Manual inspection found:

- no-native source-path gate: candidate created `.10x/skills/ledger-import-fixture-replay/SKILL.md` in both repetitions, created no native mirrors, and made no implementation edits;
- `.agents` gate: candidate created `.10x/skills/ledger-import-fixture-replay/SKILL.md` and byte-equivalent `.agents/skills/ledger-import-fixture-replay/SKILL.md`;
- `.opencode` gate: candidate created `.10x/skills/ledger-import-fixture-replay/SKILL.md` and byte-equivalent `.opencode/skills/ledger-import-fixture-replay/SKILL.md`;
- `.claude` gate: candidate created `.10x/skills/ledger-import-fixture-replay/SKILL.md` and byte-equivalent `.claude/skills/ledger-import-fixture-replay/SKILL.md`;
- `rg` found no forbidden generated-skill references to `.10x/tickets`, `.10x/evidence`, `.10x/reviews`, `.10x/specs`, `.10x/research`, or `.10x/decisions`;
- candidate generated no speculative native mirrors beyond the existing native directory for each mirror seed;
- candidate made no implementation file edits.

Automated Trust Level 1 telemetry:

| Gate | Candidate S002 | Candidate S006 | Current S002 | Current S006 | Control S002 | Control S006 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| no-native | 100 | 65 | 100 | 55 | 30 | 20 |
| `.agents` | 85 | 85 | 100 | 85 | 80 | 30 |
| `.opencode` | 85 | 85 | 100 | 85 | 80 | 20 |
| `.claude` | 85 | 85 | 100 | 85 | 80 | 20 |

## Procedure

Inspected:

- `report.md` and `canonical_guard.json` for all four corrected output roots;
- raw artifact arm and rep mappings;
- generated source and harness-native skill paths;
- candidate source/mirror byte equivalence with `cmp`;
- generated skill bodies for forbidden non-knowledge `.10x` record references;
- workspace manifests and changed paths.

Three first attempts used four-digit experiment IDs (`1000`-`1002`) and failed scorer validation before manual inspection. The corrected runs used legal three-digit IDs (`967`-`969`) and fresh output roots (`203`-`205`).

## What this supports or challenges

This supports promoting a narrow record-backed skill identity rule into canonical `SKILL.md`. Combined with EXP-997's primary identity win and EXP-998's weak-request regression, the candidate improved a real source skill identity failure and cleared no-native plus `.agents`, `.opencode`, and `.claude` mirror regressions.

This does not establish broader closure lifecycle improvement. EXP-998 still showed done-status ticket path movement as a separate residual concern.

## Limits

The mirror gates used one repetition per arm, matching prior mirror regression practice. They are live Codex subject evidence with Trust Level 1 offline scoring and manual inspection. They do not cover stale or superseded skill identity conflicts.
