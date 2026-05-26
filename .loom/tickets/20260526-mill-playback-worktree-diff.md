# Playback Working-Tree Diff Detection

ID: ticket:20260526-mill-playback-worktree-diff
Type: Ticket
Status: closed
Created: 2026-05-26
Updated: 2026-05-26
Risk: medium - changes iteration boundary logic that's core to workstation data; must handle both committed and uncommitted changes without double-counting

## Summary

Playback shows "No changes" (Files: 0, Lines: +0 -0) after a workstation run that
clearly modified files. The operator saw the subprocess run for 3m 2s with exit 0,
but iteration 1 shows an empty diff.

Root cause: `engine.py:_record_iteration_boundary()` computes diffs using
`git diff {previous_sha}..{head}` which is a commit-to-commit comparison. Many
harness subprocesses (opencode, codex, claude-code) modify working-tree files
without creating explicit git commits. The worktree has changes, but since no new
commit was created, `previous_sha == head` and the diff is empty.

The fix: When recording an iteration boundary, also detect uncommitted changes
(staged + unstaged) in the worktree and include them in the iteration diff. The
logic should:
1. First check for committed changes between `previous_sha` and current `HEAD`
2. Then check for uncommitted working-tree changes (`git diff HEAD` + `git diff --cached`)
3. Combine both into the iteration's diff
4. If the subprocess committed, use commit-to-commit diff (current behavior)
5. If the subprocess left uncommitted changes, capture the working-tree diff
6. Auto-commit uncommitted changes after recording, so subsequent iterations start clean

Closure claim: Playback correctly shows all file changes made during a workstation
run, whether committed or left as working-tree modifications.

## Related Records

- `plan:20260526-mill-factory-data-integrity` - parent plan
- `loom-mill/src/loom_mill/workstation/engine.py:260-293` - `_record_iteration_boundary()`
- `loom-mill/src/loom_mill/workstation/engine.py:295-298` - `_diff()` (commit-to-commit only)
- `loom-mill/src/loom_mill/workstation/engine.py:300-314` - `_diff_numstat()`
- `loom-mill/src/loom_mill/workstation/engine.py:243-251` - `_poll_commits()` (only detects HEAD changes)
- `loom-mill/src/loom_mill/iterations/store.py` - iteration persistence
- `loom-mill/frontend/src/lib/Playback.svelte` - consumes diffs
- `evidence:20260526-mill-playback-worktree-diff-validation` - validation observations

## Scope

Write:
- `loom-mill/src/loom_mill/workstation/engine.py`:
  - Modify `_record_iteration_boundary()` to detect uncommitted changes
  - Modify `_diff()` to include working-tree diff when no commits detected
  - Modify `_diff_numstat()` to include working-tree numstat
  - Add auto-commit of uncommitted changes after iteration recording
  - Add `_working_tree_diff()` helper
  - Add `_working_tree_numstat()` helper

Read:
- `loom-mill/src/loom_mill/iterations/store.py` - understand diff storage format
- `loom-mill/frontend/src/lib/Playback.svelte` - understand how diffs are consumed (text/plain)
- `loom-mill/frontend/src/lib/DiffViewer.svelte` - understand unified diff parsing

