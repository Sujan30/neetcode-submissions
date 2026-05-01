class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0

        low = 10000000

        for i in range(1, len(prices)):
            if prices[i-1] < low:
                low = prices[i-1]
            profit_max = max(profit_max, prices[i] - low)

        return profit_max