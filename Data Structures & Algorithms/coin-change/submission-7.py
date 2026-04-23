class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0} # key:amount val:num ways

        def dp(amount):
            if amount in memo:
                return memo[amount]

            mn = float('inf')
            for c in coins:
                if amount - c >= 0:
                    mn = min(mn, dp(amount - c))
            
            memo[amount] = 1 + mn
            return 1 + mn
            
        dp(amount)
        return memo[amount] if memo[amount] != float('inf') else -1
