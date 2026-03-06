class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column, ffd, otfd = set(), set(), set() # ffd - forty five diagonal, otf - one thirty five diagonal
        result = []
        board = [["."] * n for _ in range(n)]
        
        def dfs(row):
            if row == n:
                tmp = ["".join(eachrow) for eachrow in board]
                result.append(tmp)
                return
            

            for col in range(n):
                # check if same column, same 45 degree diag, same 135 degree diag
                same_ffd, same_otfd = row - col, row + col
                if col in column or same_ffd in ffd or same_otfd in otfd:
                    continue
                
                board[row][col] = "Q"
                column.add(col)
                ffd.add(same_ffd)
                otfd.add(same_otfd)
                dfs(row + 1)

                board[row][col] = "."
                column.remove(col)
                ffd.remove(same_ffd)
                otfd.remove(same_otfd)
                
        dfs(0)
        return result