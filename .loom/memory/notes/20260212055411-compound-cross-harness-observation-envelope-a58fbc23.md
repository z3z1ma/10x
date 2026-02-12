---
id: 20260212055411-compound-cross-harness-observation-envelope-a58fbc23
title: Compound cross-harness observation envelope
tags:
- compound
- hooks
scopes:
- kind: command
  raw: loom compound claude-hook
  pattern: loom compound claude-hook
visibility: shared
status: active
created_at: "2026-02-12T05:54:11Z"
updated_at: "2026-02-12T05:54:11Z"
---

Use one JSONL envelope in .loom/compound/runtime/observations.jsonl for both OpenCode and Claude adapters. Required keys: id, ts, harness, event, session_id, cwd. Optional keys: tool, tool_input_redacted, tool_output_summary, ok, exit_code, command, file_path, reason, metadata. Keep adapters thin: only log observations and trigger loom compound learn --auto --harness <opencode|claude>.

Related: [[[[20260212055411-compound-learn-252e8637|compound-learn]]]] [[[[20260212055411-observation-envelope-be33ca75|observation-envelope]]]]
