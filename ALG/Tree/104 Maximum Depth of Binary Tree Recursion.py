# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        return max(self.depth(node.left) + 1, self.depth(node.right) + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.depth(root)