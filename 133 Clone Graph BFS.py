"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copyNew = {}
        copyNew[node] = Node(node.val)
        visiting = deque()
        visiting.append(node)

        while visiting:
            cur = visiting.popleft()
            for neb in cur.neighbors:
                # if neighbor is not copied, copy and visit it
                if neb not in copyNew:
                    copyNew[neb] = Node(neb.val)
                    visiting.append(neb)
                
                # add copied neighbor to copied current node
                copyNew[cur].neighbors.append(copyNew[neb])
    
        return copyNew[node]