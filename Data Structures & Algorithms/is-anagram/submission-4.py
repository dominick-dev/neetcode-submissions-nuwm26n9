class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_mp = {}
        t_mp = {}

        for i in range(len(s)):
            s_mp[s[i]] = 1 + s_mp.get(s[i], 0)
            t_mp[t[i]] = 1 + t_mp.get(t[i], 0)
        
        return s_mp == t_mp
        