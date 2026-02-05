class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left for buy, right for sell
        left, right = 0, 0
        maxProfit, n = 0, len(prices)
        while right < n:
            # making profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            # if prices[right] < prices[left], right become new buying point
            else:
                left = right
            right += 1
        
        return maxProfit