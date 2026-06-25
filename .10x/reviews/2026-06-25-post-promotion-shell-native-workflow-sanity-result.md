Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/evidence/2026-06-25-post-promotion-shell-native-workflow-sanity-result.md
Verdict: concerns

# Review: Post-Promotion Shell-Native Workflow Sanity Result

## Target

`.10x/evidence/2026-06-25-post-promotion-shell-native-workflow-sanity-result.md`

## Findings

- Pass: current preserved SCN-009 graph correctness, terminal ticket movement,
  live-reference repair, and historical-reference preservation.
- Pass: current preserved SCN-004 historical prose and fenced command output
  while repairing live references and the active evidence sentence.
- Pass: current preserved the SCN-001 mutation boundary and used the verified
  dry-run rather than the mutating planning command.
- Significant concern: current failed the SCN-009 operation-quality floor by
  using assistant-side `file_change` edits across the repeated live-reference
  file set instead of a bounded shell-native rewrite.
- Significant concern: the existing Mechanical Tool Economy text and the
  record-maintenance point-of-use text are still not salient or mandatory
  enough to overcome the model's default multi-file edit behavior.
- Minor: no-op candidate arm used the desired SCN-009 mechanics, showing the
  behavior is reachable, but it also left a stale SCN-004 evidence sentence.
  Treat this as stochastic signal, not as a promotable overlay.
- Minor: automated Trust Level 1 scores remain weak for historical-reference
  scenarios and should not drive the verdict.

## Verdict

Concerns raised.

Do not revert the Mechanical Tool Economy promotion because safety held and the
text likely improves some runs. Do create a stronger candidate that makes
bounded shell-native rewrite the default for repeated exact record/file
maintenance literals after the target file set is enumerated.

## Residual Risk

The next candidate could overcorrect into blind rewriting. It must preserve the
existing exclusions for semantic text, ambiguous references, historical prose,
fenced logs, append-only progress history, generated content, and binary files.
