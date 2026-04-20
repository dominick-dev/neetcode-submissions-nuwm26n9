class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in nums:
            longest = 0
            while n - longest in seen:
                longest += 1
                res = max(res, longest)
        
        return res
