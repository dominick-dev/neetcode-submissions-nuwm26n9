class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        # around border can never be changed
        # go around boarder of board
        # call dfs on 0's around boarder
        # add all 0's connected to above to list
        # iterate through and change 0's that are not in list
        zeroes = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] == "X" or
                (r, c) in zeroes):
                return
            
            zeroes.add((r, c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1):
                    if board[r][c] == "O":
                        dfs(r, c)
        
        print(zeroes)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if (r, c) not in zeroes:
                        board[r][c] = "X"

