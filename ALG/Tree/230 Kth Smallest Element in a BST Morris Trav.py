# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            # if no left sub stree, "visit" current node and move to the right
            if not curr.left:
                # "visit": decrease k, if k becomes 0 return val
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            
            # if there is left sub stree, find its inorder predecessor
            else:
                # find inorder predecessor
                prdsr = curr.left
                while prdsr.right and prdsr.right != curr:
                    prdsr = prdsr.right
                # if prdsr has no right subtree, link it with current node (prdsr's successor) then move current to current left
                if not prdsr.right:
                    prdsr.right = curr
                    curr = curr.left
                # if prdsr has right subtree, meaning traversed through before and linked it with successor
                # cut the link, "visit it" and move current to current right
                else:
                    prdsr.right = None
                    # "visit": decrease k, if k becomes 0 return val
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1