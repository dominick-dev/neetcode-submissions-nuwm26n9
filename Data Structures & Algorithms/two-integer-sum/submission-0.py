class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in h:
                return [h.get(need), i]
            else:
                h[nums[i]] = i
        return []