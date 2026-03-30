class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        curr_min = prices[0]

        if len(prices) == 1:
            return 0

        for price in prices[1:]:
            if price < curr_min:
                curr_min = price
            curr_profit = price - curr_min
            res = max(res, curr_profit)
        
        return res

        