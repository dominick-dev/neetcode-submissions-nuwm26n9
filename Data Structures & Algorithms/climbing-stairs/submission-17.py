class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {} # key:n val:res
        dp[0] = 1
        dp[1] = 1

        def dfs(n):
            if n in dp: return dp[n]

            dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]
        
        dfs(n)
        return dp[n]
