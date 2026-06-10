# Playbooks Versus Core Activation Pressure

Status: completed
Created: 2026-05-15
Updated: 2026-05-15

## Summary

Core's surface model is coherent: `using-loom` routes truth to the owning record
skill, then only adds workflow playbooks when the record route is too thin.
Playbooks add real value for high-risk, familiar workflows, but the current
installed behavior turns the optional playbook corpus into broad mandatory runtime
pressure. The net result is likely harmful for default agent behavior unless
activation is narrowed or made explicitly route-gated.

## Question

Do Loom Playbooks add enough value over Core record skills to justify automatic
activation alongside Core, or do they dilute Core's truth-surface model and the
operator's original intent by adding workflow pressure too early?

## Scope

Covered:

- Core `using-loom` doctrine, activation discipline, OpenCode bootstrap, and record-skill descriptions.
- Playbooks package exposure, trigger descriptions, shared routing headers, and representative playbooks.
- Dogfood records that explain why Superpowers-style activation was adopted.
- Current Core and Playbooks smoke outputs.
- Existing OpenCode activation logs cited by `.loom/evidence/20260513-superpowers-style-activation-checks.md`.
- Optional Loom Weaver and Loom Driver agent prompts as alternate ways to carry shaping and execution pressure.

Excluded:

- Running a fresh live model eval across every harness.
- Changing product surfaces in this pass.
- Deciding the exact packaging or migration design for a playbook behavior change.

## Method And Sources

- `loom-core/skills/using-loom/SKILL.md` - loaded Core loop order, surface ownership, and skill priority.
- `loom-core/skills/using-loom/references/01-activation-discipline.md` - loaded the 1% activation threshold and priority order.
- `loom-playbooks/README.md` - inspected the intended role of workflow pressure.
- `loom-playbooks/loom-playbooks.mjs` - inspected package exposure and activation-description smoke checks.
- `loom-playbooks/skills/*/SKILL.md` - inspected all descriptions and representative workflow bodies.
- `tests/skill-triggering/**` - inspected natural-prompt activation checks.
- `.loom/evidence/20260513-superpowers-style-activation-checks.md` - identified prior live OpenCode activation logs and test claims.
- `.loom/evidence/20260515-playbook-activation-stacking.md` - preserves current smoke results and key log-derived observations.
- `.loom/research/20260513-superpowers-skill-activation.md` and `.loom/tickets/done/20260513-superpowers-style-activation-doctrine.md` - inspected why stronger activation was introduced.
- `loom-core/agents/loom-weaver.md` and `loom-core/agents/loom-driver.md` - inspected Core agent surfaces that already carry shaping and execution coordination behavior.

## Findings

- Core has a clear hierarchy. `using-loom` says Loom routing comes first, record
  skills own durable truth, and playbooks come after owning record skills as
  task-shaped pressure.

- Core activation is intentionally forceful. The activation reference says that if
  there is even a 1% chance a skill applies, the agent must invoke it, and skill
  invocation comes before clarification, exploration, quick checks, edits, ticket
  creation, and Ralph launches.

- Playbooks are optional at install time but mandatory once visible. The
  playbooks package does not preload Core doctrine, but it registers 25 skills
  through `config.skills.paths`. Because Core tells agents to invoke every
  relevant Loom skill before action, optional exposure becomes runtime pressure.

- All playbooks share the same pressure shape. Every sampled playbook says common
  routes use Core skills, `using-loom` must be loaded, routed skills must be
  followed completely, and the playbook adds workflow pressure rather than
  shortening record-skill procedure.

- The trigger surface is broad enough to overlap common prompts. `loom-idea-refine`
  catches rough product, engineering, workflow, research, or opportunity ideas.
  `loom-frontend-ui-engineering` catches user-facing UI components, layouts,
  flows, state, responsive behavior, and browser evidence. `loom-source-driven-development`
  catches current source authority. `loom-security-and-hardening` catches auth,
  secrets, command execution, external integrations, and hardening review.
  `loom-incremental-implementation` catches non-trivial ticket or plan execution.

- Existing live activation logs show stacking. The `Let's make a react todo list`
  run invoked both `loom-idea-refine` and `loom-frontend-ui-engineering`. The
  `Create a ticket for the auth cleanup work and start implementing it` run
  invoked `loom-tickets`, `loom-incremental-implementation`, and
  `loom-security-and-hardening`.

- Existing activation tests reward presence, not precision. The natural-prompt
  runner passes when the expected skill appears. It does not fail on additional
  playbook invocations, route stacking, or premature workflow narrowing after the
  first correct route.

- Playbooks sometimes encode genuinely valuable domain discipline. Debugging
  preserves failure before fix. TDD preserves red/green evidence. Source-driven
  development forces version and authority checks. Security, migration,
  performance, UI runtime observation, and release work have real failure modes
  that Core's generic surface model does not fully teach.

- Several playbooks duplicate Core agents rather than only augmenting Core.
  `loom-idea-refine` overlaps Loom Weaver's shaping role. `loom-incremental-implementation`
  and `loom-parallel-worker-coordination` overlap Loom Driver's execution loop.
  In an installed workspace with Core agents and playbooks, agents can receive
  three layers of pressure: Core record routing, named-agent operating frame, and
  playbook workflow route.

