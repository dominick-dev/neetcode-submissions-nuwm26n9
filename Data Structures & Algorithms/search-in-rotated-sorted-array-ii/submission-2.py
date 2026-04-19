class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # found target
            if nums[m] == target:
                return True

            # left portion is sorted
            if nums[l] < nums[m]:
                # target in left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # target not in left portion
                else:
                    l = m + 1
            # right portion sorted
            elif nums[l] > nums[m]:
                # target in right portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # target in left portion
                else:
                    r = m - 1
            # duplicate, skip it
            else:
                l += 1
        
        return False
