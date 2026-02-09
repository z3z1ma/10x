---
name: python-cli-unified-diff
description: Procedure for generating stable unified diff output in Python CLIs (human-friendly + testable).
license: MIT
compatibility: opencode,claude
metadata:
  created_at: "2026-02-09T19:02:04.864649Z"
  source_episode_ids: "6b4f92dcfe0b292c1545e85c5c8d5eb0751c41108b80b557a74a4c6539245fd9"
  source_instinct_ids: "cli-unified-diff-output,diff-output-stable-and-testable"
  tags: "cli,diff,python,testing"
  updated_at: "2026-02-09T19:02:04.864649Z"
  version: "1"
---
<!-- BEGIN:compound:skill-managed -->
# Python CLI Unified Diff

Produce a stable, readable unified diff between two text values for CLI output.

## When to use
- You want to show the user what would change (preview/dry-run) or what did change.
- You need output that is stable enough for regression tests.

## Procedure
1. Collect `before_text` and `after_text` as `str`.
2. Choose stable labels (`from_label`, `to_label`) that are meaningful in output (e.g. `"current"`/`"proposed"`, or file paths).
3. Split into lines with preserved line endings.
4. Generate unified diff with explicit `n` context and `lineterm=""`.
5. If diff is empty, print a single short line (or print nothing), and return a success exit code.

## Reference implementation
```python
from __future__ import annotations

import difflib
from typing import Iterable


def unified_diff_text(
    before_text: str,
    after_text: str,
    *,
    from_label: str = "before",
    to_label: str = "after",
    context: int = 3,
) -> str:
    before_lines = before_text.splitlines(keepends=True)
    after_lines = after_text.splitlines(keepends=True)

    diff: Iterable[str] = difflib.unified_diff(
        before_lines,
        after_lines,
        fromfile=from_label,
        tofile=to_label,
        n=context,
        lineterm="",
    )

    out = "\n".join(diff)
    # Normalize: if we printed any diff, ensure it ends with a newline for CLI friendliness.
    if out and not out.endswith("\n"):
        out += "\n"
    return out
```

## Notes
- Prefer stable labels over absolute temp paths.
- Keep the diff generation function pure; do printing/exit-code logic outside so it’s easy to test.
- If you add color, gate it behind TTY detection or an explicit `--color` flag so tests and pipes stay clean.
<!-- END:compound:skill-managed -->

## Manual notes

_This section is preserved when the skill is updated. Put human notes, caveats, and exceptions here._
