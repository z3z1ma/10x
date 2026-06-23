Status: recorded
Created: 2026-06-23
Updated: 2026-06-23
Target: autoresearch/run_codex_subject.py, autoresearch/tests/test_run_codex_subject.py
Verdict: pass

# No-10x Control Record Graph Isolation Review

## Target

Diff that removes inherited `.10x` from `no-10x-control` private execution
workspaces and adds a regression test.

## Findings

- Pass: Cleanup is scoped to `variant_id == "no-10x-control"`, so current and
  candidate continuation/retrieval scenarios still receive their prior record
  graph.
- Pass: Cleanup occurs before `subprocess.run()`, so the control cannot read
  inherited `.10x` during execution.
- Pass: Cleanup does not run after execution. The regression confirms a
  control-created `.10x/knowledge/control-created.md` remains in
  `post_run_files`.
- Pass: Manifest, command, and raw harness metadata include
  `pre_run_removed_control_record_dirs`, making cleanup auditable.
- Minor residual risk: The runner still relies on explicit prompt-injected
  instructions and Codex CLI flags for broader control isolation. System-level
  Codex context and authenticated home state remain outside this runner's
  control, as already recorded in `control_isolation.limitation`.

## Verdict

Pass.

## Residual Risk

This fix addresses inherited `.10x` contamination only. It does not make the
no-10x control an epistemically pure non-10x agent because the local Codex
system context cannot be fully controlled by this runner.
