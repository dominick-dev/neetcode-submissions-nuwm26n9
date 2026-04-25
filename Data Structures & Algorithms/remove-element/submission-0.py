class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # iterate through nums
        # swap with last element
        swap_idx = len(nums) - 1
        removed = 0

        i = 0
        while i < (len(nums) - removed):
            if nums[i] == val:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                removed += 1
                swap_idx -= 1
            else:
                i += 1

        return len(nums) - removed

