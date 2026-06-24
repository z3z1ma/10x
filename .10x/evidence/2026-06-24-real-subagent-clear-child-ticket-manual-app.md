Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-real-subagent-clear-child-ticket-manual-app.md

# Real Subagent Clear Child Ticket Manual App Harness Evidence

## What Was Observed

Ran `EXP-20260624-926-real-subagent-clear-child-ticket-manual-app` as a manual
Codex app-harness MICRO using an actual `multi_agent_v1` child agent.

Tool-level delegation:

- attempted to spawn a new subagent, but the thread limit was reached;
- reused existing completed agent `019efb4a-5f92-7c22-bd04-fcb217db5d21`;
- submitted the child ticket task with submission
  `019efbec-e0ea-75a2-a658-2d15035b16b8`;
- `wait_agent` returned a completed child result.

Child-reported changed files:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/126-real-subagent-clear-child-ticket-manual-app/subject/src/statusLabel.js`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/126-real-subagent-clear-child-ticket-manual-app/subject/src/statusLabel.test.js`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/126-real-subagent-clear-child-ticket-manual-app/subject/.10x/tickets/2026-06-24-add-paused-status-label.md`

Child-reported command:

- `npm test` in the subject workspace: passed, 2 tests, 0 failures.

Parent verification found:

- `src/statusLabel.js` now includes `paused: "Paused"`;
- `src/statusLabel.test.js` asserts `formatStatus("paused") === "Paused"` and
  preserves existing/unknown status assertions;
- the child ticket progress log records the implementation and test result;
- the subject workspace file list contains only the expected source, test,
  spec, ticket, package, and manifest files;
- parent reran `npm test` in the subject workspace and observed:

```text
> test
> node --test src/statusLabel.test.js

✔ formats existing account statuses (0.869959ms)
✔ returns Unknown for unsupported statuses (0.069375ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 399.04375
```

After parent verification, the parent moved the subject child and parent tickets
to `.10x/tickets/done/`, marked them `Status: done`, and recorded verification
notes in both records.

Canonical `git status --short` was clean after child execution because the
subject workspace lives under ignored evidence storage. No canonical source,
test, `SKILL.md`, or `autoresearch/program.md` file was changed by the child.

Subject artifact root:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/126-real-subagent-clear-child-ticket-manual-app/`

## Procedure

1. Created a subject workspace under ignored evidence storage with a parent
   ticket, executable child ticket, active spec, source helper, tests, and
   `package.json`.
2. Registered the experiment in commit `862e66e4`.
3. Delegated the child ticket to real `multi_agent_v1` agent
   `019efb4a-5f92-7c22-bd04-fcb217db5d21`.
4. Waited for the child completion result.
5. Independently inspected source, tests, child ticket progress notes, and the
   subject file list.
6. Reran `npm test` in the subject workspace.
7. Moved subject parent/child tickets to done and recorded closure notes after
   verification.

## What This Supports Or Challenges

Supports marking real subagent clear-child execution as partially covered by
manual app-harness evidence. Current 10x behavior successfully kept parent and
child roles separate, delegated the executable child ticket, verified artifacts
instead of trusting the child final message alone, and closed only after
evidence coherence.

Challenges the conformance map's earlier "real subagent untested" status for
the clear-child positive path.

## Limits

This is not a repeatable `run_once.py` fixture and has no no-10x control arm.

The child was an existing completed agent reused because the app thread limit
prevented spawning a fresh subagent. That means it is real tool-level delegation
but not a fully clean cold-start child.

This run covers the positive clear-child path only. It does not cover real
subagent ambiguity gating, child blocker propagation, out-of-scope discovery,
weak child artifacts, or true parallel child execution.
