class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # track num of prereqs for each crs
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for s, d in prerequisites:
            indegree[d] += 1
            adj[s].append(d)
        
        # add courses w/ prereqs to q
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for crs in adj[curr]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        return finish == numCourses 
                


