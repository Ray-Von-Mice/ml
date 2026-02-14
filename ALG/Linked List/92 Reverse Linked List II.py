# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        p = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = p
            p = curr
            curr = tmp
        
        # prev.next still points to original pos[left] node, now the reversed tail
        reversedTail = prev.next

        # disconnect and points prev.next to the reversed head, p
        prev.next = p
        reversedTail.next = curr

        return dummy.next
