class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def explore(grid, r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return False
            if grid[r][c] == "0":
                return False
            
            grid[r][c] = "0"
            explore(grid, r, c + 1)
            explore(grid, r, c - 1)
            explore(grid, r + 1, c)
            explore(grid, r - 1, c)

            return True
        
        for r in range(rows):
            for c in range(cols):
                if explore(grid, r, c):
                    count += 1
        
        return count
