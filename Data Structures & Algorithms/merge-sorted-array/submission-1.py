class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1    # last idx in array
        i, j = m - 1, n - 1 # nums1 and nums2 pointers

        # continue until all of nums2 is processed
        while j >= 0:
            # nums1 has remaining elements and its current element is larger, so place it at write position
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            # nums2 element is larger (or nums1 is exhausted), so place nums2 element at write position
            else:
                nums1[last] = nums2[j]
                j -= 1
            # move write position left
            last -= 1
