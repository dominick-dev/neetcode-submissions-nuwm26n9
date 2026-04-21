class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get length and starting idx
        n = len(nums)
        i = n - 2
        # find pivot (first time nums[i] >= nums[i + 1])
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # found pivot
        if i >= 0:
            j = n - 1
            # search for swap to left of piot
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse right side of i
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



