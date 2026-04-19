class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1

        for n in nums[1:]:
            if n == curr:
                count += 1
            else:
                 count -= 1
            
            if count < 1:
                curr = n
                count = 0
        
        return curr

