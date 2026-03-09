class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, maxLen = "", 0
        n = len(s)

        def palinUpd(l, r):
            nonlocal result, maxLen
            while (l >= 0 and r < n) and s[l] == s[r]:
                if maxLen < (r - l + 1):
                    result = s[l : r + 1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

        # two pointers initiate at each i, and expand both ways to scan for palindrome
        for i in range(n):
            
            # odd length palindrome
            left, right = i, i
            palinUpd(left, right)

            # even length palindrome
            left, right = i, i + 1
            palinUpd(left, right)

        return result