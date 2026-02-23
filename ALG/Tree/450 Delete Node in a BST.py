# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        curr, parent = root, None
        while curr and curr.val != key:
            parent = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        # key not found
        if not curr:
            return root
        
        # one or none subtree
        if not curr.left or not curr.right: 
            tmp = curr.left if curr.left else curr.right
            # if parent is None, then delelting root
            if not parent:
                return tmp
            if curr.left:
                tmp = curr.left
                curr.left = None
                
            elif curr.right:
                tmp = curr.right
                curr.right = None

            else:
                pass
            
            if parent.left == curr:
                parent.left = tmp
            else:
                parent.right = tmp
        # two children of deletion node
        else:
            delNode, parsub = curr, None
            curr = curr.right
            while curr.left:
                parsub = curr
                curr = curr.left
            
            if parsub:
                parsub.left = curr.right if curr.right else None
                curr.right = delNode.right
                curr.left = delNode.left
                
            else:
                curr.left = delNode.left
            
            delNode.left, delNode.right = None, None
            # if parent is None, then delelting root
            if not parent:
                return curr

            if parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr
            
        return root