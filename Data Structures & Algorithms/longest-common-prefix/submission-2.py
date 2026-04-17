class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            curr = 0
            for i in range(len(s)):
                if i < len(res) and s[i] == res[i]:
                    curr += 1
                else:
                    break
            res = res[0:curr]
        
        return res

        