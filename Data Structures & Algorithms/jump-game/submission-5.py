class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True

        for i, n in enumerate(nums):
            if dp[i] == False or n == 0:
                continue

            for j in range(n + 1):
                if i + j < len(nums):
                    dp[i + j] = True 
            
        return dp[-1]

        