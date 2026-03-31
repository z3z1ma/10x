# Constitution Examples

## Example Constitution Record Types

- one main constitutional statement for durable project identity
- one decision record for a major strategic or architectural choice
- one roadmap record that may link long-lived direction into downstream work

## What To Notice In Strong Constitutional Writing

- the writing sounds durable, not like a sprint note
- the record explains why the truth matters, not only what changed
- downstream consequences are visible
- the main constitution does not need outbound frontmatter links to be authoritative
- another agent could use the record to judge later work

## Example Main Constitution Excerpt

```text
Vision
Create a portable, inspectable Loom protocol that remains useful across harness changes and across repositories with different runtime stacks.

Principles
- durable Markdown records remain primary truth
- tickets remain the live execution ledger
- packet-consuming work prefers fresh contexts when bounded execution matters
- rules and skills should tell the operator what to do before listing prohibitions

Constraints
- no hidden execution center
- no monolithic product CLI that quietly outranks the Markdown corpus
- no silent widening of scope or write authority

Strategic Direction
Favor visible doctrine, explicit packet contracts, and artifact-owned truth over runtime magic or transcript-dependent workflows.

Current Focus
Make each Loom layer understandable enough that a fresh agent can route correctly, execute safely, and reconcile results without hidden local knowledge.
```

Why this is strong:

- it defines durable identity and principles
- it constrains future tool and architecture choices
- it gives downstream specs, plans, and tickets a strategic frame to inherit
- it does that without enumerating downstream links in frontmatter

## Example Decision Record Excerpt

```text
Decision
Keep skills as flat siblings instead of introducing a nested inheritance tree.

Why This Decision Exists
Operators and future agents need to see always-on doctrine directly instead of having skill behavior hidden behind an implicit parent bundle.

Consequences
- build assembly stays simpler and more inspectable
- each skill must carry clearer activation guidance in its own `SKILL.md`
- cross-skill duplication should be handled by shared helpers or references rather than hidden inheritance

Supersession
This supersedes earlier assumptions that a shared core skill might quietly provide common operating behavior.
```

Why this is strong:

- the decision is explicit
- the reasoning is durable
- downstream consequences are obvious

## Example Roadmap Excerpt

```text
Strategic Theme
Make every Loom layer operationally resumable by a fresh agent.

Focus Areas
- strengthen skill activation descriptions and playbooks
- deepen schema and example references so operators know what good records look like
- improve helper scripts only when they mechanize already-published rules

Milestones
- all skills route clearly from frontmatter description alone
- every skill has strong schema and worked-example references
- helper naming and invocation patterns read like natural operator verbs

Downstream Work
- initiative updates for corpus quality
- spec and plan updates for record and workflow expectations
- tickets for concrete documentation and helper improvements
```

## Weak Example

```text
Strategic Direction
Keep improving the system.
```

Why this is weak:

- it is too vague to constrain later work
- it does not tell a future agent what should now be true
- it has no downstream consequence or judgment value
