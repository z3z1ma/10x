export interface LayoutNode {
  id: string;
  parent_id: string | null;
  position: { x: number; y: number } | null;
  status?: string;
}

export interface LayoutResult {
  positions: Record<string, { x: number; y: number }>;
}

export function computeTreeLayout(nodes: LayoutNode[], edges: any[]): LayoutResult {
  const positions: Record<string, { x: number; y: number }> = {};
  
  // 1. Build adjacency
  const childrenMap: Record<string, string[]> = {};
  const nodeMap: Record<string, LayoutNode> = {};
  
  nodes.forEach(n => {
    nodeMap[n.id] = n;
    childrenMap[n.id] = [];
  });
  
  const roots: string[] = [];
  nodes.forEach(n => {
    if (n.parent_id && nodeMap[n.parent_id]) {
      childrenMap[n.parent_id].push(n.id);
    } else {
      roots.push(n.id);
    }
  });
  
  // 2. Assign layers (depth from root)
  const depths: Record<string, number> = {};
  function assignDepth(nodeId: string, depth: number) {
    depths[nodeId] = depth;
    childrenMap[nodeId].forEach(childId => assignDepth(childId, depth + 1));
  }
  roots.forEach(r => assignDepth(r, 0));
  
  // 3. Assign X coordinates
  let nextLeafX = 0;
  
  function assignX(nodeId: string): number {
    const node = nodeMap[nodeId];
    const children = childrenMap[nodeId];
    
    let x: number;
    
    if (children.length === 0) {
      // Leaf node
      if (node.position) {
        x = node.position.x;
        nextLeafX = Math.max(nextLeafX, x + 250);
      } else {
        x = nextLeafX;
        nextLeafX += 250;
      }
    } else {
      // Parent node
      let sumX = 0;
      children.forEach(childId => {
        sumX += assignX(childId);
      });
      
      if (node.position) {
        x = node.position.x;
      } else {
        x = sumX / children.length;
      }
    }
    
    positions[nodeId] = {
      x,
      y: node.position ? node.position.y : (depths[nodeId] * 150 + 50)
    };
    
    return x;
  }
  
  roots.forEach(r => assignX(r));
  
  // 5. Center parents over their children (already done by average)
  // 6. Handle nodes with saved positions (pinned) — skip them, layout around them (handled by using node.position)
  
  // Adjust root to start at (400, 50) if it's not pinned
  if (roots.length > 0) {
    const firstRoot = roots[0];
    if (!nodeMap[firstRoot].position) {
      const shiftX = 400 - positions[firstRoot].x;
      Object.keys(positions).forEach(id => {
        if (!nodeMap[id].position) {
          positions[id].x += shiftX;
        }
      });
    }
  }
  
  return { positions };
}
