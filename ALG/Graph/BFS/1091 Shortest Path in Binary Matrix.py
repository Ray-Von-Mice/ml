class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            print("A")
            return -1
        visit = set()
        visit.add((0, 0))
        length = 1
        traverse = deque()
        traverse.append((0, 0, length))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1]]

        while traverse:

            r, c, path_len = traverse.popleft()
            if r == n - 1 and c == n - 1:
                return path_len

            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if nr < 0 or nr == n or nc < 0 or nc == n or \
                (nr, nc) in visit or grid[nr][nc] == 1:
                    continue

                
                traverse.append((nr, nc, path_len + 1))
                visit.add((nr, nc))

        return -1