Non-goals:
- Do NOT change the playback frontend UI (that's working correctly with valid diff data)
- Do NOT change the iteration storage format
- Do NOT change commit-poll behavior for real commits (that still works fine)
- Do NOT track individual file saves within an iteration (too granular)
- Do NOT auto-commit partial work mid-iteration (only at iteration boundary)

### Detailed Design

**Detection logic in `_record_iteration_boundary()`:**

```python
async def _record_iteration_boundary(self, exit_code, *, new_sha=None):
    # ... existing lock and validation ...
    
    previous_sha = self._iteration_base_sha
    head = new_sha or (await self._git_output(worktree, "rev-parse", "HEAD")).strip()
    
    # Check for committed changes (existing behavior)
    committed_diff = ""
    if previous_sha and previous_sha != head:
        committed_diff = await self._git_output(worktree, "diff", f"{previous_sha}..{head}")
    
    # Check for uncommitted changes (NEW)
    working_diff = await self._working_tree_diff(worktree)
    
    # Combine: committed changes + uncommitted changes
    combined_diff = committed_diff
    if working_diff:
        if combined_diff:
            combined_diff += "\n" + working_diff
        else:
            combined_diff = working_diff
    
    # Compute numstat from combined sources
    files_changed, lines_added, lines_removed = await self._combined_numstat(
        previous_sha, head, worktree
    )
    
    # Auto-commit uncommitted changes so next iteration starts clean
    if working_diff:
        await self._auto_commit_working_changes(worktree, iteration_num)
        head = (await self._git_output(worktree, "rev-parse", "HEAD")).strip()
    
    record = IterationRecord(...)
    # ... rest of existing logic with combined_diff instead of diff ...
```

**New helper methods:**

```python
async def _working_tree_diff(self, worktree: Path) -> str:
    """Get diff of all uncommitted changes (staged + unstaged)."""
    # This gets both staged and unstaged changes vs HEAD
    try:
        return await self._git_output(worktree, "diff", "HEAD")
    except RuntimeError:
        return ""

async def _working_tree_numstat(self, worktree: Path) -> tuple[list[str], int, int]:
    """Get numstat for uncommitted changes."""
    try:
        output = await self._git_output(worktree, "diff", "--numstat", "HEAD")
    except RuntimeError:
        return [], 0, 0
    # ... parse same as _diff_numstat ...

async def _auto_commit_working_changes(self, worktree: Path, iteration: int) -> None:
    """Auto-commit all working changes with a mill-generated message."""
    await self._git_output(worktree, "add", "-A")
    await self._git_output(
        worktree, "commit", "-m", f"[mill] iteration {iteration} working changes",
        "--allow-empty-message"
    )
```

**Edge cases:**
- If subprocess committed AND left uncommitted changes: include both in same iteration
- If subprocess only committed: behave exactly as before (no regression)
- If subprocess only left uncommitted changes: capture working-tree diff, auto-commit
- If subprocess did nothing: empty diff, no commit needed
- If git operations fail (detached HEAD, corrupt worktree): log warning, produce empty diff

## Acceptance

- ACC-001: After a workstation run where the subprocess modifies files without
  committing, Playback shows the correct file changes.
  - Evidence: Run a workstation with a harness that modifies files without git commit.
    Verify Playback shows the diff with correct file count and line counts.
  - Audit: Verify diff content matches actual file modifications.

- ACC-002: After a workstation run where the subprocess creates proper commits,
  Playback still works correctly (no regression).
  - Evidence: Run a workstation with a harness that commits. Verify Playback shows commit diff.
  - Audit: Verify existing commit-based path is preserved.

- ACC-003: Uncommitted changes are auto-committed at iteration boundary so
  subsequent iterations start with a clean base.
  - Evidence: Check git log in worktree after iteration completes.
  - Audit: Verify auto-commit message format and that next iteration base SHA is updated.

- ACC-004: Backend tests pass (`pytest loom-mill/tests/`).
  - Evidence: Test output.

- ACC-005: No data loss - if both committed and uncommitted changes exist, both
  appear in the iteration diff without double-counting.
  - Evidence: Create scenario with both types; verify combined diff is correct.
  - Audit: Verify numstat addition doesn't double-count committed files.

## Current State

Implementation complete and awaiting review/audit. `engine.py` now records committed
diffs plus staged working-tree snapshots at iteration boundaries, auto-commits the
captured working-tree snapshot with `[mill] iteration {N} auto-commit`, and updates
the next iteration base SHA to that auto-commit. Focused tests cover committed,
uncommitted, no-op, and mixed commit-plus-worktree paths. Frontend playback remains
out of scope.

## Journal

- 2026-05-26: Created ticket. Source: operator observed "Files: 0, Lines: +0 -0"
  in Playback after workstation that clearly modified files. Triage confirmed the
  subprocess left working-tree changes without git commits.
- 2026-05-26: Started bounded implementation run in current session. Read ticket,
  parent plan, engine, iteration store, Playback, and DiffViewer before editing.
- 2026-05-26: Implemented backend iteration boundary fix and focused tests. Evidence
  recorded in `evidence:20260526-mill-playback-worktree-diff-validation`. Ticket
  moved to `review` pending audit/acceptance judgment.
