class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        # for each coin, we have 0 to amount numbers we can reach; memo[i][num] how many ways we can reach num using coins[i]
        memo = [[-1] * (amount + 1) for _ in range(n)]

        def dfs(indx, remain):
            if remain == 0:
                return 1
            if indx >= n or remain < 0:
                return 0
            if memo[indx][remain] != -1:
                return memo[indx][remain]
            
            count = 0
            if remain - coins[indx] >= 0:
                # skip current index, move to next coin
                count += dfs(indx + 1, remain)
                # pick current indx, remain deduct current coin value
                count += dfs(indx, remain - coins[indx])
            
            memo[indx][remain] = count
            return count
        
        return dfs(0, amount)