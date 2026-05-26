<script lang="ts">
  let { onSelect }: { onSelect: (surface: string) => void } = $props();
  
  let isOpen = $state(false);
  let dropdownRef: HTMLDivElement;

  function toggle() {
    isOpen = !isOpen;
  }

  function select(surface: string) {
    onSelect(surface);
    isOpen = false;
  }

  function handleClickOutside(event: MouseEvent) {
    if (isOpen && dropdownRef && !dropdownRef.contains(event.target as Node)) {
      isOpen = false;
    }
  }
</script>

<svelte:window onclick={handleClickOutside} />

<div class="relative" bind:this={dropdownRef}>
  <button 
    class="px-2 py-1 bg-bg-surface-hover hover:bg-bg-surface-active rounded text-text-secondary transition-colors"
    onclick={toggle}
  >
    + New
  </button>
  
  {#if isOpen}
    <div class="absolute top-full right-0 mt-1 w-32 bg-bg-surface border border-border-default rounded shadow-lg z-10 py-1">
      <button class="w-full text-left px-3 py-1.5 hover:bg-bg-surface-hover text-text-secondary flex items-center gap-2" onclick={() => select('tickets')}>
        <span>🎫</span> Ticket
      </button>
      <button class="w-full text-left px-3 py-1.5 hover:bg-bg-surface-hover text-text-secondary flex items-center gap-2" onclick={() => select('specs')}>
        <span>📐</span> Spec
      </button>
      <button class="w-full text-left px-3 py-1.5 hover:bg-bg-surface-hover text-text-secondary flex items-center gap-2" onclick={() => select('plans')}>
        <span>📊</span> Plan
      </button>
      <button class="w-full text-left px-3 py-1.5 hover:bg-bg-surface-hover text-text-secondary flex items-center gap-2" onclick={() => select('research')}>
        <span>🔬</span> Research
      </button>
      <button class="w-full text-left px-3 py-1.5 hover:bg-bg-surface-hover text-text-secondary flex items-center gap-2" onclick={() => select('knowledge')}>
        <span>💡</span> Knowledge
      </button>
    </div>
  {/if}
</div>
