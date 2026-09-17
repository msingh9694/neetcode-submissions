from typing import List

class Solution:

    def dfs(self, i, j, visited, grid):

        rows = len(grid)
        cols = len(grid[0])

        # Boundary check
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0

        # Water
        if grid[i][j] == 0:
            return 0

        # Already visited
        if visited[i][j] == 1:
            return 0

        visited[i][j] = 1

        # Count current cell
        count = 1

        # Explore 4 directions
        count += self.dfs(i - 1, j, visited, grid)
        count += self.dfs(i + 1, j, visited, grid)
        count += self.dfs(i, j - 1, visited, grid)
        count += self.dfs(i, j + 1, visited, grid)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        max_area = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and visited[r][c] == 0:

                    area = self.dfs(r, c, visited, grid)

                    max_area = max(max_area, area)

        return max_area