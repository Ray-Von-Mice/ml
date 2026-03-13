class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mp = [(1 , costs[0]), (7 , costs[1]), (30 , costs[2])]
        memo = [-1] * max(days)
        def dfs(indx):
            if indx == len(days):
                return 0

            if memo[indx] != -1:
                return memo[indx]
            
            result = float("inf")
            j = indx
            for duration, cost in mp:
                while j < n and days[j] < days[indx] + duration:
                    j += 1
                result = min(result, cost + dfs(j))
            memo[indx] = result
            return result
        
        return dfs(0)