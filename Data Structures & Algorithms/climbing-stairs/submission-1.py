class Solution:
    def climbStairs(self, n: int) -> int:
        c = {}

        def helper(n):
            if n == 2:
                c[2] = 2
                return 2
            if n == 1:
                c[1] = 1
                return 1
            
            c[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return c[n]
        
        return helper(n)