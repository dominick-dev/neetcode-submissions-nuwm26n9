class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r, c) not in visit and grid[r][c] == 1:
                visit.add((r, c))

                curr = 1
                if r > 0:
                    curr += dfs(r - 1, c)
                if c > 0:
                    curr += dfs(r, c - 1)
                if r < ROWS - 1:
                    curr += dfs(r + 1, c)
                if c < COLS - 1:
                    curr += dfs(r, c + 1)
                return curr

            return 0
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        
        return area

