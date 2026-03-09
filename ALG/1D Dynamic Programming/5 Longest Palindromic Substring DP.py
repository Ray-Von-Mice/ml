class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, maxLen = "", 0
        n = len(s)
        # isPalind[i][j] for if s[i to j] is palindrome
        isPalind = [[False] * n for _ in range(n)]

        # scanning backwards for avoiding isPalind[i + 1][j - 1] is palindrom but haven't updated
        # when reach "bab" substr, bab is palin, but a at index 1 has not been updated if loop start from 0 to n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 2 or isPalind[i + 1][j - 1]):
                    isPalind[i][j] = True
                    if maxLen < (j - i + 1):
                        result = s[i : j + 1]
                        maxLen = j - i + 1
        
        return result