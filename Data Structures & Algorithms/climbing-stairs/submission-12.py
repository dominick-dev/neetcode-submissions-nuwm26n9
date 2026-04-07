class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 0, 1

        for i in range(n):
            temp = first + second
            first = second
            second = temp
        
        return second
        