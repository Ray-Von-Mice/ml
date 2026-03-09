class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        # 2d array to record whether s[i : j + 1] is palindrome
        isPalind = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 2 or isPalind[i + 1][j - 1]):
                    isPalind[i][j] = True
                    result += 1
        
        return result