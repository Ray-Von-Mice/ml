# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # pair {index on current level, node}
        traverse = deque([(0, root)])
        result = 0
        while traverse:
            n, cur_max_index = len(traverse), 0
            lvl_first_index, lvl_head = traverse[0]
            for _ in range(n):
                cur_lvl_index, node = traverse.popleft()
                cur_max_index = cur_lvl_index
                # feature of bfs, left child index = parent's index * 2, right = parent's index * 2 + 1
                if node.left:
                    traverse.append((cur_lvl_index * 2, node.left))
                if node.right:
                    traverse.append((2 * cur_lvl_index + 1, node.right))
            result = max(cur_max_index - lvl_first_index + 1, result)

        return result