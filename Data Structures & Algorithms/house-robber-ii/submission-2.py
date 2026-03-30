class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        first_n = nums[:-1]
        second_n = nums[1:]

        def rob1(nums):
            first, second = 0, 0
            for n in nums:
                temp = max(n + first, second)
                first = second
                second = temp
            return second
        
        return max(rob1(first_n), rob1(second_n))
        