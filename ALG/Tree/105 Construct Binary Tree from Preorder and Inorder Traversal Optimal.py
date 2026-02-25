# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_d, n = {}, len(preorder)
        for indx, value in enumerate(inorder):
            inorder_d[value] = indx
        
        curr_index = 0
        def depthTraverse(left, right):
            if left > right:
                return None
            nonlocal curr_index
            curr_value = preorder[curr_index]
            curr = TreeNode(curr_value)
            curr_index += 1
            centr = inorder_d[curr_value]
            curr.left = depthTraverse(left, centr - 1)
            curr.right = depthTraverse(centr + 1, right)
            return curr
        
        return depthTraverse(0, n - 1)