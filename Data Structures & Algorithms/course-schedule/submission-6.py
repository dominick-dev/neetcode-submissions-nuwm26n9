class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i : [] for i in range(numCourses)}

        # populate mp
        for c, p in prerequisites:
            mp[c].append(p)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if mp[crs] == []:
                return True
            
            visit.add(crs)

            for prereq in mp[crs]:
                if not dfs(prereq):
                    return False
            
            visit.remove(crs)
            mp[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True

