# Packet Styles

## Reference-first

Use when:

- the child can read the workspace directly
- you want a smaller packet
- replayability matters less than boundedness

## Snapshot-first

Use when:

- the child should get more of the context in one place
- you want fewer workspace hops during execution
- the parent wants stronger curation of source excerpts

## Hermetic

Use when:

- replayability matters a lot
- the trust boundary should be tight
- you want the packet to carry almost everything needed

## Choosing well

Default to `reference-first` unless there is a real reason not to.
Use `hermetic` deliberately, not because it sounds rigorous.
