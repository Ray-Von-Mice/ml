class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        traverse = deque()
        time = 0
        fresh = 0


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    traverse.append((i, j, time))
                elif grid[i][j] == 1:
                    fresh += 1
                else:
                    pass
        # edge cases: no rotten with or without fresh fruit
        if not traverse:
            if fresh:
                return -1
            return 0

        while traverse:
            r, c, t = traverse.popleft()
            time = max(t, time)
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if nr < 0 or nr == ROW or nc < 0 or nc == COL or\
                grid[nr][nc] == 2 or grid[nr][nc] == 0:
                    continue
                grid[nr][nc] = 2
                fresh -= 1
                traverse.append((nr, nc, t + 1))
        
        return -1 if fresh else time