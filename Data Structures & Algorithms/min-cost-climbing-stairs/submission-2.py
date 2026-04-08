class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]
        
        dfs(0)
        return min(dp[0], dp[1])
        
