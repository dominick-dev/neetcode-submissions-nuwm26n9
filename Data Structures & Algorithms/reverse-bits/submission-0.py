class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""

        for i in range(32):
            if n % 2 == 0:
                res += "0"
            else:
                res += "1"
            n = n >> 1
        
        return int(res, 2)
        