class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        seen = set()
        res = 1

        l, r = 0, 1
        seen.add(s[l])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
            r += 1
        
        return res
