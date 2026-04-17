---
id: packet:ralph-<target>-<UTC compact timestamp>
kind: packet
packet_kind: ralph
status: compiled
target: ticket:<token>
mode: execution
style: reference-first
iteration: 1
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
write_scope:
  records:
    - ticket:<token>
  paths: []
sources:
  constitution:
    - constitution:main
  initiative: []
  research: []
  spec: []
  plan: []
  ticket:
    - ticket:<token>
links: {}
---

# Mission

What this iteration is meant to achieve.

# Bound Context

What larger chain constrains the work.

# Source Snapshot

Curated excerpts, summaries, or directions to the important source records.

# Task For This Iteration

The exact bounded task for the child.

# Stop Conditions

When the child should stop, block, or escalate instead of widening scope.

# Output Contract

The child must return:
- outcome (`continue|stop|blocked|escalate`)
- files changed
- records changed
- evidence gathered
- blockers or risks
- ticket recommendation

# Working Notes

Optional parent notes before launch.

# Child Output

To be filled by the child or copied back by the parent.

# Parent Merge Notes

What the parent concluded after reconciliation.
