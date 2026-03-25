class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        traverse = deque()
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(ROW):
            for j in range(COL):
                if mat[i][j] == 0:
                    traverse.append((i, j))
                    visit.add((i, j))

        dst = 1
        while traverse:
            n = len(traverse)

            for _ in range(n):
                r, c = traverse.popleft()

                for dir in directions:
                    nr, nc = r + dir[0], c + dir[1]
                    if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or (nr, nc) in visit:
                        continue
                    mat[nr][nc] = dst
                    traverse.append((nr, nc))
                    visit.add((nr, nc))
            dst += 1

        return mat