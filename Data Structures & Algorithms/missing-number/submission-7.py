class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor all expected nums in range
        expected = 0
        for i in range(len(nums) + 1):
            expected ^= i
        
        # xor actual nums in range
        seen = 0
        for n in nums:
            seen ^= n
        
        # cancel out nums that appear in both
        return expected ^ seen
