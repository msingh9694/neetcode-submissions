class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row check
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k]:
                        return False

        # Column check
        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue

                for k in range(i + 1, 9):
                    if board[i][j] == board[k][j]:
                        return False

        # 3x3 box check
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                cells = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            cells.append(board[i][j])

                for i in range(len(cells)):
                    for j in range(i + 1, len(cells)):
                        if cells[i] == cells[j]:
                            return False

        return True