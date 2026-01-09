class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])
        
        # search starts from the 4 banks of the height
        def bfs(oBank, rOcean) -> None:
            travel = deque(oBank)
            while travel:
                cur = travel.popleft()
                rOcean.add((cur[0], cur[1]))
                for dir in directions:
                    nx = cur[0] + dir[0]
                    ny = cur[1] + dir[1]
                    if (nx < 0 or nx >= rows or ny < 0 or ny >= cols
                    or heights[nx][ny] < heights[cur[0]][cur[1]] or (nx, ny) in rOcean):
                        continue
                    travel.append((nx, ny))
        
        pacBank, atlBank = [], []
        # making banks from 2 oceans
        for i in range(rows):
            pacBank.append((i, 0))
            atlBank.append((i, cols - 1))
        
        for j in range(cols):
            pacBank.append((0, j))
            atlBank.append((rows - 1, j))

        bfs(pacBank, pac)
        bfs(atlBank, atl)

        result = []
        for rx in range(rows):
            for ry in range(cols):
                if (rx, ry) in pac and (rx, ry) in atl:
                    result.append([rx, ry])

        return result
            