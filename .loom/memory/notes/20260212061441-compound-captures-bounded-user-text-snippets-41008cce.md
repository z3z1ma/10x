---
id: 20260212061441-compound-captures-bounded-user-text-snippets-41008cce
title: Compound captures bounded user text snippets
tags:
- compound
- observations
scopes:
- kind: command
  raw: loom compound claude-hook
  pattern: loom compound claude-hook
visibility: shared
status: active
created_at: "2026-02-12T06:14:41Z"
updated_at: "2026-02-12T06:14:41Z"
---

To improve learning signal without full transcript logging, capture bounded user text snippets in observation metadata. OpenCode: message.updated events are logged only when role=user, with redacted/truncated text_excerpt and text_len. Claude: UserPromptSubmit hook logs prompt_excerpt and prompt_len. Keep the canonical envelope stable and place extra language context under metadata.

Related: [[[[20260212055411-observation-envelope-be33ca75|20260212055411-observation-envelope-be33ca75]]]]
