"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:

    def isAllSame(self, grid, x, y, n):

        val = grid[x][y]

        for i in range(x, x + n):
            for j in range(y, y + n):
                if grid[i][j] != val:
                    return False

        return True

    def construct(self, grid: List[List[int]]) -> 'Node':

        def solve(x, y, n):

            if self.isAllSame(grid, x, y, n):
                return Node(grid[x][y], True)

            half = n // 2

            root = Node(1, False)

            root.topLeft = solve(x, y, half)
            root.topRight = solve(x, y + half, half)
            root.bottomLeft = solve(x + half, y, half)
            root.bottomRight = solve(x + half, y + half, half)

            return root

        return solve(0, 0, len(grid))