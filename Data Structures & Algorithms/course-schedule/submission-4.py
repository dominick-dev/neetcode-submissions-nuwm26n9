class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj matrix of course: [prereqs]
        mp = {i: [] for i in range(numCourses)}

        # fill map
        for c, p in prerequisites:
            mp[c].append(p)
        
        visit = set()

        # dfs helper
        # check for cycles! This means can't finish
        def dfs(crs):
            # already visited in curr run
            if crs in visit:
                return False
            # reached end of curr run
            if mp[crs] == []:
                return True
            
            # still visiting...
            visit.add(crs)

            # go through curr courses prereqs
            for p in mp[crs]:
                # check if prereq course is impossible to finish
                if not dfs(p):
                    return False

            # all prereqs checked
            # allow crs to be visited again in different path
            visit.remove(crs)
            # avoid checking this course again, already know it works
            mp[crs] = []
            return True 
        
        # call dfs on each crs
        for crs in range(numCourses):
            # if one can't be finished return false
            if not dfs(crs): return False
        return True

