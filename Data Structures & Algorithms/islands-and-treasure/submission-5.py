class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # init vars
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # adds cell to visit and q if valid
        def add_cell(r, c):
            # not in range, already visited, water
            if (min(r,c) < 0 or r == ROWS or 
                c == COLS or (r, c) in visit or 
                grid[r][c] == -1):
                return
            
            visit.add((r, c))
            q.append([r, c])
        
        # add chests to q and visit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])
        
        # init dist to 0 for first pass
        # each pass will be same dist from a chest
        dist = 0
        while q:
            # add surrounding cells for each in q
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r, c + 1)
                add_cell(r - 1, c)
                add_cell(r, c - 1)
            # next level
            dist += 1

