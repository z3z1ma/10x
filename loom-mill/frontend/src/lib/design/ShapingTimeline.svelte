<script lang="ts">
  import type { InteractionBlock } from '../types';
  import ShapingBlock from './ShapingBlock.svelte';
  import { onMount, tick } from 'svelte';

  let { 
    sessionId, 
    blocks, 
    activeExplorations, 
    phase,
    advancing,
    onRespond 
  }: { 
    sessionId: string; 
    blocks: InteractionBlock[]; 
    activeExplorations: string[]; 
    phase: string;
    advancing: boolean;
    onRespond: (content: string) => void;
  } = $props();

  let timelineContainer: HTMLDivElement;
  let autoScroll = $state(true);
  let operatorInput = $state('');

  // Auto-scroll logic
  $effect(() => {
    if (blocks.length && autoScroll && timelineContainer) {
      tick().then(() => {
        timelineContainer.scrollTop = timelineContainer.scrollHeight;
      });
    }
  });

  function handleScroll() {
    if (!timelineContainer) return;
    const { scrollTop, scrollHeight, clientHeight } = timelineContainer;
    const isAtBottom = scrollHeight - scrollTop - clientHeight < 10;
    autoScroll = isAtBottom;
  }

  function blockColor(type: string) {
    switch (type) {
      case 'operator_input': return 'bg-text-secondary';
      case 'agent_question': return 'bg-accent-primary';
      case 'agent_observation': return 'bg-status-success-text';
      case 'agent_proposal': return 'bg-accent-secondary';
      case 'exploration_start': return 'bg-text-tertiary';
      case 'exploration_complete': return 'bg-text-tertiary';
      case 'branch_point': return 'bg-status-warning-text';
      case 'system': return 'bg-text-tertiary/50';
      default: return 'bg-text-tertiary';
    }
  }

  async function submitResponse() {
    if (!operatorInput.trim()) return;
    onRespond(operatorInput);
    operatorInput = '';
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      submitResponse();
    }
  }

  // Determine if we are awaiting input (last block is a question, or we just want to allow input)
  let awaitingInput = $derived(true); // For now, always allow input

  const phases = ['exploring', 'narrowing', 'proposing', 'refining', 'ready'];
  
  function getPhaseIndex(p: string) {
    return phases.indexOf(p);
  }
</script>

<div class="flex flex-col h-full relative bg-bg-primary">
  <!-- Phase Banner -->
  <div class="shrink-0 px-6 py-3 border-b border-border-default bg-bg-surface flex items-center justify-between shadow-sm z-10">
    <div class="flex items-center gap-2">
      <span class="text-[12px] font-medium text-text-primary uppercase tracking-wider">Phase:</span>
      <span class="text-[12px] text-accent-primary font-mono">{phase}</span>
    </div>
    <div class="flex items-center gap-1">
      {#each phases as p, i}
        <div class="flex items-center">
          <div class="h-1.5 rounded-full transition-all duration-500 {i <= getPhaseIndex(phase) ? 'w-8 bg-accent-primary' : 'w-4 bg-border-default'}"></div>
          {#if i < phases.length - 1}
            <div class="w-1 h-px bg-border-default mx-0.5"></div>
          {/if}
        </div>
      {/each}
    </div>
  </div>

  <div 
    bind:this={timelineContainer}
    onscroll={handleScroll}
    class="flex-1 overflow-y-auto p-6 flex flex-col gap-0"
  >
    {#each blocks as block (block.id)}
      <div class="flex gap-4 py-4 border-b border-border-subtle/30 animate-in fade-in slide-in-from-bottom-2 duration-300 group">
        <!-- Timeline gutter -->
        <div class="w-8 flex flex-col items-center pt-1.5 shrink-0 relative">
          <div class="w-3 h-3 rounded-full {blockColor(block.type)} shadow-sm ring-4 ring-bg-primary z-10 transition-transform group-hover:scale-125"></div>
          <div class="absolute top-4 bottom-[-2rem] w-px bg-gradient-to-b from-border-subtle to-transparent z-0"></div>
        </div>
        <!-- Block content -->
        <div class="flex-1 min-w-0">
          <ShapingBlock {block} {sessionId} {onRespond} />
        </div>
      </div>
    {/each}
    
    <!-- Active exploration indicators -->
    {#each activeExplorations as exp}
      <div class="flex gap-4 py-4 animate-in fade-in duration-500">
        <div class="w-8 flex flex-col items-center pt-1.5 shrink-0 relative">
          <div class="w-3 h-3 rounded-full border-2 border-accent-primary border-t-transparent animate-spin z-10 bg-bg-primary ring-4 ring-bg-primary"></div>
          <div class="absolute top-4 bottom-[-2rem] w-px bg-gradient-to-b from-border-subtle to-transparent z-0"></div>
        </div>
        <div class="text-[12px] text-text-secondary font-mono flex items-center gap-2 bg-bg-surface px-3 py-1.5 rounded-full border border-border-subtle shadow-sm">
          <span class="text-accent-primary">🔍</span> {exp}
        </div>
      </div>
    {/each}

    <!-- Thinking indicator -->
    {#if advancing && activeExplorations.length === 0}
      <div class="flex gap-4 py-4 animate-in fade-in duration-300">
        <div class="w-8 flex flex-col items-center pt-1.5 shrink-0 relative">
          <div class="flex gap-1 z-10 bg-bg-primary ring-4 ring-bg-primary rounded-full px-1">
            <div class="w-1.5 h-1.5 rounded-full bg-text-tertiary animate-bounce" style="animation-delay: 0ms"></div>
            <div class="w-1.5 h-1.5 rounded-full bg-text-tertiary animate-bounce" style="animation-delay: 150ms"></div>
            <div class="w-1.5 h-1.5 rounded-full bg-text-tertiary animate-bounce" style="animation-delay: 300ms"></div>
          </div>
        </div>
        <div class="text-[12px] text-text-tertiary italic font-medium">
          {phase === 'exploring' ? 'Exploring...' : phase === 'proposing' ? 'Drafting proposals...' : 'Reasoning...'}
        </div>
      </div>
    {/if}
    
    <!-- Operator input area -->
    {#if awaitingInput}
      <div class="flex gap-4 py-4 mt-4">
        <div class="w-8 shrink-0"></div>
        <div class="flex-1 flex flex-col gap-2">
          <textarea 
            bind:value={operatorInput}
            onkeydown={handleKeydown}
            disabled={advancing}
            class="w-full min-h-[80px] p-3 rounded border border-border-default bg-bg-surface text-[13px] text-text-primary font-mono resize-y focus:outline-none focus:border-accent-primary disabled:opacity-50 disabled:cursor-not-allowed shadow-sm transition-all"
            placeholder="Type your response... (Enter to send, Shift+Enter for new line)"
          ></textarea>
          <div class="flex justify-end">
            <button 
              onclick={submitResponse}
              disabled={!operatorInput.trim() || advancing}
              class="px-4 py-1.5 rounded bg-accent-primary text-white text-[12px] font-medium hover:bg-accent-primary/90 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm"
            >
              {advancing ? 'Thinking...' : 'Send'}
            </button>
          </div>
        </div>
      </div>
    {/if}
  </div>
</div>
