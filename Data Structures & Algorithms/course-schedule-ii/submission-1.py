class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # init map
        mp = {i: [] for i in range(numCourses)} 
        
        # populate map
        for c, p in prerequisites:
            mp[c].append(p)
        
        # init vars
        visit = set()
        cycle = set()
        res = []

        # dfs helper
        def dfs(crs):
            # cycle detected
            if crs in cycle:
                return False
            # check if crs already visited in prev dfs
            if crs in visit:
                return True
            
            cycle.add(crs)

            # iter through curr prereqs
            for prereq in mp[crs]:
                # if prereq has cycle not possible
                if dfs(prereq) == False:
                    return False
            # no cycle, good to go
            # remove crs from cycle
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return res


