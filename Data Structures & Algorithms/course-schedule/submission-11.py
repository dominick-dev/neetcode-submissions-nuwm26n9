class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        mp = {}
        for c, p in prerequisites:
            if c not in mp:
                mp[c] = []
            mp[c].append(p)
        
        visited = set()
        def dfs(c):
            # go through neighbors of course and look for cycle
            # found cycle return false
            # otherwise can continue
            if c in visited:
                return False
            if c not in mp or len(mp[c]) == 0:
                mp[c] = []
                return True
            visited.add(c)
            for neighbor in mp[c]:
                if not dfs(neighbor):
                    return False
            visited.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            visited = set()
        
        return True
            

