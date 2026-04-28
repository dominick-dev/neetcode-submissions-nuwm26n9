class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1    # last idx in array
        i, j = m - 1, n - 1 # nums1 and nums2 pointers

        # continue until all of nums2 is processed
        while j >= 0:
            # still element in nums1 to move
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            # 
            else:
                nums1[last] = nums2[j]
                j -= 1
            # process next idx in nums1
            last -= 1
