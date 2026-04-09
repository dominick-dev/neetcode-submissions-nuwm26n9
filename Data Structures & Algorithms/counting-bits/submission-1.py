class Solution:
    def countBits(self, n: int) -> List[int]:

        def get_ones(i):
            res = 0

            for _ in range(32):
                if i % 2 != 0:
                    res += 1
                i = i >> 1
            return res
        
        res = []
        for i in range(n + 1):
            res.append(get_ones(i))
        
        return res
