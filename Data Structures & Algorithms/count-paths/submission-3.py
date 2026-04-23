class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # key:i, j val:num ways
        memo[(0, 0)] = 1

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == 0 or j == 0:
                memo[(i, j)] = 1
                return 1
            elif i < 0 or j < 0:
                memo[(i, j)] = 0
                return 0
            else:
                memo[(i, j)] = dp(i-1, j) + dp(i, j-1)

            return memo[(i, j)]

        dp(m-1, n-1)
        return memo[m-1, n-1]
        