- The likely failure mode is not that playbooks tell agents to ignore Core. They
  usually say the right thing. The failure mode is salience and sequencing:
  workflow-specific content becomes louder than the operator's ask and the
  owning surface. The agent starts optimizing for the named workflow's route
  rather than the smallest truthful Core move.

## Tradeoffs

- Keep all playbooks automatically active.
  - Strength: catches many risky workflows early and preserves specialized
    evidence, audit, and packet discipline.
  - Weakness: high token and attention cost, broad overlap, route stacking, and
    weaker preservation of operator intent.
  - Downstream consequence: tests can keep passing while user experience worsens.

- Remove or stop installing Playbooks by default.
  - Strength: restores Core's simpler mental model and reduces accidental workflow
    pressure.
  - Weakness: loses specialized guardrails unless agents know to request them.
  - Downstream consequence: Core record skills and Loom Weaver/Driver must carry
    more workflow judgment.

- Keep Playbooks but gate activation after Core routing.
  - Strength: preserves specialized value while making the owning record surface
    or explicit operator choice the first route.
  - Weakness: requires changing descriptions, doctrine, tests, and possibly
    install guidance.
  - Downstream consequence: most compatible with the existing split-package idea.

- Split Playbooks into smaller profiles or explicit lenses.
  - Strength: users can install only debugging, UI, security, release, or driver
    lenses relevant to a workspace.
  - Weakness: more packaging and documentation surface.
  - Downstream consequence: reduces broad accidental activation without deleting
    high-value workflows.

## Rejected Paths And Null Results

- Treating the current issue as a bug in an individual playbook is too narrow.
  The shared headers, trigger-description checks, Core 1% activation rule, and
  activation tests all work together to create the stacking behavior.

- Relying on "optional package" language is not enough. Once installed, the Core
  activation doctrine makes playbooks mandatory when any material chance exists.

- Counting only successful expected-skill activation is insufficient evidence of
  good behavior. The observed extra playbook invocations show that precision must
  be tested separately.

## Conclusions

- The operator concern is well-founded. Playbooks can degrade agent behavior in
  exactly the way described: not by violating Core directly, but by adding broad
  workflow pressure that competes with Core's simpler truth-surface routing and
  can dilute the original request.

- Current Playbooks are not worthless. They are useful as specialized workflow
  lenses for debugging, TDD, source authority, security, UI observation,
  performance, migration, release, branch finish, and review. Their value is
  highest when a Core route has already established that the workflow is the
  next dominant problem.

- The current default posture is probably net harmful if Playbooks are installed
  broadly. The core product should prefer Core plus Loom Weaver/Driver for the
  default mental model, with playbooks invoked only after Core says a specific
  workflow lens is needed or the operator explicitly asks for it.

- The sharp product distinction should be: record skills are activation owners;
  playbooks are optional lenses. A lens should not become a first material route
  just because a prompt contains a broad trigger word like UI, auth, tests, review,
  source, or implementation.

## Recommendations

- Demote playbook activation from "any matching task" to "after Core routing has
  selected this workflow as the dominant lens" or "when explicitly requested by
  the operator." Encode that in playbook descriptions, not only docs.

- Add a single-workflow-lens rule to Core activation discipline: when a record
  skill route is sufficient, do not add a playbook; when a playbook is useful,
  choose one primary playbook unless a second is explicitly justified.

- Add negative activation tests. Examples: `Let's make a react todo list` should
  trigger shaping but should not load UI implementation before direction is
  selected; `Create a ticket for auth cleanup and start implementing it` should
  not load security or incremental implementation before ticket scope is shaped.

- Keep or promote a small number of high-value playbooks as explicit specialist
  lenses, likely debugging, source-driven development, security/hardening,
  browser/UI observation, and release/migration. Treat idea refinement and
  incremental implementation as especially duplicative with Loom Weaver and Loom
  Driver unless their trigger surface is narrowed.

- Consider packaging profiles or adapter config that lets installed workspaces
  expose Core only by default, then opt into selected playbook categories.

- If a product change is accepted, route it through a constitution decision or
  product spec first, then a ticket to update descriptions, activation doctrine,
  tests, and docs together.

## Open Questions

- Should `loom-idea-refine` remain a playbook, or should its useful content be
  absorbed into Loom Weaver and Core shaping references?
- Should Playbooks remain one package, or split into explicit profiles such as
  debug, UI, security, release, and execution?
- Which harnesses expose enough skill metadata to support "explicit only" or
  "route-gated" playbooks without losing discoverability?

## Related Records

- `.loom/evidence/20260515-playbook-activation-stacking.md` - key observations for current package shape and prior live activation logs.
- `.loom/research/20260513-superpowers-skill-activation.md` - source of the stronger activation strategy.
- `.loom/tickets/done/20260513-superpowers-style-activation-doctrine.md` - implemented the activation strategy that made playbook stacking likely.
- `.loom/evidence/20260513-superpowers-style-activation-checks.md` - earlier validation dossier whose log paths were inspected.
- `loom-core/skills/using-loom/SKILL.md` - Core activation and loop-order owner.
- `loom-playbooks/skills/*/SKILL.md` - playbook trigger and workflow surfaces.
