class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]
        ans = []

        def isSafe(row, col):
            duprow = row
            dupcol = col

            # Upper-left diagonal
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row = duprow
            col = dupcol

            # Left row
            while col >= 0:
                if board[row][col] == "Q":
                    return False
                col -= 1

            row = duprow
            col = dupcol

            # Lower-left diagonal
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                row += 1
                col -= 1

            return True

        def backtrack(col):
            if col == n:
                ans.append(["".join(row) for row in board])
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"

                    backtrack(col + 1)

                    board[row][col] = "."

        backtrack(0)

        return ans