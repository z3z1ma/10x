<script lang="ts">
  import type { InteractionBlock } from '../types';
  import ProposalCard from './ProposalCard.svelte';

  let { block, sessionId, onRespond }: { block: InteractionBlock, sessionId: string, onRespond: (content: string) => void } = $props();

  let expanded = $state(false);
</script>

<div class="flex flex-col gap-2 w-full group">
  {#if block.type === 'operator_input'}
    <div class="bg-bg-surface-active p-4 rounded-lg text-[13px] text-text-primary font-mono whitespace-pre-wrap shadow-sm border border-border-default/50">
      {block.content.text}
    </div>
    
  {:else if block.type === 'agent_question'}
    <div class="bg-bg-surface border border-accent-primary/30 p-4 rounded-lg shadow-md flex flex-col gap-3 relative overflow-hidden">
      <div class="absolute top-0 left-0 w-1 h-full bg-accent-primary"></div>
      <div class="flex items-start gap-3">
        <div class="w-6 h-6 rounded-full bg-accent-primary/10 flex items-center justify-center shrink-0 mt-0.5">
          <span class="text-accent-primary text-[12px]">❓</span>
        </div>
        <div class="text-[14px] text-text-primary whitespace-pre-wrap leading-relaxed font-medium">{block.content.question}</div>
      </div>
      {#if block.content.options && block.content.options.length > 0}
        <div class="flex flex-wrap gap-2 mt-2 ml-9">
          {#each block.content.options as option}
            <button 
              class="px-4 py-1.5 text-[12px] rounded-full border border-border-default bg-bg-primary hover:bg-accent-primary/10 hover:border-accent-primary/50 hover:text-accent-primary text-text-secondary transition-all shadow-sm"
              onclick={() => onRespond(option)}
            >
              {option}
            </button>
          {/each}
        </div>
      {/if}
    </div>
    
  {:else if block.type === 'agent_observation'}
    <div class="bg-bg-surface border border-status-success-border/30 p-4 rounded-lg shadow-sm flex flex-col gap-2 relative overflow-hidden">
      <div class="absolute top-0 left-0 w-1 h-full bg-status-success-text/50"></div>
      <div class="flex items-start gap-3">
        <div class="w-6 h-6 rounded-full bg-status-success-bg/20 flex items-center justify-center shrink-0 mt-0.5">
          <span class="text-status-success-text text-[12px]">👁️</span>
        </div>
        <div class="text-[13px] text-text-primary whitespace-pre-wrap leading-relaxed">{block.content.observation}</div>
      </div>
      {#if block.content.evidence}
        <div class="ml-9 mt-2">
          <button 
            class="text-[11px] text-text-tertiary hover:text-text-secondary flex items-center gap-1 bg-bg-primary px-2 py-1 rounded border border-border-subtle transition-colors"
            onclick={() => expanded = !expanded}
          >
            <span class="transform transition-transform {expanded ? '' : '-rotate-90'}">▼</span>
            {expanded ? 'Hide evidence' : 'Show evidence'}
          </button>
          {#if expanded}
            <div class="mt-2 p-3 bg-[#0d1117] rounded-md border border-border-subtle text-[11px] font-mono text-text-secondary overflow-x-auto whitespace-pre-wrap shadow-inner">
              {block.content.evidence}
            </div>
          {/if}
        </div>
      {/if}
    </div>
    
  {:else if block.type === 'agent_proposal'}
    <div class="animate-in zoom-in-95 duration-500">
      <ProposalCard proposal={block.content.proposal} {sessionId} />
    </div>
    
  {:else if block.type === 'exploration_start'}
    <div class="text-[12px] text-text-tertiary flex items-center gap-2 bg-bg-surface px-3 py-2 rounded-md border border-border-subtle w-fit">
      <span class="animate-pulse text-accent-primary">🔍</span> 
      <span class="font-mono">Exploring: {block.content.goal}</span>
    </div>
    
  {:else if block.type === 'exploration_complete'}
    <div class="text-[12px] text-text-tertiary flex items-center gap-2 bg-bg-surface px-3 py-2 rounded-md border border-border-subtle w-fit opacity-70">
      <span class="text-status-success-text">✓</span> 
      <span class="font-mono">Explored: {block.content.summary}</span>
    </div>
    
  {:else if block.type === 'branch_point'}
    <div class="bg-status-warning-bg/10 border border-status-warning-border/30 rounded-lg p-4 flex flex-col gap-3 shadow-sm relative overflow-hidden">
      <div class="absolute top-0 left-0 w-1 h-full bg-status-warning-text"></div>
      <div class="text-[13px] font-medium text-status-warning-text flex items-center gap-2">
        <span class="text-[14px]">🔀</span> Branch Point
      </div>
      <div class="text-[13px] text-text-primary">{block.content.description}</div>
      <div class="flex flex-wrap gap-2 mt-2">
        {#each block.content.branches as branch}
          <button 
            class="px-4 py-2 text-[12px] rounded-md bg-bg-surface hover:bg-status-warning-bg/20 border border-status-warning-border/50 text-text-primary transition-all shadow-sm flex items-center gap-2 font-medium"
            onclick={() => onRespond(`Switch to branch: ${branch.label || branch.name || branch.id}`)}
          >
            <span class="text-status-warning-text">↳</span> {branch.label || branch.name || branch.id}
          </button>
        {/each}
      </div>
    </div>
    
  {:else if block.type === 'system'}
    <div class="text-[11px] text-text-tertiary italic flex items-center gap-2 justify-center my-2">
      <div class="h-px w-8 bg-border-subtle"></div>
      {block.content.message}
      <div class="h-px w-8 bg-border-subtle"></div>
    </div>
    
  {:else}
    <div class="text-[12px] text-text-secondary p-3 bg-bg-surface rounded border border-border-default">
      Unknown block type: {block.type}
    </div>
  {/if}
  
  <div class="text-[10px] text-text-tertiary text-right mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
    {new Date(block.timestamp).toLocaleTimeString()}
  </div>
</div>
