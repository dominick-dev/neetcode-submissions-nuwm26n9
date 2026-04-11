class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # get rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                if r != 0 and grid[r - 1][c] == 1:
                    fresh -= 1
                    grid[r-1][c] = 2
                    q.append((r-1, c))
                if c != 0 and grid[r][c - 1] == 1:
                    fresh -= 1
                    grid[r][c-1] = 2
                    q.append((r, c-1))
                if r != ROWS - 1 and grid[r+1][c] == 1:
                    fresh -= 1
                    grid[r+1][c] = 2
                    q.append((r+1, c))
                if c != COLS - 1 and grid[r][c+1] == 1:
                    fresh -= 1
                    grid[r][c+1] = 2
                    q.append((r, c+1))
        
        return time if fresh == 0 else -1
