class Solution:
    def longestPalindrome(self, s: str) -> str:
        # track result and length of
        res = ""
        res_len = 0

        # iterate through each "center" char for pal
        for i in range(len(s)):
            # odd case
            l, r = i, i
            # while in range and we have a pal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # only care if longer than curr res
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = len(res)
                l -= 1
                r += 1
            
            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = len(res)
                l -= 1
                r += 1

        return res

