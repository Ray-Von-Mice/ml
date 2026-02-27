# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def calc(node) -> int:
            if not node:
                return 0
            nonlocal result
            left_res = max(calc(node.left), 0 )
            right_res = max(calc(node.right), 0)
            # update result for calculating result from both substree
            result = max(result, left_res + right_res + node.val)

            # definition of path dictate when you return, you can only choose one path from left or right
            # path is NOT result
            return node.val + max(left_res, right_res)
        
        calc(root)
        return result