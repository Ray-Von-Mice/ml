class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # memo[i] -> fewest number of coins to reach amount i
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in memo:
                return memo[remain]
            
            curMinCombs = float("inf")
            for coin in coins:
                combs = dfs(remain - coin)
                if combs == -1:
                    continue
                curMinCombs = min(curMinCombs, combs + 1)
            memo[remain] = -1 if curMinCombs == float("inf") else curMinCombs
            return memo[remain]

        return dfs(amount)