# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
        prev = None
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            new_val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            new_node = ListNode(new_val)
            if prev:
                prev.next = new_node
            else:
                dummy.next = new_node
            prev = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            new_node = ListNode(carry)
            prev.next = new_node

        return dummy.next