class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {} # key:sorted chars val:anagrams

        # populate mp
        for s in strs:
            # sort chars
            s_sorted = "".join(sorted(s))
            # add to mp
            if s_sorted not in mp:
                mp[s_sorted] = []
            mp[s_sorted].append(s)

        # populate res array
        res = []
        for c, lst in mp.items():
            res.append(lst)
        
        return res
        