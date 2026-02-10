class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(rooms), len(rooms[0])
        EMPTY = 2147483647

        travel = deque()
        # only travel valid point, the gate
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    travel.append((i, j))

        # only gate in travel queue, neighbor will be updated (+1) based on gate (value 0)
        while travel:
            vpt = travel.popleft()
            x, y = vpt[0], vpt[1]
            for dir in directions:
                nx = x + dir[0]
                ny = y + dir[1]
                if (nx < 0 or nx >= rows or ny < 0 or ny >= cols 
                or rooms[nx][ny] != EMPTY):
                    continue
                rooms[nx][ny] = rooms[x][y] + 1
                travel.append((nx, ny))
        return