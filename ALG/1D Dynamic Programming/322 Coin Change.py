class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            choose any coin -> 1 + solution[amount - chosen]
            amount 11, coins [1, 2, 5]
            chose 1 -> 1 + solution[10] -> chose 1: 1 + solution[9] or 2: 1 + solution[7] or 5: 1 + solution[5]
            chose 2 -> 1 + solution[9] -> ...
            chose 5 -> 1 + solution[6] -> ...
        '''

        solution = [float("inf")] * (amount + 1)
        solution[0] = 0
        for num in range(1, amount + 1):
            for cn in coins:
                change = num - cn
                if change >= 0:
                    solution[num] = min(solution[num], 1 + solution[change])
        
        if solution[amount] == float("inf"):
            return -1
        return solution[amount]