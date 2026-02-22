# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        # get height, but update result
        def getHeight(node):
            if not node:
                return 0
            nonlocal result
            height_l = getHeight(node.left)
            height_r = getHeight(node.right)
            if height_l - height_r > 1 or height_l - height_r < -1:
                result = False
            return 1 + max(height_l, height_r)
        
        getHeight(root)
        return result