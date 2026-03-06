class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [["."] * n for _ in range(n)]
        # same column, same 45 degree diagonal, same 135 degree diagonal
        same_col, same_ffd, same_otfd = set(), set(), set() 

        def dfs(r):
            if r == n:
                serial = "".join(elem for eachrow in board for elem in eachrow)
                result.append(serial)
                return
            
            for col in range(n):
                ffd, otfd = r - col, r + col
                if col in same_col or ffd in same_ffd or otfd in same_otfd:
                    continue
                
                board[r][col] = "Q"
                same_col.add(col)
                same_ffd.add(ffd)
                same_otfd.add(otfd)
                dfs(r + 1)
                board[r][col] = "."
                same_col.remove(col)
                same_ffd.remove(ffd)
                same_otfd.remove(otfd)
            
        dfs(0)
        return len(result)