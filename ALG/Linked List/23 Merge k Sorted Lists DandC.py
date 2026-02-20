# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divideAndConquer(self, left: int, right: int, lists: List[Optional[ListNode]]):
        if left > right:
            return None
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        list_Left = self.divideAndConquer(left, mid, lists)
        list_Right = self.divideAndConquer(mid + 1, right, lists)
        return self.conquer(list_Left, list_Right)
    
    def conquer(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(-1, None)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists is None:
            return None
        
        result = self.divideAndConquer(0, len(lists) - 1, lists)
        return result