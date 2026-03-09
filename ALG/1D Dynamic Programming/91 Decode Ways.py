class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        # standing at i, looking backwards how many ways to reach current pos (1 digit only or both 1 and 2 digits)
        for i in range(2, n + 1):
            if "1" <= s[i - 1] <= "9":
                dp[i] += dp[i - 1]
            two_digits = s[i - 2: i]
            if "10" <= two_digits <= "26":
                dp[i] += dp[i - 2]
        
        return dp[n]