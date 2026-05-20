class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            pre[i] = nums[i-1] * pre[i-1]
        

        post = [1 for _ in range(len(nums))]
        for j in range(len(nums) - 2, -1, -1):
            post[j] = nums[j+1] * post[j+1]
        
        for k in range(len(nums)):
            pre[k] *= post[k]
        
        return pre
