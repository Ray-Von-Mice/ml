class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = [[False] * n for _ in range(m)]

        def dfs(r, c, indx):
            if indx == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            if board[r][c] != word[indx] or visit[r][c] == True:
                return False
            
            visit[r][c] = True
            res1 = dfs(r + 1, c, indx + 1) 
            res2 = dfs(r, c + 1, indx + 1) 
            res3 = dfs(r - 1, c, indx + 1)
            res4 = dfs(r, c - 1, indx + 1)
            visit[r][c] = False
            return (res1 or res2 or res3 or res4)
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False