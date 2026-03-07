class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top is index n
        cost.append(0)
        n = len(cost)
        
        # in order to reach n, old index n - 1 pay for itself, so start from old n - 2 (new n -3)
        for i in range(n - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])