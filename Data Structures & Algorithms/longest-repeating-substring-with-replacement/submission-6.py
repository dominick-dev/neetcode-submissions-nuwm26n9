class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {} # key:char val:count
        l = 0
        maxF = 0 # count of highest freq char

        # iterate through s
        for r in range(len(s)):
            # get count of current char
            count[s[r]] = 1 + count.get(s[r], 0)
            # update maxF
            maxF = max(maxF, count[s[r]])
            # while window contains too man non maxF chars
            while (r - l + 1) - maxF > k:
                # dec s[l] count and move l
                count[s[l]] -= 1
                l += 1
            # update res
            res = r - l + 1
        
        return res


