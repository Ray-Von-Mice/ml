# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        travel, result = deque([root]), []
        while travel:
            n, level = len(travel), []
            for _ in range(n):
                curr = travel.popleft()
                if curr.left:
                    travel.append(curr.left)
                if curr.right:
                    travel.append(curr.right)
                level.append(curr.val)
            result.append(level)
        return result