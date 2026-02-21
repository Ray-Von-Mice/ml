# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        travel = deque()
        travel.append(root)
        depth = 0
        while travel:
            n = len(travel)
            for i in range(n):
                curr = travel.popleft()
                if curr.left:
                    travel.append(curr.left)
                if curr.right:
                    travel.append(curr.right)
            depth += 1
        return depth