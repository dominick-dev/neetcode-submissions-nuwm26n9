class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        atl = set()
        pac = set()

        def dfs(r, c, ocean, prev_height):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in ocean or
                heights[r][c] < prev_height):
                return
            
            ocean.add((r, c))

            dfs(r+1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, pac, heights[r][c])
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atl, heights[r][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res



        # start from each ocean location
        # run dfs and add too given ocean visited
        # return array that contains both
        