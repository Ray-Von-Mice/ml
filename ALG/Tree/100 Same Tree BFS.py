# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        travel_p, travel_q = deque([p]), deque([q])
        while travel_p and travel_q:
            for _ in range(len(travel_p)):
                cur_p = travel_p.popleft()
                cur_q = travel_q.popleft()
                
                if not cur_p and not cur_q:
                    continue
                if (not cur_p or not cur_q) or cur_p.val != cur_q.val:
                    return False
                
                travel_p.append(cur_p.left)
                travel_p.append(cur_p.right)
                travel_q.append(cur_q.left)
                travel_q.append(cur_q.right)
        return True