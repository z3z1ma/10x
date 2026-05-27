<script lang="ts">
  import { onMount } from 'svelte';
  import { apiUrl } from '../../api';

  let { onSelectSession, onNewSession }: {
    onSelectSession: (sessionId: string) => void;
    onNewSession: () => void;
  } = $props();

  type SessionSummary = {
    id: string;
    created_at: string;
    seed_text: string;
    node_count: number;
    status: string;
  };

  let sessions = $state<SessionSummary[]>([]);
  let loading = $state(true);
  let error = $state<string | null>(null);
  let searchQuery = $state('');

  let filteredSessions = $derived(
    searchQuery.trim()
      ? sessions.filter(s =>
          s.seed_text.toLowerCase().includes(searchQuery.toLowerCase()) ||
          s.status.toLowerCase().includes(searchQuery.toLowerCase())
        )
      : sessions
  );

  function relativeDate(value: string) {
    const created = new Date(value);
    if (Number.isNaN(created.getTime())) return 'Unknown date';

    const diffMs = Date.now() - created.getTime();
    const minutes = Math.floor(diffMs / 60000);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (minutes < 1) return 'just now';
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    if (days === 1) return 'yesterday';
    if (days < 7) return `${days}d ago`;

    return created.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
  }

  onMount(async () => {
    try {
      const res = await fetch(apiUrl('/shaping/sessions'));
      if (res.ok) {
        sessions = await res.json();
      } else {
        error = `Failed to load sessions (${res.status})`;
      }
    } catch (err) {
      error = 'Network error loading sessions';
    } finally {
      loading = false;
    }
  });
</script>

<div class="flex h-full w-full flex-col bg-bg-primary">
  <!-- Header with top padding -->
  <div class="shrink-0 px-8 pt-12 pb-4 max-w-3xl mx-auto w-full">
    <h2 class="text-lg font-semibold text-text-primary">Shaping Sessions</h2>
    <p class="mt-1 text-[12px] text-text-tertiary">
      Browse prior decision trees, resume active work, or start a fresh shaping session.
    </p>

    <!-- Search -->
    <input
      type="text"
      bind:value={searchQuery}
      placeholder="Search sessions..."
      class="mt-4 w-full rounded border border-border-default bg-bg-surface px-3 py-2
        text-[12px] text-text-primary placeholder-text-tertiary
        focus:outline-none focus:border-accent-primary transition-colors"
    />
  </div>

  <!-- Scrollable session list -->
  <div class="flex-1 overflow-y-auto px-8 pb-8">
    <div class="max-w-3xl mx-auto w-full flex flex-col gap-3">
      <!-- New session card -->
      <button
        onclick={onNewSession}
        class="group flex w-full items-center gap-4 rounded-lg border border-accent-primary/40 bg-accent-primary/10 p-4 text-left transition-colors hover:border-accent-primary hover:bg-accent-primary/15"
      >
        <span class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-accent-primary text-xl leading-none text-white shadow-sm">+</span>
        <span class="flex flex-col gap-1">
          <span class="text-[13px] font-semibold text-text-primary">Start new session</span>
          <span class="text-[12px] text-text-tertiary">Begin from a new seed input without losing existing sessions.</span>
        </span>
      </button>

      {#if loading}
        <div class="flex flex-col gap-3">
          {#each [1, 2, 3] as _}
            <div class="rounded-lg border border-border-default bg-bg-surface p-4 animate-pulse">
              <div class="h-4 w-3/4 rounded bg-bg-surface-hover"></div>
              <div class="mt-3 flex items-center gap-2">
                <div class="h-5 w-16 rounded-full bg-bg-surface-hover"></div>
                <div class="h-5 w-20 rounded-full bg-bg-surface-hover"></div>
              </div>
            </div>
          {/each}
        </div>
      {:else if error}
        <div class="rounded-lg border border-status-error-text/30 bg-status-error-text/5 p-4 text-center">
          <p class="text-[13px] text-status-error-text">{error}</p>
          <button
            onclick={() => location.reload()}
            class="mt-2 text-[11px] text-text-tertiary hover:text-text-primary transition-colors"
          >
            Retry
          </button>
        </div>
      {:else if filteredSessions.length === 0 && searchQuery}
        <div class="rounded-lg border border-border-default bg-bg-surface p-6 text-center">
          <p class="text-[13px] text-text-secondary">No sessions match "{searchQuery}"</p>
        </div>
      {:else if sessions.length === 0}
        <div class="rounded-lg border border-border-default bg-bg-surface p-6 text-center">
          <p class="text-[13px] text-text-secondary">No sessions yet. Start your first one above.</p>
        </div>
      {:else}
        {#each filteredSessions as session (session.id)}
          <button
            onclick={() => onSelectSession(session.id)}
            class="flex w-full items-center justify-between gap-4 rounded-lg border border-border-default bg-bg-surface p-4 text-left shadow-sm transition-colors hover:border-accent-primary/60 hover:bg-bg-surface-hover"
          >
            <span class="min-w-0 flex-1">
              <span class="block truncate text-[13px] font-medium text-text-primary">
                {session.seed_text || 'Untitled shaping session'}
              </span>
              <span class="mt-2 flex items-center gap-2 text-[11px] text-text-tertiary">
                <span>{relativeDate(session.created_at)}</span>
                <span aria-hidden="true">/</span>
                <span class="inline-flex items-center gap-1 capitalize">
                  <span class="h-2 w-2 rounded-full {session.status === 'active' ? 'bg-green-500' : 'bg-text-tertiary'}"></span>
                  {session.status}
                </span>
              </span>
            </span>
            <span class="shrink-0 rounded-full border border-border-default bg-bg-primary px-2.5 py-1 text-[11px] font-medium text-text-secondary">
              {session.node_count} {session.node_count === 1 ? 'node' : 'nodes'}
            </span>
          </button>
        {/each}
      {/if}
    </div>
  </div>
</div>
