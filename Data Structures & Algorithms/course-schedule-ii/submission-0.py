class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)} 
        
        for c, p in prerequisites:
            mp[c].append(p)
        
        visit = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)

            for prereq in mp[crs]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return res


