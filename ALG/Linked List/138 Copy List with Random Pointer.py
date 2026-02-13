"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        mp = {}
        curr = head
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            # mapping old nodes with respective new nodes
            mp[curr] = new_node
            curr = curr.next
        
        
        dummy = Node(100001)
        curr = head
        dummy.next = mp[curr]
        # connect each next and random ptr based on old nodes
        while curr:
            mp[curr].next = mp[curr.next] if curr.next else None
            mp[curr].random = mp[curr.random] if curr.random else None
            curr = curr.next

        return dummy.next