# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_h = self.getHeight(root.left)
        right_h = self.getHeight(root.right)
        d = left_h + right_h
        subtree_d = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(d, subtree_d)