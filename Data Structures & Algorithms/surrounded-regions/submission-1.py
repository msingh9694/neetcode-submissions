class Solution:

    def dfs(self, r, c, visited, rows, cols, board):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if board[r][c] == "X":
            return

        if visited[r][c] == 1:
            return

        visited[r][c] = 1

        self.dfs(r - 1, c, visited, rows, cols, board)
        self.dfs(r, c - 1, visited, rows, cols, board)
        self.dfs(r, c + 1, visited, rows, cols, board)
        self.dfs(r + 1, c, visited, rows, cols, board)

    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # First column
        for r in range(rows):
            if board[r][0] == "O" and visited[r][0] == 0:
                self.dfs(r, 0, visited, rows, cols, board)

        # Last column
        for r in range(rows):
            if board[r][cols - 1] == "O" and visited[r][cols - 1] == 0:
                self.dfs(r, cols - 1, visited, rows, cols, board)

        # Upper row
        for c in range(cols):
            if board[0][c] == "O" and visited[0][c] == 0:
                self.dfs(0, c, visited, rows, cols, board)

        # Bottom row
        for c in range(cols):
            if board[rows - 1][c] == "O" and visited[rows - 1][c] == 0:
                self.dfs(rows - 1, c, visited, rows, cols, board)

        # Convert surrounded O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"