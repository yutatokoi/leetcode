class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit_max = max(profit_max, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return profit_max

        
