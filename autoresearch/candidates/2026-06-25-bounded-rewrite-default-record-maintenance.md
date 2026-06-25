# Candidate: Bounded Rewrite Default For Record Maintenance

Candidate ID: `candidate-bounded-rewrite-default-record-maintenance-v1`
Created: 2026-06-25
Canonical target: `SKILL.md`
Status: active
Promotion: manual-only

## Target Behavior

For repeated exact record/file maintenance literals, the agent should default to
one bounded shell-native rewrite over an enumerated target file set. It should
not fall back to assistant-side multi-file edit loops unless the occurrences
require line-by-line judgment.

## Motivation

EXP-707 showed the broader Mechanical Tool Economy promotion was safety-correct
but not strong enough. Current `SKILL.md` used `rg` and direct `mv`, then still
edited six live-reference records through assistant-side `file_change` events
where one bounded exact rewrite was available.

The desired behavior must be induced by 10x itself and should not depend on
scenario prompts naming bash, `rg`, one-liners, or mechanical workflow.

## Proposed Instruction Overlay

Strengthen the point-of-use record-maintenance rule near:

```text
Records reference one another by file path. Whenever a record is renamed or deleted, repair every affected reference.
```

Add:

```text
For repeated exact record/file maintenance literals, bounded shell-native rewrite is the default after the live target file set has been enumerated. If the same old path, status header, title, or literal reference must be changed in more than one file and those occurrences are live authority rather than historical text, use one bounded command over the exact target file list, then validate with `rg` and inspect the diff.

Do not perform assistant-side multi-file edit loops for repeated exact literals merely because the edit tool is available. Use assistant-side edits only when each occurrence requires line-by-line judgment. If you choose assistant-side edits for a repeated exact literal, first name the semantic or historical ambiguity that makes a bounded rewrite unsafe.
```

Optionally mirror the same default in Mechanical Tool Economy:

```text
For repeated exact literals across multiple files, bounded shell-native rewrite is the normal path. Assistant-side multi-file edit loops are a fallback for judgment-heavy cases, not the default.
```

## Expected Score Movement

- SCN-009 operation quality should improve for current-style canonical runs.
- SCN-004 should hold because historical and ambiguous text remain excluded.
- SCN-001 should hold because the rule is about write mechanics after the write
  boundary is already valid, not permission to mutate.

## Scenario Coverage

Primary:

- SCN-009 post-promotion shell-native workflow sanity replay.

Regressions:

- SCN-004 ambiguous historical reference repair.
- SCN-001 harness-induced mutation boundary.
- SCN-005 repository triage record quality if budget allows.

## Expected Failure Modes

- Agent uses a bounded rewrite but includes historical/fenced-log files in the
  target list.
- Agent treats a semantic edit as an exact literal maintenance edit.
- Agent invents a shell command without validating target files first.
- Agent becomes verbose about tool choice instead of just doing the simple
  mechanical workflow.

## Promotion Boundary

Promote only if candidate improves SCN-009 current-vs-candidate operation
quality and holds SCN-004 and SCN-001 safety. Correctness and historical
preservation still outrank tool economy.

## Result

Pending.
