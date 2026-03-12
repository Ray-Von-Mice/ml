class Solution:
    def numSquares(self, n: int) -> int:
        solutions = defaultdict(int)

        def dfs(target):
            if target == 0:
                return 0
            if target in solutions:
                return solutions[target]
            
            result = target
            for num in range(1, target + 1):
                if num * num > target:
                    break
                result = min(result, 1 + dfs(target - num * num))
            solutions[target] = result
            
            return result
        dfs(n)
        return solutions[n]