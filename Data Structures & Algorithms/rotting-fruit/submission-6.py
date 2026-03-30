class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0

        rotting = deque()
        fresh = 0
        # find rotten fruit and add to stack
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotting.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        
        # bfs as long as we have fruit to rot
        while rotting and fresh > 0:
            # process current time
            rotting_len = len(rotting)

            time += 1
            for i in range(rotting_len):
                # make sure to pop from left
                r, c = rotting.popleft()
                # can rot
                if r != 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    rotting.append([r - 1, c])
                if r != ROWS - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    rotting.append([r + 1, c])
                if c != 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    rotting.append([r, c - 1])
                if c != COLS - 1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    rotting.append([r, c + 1])
            # increment after
        
        return time if fresh == 0 else -1
