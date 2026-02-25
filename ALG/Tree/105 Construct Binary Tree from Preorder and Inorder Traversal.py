# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: node->left->right, inorder: left->node->right
        if not preorder or not inorder:
            return
        # chop the first one out as root of tree(subtrees)
        root = TreeNode(preorder[0], None, None)
        left_centr = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : left_centr + 1], inorder[ : left_centr])
        root.right = self.buildTree(preorder[left_centr + 1: ], inorder[left_centr + 1 :])
        return root