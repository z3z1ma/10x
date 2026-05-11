---
id: evidence:query-recipe-validation
kind: evidence
status: recorded
created_at: 2026-05-03T05:54:48Z
updated_at: 2026-05-03T06:01:35Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:queryrc9
  packet:
    - packet:ralph-ticket-queryrc9-20260503T055023Z
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
external_refs: {}
---

# Summary

Observed the Markdown-native query recipe consolidation for `ticket:queryrc9`,
including recipe coverage, ordinary-tool/discovery-only boundaries, owner-truth
guardrails, forbidden-surface wording, and `git diff --check`.

# Procedure

Observed at: 2026-05-03T05:54:48Z

Source state: working tree on `main` based on commit
`477b6fe7b77dc0752daef13e1b78c7319a8eb115`, after Ralph child output and packet
reconciliation and before mandatory critique.

Procedure:

- Ran targeted `rg` checks over records query guidance, records skill discovery,
  and bootstrap filesystem/tooling guidance.
- Added the new Ralph packet to the index with intent-to-add and ran
  `git diff --check` so the check covered new packet content and tracked edits.

Procedure verdict / exit code: pass; targeted searches returned expected query
recipe, boundary, and owner-truth wording, and `git diff --check` returned no
output.

# Artifacts

## Query Recipe Section Coverage

Command:

```bash
rg -n 'Cold-start orientation|List active/open tickets|Find pending or stale compiled packets|Trace a claim through tickets, packets, evidence, and critique|Find open critique findings|Find stale or superseded records|Find unreplaced placeholders' "skills/loom-records/references/query-and-linking.md"
```

Output:

```text
18:### Cold-start orientation
74:### List active/open tickets
85:### Find pending or stale compiled packets
99:### Find stale or superseded records
122:### Trace a claim through tickets, packets, evidence, and critique
153:### Find open critique findings
163:### Find unreplaced placeholders
```

## Ordinary Tool And Discovery-Only Boundary

Command:

```bash
rg -n 'discovery.*orientation|mandatory runtime|generated index|schema validator|proof by themselves|ordinary-tool|runtime dependencies|validation proof|generated index or separate reconciliation ledger' "skills/loom-records/references/query-and-linking.md" "skills/loom-records/SKILL.md" "skills/loom-bootstrap/references/06-filesystem-and-tooling.md"
```

Output:

```text
skills/loom-records/references/query-and-linking.md:5:The recipes below are examples for discovery and orientation. They are not a
skills/loom-records/references/query-and-linking.md:6:mandatory runtime, generated index, schema validator, or proof by themselves.
skills/loom-records/references/query-and-linking.md:44:not a schema validator. Read `naming-and-ids.md` and the owning template before
skills/loom-records/references/query-and-linking.md:96:according to `status-lifecycle.md`; do not create a generated index or separate
skills/loom-records/references/query-and-linking.md:203:Use these as discovery queries, not proof by themselves. Read the owning record
skills/loom-records/SKILL.md:21:- how to use ordinary-tool graph queries for tickets, packets, claims, evidence,
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:50:For a larger catalog of ordinary-tool recipes for tickets, packets, claims,
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:53:discovery aids, not mandatory runtime dependencies or validation proof by
```

## Recipe Command Examples

Command:

```bash
rg -n 'rg -n|rg -l|find .*\.loom|claim=' "skills/loom-records/references/query-and-linking.md"
```

Output excerpt:

