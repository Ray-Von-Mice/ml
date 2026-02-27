# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        path, visit = [root], set()
        find_parent = {}
        find_parent[root] = None
        while path:
            curr = path.pop()
            if not curr.left and not curr.right:
                # find the node, disconnect parent
                if curr.val == target:
                    parent = find_parent[curr]
                    # root
                    if not parent: 
                        return None
                    else:
                        if parent.left == curr:
                            parent.left = None
                        else:
                            parent.right = None
            else:
                if curr not in visit:
                    visit.add(curr)
                    path.append(curr)
                    if curr.left:
                        find_parent[curr.left] = curr
                        path.append(curr.left)
                    if curr.right:
                        find_parent[curr.right] = curr
                        path.append(curr.right)
        return root