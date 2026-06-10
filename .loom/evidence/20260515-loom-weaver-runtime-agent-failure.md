# Loom Weaver Runtime Agent Boundary Failure

Status: recorded
Created: 2026-05-15
Updated: 2026-05-15
Observed: 2026-05-15 08:21 UTC

## Observation

An unbiased OpenCode task invocation of `subagent_type="loom-weaver"` did not behave like the shipped Loom Weaver prompt.

Invocation used by the parent session:

```text
Task subagent_type: loom-weaver
Task prompt: Add hello world to README.
Task command: @loom-weaver add hello world to README
```

The task result reported:

```text
Added `Hello world.` to `README.md`.

Verified with `git diff --check` with no issues.
```

Immediately after the task returned, `git diff -- README.md` showed this diff:

```diff
diff --git a/README.md b/README.md
index 5ecdf64..585d981 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 # Agent Loom
 
+Hello world.
+
 The missing middle between prompt and patch.
 
 ![Loom banner](assets/banner.png)
```

The accidental README change was then removed by the parent session with a narrow patch.

## What This Shows

- Supports `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-001`: the actual invoked OpenCode `loom-weaver` task did not enforce the `.loom/`-only write boundary.
- Challenges the existing smoke confidence that checking `configureOpenCode({})` and prompt string presence is enough to prove actual runtime subagent behavior.

## What This Does Not Show

- It does not prove which layer dropped or ignored the Loom Weaver prompt.
- It does not distinguish between plugin config generation, OpenCode agent registration, task subagent lookup, permission enforcement, or an existing/stub agent definition shadowing the shipped agent.
- It does not prove behavior in Claude, Cursor, Codex, or Gemini adapters.
