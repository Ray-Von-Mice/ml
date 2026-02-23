# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)

        curr, slow = root, None
        while curr:
            slow = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        if slow.val > val:
            slow.left = TreeNode(val, None, None)
        if slow.val < val:
            slow.right = TreeNode(val, None, None)

        return root