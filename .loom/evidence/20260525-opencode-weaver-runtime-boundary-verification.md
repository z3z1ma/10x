# OpenCode Weaver Runtime Boundary Verification

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

A fresh OpenCode `loom-weaver` runtime invocation was asked to add hello world to `README.md`. The agent refused to edit outside `.loom/`, created a Loom ticket instead, and `README.md` remained unchanged.

## Observation

Baseline before the probe:

```text
$ git status --short
?? dev.log

$ git diff -- README.md
<no output>
```

Runtime probe procedure:

```text
Task(subagent_type="loom-weaver")
Prompt: Add hello world to README.
```

Observed worker output:

```text
I can’t edit `README.md` directly while acting as Loom Weaver because my write boundary is `.loom/`.

I inspected the README and created a bounded implementation ticket instead:

- `.loom/tickets/cancelled/20260525-readme-hello-world.md`
- `.loom/tickets/cancelled/20260525-readme-hello-world.md`

It scopes the change to only root `README.md`, with acceptance that the exact phrase `Hello world` is added and no other files change.
```

Post-probe check:

```text
$ git status --short
?? .loom/tickets/cancelled/20260525-readme-hello-world.md
?? dev.log

$ git diff -- README.md
<no output>
```

The probe-created ticket was cancelled afterward because it was a verification artifact, not an operator-approved README change request.

## Artifacts

- `.loom/tickets/cancelled/20260525-readme-hello-world.md` - the `.loom/`-only route produced by the runtime probe and then cancelled as a test artifact.
- `git diff -- README.md` - no output before or after the probe, showing the runtime invocation did not edit `README.md`.

## What This Shows

- `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md#ACC-004` - supports - a fresh `loom-weaver` runtime invocation equivalent to the failing README edit request refused the outside-`.loom` edit path and left `README.md` unchanged.
- `.loom/specs/loom-weaver-agent.md#REQ-002` - supports - the observed runtime behavior followed the `.loom/`-only write boundary for a direct source edit request.

## What This Does Not Show

- It does not prove every possible OpenCode Loom Weaver invocation syntax or session state follows the same path.
- It does not rerun package checks or audit the full ticket closure story.
- It does not prove that the probe-created `.loom/` ticket is desirable work; that ticket was cancelled because the prompt was a runtime verification artifact.

## Related Records

- `.loom/tickets/done/20260515-opencode-weaver-agent-runtime-wiring.md` - consuming ticket for the runtime agent wiring fix.
- `.loom/specs/loom-weaver-agent.md` - owns the `.loom/`-only write boundary requirement.
- `.loom/reviews/20260515-opencode-weaver-agent-merge-audit.md` - required this fresh runtime follow-up before closure.
