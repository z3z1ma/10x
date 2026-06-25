Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-real-subagent-authored-skill-manual-app.md

# Real Subagent Authored Skill Manual App Evidence

## What Was Observed

Ran `EXP-20260625-963-real-subagent-authored-skill-manual-app` as a manual Codex
app-harness MICRO using an actual `multi_agent_v1` worker subagent.

Subject workspace:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/209-real-subagent-authored-skill-manual-app/subject/`

Tool-level delegation:

- spawned worker subagent `019eff0a-dd61-74a1-830c-f8b278461194`;
- assigned only the subject workspace and
  `.10x/tickets/2026-06-25-author-ledger-import-fixture-replay-skill.md`;
- child completed and was closed after result recording.

Child-reported changed files:

- `.10x/skills/ledger-import-fixture-replay/SKILL.md`
- `.agents/skills/ledger-import-fixture-replay/SKILL.md`
- `.10x/tickets/2026-06-25-author-ledger-import-fixture-replay-skill.md`

Child-reported commands:

```text
cmp -s .10x/skills/ledger-import-fixture-replay/SKILL.md .agents/skills/ledger-import-fixture-replay/SKILL.md
rg -n "\.10x/(tickets|evidence|reviews|specs|research|decisions)" ...
find . -path './.claude/skills' -o -path './.opencode/skills'
git status --short -- .
```

Parent verification found:

- `.10x/skills/ledger-import-fixture-replay/SKILL.md` exists;
- `.agents/skills/ledger-import-fixture-replay/SKILL.md` exists;
- `cmp -s` between source and mirror returned exit code 0;
- skill frontmatter contains `name: ledger-import-fixture-replay`, a
  `description` beginning with `Use when`, and `metadata.created` /
  `metadata.updated`;
- skill body contains Objective, Prerequisites, Procedure, and Validation
  sections;
- searching source and mirror skill files for forbidden references to
  `.10x/tickets`, `.10x/evidence`, `.10x/reviews`, `.10x/specs`,
  `.10x/research`, and `.10x/decisions` returned no matches;
- no `.claude/skills` or `.opencode/skills` directory exists in the subject;
- the subject contains no implementation files beyond `workspace-manifest.json`;
- the child did not edit or close the parent ticket;
- parent recorded subject evidence and review;
- parent opened
  `.10x/tickets/2026-06-25-add-archive-malformed-currency-coverage.md`;
- parent moved the skill-authoring child and parent tickets to
  `.10x/tickets/done/`;
- no top-level subject ticket has `Status: done`;
- no stale live references remain to the moved parent or skill-child paths.

Canonical `git status --short` was clean after the manual app subject run
because subject mutations remained under ignored evidence storage.

## Procedure

1. Created an isolated subject workspace under ignored evidence storage.
2. Registered the manual app experiment.
3. Spawned a real worker subagent with a self-contained child prompt and strict
   subject workspace boundary.
4. Waited for child completion.
5. Independently inspected source skill, mirror skill, child ticket, parent
   ticket, subject file list, absent native roots, and forbidden references.
6. Recorded subject evidence/review and moved subject terminal tickets to done.
7. Closed the child subagent.

## What This Supports Or Challenges

Supports marking real subagent-authored skill creation as covered by manual
app-harness evidence. Current 10x behavior successfully kept parent and child
roles separate while authoring a governed skill and `.agents` exposure copy.

Challenges the remaining skill-authoring gap list: after this run, basic real
subagent skill authoring is no longer untested. Remaining risk is richer
closure/reference hygiene and forward-use validation.

## Limits

This is not a repeatable `run_once.py` fixture and has no no-10x control arm.

The run proves structural skill and mirror correctness plus parent verification.
It does not prove the generated skill will be selected and used by a separate
cold-start agent.
