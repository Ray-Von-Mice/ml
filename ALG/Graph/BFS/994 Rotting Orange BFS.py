class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh, elapse = 0, 0
        rotten = deque()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            tmp = len(rotten)
            for i in range(tmp):
                cur = rotten.popleft()
                x, y = cur[0], cur[1]
                for dir in directions:
                    nx = x + dir[0]
                    ny = y + dir[1]
                    # out of boundries, or NOT fresh -> invalid
                    if (nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1):
                        continue
                    
                    rotten.append((nx, ny))
                    grid[nx][ny] = 2
                    fresh -= 1
            elapse += 1
        
        return -1 if fresh > 0 else elapse