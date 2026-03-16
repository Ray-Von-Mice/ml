class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = (10**9 + 7)
        coins = [1, 2, 6]
        memo = [[-1] * (n + 1) for _ in range(3)]
        def dfs(indx, remain):
            if remain == 0:
                return 1
            
            if indx >= 3:
                if (remain - 4) == 0 or (remain - 8) == 0:
                    return 1
                return 0
            
            if remain < 0:
                return 0

            if memo[indx][remain] != -1:
                return memo[indx][remain]
            
            result = dfs(indx + 1, remain)
            if remain - coins[indx] >= 0:
                result += dfs(indx, remain - coins[indx])
            
            memo[indx][remain] = result
            return result

        return dfs(0, n) % MOD