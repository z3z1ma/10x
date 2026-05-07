# Task Routing Catalog

This catalog maps ordinary coding prompts to Loom owner layers and workflow
skills. Use it after `routing.md` when the user asks in product, code, or tool
language rather than Loom layer language.

Named playbook routes are optional package-dependent helpers. If one is absent,
use the listed core owner layers plus local execution, Ralph, or a project-provided
equivalent workflow that leaves durable truth in the same owner layers.

Do not save these rows as route fields. They are prompts for agent judgment. The
ticket, spec, plan, evidence, critique, or other owner record must still carry the
truth that makes the next action recoverable.

## Common Coding Prompts

| User request shape | First owner question | Usual Loom route |
| --- | --- | --- |
| "Fix this bug", failing test, broken build, regression, flaky behavior, incident, unexpected error | Is the failure reproduced and is root cause known? | optional `loom-debugging` or equivalent investigation -> evidence -> `loom-tickets` -> local execution or `loom-ralph` |
| Add feature, change product behavior, alter UX flow, change API behavior | Is intended behavior or acceptance fuzzy? | `loom-specs` if fuzzy -> `loom-tickets` -> local execution or `loom-ralph` |
| Refactor, cleanup, simplify, reduce complexity without behavior change | Is behavior preservation clear and bounded? | `loom-tickets` with `code-structure` -> evidence for preservation -> critique when nontrivial |
| Add or change tests, fixtures, smoke checks, browser checks, CI validation | Is this validating existing acceptance or defining new expectations? | `loom-tickets` with `validation-instrumentation`; update `loom-specs` if expectations become behavior contract |
| Dependency upgrade, package manager change, build/lint/typecheck/tooling config | Is compatibility or migration risk unknown? | `loom-research` when unknown -> `loom-tickets` with `dependency-tooling` -> evidence and critique |
| Performance problem, slow path, bundle size, Core Web Vitals, high traffic concern | Is there a baseline measurement? | `loom-evidence` baseline -> `loom-research` or optional `loom-spike` or equivalent exploration workflow -> ticket -> after evidence -> performance critique |
| Security, auth, permissions, secrets, untrusted input, data exposure | Is policy or intended trust boundary unclear? | `loom-specs` or `loom-constitution` if policy-bearing -> ticket -> evidence -> security critique |
| UI page, component, styling, responsive layout, accessibility, visual polish | Is primary user task and quality bar clear? | `loom-specs` if fuzzy -> optional `loom-spike` or equivalent exploration workflow for variants when needed -> ticket -> visual/product evidence -> critique |
| API, module boundary, public interface, contract between systems | Is the interface contract stable enough? | `loom-specs` and possibly `loom-research` -> plan/ticket -> critique for interface risk |
| Architecture improvement, module deepening, codebase more testable, tangled dependency | Is this investigation, decision, or execution? | optional `loom-codemap` or equivalent atlas workflow, or `loom-research` -> `loom-specs` or `loom-constitution` for decisions -> plan/ticket |
| Database schema, storage, data migration, import/export, persistence safety | Does order, rollback, or idempotency matter? | `loom-plans` when planning/decomposition matters -> ticket with `data-migration` -> before/after evidence -> critique |
| Documentation, ADR, troubleshooting note, domain terminology, shared language | Is this policy, behavior, investigation, or accepted explanation? | `loom-constitution`, `loom-specs`, `loom-research`, or `loom-wiki` by owner truth |
| "Grill me", stress-test this idea/plan, refine idea, ideate, challenge assumptions | Is the output a behavior contract, investigation, planning decision, or accepted explanation? | `loom-workspace` problem shaping -> `loom-research`, `loom-specs`, `loom-plans`, or `loom-wiki` by owner truth |
| Prototype this, try a few designs, sanity-check a state model, let me play with it | What question should the throwaway artifact answer? | optional `loom-spike` or equivalent exploration workflow -> evidence/research -> spec/wiki/ticket route after conclusion |
| Use TDD, test-first, red/green/refactor, add regression coverage | Which acceptance or bug claim should the failing check prove? | ticket/Ralph/local execution with `test-first` posture -> evidence red/green -> critique when warranted |
| Review comments, fix feedback, reviewer says, apply suggestions | Are the findings understood and valid for this ticket/codebase? | `loom-critique` finding disposition -> ticket-owned disposition -> local execution/Ralph if fixes are needed |
| "Where is X?", unfamiliar code, understand this module, map architecture | Is durable orientation useful for future agents? | optional `loom-codemap` or equivalent atlas workflow -> evidence/research -> wiki atlas when accepted |
| PR description, changelog, release note, launch, rollback, monitoring, handoff, merge package | Are tickets/evidence/critique already truthful? | optional `loom-ship` or equivalent shipping workflow; route back to tickets/evidence/critique if not truthful |
| "Is this done?", "close it", "ready to merge?", acceptance or residual risk check | Does ticket-owned acceptance support closure? | `loom-tickets` acceptance gate; optional `loom-ship` only after truth is current |
| User asks to keep going on a broad outcome | Is there delegated objective, success criteria, and stop conditions? | optional `loom-drive` or equivalent objective driver -> owner layers -> tickets/Ralph/evidence/critique |

## Ambiguity Gates

Route outward before implementation when:

- product direction would be invented by the agent;
- behavior could be implemented in materially different ways;
- success criteria or quality bar is missing;
- hidden assumptions, target user, or not-doing boundary would change the shape;
- evidence baseline is missing for a performance, bug, or migration claim;
- security, privacy, data-loss, or trust-boundary risk is unclear;
- the change is wider than one bounded ticket or write scope.

## Shared-Language Prompts

When the user uses domain terms, project jargon, or ambiguous nouns that matter to
the implementation, do not let the meaning stay in chat.

Route the clarification by owner:

- reusable behavior meaning -> `loom-specs`
- accepted explanation or glossary -> `loom-wiki`
- uncertainty or term conflict investigation -> `loom-research`
- project policy or durable naming principle -> `loom-constitution`
- one-ticket assumption that will not be reused -> `loom-tickets`

## Local vs Ralph

After the owning ticket is clear, choose execution shape:

- local execution when the write boundary is tiny, obvious, and safe in the
  current context;
- `loom-ralph` when the implementation/refactor/test/migration slice benefits
  from fresh context, explicit child write scope, replayable packet contract, or
  stronger isolation;
- optional `loom-debugging` or equivalent investigation workflow when root cause
  is unknown;
- optional `loom-spike` or equivalent exploration workflow when the right design,
  API, data model, or UI shape is still being explored.
