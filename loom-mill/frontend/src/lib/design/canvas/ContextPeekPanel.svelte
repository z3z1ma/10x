<script lang="ts">
  import { apiUrl } from '../../api';

  let { sessionId }: { sessionId: string } = $props();

  let open = $state(false);
  let context = $state('');
  let loading = $state(false);
  let error = $state<string | null>(null);

  async function load() {
    loading = true;
    error = null;
    try {
      const resp = await fetch(apiUrl(`/shaping/sessions/${sessionId}/context`));
      if (resp.ok) {
        const body = await resp.json();
        context = body.content ?? '';
      } else {
        error = `Failed to load context (${resp.status})`;
      }
    } catch (e) {
      error = String(e);
    } finally {
      loading = false;
    }
  }

  function toggle() {
    open = !open;
    if (open) load();
  }
</script>

<button
  class="absolute top-16 left-4 z-20 px-3 py-1.5 text-[11px] rounded border border-border-default
    bg-bg-surface text-text-secondary hover:text-text-primary shadow-sm"
  onclick={toggle}
>
  {open ? 'Hide context' : 'Context'}
</button>

{#if open}
  <div class="absolute top-28 left-4 z-20 w-[420px] max-w-[90vw] max-h-[60vh] overflow-auto
    bg-bg-surface border border-border-default rounded-lg shadow-lg p-3">
    <div class="text-[10px] uppercase tracking-wider text-text-tertiary mb-2">Context document</div>
    {#if loading}
      <div class="text-[11px] text-text-tertiary">Loading…</div>
    {:else if error}
      <div class="text-[11px] text-red-400">{error}</div>
    {:else}
      <pre class="text-[11px] font-mono text-text-secondary whitespace-pre-wrap break-words">{context}</pre>
    {/if}
  </div>
{/if}
