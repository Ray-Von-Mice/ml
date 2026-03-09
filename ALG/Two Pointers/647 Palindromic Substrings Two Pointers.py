class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        def palindUpd(l, r) -> None:
            nonlocal result
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        
        for i in range(n):
            # odd length palindrome
            left, right = i, i
            palindUpd(left, right)

            # even length palindrome
            left, right = i, i + 1
            palindUpd(left, right)
        
        return result