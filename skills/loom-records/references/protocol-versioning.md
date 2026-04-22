# Protocol Versioning

Protocol versions describe Loom record grammar and workflow expectations.

They do not make older records false by themselves.

## Version Meaning

Use protocol versions for:

- required record fields
- legal status vocabularies
- packet contract shape
- owner-layer expectations
- workflow semantics that future agents must honor

## Record Migration

Older records remain valid until one of these happens:

- they are migrated
- they are marked `stale`, `superseded`, or `retired`
- an owner record explicitly changes the truth they carry

Migration changes owner truth only when the owner layer is updated. A generated
migration, script, or bulk edit is a support operation, not a truth owner.

## Compatibility

When changing grammar:

1. document the new expectation in rules, skills, references, or templates
2. update examples that teach the shape
3. mark legacy records only when their current shape is misleading
4. create repair or migration tickets for broad sweeps
5. keep old records readable unless removal is explicitly justified

## Frontmatter

Skill frontmatter may carry:

```yaml
metadata:
  protocol_version: "2.0"
```

Canonical records may add grammar-specific version fields later, but do not add
them casually. The visible record shape and owner truth matter more than a
version number.
