class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)

        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] = 1 + mp.get(n)
        
        for n, ct in mp.items():
            if ct > (l // 2):
                return n
        