class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        if n == 1: return first
        if n == 2: return second

        for i in range(n - 2):
            temp = first + second
            first = second
            second = temp
        
        return second