```text
15:rg -n '^id:' .loom
21:rg -n '^id:|^kind:|^status:|^target:|^links:' .loom/constitution .loom/initiatives .loom/plans .loom/tickets .loom/packets 2>/dev/null
22:find .loom/tickets .loom/packets .loom/critique .loom/evidence -type f -name '*.md' 2>/dev/null | sort
77:rg -n '^id: ticket:|^status: (proposed|ready|active|blocked|review_required|complete_pending_acceptance)$|^updated_at:|^links:' .loom/tickets
78:rg -l '^status: (proposed|ready|active|blocked|review_required|complete_pending_acceptance)$' .loom/tickets
88:rg -l '^status: compiled$' .loom/packets
89:rg -n '^id: packet:|^target:|^updated_at:|^  (git_commit|integration_ref|integration_commit|git_status_summary):|^child_write_scope:|^parent_merge_scope:' .loom/packets
102:rg -n '^status: (stale|superseded|abandoned)$|^supersedes:|superseded by|replaced by' .loom
125:claim='spec:<slug>#ACC-002'
126:rg -n "$claim" .loom/specs .loom/tickets .loom/packets .loom/evidence .loom/critique .loom/wiki 2>/dev/null
127:rg -n '^# Supports Claims|^Supports:|^Challenges:|^Evidence:|^Critique:' .loom/tickets .loom/evidence .loom/critique 2>/dev/null
156:rg -n '^id: critique:|^status:|^target:|^verdict:|^severity:|^confidence:|^disposition:|\b(open|unresolved|requires_follow_up|needs_follow_up|blocked)\b' .loom/critique
166:rg -n '<(TBD|TODO|token|slug|YYYYMMDD|UTC timestamp|path|id)>|\b(TBD|TODO|FIXME|XXX)\b' .loom skills
167:rg -n '<[^>]*(slug|token|id|path|timestamp|summary|description)[^>]*>' .loom skills
```

## Owner-Truth Boundary Wording

Command:

```bash
rg -n 'Evidence and critique can support or challenge claims|do not redefine the acceptance contract|critique record owns findings|ticket owns whether each relevant finding blocks acceptance|Read the ticket before|read the owning record' "skills/loom-records/references/query-and-linking.md"
```

Output:

```text
7:After a query finds something relevant, read the owning record before changing
81:These statuses are the non-terminal ticket ledger states. Read the ticket before
132:challenge claims; they do not redefine the acceptance contract owned by specs or
```

## Forbidden Surface Boundary Wording

Command:

```bash
rg -n 'dashboard|MCP|command wrapper|schema validator|generated index|new owner layer|mandatory runtime' "skills/loom-records/references/query-and-linking.md" "skills/loom-records/SKILL.md" "skills/loom-bootstrap/references/06-filesystem-and-tooling.md"
```

Output:

```text
skills/loom-records/references/query-and-linking.md:6:mandatory runtime, generated index, schema validator, or proof by themselves.
skills/loom-records/references/query-and-linking.md:44:not a schema validator. Read `naming-and-ids.md` and the owning template before
skills/loom-records/references/query-and-linking.md:96:according to `status-lifecycle.md`; do not create a generated index or separate
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:53:discovery aids, not mandatory runtime dependencies or validation proof by
```

Observed result: matches are prohibition/boundary wording and not new runtime,
dashboard, MCP, command-wrapper, schema-validator, generated-index, or owner-layer
surface creation.

## Diff Whitespace Check

Command:

```bash
git add -N ".loom/packets/ralph/20260503T055023Z-ticket-queryrc9-iter-01.md" && git diff --check
```

Output:

```text
```

Exit status: pass; no whitespace errors were reported.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009`
- `ticket:queryrc9#ACC-001`
- `ticket:queryrc9#ACC-002`
- `ticket:queryrc9#ACC-003`
- `ticket:queryrc9#ACC-004`

# Challenges Claims

None - no challenged claims were observed.

# Environment

Commit: `477b6fe7b77dc0752daef13e1b78c7319a8eb115` plus uncommitted
ticket-scoped working-tree changes

Branch: `main`

Runtime: none; Markdown corpus only

OS: macOS / Darwin

Relevant config: no app runtime or automated test suite

# Validity

Valid for: the listed files observed at 2026-05-03T05:54:48Z.

Fresh enough for: mandatory critique and ticket acceptance review for
`ticket:queryrc9`.

Recheck when: records query guidance, bootstrap filesystem/tooling guidance,
ticket criteria, or critique findings change before closure.

Invalidated by: later edits that remove query recipe coverage, make query output
proof by itself, make recipes mandatory runtime dependencies, or introduce a
generated index, dashboard, MCP dependency, schema validator, command wrapper, or
new owner layer.

Supersedes / superseded by: None.

# Limitations

This evidence verifies structural Markdown guidance and targeted wording only. It
does not prove every recipe is exhaustive or that every future operator will use
the recipes correctly.

