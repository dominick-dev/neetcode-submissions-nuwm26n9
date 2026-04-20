class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # key: time val: start (+) end (-)
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []        # result
        interval = []   # curr interval
        have = 0        # track start/stop
        for i in sorted(mp):
            # new interval, add start
            if not interval:
                interval.append(i)
            # update have count
            have += mp[i]
            # reached interval close, add to res and reset
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        
        return res
            
