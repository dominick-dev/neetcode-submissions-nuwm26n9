class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sm = 0

        for n in nums:
            sm ^= n
        
        return sm
