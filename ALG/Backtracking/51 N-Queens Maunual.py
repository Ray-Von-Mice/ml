class Solution:
    def isValid(self, rw: int, cl: int, board: List[List[str]]) -> bool:
        # check same colum above this
        row = rw - 1
        while row >= 0:
            if board[row][cl] == "Q":
                return False
            row -= 1
        
        # reset row number and check 45 degree diagonal
        row, col = rw - 1, cl - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # reset row and column number and check 135 degree diagonal
        row, col = rw - 1, cl + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        
        def dfs(row):
            if row == n:
                tmp = ["".join(eachrow) for eachrow in board]
                result.append(tmp)
                return
            

            for col in range(n):
                # check if the point is valid, but looking at the points that have been through
                if self.isValid(row, col, board):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."
                
        dfs(0)
        return result