class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            if buy < sell:
                result = max(result, sell - buy)
            else:
                l = r
            r += 1

        return result

