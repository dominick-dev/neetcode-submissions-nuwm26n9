class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < (len(nums) - 1) and nums[l] == nums[l-1]:
                        l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
                
