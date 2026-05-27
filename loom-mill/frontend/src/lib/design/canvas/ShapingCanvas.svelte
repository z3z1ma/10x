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

  let { sessionId, advancing }: { sessionId: string, advancing: boolean } = $props();

  let nodes = $derived(store.shapingSession?.nodes ? Object.values(store.shapingSession.nodes) : []);
  let edges = $derived(store.shapingSession?.edges ?? []);

  function getChildConnections(nodeId: string) {
    const conns = edges
      .filter(e => e.source_id === nodeId && store.shapingSession?.nodes[e.target_id])
      .map(e => [e.target_id, `${e.target_id}-in`]);
    return conns;
  }

  // Simple layout computation for nodes without position
  // In a real app, we'd use a layout engine like dagre
  function computePosition(node: CanvasNode) {
    if (node.position) return node.position;
    
    // Fallback simple layout
    if (!node.parent_id) return { x: 400, y: 100 };
    
    const parent = store.shapingSession?.nodes[node.parent_id];
    if (!parent) return { x: 400, y: 100 };
    
    const parentPos = parent.position || computePosition(parent);
    
    // Find siblings to offset horizontally
    const siblings = nodes.filter(n => n.parent_id === node.parent_id);
    const index = siblings.findIndex(n => n.id === node.id);
    const total = siblings.length;
    
    const spacing = 350;
    const offset = (index - (total - 1) / 2) * spacing;
    
    return {
      x: parentPos.x + offset,
      y: parentPos.y + 200
    };
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
</script>

<div class="w-full h-full bg-bg-primary">
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
        <OptionNode {node} position={node.position ?? computePosition(node)} connections={getChildConnections(node.id)} onSelect={(id) => console.log('Selected option:', id)} />
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
