class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        curr_max = 0

        def explore(grid, r, c):
            count = 0
            if r < 0 or c < 0 or r == rows or c == cols:
                return count
            if grid[r][c] == 0:
                return count
            else:
                grid[r][c] = 0
                count += 1
            
            count += explore(grid, r, c + 1)
            count += explore(grid, r, c - 1)
            count += explore(grid, r + 1, c)
            count += explore(grid, r - 1, c)

            return count
        
        for r in range(rows):
            for c in range(cols):
                curr_max = max(curr_max, explore(grid, r, c))
        return curr_max
