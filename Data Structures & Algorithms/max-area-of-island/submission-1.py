class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        def dfs(r, c):
            nonlocal curr_area
            if grid[r][c] == 1:
                curr_area += 1
                grid[r][c] = 0

                if r > 0:
                    dfs(r - 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if r < ROWS - 1:
                    dfs(r + 1, c)
                if c < COLS - 1:
                    dfs(r, c + 1)
        

        for r in range(ROWS):
            for c in range(COLS):
                curr_area = 0
                dfs(r, c)
                max_area = max(max_area, curr_area)

        
        return max_area
