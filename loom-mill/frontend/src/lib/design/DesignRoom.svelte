<script lang="ts">
  import { store } from '../ws.svelte';
  import { apiUrl } from '../api';
  import GraphSidebar from './GraphSidebar.svelte';
  import DocumentEditor from './DocumentEditor.svelte';
  import ChatPanel from './ChatPanel.svelte';

  let selectedDocumentId = $state<string | null>(null);
  let chatContext = $state<any>(null);

  function handleAttachContext(context: { path: string, selected_text: string, line_range: [number, number] }) {
    chatContext = context;
  }

  async function handleCreateRecord(surface: string) {
    try {
      const response = await fetch(apiUrl('/records'), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ surface })
      });
      
      if (response.ok) {
        const data = await response.json();
        if (data.path) {
          selectedDocumentId = data.path;
        }
      } else {
        console.error('Failed to create record:', await response.text());
      }
    } catch (err) {
      console.error('Error creating record:', err);
    }
  }

  async function handleSaveDocument(content: string) {
    if (!selectedDocumentId) return;
    
    try {
      const response = await fetch(apiUrl(`/records/${encodeURIComponent(selectedDocumentId)}`), {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
      });
      
      if (!response.ok) {
        console.error('Failed to save record:', await response.text());
      }
    } catch (err) {
      console.error('Error saving record:', err);
    }
  }
</script>

<div class="flex h-full w-full overflow-hidden">
  <!-- Left: Graph sidebar -->
  <div class="w-60 shrink-0 border-r border-border-default overflow-y-auto bg-bg-surface flex flex-col">
    <GraphSidebar 
      records={store.state.records} 
      selectedId={selectedDocumentId} 
      onSelect={(id) => selectedDocumentId = id}
      onCreateRecord={handleCreateRecord}
    />
  </div>
  
  <!-- Center: Document editor -->
  <div class="flex-1 min-w-0 flex flex-col">
    <DocumentEditor 
      documentPath={selectedDocumentId} 
      onSave={handleSaveDocument} 
      onAttachContext={handleAttachContext}
    />
  </div>
  
  <!-- Right: Chat panel -->
  <div class="w-[360px] shrink-0 border-l border-border-default flex flex-col bg-bg-surface">
    <ChatPanel 
      documentPath={selectedDocumentId} 
      attachedContext={chatContext}
      onClearContext={() => chatContext = null}
    />
  </div>
</div>
