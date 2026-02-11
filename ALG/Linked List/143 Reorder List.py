# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow.next is the head of the second half, need to disconnect slownext two parts
        newHead = slow.next
        slow.next = None

        # reverse second half
        prev, curr = None, newHead
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # now pre is the head of the reversed second half
        l1, l2 = head, prev
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2