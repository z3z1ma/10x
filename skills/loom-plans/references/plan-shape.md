# Plan Shape

## Core sections

- Purpose
- Strategy
- Strategy Snapshot
- Workstreams
- Milestones
- Sequencing
- Execution Waves
- Risks
- Evidence Strategy
- Exit Criteria
- Completion Basis when `status: completed`

## Notes

`Strategy Snapshot` in a plan is not the same as ticket execution truth.

Use it for the current strategic picture, not line-by-line implementation
journal entries.

Plan milestones are execution-sequencing checkpoints. They are not roadmap
commitments, initiative outcome metrics, or ticket progress state.

## Good linking

Plans usually link to:

- initiative
- research
- spec
- tickets
- critique when review changes the route

## Execution Waves

Use `# Execution Waves` when a plan contains tickets that may be run in
parallel or must be staged.

Parallel work is allowed only when:

- ticket `depends_on` relationships do not conflict
- expected packet `child_write_scope` values do not overlap
- there is no shared generated file, migration, lockfile, or stateful resource
  contention

The plan names the wave. Each ticket and packet still owns its own execution
truth.
