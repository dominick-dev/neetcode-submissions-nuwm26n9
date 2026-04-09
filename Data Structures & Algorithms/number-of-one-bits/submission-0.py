class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if n % 2 != 0:
                res += 1
            n = n >> 1
        
        return res
        