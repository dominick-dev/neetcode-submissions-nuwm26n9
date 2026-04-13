class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        while goal > 0:
            for i in range(goal - 1, -1, -1):
                if nums[i] + i >= goal:
                    goal = i
                    break
                if i == 0:
                    return False
        
        return True
            

