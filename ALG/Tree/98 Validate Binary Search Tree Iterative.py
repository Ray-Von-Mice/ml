# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        travel = deque([(root, float("-inf"), float("inf"))])
        while travel:
            n = len(travel)
            for _ in range(n):
                curr, low, upper = travel.popleft()
                if low >= curr.val or curr.val >= upper:
                    return False
                if curr.left:
                    travel.append((curr.left, low, curr.val))
                if curr.right:
                    travel.append((curr.right, curr.val, upper))
        
        return True