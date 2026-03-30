class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {} #key=amount val=min num coins 
        
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            # base case
            if amount == 0:
                dp[0] = 0
                return 0
        
            # init to max
            res = float('inf')

            # iterate through each coin
            for c in coins:
                # need more coins
                if amount - c >= 0:
                    curr_amount = 1 + dfs(amount - c)
                    res = min(res, curr_amount)
            
            dp[amount] = res
            return res

        result = dfs(amount)

        return result if result < float('inf') else -1


