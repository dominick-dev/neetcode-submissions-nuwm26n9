class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_min = prices[0]

        for price in prices:
            if price < curr_min:
                curr_min = price
            res = max(res, price - curr_min)
        
        return res
        