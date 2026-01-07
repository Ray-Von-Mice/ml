class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
        islandMax = 0
        rows, cols = len(grid), len(grid[0])

        def helper(r, c) -> int:
            visiting = deque()
            pt = (r, c)
            visiting.append(pt)

            # 2 as visited
            grid[r][c] = 2
            island = 1

            while visiting:
                cur = visiting.popleft()
                for dir in directions:
                    curn_x = cur[0] + dir[0]
                    curn_y = cur[1] + dir[1]

                    # out of boundries, water, visited
                    if (curn_x < 0 or curn_x >= rows or curn_y < 0 or curn_y >= cols or grid[curn_x][curn_y] == 0 
                    or grid[curn_x][curn_y] == 2):
                        continue
                    
                    visiting.append((curn_x, curn_y))
                    grid[curn_x][curn_y] = 2
                    island += 1
            return island
        
        for rw in range(rows):
            for cl in range(cols):
                if (grid[rw][cl] == 1):
                    islandMax = max(islandMax, helper(rw, cl))
        
        return islandMax

