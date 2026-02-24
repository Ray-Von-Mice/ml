"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # each grid represented by its topleft coordinates (at which point it starts)
        def depthTraverse(n, row, col) -> 'Node':
            sameVals, value = True, grid[row][col]
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        sameVals = False
                        break
            # same values, leaf
            if sameVals == True:
                return Node(value, True, None, None, None, None)
            # not all same values, not leaf
            halv = n // 2
            topLeft_n = depthTraverse(halv, row, col)
            topRight_n = depthTraverse(halv, row, col + halv)
            bottomLeft_n = depthTraverse(halv, row + halv, col)
            bottomRight_n = depthTraverse(halv, row + halv, col + halv)
            return Node(0, False, topLeft_n, topRight_n, bottomLeft_n, bottomRight_n)

        return depthTraverse(len(grid), 0, 0)