class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = strs[0]

        for s in strs[1:]:
            longest = 0
            for i in range(len(s)):
                if i >= len(curr) or curr[i] != s[i]:
                    break
                longest += 1
            curr = curr[0:longest]

        return curr
        