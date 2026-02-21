# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getkthNode(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev_tail = dummy
        while True:
            kth_node = self.getkthNode(prev_tail, k)
            if kth_node == None:
                break
            next_head = kth_node.next

            # prev need to be initialized to link each reversed sub lists
            prev, curr = kth_node.next, prev_tail.next
            while curr != next_head:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # capture reversed tail, connect prev tail with reversed head, moving prev tail for next iteration
            r_tail = prev_tail.next
            prev_tail.next = prev
            prev_tail = r_tail
        
        return dummy.next