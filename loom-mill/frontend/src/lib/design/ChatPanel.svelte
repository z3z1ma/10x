<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { store } from '../ws.svelte';
  import { apiUrl } from '../api';
  import ChatMessage from './ChatMessage.svelte';
  import ChatInput from './ChatInput.svelte';

  export let documentPath: string | null = null;
  export let attachedContext: any = null;
  export let onClearContext: () => void;

  let messagesContainer: HTMLDivElement;
  let isCreatingSession = false;

  // Auto-scroll when messages change
  $: if (store.chatSession.messages.length || store.chatSession.streamingContent) {
    scrollToBottom();
  }

  async function scrollToBottom() {
    await tick();
    if (messagesContainer) {
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
  }

  async function createSession() {
    if (isCreatingSession) return;
    isCreatingSession = true;
    
    try {
      const response = await fetch(apiUrl('/chat/sessions'), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          document_path: documentPath
        })
      });
      
      if (response.ok) {
        const data = await response.json();
        store.chatSession.id = data.session_id;
        store.chatSession.messages = [];
        store.chatSession.streamingContent = '';
        store.chatSession.streaming = false;
      } else {
        console.error('Failed to create chat session:', await response.text());
        store.chatSession.messages.push({
          role: 'system',
          content: 'Failed to create chat session. Is the harness running?',
          timestamp: new Date().toISOString()
        });
      }
    } catch (err) {
      console.error('Error creating chat session:', err);
      store.chatSession.messages.push({
        role: 'system',
        content: 'Error connecting to chat backend.',
        timestamp: new Date().toISOString()
      });
    } finally {
      isCreatingSession = false;
    }
  }

  async function handleSend(text: string, context?: any) {
    if (!store.chatSession.id) {
      await createSession();
      if (!store.chatSession.id) return; // Failed to create
    }

    // Optimistic update
    const userMessage = {
      role: 'user',
      content: text,
      context,
      timestamp: new Date().toISOString()
    };
    store.chatSession.messages = [...store.chatSession.messages, userMessage];

    try {
      const response = await fetch(apiUrl(`/chat/sessions/${store.chatSession.id}/messages`), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          content: text,
          context
        })
      });

      if (!response.ok) {
        console.error('Failed to send message:', await response.text());
        store.chatSession.messages = [...store.chatSession.messages, {
          role: 'system',
          content: 'Failed to send message.',
          timestamp: new Date().toISOString()
        }];
      }
    } catch (err) {
      console.error('Error sending message:', err);
      store.chatSession.messages = [...store.chatSession.messages, {
        role: 'system',
        content: 'Network error sending message.',
        timestamp: new Date().toISOString()
      }];
    }
  }

  onMount(() => {
    if (!store.chatSession.id) {
      createSession();
    }
  });
</script>

<div class="flex flex-col h-full w-full bg-bg-surface">
  <!-- Header -->
  <div class="flex items-center justify-between h-8 px-4 border-b border-border-default shrink-0">
    <div class="text-[11px] font-medium text-text-secondary">Chat</div>
    <button 
      class="text-[10px] text-text-tertiary hover:text-text-primary transition-colors"
      on:click={createSession}
      disabled={isCreatingSession || store.chatSession.streaming}
    >
      New Session
    </button>
  </div>

  <!-- Messages Area -->
  <div 
    bind:this={messagesContainer}
    class="flex-1 overflow-y-auto p-4 flex flex-col gap-2"
  >
    {#if store.chatSession.messages.length === 0 && !store.chatSession.streamingContent}
      <div class="flex-1 flex flex-col items-center justify-center text-center text-text-tertiary p-4">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mb-2 opacity-50"><path d="M14 9a2 2 0 0 1-2 2H6l-4 4V4c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v5Z"/><path d="M18 9h2a2 2 0 0 1 2 2v11l-4-4h-6a2 2 0 0 1-2-2v-1"/></svg>
        <p class="text-[12px]">Shape work with the AI harness.</p>
        <p class="text-[11px] mt-1 opacity-70">Select text in the editor to attach context.</p>
      </div>
    {:else}
      {#each store.chatSession.messages as message}
        <ChatMessage {message} />
      {/each}
      
      {#if store.chatSession.streamingContent}
        <ChatMessage 
          message={{ role: 'assistant', content: store.chatSession.streamingContent, timestamp: new Date().toISOString() }} 
          streaming={true} 
        />
      {/if}
    {/if}
  </div>

  <!-- Input Area -->
  <ChatInput 
    onSend={handleSend} 
    disabled={store.chatSession.streaming || isCreatingSession} 
    {attachedContext}
    {onClearContext}
  />
</div>
