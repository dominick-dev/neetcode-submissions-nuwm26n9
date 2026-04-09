class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(i):
            ones = 0
            for j in range(32):
                if i % 2 != 0:
                    ones += 1
                i = i >> 1
            return ones

        res = []
        for i in range(n + 1):
            res.append(count(i))
        
        return res
        

        
                    
