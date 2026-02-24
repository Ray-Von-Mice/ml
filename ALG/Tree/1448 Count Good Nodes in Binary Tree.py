# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        if root:
            result.append(root.val)
        
        def traverse(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                currMax = node.val
                result.append(node.val)
            
            traverse(node.left, currMax)
            traverse(node.right, currMax)

        traverse(root.left, root.val)
        traverse(root.right, root.val)
        
        return len(result)