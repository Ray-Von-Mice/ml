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
        # hashmap for recording each old node to clone new node and visit set
        mp = {}
        traverse = deque()
        mp[node] = Node(node.val)
        traverse.append(node)

        while traverse:
            cur = traverse.popleft()

            for ne in cur.neighbors:
                # clone
                if ne not in mp:
                    mp[ne] = Node(ne.val)
                    traverse.append(ne)
                # connect edges
                mp[cur].neighbors.append(mp[ne])
        
        return mp[node]