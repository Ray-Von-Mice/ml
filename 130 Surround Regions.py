class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        
        # mark all 'O's that are connecting to edge as 'M'
        def bfs():
            travel = deque()
            # search and record all 'O's on edge, as BFS starting points
            for i in range(rows):
                for j in range(cols):
                    if ((i == 0 or i == rows - 1 or j == 0 or j == cols - 1) 
                    and board[i][j] == 'O'):
                        travel.append((i, j))

            while travel:
                cur = travel.popleft()
                x, y = cur[0], cur[1]
                
                if (board[x][y] == 'O'):
                    board[x][y] = 'M'
                    for dir in directions:
                        nx, ny = x + dir[0], y + dir[1]
                        if (nx < 0 or nx >= rows or ny < 0 or ny >= cols or 
                        board[nx][ny] == 'X'):
                            continue
                        travel.append((nx, ny))

        bfs()

        # flip 'M' to 'O', 'O'(not connecting to edge) to 'X' 
        for px in range(rows):
            for py in range(cols):
                if board[px][py] == 'M':
                    board[px][py] = 'O'
                elif board[px][py] == 'O':
                    board[px][py] = 'X'