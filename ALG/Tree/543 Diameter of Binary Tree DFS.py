# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pathes = 0

        # return height, BUT make diameter - "pathes"
        def getHeight(node):
            if not node:
                return 0
            nonlocal pathes
            left_h = getHeight(node.left)
            right_h = getHeight(node.right)
            pathes = max(pathes, left_h + right_h)
            return 1 + max(left_h, right_h)

        getHeight(root)
        return pathes