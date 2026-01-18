class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col, square
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        height, width = len(board), len(board[0])
        for r in range(height):
            for c in range(width):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        
        return True