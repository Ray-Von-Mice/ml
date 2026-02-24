# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def verifyTree(lowerbound, upperbound, node) -> bool:
            if not node:
                return True
            if lowerbound >= node.val or upperbound <= node.val:
                return False

            subTree_l = verifyTree(lowerbound, node.val, node.left)
            subTree_r = verifyTree(node.val, upperbound, node.right)
            return subTree_l and subTree_r
        
        return verifyTree(float("-inf"), float("inf"), root)