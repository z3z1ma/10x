# Appendix E — Harness Invocation Templates

## Purpose

Harness invocation templates explain how the parent turns a compiled packet into a fresh child run.

The key idea is that the packet is the main local contract. The command and prompt are the launch mechanism.

## General Rule

Packet-consuming skills document direct harness CLI command shapes. The parent context compiles the packet and invokes the harness directly.

## OpenCode / OpenAI Harness Shape

```bash
opencode run -f <packet-path> -- <prompt>
```

The `--` separator matters because it cleanly separates attached file arguments from the freeform prompt string.

## What A Good Invocation Doc Should Cover

For each packet-consuming subsystem, document:

- command shape
- required packet path form
- prompt shape
- expected output shape
- continue/stop/escalate conventions
- retry/failure guidance
- parent-side reconciliation expectations

## Parent Responsibilities Before Launch

Before launching a child run, the parent should:

1. ensure packet freshness
2. ensure skill selection is correct
3. ensure scope is explicit
4. ensure the write set is explicit when execution authority exists
5. know how the child result will be reconciled afterward

## Parent Responsibilities After Return

After the child returns, the parent should:

1. inspect the returned outcome
2. confirm the child stayed within scope
3. validate affected records when needed
4. update tickets or other canonical records truthfully
5. record or link verification evidence

## Prompt Design Guidance

Good prompts for packet-consuming work should be short and positive.

They should name:

- the subsystem
- the target
- the kind of work to perform
- the output contract the child must satisfy

The prompt should not try to restate the entire protocol if the packet already contains that context.
