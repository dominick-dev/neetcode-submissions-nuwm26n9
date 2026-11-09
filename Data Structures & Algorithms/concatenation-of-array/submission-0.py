class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0 for _ in range(2 * l)]

        for i, n in enumerate(nums):
            res[i] = n
            res[i + l] = n
        
        return res
        
        