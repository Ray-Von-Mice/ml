class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            similar to climb stairs, to reach the top (len(s) + 1), use the 'stairs' define in wordDicts
            the final result, is dp[0] -> can we reach top from the beginning
        '''
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i] == True:
                    break
        
        return dp[0]