# Result

The observed query recipe changes are Markdown-only, ordinary-tool oriented, and
stay within the declared write scope.

# Repair Check After Initial Critique

Observed at: 2026-05-03T06:01:35Z

Context: after `critique:query-recipe-review` found the cold-start recipe
under-mapped research/spec owners and typed link targets, the query recipe was
expanded and structural checks were rerun.

Cold-start repair command:

```bash
rg -n 'loom/research|loom/specs|typed link targets|initiative / research / spec / plan / ticket|\^    - \(constitution\|decision\|roadmap\|initiative\|research\|spec' "skills/loom-records/references/query-and-linking.md"
```

Output:

```text
21:rg -n '^id:|^kind:|^status:|^target:|^links:|^  [a-z_]+:|^    - (constitution|decision|roadmap|initiative|research|spec|plan|ticket|packet|critique|wiki|evidence|workspace|support):' .loom/constitution .loom/initiatives .loom/research .loom/specs .loom/plans .loom/tickets .loom/packets .loom/critique .loom/evidence .loom/wiki 2>/dev/null
22:find .loom/initiatives .loom/research .loom/specs .loom/plans .loom/tickets .loom/packets .loom/critique .loom/evidence .loom/wiki -type f -name '*.md' 2>/dev/null | sort
26:research/spec owners and typed link targets. It does not replace reading the
27:constitution, governing initiative / research / spec / plan / ticket chain,
127:rg -n "$claim" .loom/specs .loom/tickets .loom/packets .loom/evidence .loom/critique .loom/wiki 2>/dev/null
201:rg -n 'promoted to|promotion|promote' .loom/memory .loom/wiki .loom/research .loom/tickets
```

Section coverage recheck command:

```bash
rg -n 'Cold-start orientation|List active/open tickets|Find pending or stale compiled packets|Trace a claim through tickets, packets, evidence, and critique|Find open critique findings|Find stale or superseded records|Find unreplaced placeholders' "skills/loom-records/references/query-and-linking.md"
```

Output:

```text
18:### Cold-start orientation
75:### List active/open tickets
86:### Find pending or stale compiled packets
100:### Find stale or superseded records
123:### Trace a claim through tickets, packets, evidence, and critique
154:### Find open critique findings
164:### Find unreplaced placeholders
```

Runtime boundary recheck command:

```bash
rg -n 'mandatory runtime|generated index|schema validator|proof by themselves|ordinary-tool|runtime dependencies|validation proof|generated index or separate reconciliation ledger' "skills/loom-records/references/query-and-linking.md" "skills/loom-records/SKILL.md" "skills/loom-bootstrap/references/06-filesystem-and-tooling.md"
```

Output:

```text
skills/loom-records/SKILL.md:21:- how to use ordinary-tool graph queries for tickets, packets, claims, evidence,
skills/loom-records/references/query-and-linking.md:6:mandatory runtime, generated index, schema validator, or proof by themselves.
skills/loom-records/references/query-and-linking.md:45:not a schema validator. Read `naming-and-ids.md` and the owning template before
skills/loom-records/references/query-and-linking.md:97:according to `status-lifecycle.md`; do not create a generated index or separate
skills/loom-records/references/query-and-linking.md:204:Use these as discovery queries, not proof by themselves. Read the owning record
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:50:For a larger catalog of ordinary-tool recipes for tickets, packets, claims,
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:53:discovery aids, not mandatory runtime dependencies or validation proof by
```

Full diff whitespace recheck command:

```bash
git add -N ".loom/packets/ralph/20260503T055023Z-ticket-queryrc9-iter-01.md" ".loom/evidence/20260503-query-recipe-validation.md" ".loom/critique/query-recipe-review.md" && git diff --check
```

Output:

```text
```

Exit status: pass; no whitespace errors were reported after the repair.

# Interpretation

The observations support the ticket's structural claims, pending mandatory
critique re-review.

# Related Records

- `ticket:queryrc9`
- `packet:ralph-ticket-queryrc9-20260503T055023Z`
- `initiative:skills-corpus-context-integrity-hardening-pass`
