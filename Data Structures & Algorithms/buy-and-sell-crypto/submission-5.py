class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        curr_min = float('inf')

        for price in prices:
            if price < curr_min:
                curr_min = price
            res = max(res, price - curr_min)
        
        return res
        