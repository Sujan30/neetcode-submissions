class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit_max = max(prices[j]- prices[i], profit_max)
        
        return profit_max