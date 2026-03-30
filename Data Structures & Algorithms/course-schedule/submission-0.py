class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj matrix of course: [prereqs]
        mp = {i: [] for i in range(numCourses)} # key:course val:prereqs

        for c, p in prerequisites:
            if c not in mp:
                mp[c] = []
            mp[c].append(p)
        
        visit = set()

        # dfs from each course
        def dfs(crs):
            if crs in visit:
                return False
            if mp[crs] == []:
                return True
            
            visit.add(crs)
            for p in mp[crs]:
                if not dfs(p):
                    return False
            visit.remove(crs)
            mp[crs] = []
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

