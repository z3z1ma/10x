# Workspace Doctor Reference

## Purpose

Doctor is the parent agent's structural readiness check.

Use this reference when the next question is whether the workspace is healthy enough to trust for further work.

## What A Workspace Health Check Should Report

A good workspace health check should make the current trust state legible by checking:

- Loom bundle presence such as `.opencode/rules/` and `.opencode/skills/`
- source-tree `rules/` and `skills/` only when the workspace is the Loom source repository
- `.loom` canonical tree presence
- scope discovery
- record validation health
- packet readiness

Workspace root discovery should stay simple:

- search upward for a directory containing both `.git/` and `.loom/`
- if no established workspace exists, allow the current working directory as the workspace root unless it is a non-root subdirectory of a git repository

The point is to help the parent answer one practical question: is the workspace trustworthy enough for the next durable step?

## Inputs A Good Health Check Uses

A strong health check usually inspects:

- required rule and skill directories
- canonical `.loom/` subtrees
- record parse and validation health
- link integrity
- repository discovery and scope resolution readiness
- helper or assembly surfaces when the workflow depends on them

## How To Interpret A Health Report

Treat doctor output as a routing decision, not just a report.

- if doctor is healthy, continue with the owning subsystem workflow
- if doctor reports missing structure, repair that structure first
- if doctor reports validation or link issues, fix those before trusting packetized work
- if doctor reports scope problems, resolve scope before continuing

Healthy output should change behavior. If the workspace is unhealthy, do not proceed as though the report were informational only.

Health output should trigger a decision, not admiration. Use it when you actually intend to change, launch, or trust something important.

## Good Use Pattern

Run a workspace health check:

1. when entering the repo fresh
2. before a significant build or packet run
3. after broad structural changes
4. after assembling skills

## Strong Workspace Health Output Characteristics

A useful doctor report should be:

- explicit about what is healthy
- explicit about what is missing
- explicit about what blocks downstream trust
- short enough to route action quickly

It should also distinguish:

- missing structure versus malformed structure
- link problems versus scope problems
- warnings that can wait versus failures that must block downstream work

## Worked Example

Parent question:

```text
I am about to launch a fresh packet-consuming child run. Can I trust the workspace enough to do that, or is there unresolved structural debt first?
```

Good interpretation:

- if the workspace is healthy, proceed to the owning subsystem
- if the report shows validation or link failures, fix those before launch
- if ownership or scope is unclear, stop before packet work and resolve scope first

## Anti-Pattern

This is a bad parent reaction:

```text
The health report mentions broken links, but the task is probably unrelated, so I will continue with packet work anyway.
```

Why this is bad:

- structural trust is a precondition, not a decorative metric
- packet work becomes less trustworthy when the surrounding record graph is already inconsistent
