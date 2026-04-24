class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)   
        for src, tar, wt in times:
            adj[src].append((tar, wt))
        
        hp = [(0, k)]
        visited = set()
        t = 0

        while hp:
            curr_wt, curr_n = heapq.heappop(hp)
            if curr_n in visited:
                continue
            visited.add(curr_n)
            t = curr_wt

            for neighbor_n, neighbor_wt in adj[curr_n]:
                if neighbor_n not in visited:
                    heapq.heappush(hp, (curr_wt + neighbor_wt, neighbor_n))
        
        return t if len(visited) == n else -1


