class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # get rightmost bit
            bit = (n >> i) & 1
            # place bit at position 31 - i
            res += (bit << (31 - i))
        
        return res
