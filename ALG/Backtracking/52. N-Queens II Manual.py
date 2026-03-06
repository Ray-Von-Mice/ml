class Solution:
    def isValid(self, rw: int, cl: int, board: List[List[str]]) -> bool:
        # check same column
        row = rw - 1
        while row >= 0:
            if board[row][cl] == "Q":
                return False
            row -= 1
        
        # check 45 degree diagonal
        row, col = rw - 1, cl - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        # check 135 degree diagonal
        row, col = rw - 1, cl + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True
    
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                serial = "".join(elem for eachrow in board for elem in eachrow)
                result.append(serial)
                return
            
            for col in range(n):
                if self.isValid(r, col, board):
                    board[r][col] = "Q"
                    dfs(r + 1)
                    board[r][col] = "."
            
        dfs(0)
        return len(result)