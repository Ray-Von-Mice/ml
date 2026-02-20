# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or (len(lists) == 1 and lists[0] == None):
            return None
        mp = PriorityQueue()
        for i in range(len(lists)):
            tmp = lists[i]
            while tmp:
                mp.put(tmp.val)
                tmp = tmp.next

        dummy = ListNode(-1, None)
        curr = dummy
        while not mp.empty():
            node = ListNode(mp.get(), None)
            curr.next = node
            curr = node
        return dummy.next
