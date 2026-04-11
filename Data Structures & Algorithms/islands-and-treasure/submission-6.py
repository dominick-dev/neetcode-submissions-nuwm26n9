class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # helper to add a cell
        def add_cell(r, c):
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == -1):
                return
            q.append([r, c])
            visited.add((r, c))
        
        # add all chests to q and visited
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        # run through q
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r+1, c)
                add_cell(r, c+1)
                add_cell(r-1, c)
                add_cell(r, c-1)
            dist += 1

        