class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i] - mn
            mn = min(prices[i], mn)
            profit = max(profit, p)
        return profit