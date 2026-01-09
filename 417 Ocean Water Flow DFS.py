class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        1. reversely, water from both pac and atl can reach the valid point:
            pac : upper edge row = 0, left edge col = 0
            atl : bottom edge row = len(heights) - 1, right edge col = len(heights[0] - 1)
            and this height NEED to be higher than previous pt: height(cur) >= prevHeight
        2. data structure represent pac and atl
        3. ultimately, points that's reachable from both pac and atl form the result
        """
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(x, y, prevHt, rOcean) -> None:
            if (x < 0 or x >= rows or y < 0 or y >= cols 
        or heights[x][y] < prevHt or (x, y) in rOcean):
                return
            rOcean.add((x, y))
            dfs(x - 1, y, heights[x][y], rOcean)
            dfs(x + 1, y, heights[x][y], rOcean)
            dfs(x, y - 1, heights[x][y], rOcean)
            dfs(x, y + 1, heights[x][y], rOcean)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)

        result = []
        for rx in range(rows):
            for ry in range(cols):
                if (rx, ry) in pac and (rx, ry) in atl:
                    result.append([rx, ry])

        return result