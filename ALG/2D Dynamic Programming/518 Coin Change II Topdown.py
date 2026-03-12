class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        solutions = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(indx, total):
            if total == 0:
                return 1
            if indx >= n:
                return 0
            
            if solutions[indx][total] != -1:
                return solutions[indx][total]
            
            result = 0
            if total >= coins[indx]:
                result += dfs(indx + 1, total)
                result += dfs(indx, total - coins[indx])
            
            solutions[indx][total] = result
            return result

        return dfs(0, amount)