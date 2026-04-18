class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make sure B < A
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # alias and set pointers
        A, B = nums1, nums2
        l, r = 0, len(A) - 1
        # arr stats
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            i = (r + l) // 2 # mid of A
            j = half - i - 2 # mid of B

            # get bounds of current partition
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            
