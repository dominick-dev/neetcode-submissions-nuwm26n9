class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # init dp array
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        # iterate through each amount
        for a in range(1, amount + 1):
            # iterate through each coin
            for c in coins:
                # update dp if coin doesn't overshoot
                if a - c  >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != float('inf') else -1
