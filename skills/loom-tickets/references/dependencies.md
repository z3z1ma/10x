# Dependencies

## `depends_on`

Use for hard prerequisites between tickets.

Example:

```yaml
depends_on:
  - ticket:abcd1234
```

Use it when a ticket should not proceed until another ticket lands or reaches a defined state.

## `links`

Use `links:` for relationships that matter but are not strict execution prerequisites.

Examples:

- critique related to the ticket
- wiki pages created from the ticket
- research notes the ticket uses
- sibling tickets that are related but not blocking
