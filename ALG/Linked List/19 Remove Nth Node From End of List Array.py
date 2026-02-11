# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        sz = 0
        while curr:
            nodes.append(curr)
            sz += 1
            curr = curr.next
        
        if sz - n == 0:
            return head.next
        index = sz - n
        nodes[index - 1].next = nodes[index + 1] if index + 1 < sz else None
        return head