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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        travel = deque()
        travel.append(root)

        while travel:
            n = len(travel)
            for _ in range(n):
                curr = travel.popleft()
                curr_lh = self.getHeight(curr.left)
                curr_rh = self.getHeight(curr.right)
                if curr_lh - curr_rh > 1 or curr_lh - curr_rh < -1:
                    return False
                if curr.left:
                    travel.append(curr.left)
                if curr.right:
                    travel.append(curr.right)
        return True