class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # init vars
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inf = 2147483647

        # bfs helper
        def bfs(r, c):
            # add curr to queue
            q = deque([(r, c)])
            # init visit array, set curr to True
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True

            # track steps
            steps = 0
            while q:
                # iterate through q
                for _ in range(len(q)):
                    row, col = q.popleft()
                    # reached chest, 0 steps
                    if grid[row][col] == 0:
                        return steps
                    
                    # go through each possible direction
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and      # dont go OOB
                            0 <= nc < COLS and      # dont go OOB
                            not visit[nr][nc] and   # skip already visited
                            grid[nr][nc] != -1):    # skip water

                            # mark as visited and add to q
                            visit[nr][nc] = True
                            q.append((nr, nc))
                # finished current level, increment steps
                steps += 1
            return inf
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == inf:
                    # found land, set to bfs result
                    grid[r][c] = bfs(r, c)

