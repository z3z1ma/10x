<script lang="ts">
  export let message: { role: string; content: string; context?: any; timestamp: string };
  export let streaming: boolean = false;

  let showContext = false;

  function formatTime(isoString: string) {
    const date = new Date(isoString);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    if (diffMins < 1) return 'just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h ago`;
    return `${Math.floor(diffHours / 24)}d ago`;
  }

  // Basic markdown formatting
  function formatContent(text: string) {
    if (!text) return '';
    let formatted = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/`(.*?)`/g, '<code class="bg-bg-surface-hover px-1 py-0.5 rounded text-[11px]">$1</code>')
      .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" class="text-text-accent hover:underline" target="_blank">$1</a>')
      .replace(/\n/g, '<br>');
    return formatted;
  }
</script>

<div class="flex flex-col w-full mb-4 group text-[13px]">
  {#if message.role === 'user'}
    <div class="self-end max-w-[85%] flex flex-col items-end">
      {#if message.context}
        <div class="mb-1 text-[11px] text-text-tertiary flex items-center gap-1 cursor-pointer hover:text-text-secondary" on:click={() => showContext = !showContext}>
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
          {message.context.path} (lines {message.context.line_range[0]}-{message.context.line_range[1]})
        </div>
        {#if showContext}
          <div class="mb-2 p-2 bg-bg-surface-hover rounded border border-border-default text-[11px] text-text-secondary max-w-full overflow-x-auto whitespace-pre font-mono">
            {message.context.selected_text}
          </div>
        {/if}
      {/if}
      <div class="bg-bg-accent/10 text-text-primary px-3 py-2 rounded-lg rounded-tr-sm border border-bg-accent/20" title={new Date(message.timestamp).toLocaleString()}>
        {@html formatContent(message.content)}
      </div>
      <div class="text-[10px] text-text-tertiary mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
        {formatTime(message.timestamp)}
      </div>
    </div>
  {:else if message.role === 'system'}
    <div class="self-center text-[11px] text-text-error bg-bg-error/10 px-2 py-1 rounded border border-bg-error/20 my-2">
      {message.content}
    </div>
  {:else}
    <div class="self-start w-full flex flex-col">
      <div class="text-text-primary leading-relaxed">
        {@html formatContent(message.content)}
        {#if streaming}
          <span class="inline-block w-2 h-3 bg-text-primary ml-1 animate-pulse align-middle"></span>
        {/if}
      </div>
      <div class="text-[10px] text-text-tertiary mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
        {formatTime(message.timestamp)}
      </div>
    </div>
  {/if}
</div>
