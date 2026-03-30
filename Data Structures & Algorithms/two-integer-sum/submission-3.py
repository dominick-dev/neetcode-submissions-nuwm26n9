class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key=number val=index

        for i, n in enumerate(nums):
            need = target - n
            if need in seen:
                return [seen.get(need), i]
            seen[n] = i

