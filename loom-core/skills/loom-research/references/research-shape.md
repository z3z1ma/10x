# Research Shape

Research creation is outer-loop work.

Create research when a question and its reasoning are durable enough that future
work would be worse without the record.

A research record gives a future agent the question, scope, grounding path,
findings, tradeoffs, rejected paths, conclusions, limits, and downstream route.

## Shaping Standard

Before writing research, shape the investigation until four things are true:

- durable question: the investigation matters beyond the current chat
- bounded scope: the record can say what is covered and excluded
- grounding path: there is a plausible method, source set, experiment, or
  inspection path
- downstream consumer: a spec, ticket, plan, constitution record, evidence record,
  audit, knowledge record, source area, or future agent can use the result

Inspect source and records first. Ask one material question when operator input is
needed. Offer a recommended answer when the tradeoff is clear.

## Create Research Only When

Create an `active` research record when all of these are true:

- the question is clear enough to investigate
- the scope is narrow enough to avoid becoming a parking lot
- the likely sources or inspection path are known enough to begin
- the likely downstream consumer is known
- the investigation, rejection, null result, or conclusion should remain available
  to future work

Create active research before conclusions when the investigation itself needs a
durable home.

## Route Elsewhere When

Research informs other surfaces. It should not replace them.

Route instead:

- intended behavior, requirements, scenarios, interface expectations, or invariants to
  specs
- bounded executable work to tickets
- complex multi-ticket strategy, sequencing, or decomposition to plans
- durable policy, principles, architectural precedent, or roadmap direction to
  constitution
- observed validation artifacts to evidence when the observation itself must be
  inspectable
- adversarial review to audit
- accepted reusable explanation to knowledge

## Core Sections

Use the default sections unless a research record has a strong reason to vary:

- `## Summary`
- `## Question`
- `## Scope`
- `## Method And Sources`
- `## Findings`
- `## Tradeoffs`
- `## Rejected Paths And Null Results`
- `## Conclusions`
- `## Recommendations`
- `## Open Questions`
- `## Related Records`

Research does not use a journal by default. If investigation history matters, fold
the material facts into Method, Findings, Rejected Paths, or Conclusions. Tickets
and plans carry live execution journals.

## Summary

Summary should answer:

- what was investigated
- why the investigation matters
- what conclusion or current state a future agent should notice first

Keep it short, but make the record understandable without chat history.

## Question

The question should be specific enough to investigate and specific enough to know
when the record is done.

Weak questions sound like:

- research auth
- compare options
- see how migrations work
- figure out best practice

Better questions name the decision pressure:

- Which validation route is strong enough for `ticket:YYYYMMDD-<slug>#ACC-001`?
- Which migration strategy avoids breaking existing persisted records?
- Which library API behavior applies to the version this repository actually uses?
- Which implementation seam lets the next ticket stay bounded and reviewable?

## Scope

Scope should say what the research covers and excludes.

Good scope names:

- source paths, records, systems, versions, or environments inspected
- options or hypotheses considered
- scenarios intentionally excluded
- assumptions the conclusion depends on
- freshness or recheck triggers when obvious

If the scope cannot be bounded, the research is not ready.

## Method And Sources

Method explains how the investigation was grounded.

It can include code inspection, record review, command output, experiments,
external documentation, source-material artifacts, operator input, model debate,
or peer repository comparison.

Keep method concise. Expand source quality, provenance, version, or freshness only
when it materially affects trust.

## Findings

Findings are what the investigation found before the record claims what it means.

Separate observed or sourced facts from conclusions. When a finding depends on an
artifact that should survive independently, cite or create evidence.

A useful finding names enough source context for a future agent to recheck it.

## Tradeoffs

Use Tradeoffs when options, variants, hypotheses, libraries, strategies, or
implementation routes are compared.

Compare meaningful differences, not cosmetic variants. A useful comparison names:

- option or hypothesis
- evidence-backed strength
- risk, weakness, or limit
- decision pressure or downstream consequence

Remove the section if no real comparison exists.

## Rejected Paths And Null Results

Capture dead ends when future agents would otherwise rediscover them.

For each useful rejection or null result, say:

- what was considered or tried
- what rejected it
- what a future agent should do instead, if known

## Conclusions

Conclusions say what is justified by the findings.

Do not make conclusions stronger than the source quality supports. If the result
depends on a version, environment, assumption, or unverified source, say so.

`Status: completed` means the conclusions and recommendations are bounded enough
to cite. It does not mean the consuming ticket, spec, plan, constitution record,
knowledge record, or audit automatically accepts them.

## Recommendations

Recommendations route the result.

Good recommendations name the next owner:

- create or update a spec for intended behavior
- create a ticket for bounded executable work
- create a plan for complex multi-ticket strategy
- create or update constitution for durable judgment
- create evidence for an observation that must be inspectable
- route to audit for adversarial review
- promote settled explanation into knowledge

Research may recommend. The receiving surface owns the next truth change.

## Open Questions

Open questions are honest limits.

Keep them short. Split into a new research record only when a question becomes an
independently actionable investigation or would bloat the current record.

Do not use open questions as a parking lot for vague future work.

## Related Records

Use Related Records when another record or source path materially helps a future
agent interpret the research.

Each entry should say why it matters. Add only records that materially constrain or
explain the research.

## Spike, Sketch, And Experiment Results

A spike, sketch, prototype, or experiment belongs in research when its durable
product is a conclusion, comparison, rejection, or null result.

The research record should preserve the question, method, artifact pointers,
findings, limits, and downstream route. Omit throwaway implementation steps.
