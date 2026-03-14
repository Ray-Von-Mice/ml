class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        # for each coin, we have 0 to amount numbers we can reach; memo[i][num] how many ways we can reach num using coins from 0 to i
        # hence the one extra row for explicit 0 index
        memo = [[0] * (amount + 1) for _ in range(n + 1)]

        # only one way to form amount 0 for each coin, not picking
        for i in range(n + 1):
            memo[i][0] = 1

        for i in range(1, n + 1):
            # cur coin represent coins from 0 to i - 1, first i coins
            cur_coin = coins[i - 1]
            for num in range(amount + 1):
                # skip current coin, use the accumulative number before
                memo[i][num] = memo[i - 1][num]

                # if cur_coin is valid, use it and deduct its value from current number
                if num - cur_coin >= 0:
                    memo[i][num] += memo[i][num - cur_coin]

        return memo[n][amount]