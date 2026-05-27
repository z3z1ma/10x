<script lang="ts">
  import { Svelvet, Node, Anchor } from 'svelvet';
  import { store } from '../../ws.svelte.ts';
  import InputNode from './InputNode.svelte';
  import ProcessingNode from './ProcessingNode.svelte';
  import QuestionNode from './QuestionNode.svelte';
  import ObservationNode from './ObservationNode.svelte';
  import OptionNode from './OptionNode.svelte';
  import RecordNode from './RecordNode.svelte';
  import { apiUrl } from '../../api';
  import type { CanvasNode } from '../../types';
  import { computeTreeLayout } from './layout';

  let { sessionId, advancing }: { sessionId: string, advancing: boolean } = $props();

  let allNodes = $derived(store.shapingSession?.nodes ? Object.values(store.shapingSession.nodes) : []);
  let allEdges = $derived(store.shapingSession?.edges ?? []);

  let collapseDead = $state(false);

  let nodes = $derived(
    collapseDead
      ? allNodes.filter(n => n.status !== 'dead')
      : allNodes
  );

  let edges = $derived(
    collapseDead
      ? allEdges.filter(e => {
          const source = store.shapingSession?.nodes[e.source_id];
          const target = store.shapingSession?.nodes[e.target_id];
          return source?.status !== 'dead' && target?.status !== 'dead';
        })
      : allEdges
  );

  let hiddenCount = $derived(allNodes.length - nodes.length);

  let layoutResult = $derived(computeTreeLayout(nodes, edges));

  function getChildConnections(nodeId: string) {
    const conns = edges
      .filter(e => e.source_id === nodeId && store.shapingSession?.nodes[e.target_id])
      .map(e => [e.target_id, `${e.target_id}-in`]);
    return conns;
  }

  function computePosition(node: CanvasNode) {
    if (node.position) return node.position;
    return layoutResult.positions[node.id] ?? { x: 0, y: 0 };
  }

  async function handleRespond(content: string, parentNodeId: string) {
    if (!sessionId) return;
    try {
      const inputRes = await fetch(apiUrl(`/shaping/sessions/${sessionId}/input`), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: content, parent_node_id: parentNodeId })
      });
      if (!inputRes.ok) {
        console.error('Error sending input:', await inputRes.text());
        return;
      }
      
      // Trigger the engine to produce the next node
      await fetch(apiUrl(`/shaping/sessions/${sessionId}/advance`), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
    } catch (err) {
      console.error('Error in shaping respond:', err);
    }
  }

  async function handleSelect(nodeId: string) {
    if (!sessionId) return;
    try {
      const selectRes = await fetch(apiUrl(`/shaping/sessions/${sessionId}/nodes/${nodeId}/select`), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      if (!selectRes.ok) {
        console.error('Error selecting option:', await selectRes.text());
        return;
      }

      await fetch(apiUrl(`/shaping/sessions/${sessionId}/advance`), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
    } catch (err) {
      console.error('Error in shaping option select:', err);
    }
  }
</script>

<div class="w-full h-full bg-bg-primary relative">
  <div class="absolute top-4 right-4 z-10 flex items-center gap-2 bg-bg-surface p-2 rounded border border-border-default shadow-sm">
    <label class="flex items-center gap-2 text-sm text-text-primary cursor-pointer">
      <input type="checkbox" bind:checked={collapseDead} class="rounded border-border-default bg-bg-primary text-brand-primary focus:ring-brand-primary" />
      Collapse dead branches
    </label>
    {#if collapseDead && hiddenCount > 0}
      <span class="text-xs bg-bg-secondary text-text-secondary px-1.5 py-0.5 rounded-full">
        {hiddenCount} hidden
      </span>
    {/if}
  </div>

  <Svelvet theme="dark" minimap controls>
    {#each nodes as node (node.id)}
      {#if node.type === 'input'}
        <InputNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} />
      {:else if node.type === 'processing'}
        <ProcessingNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} />
      {:else if node.type === 'question'}
        <QuestionNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} onRespond={(content) => handleRespond(content, node.id)} />
      {:else if node.type === 'observation'}
        <ObservationNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} />
      {:else if node.type === 'option'}
        <OptionNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} onSelect={handleSelect} />
      {:else if node.type === 'record'}
        <RecordNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} onAccept={(id) => console.log('Accept:', id)} onReject={(id) => console.log('Reject:', id)} onEdit={(id) => console.log('Edit:', id)} />
      {:else}
        <Node id={node.id} position={node.position ?? computePosition(node)}>
          <div class="p-4 bg-bg-surface border border-border-default rounded text-text-primary">
            Unknown node type: {node.type}
          </div>
          <div slot="anchorNorth">
            {#if node.parent_id}
              <Anchor id="{node.id}-in" input />
            {/if}
          </div>
          <div slot="anchorSouth">
            {#if getChildConnections(node.id).length > 0}
              <Anchor id="{node.id}-out" output connections={getChildConnections(node.id)} />
            {:else}
              <Anchor id="{node.id}-out" output />
            {/if}
          </div>
        </Node>
      {/if}
    {/each}
  </Svelvet>
</div>
