from collections import deque
from typing import List

class Solution:

    def bfs(self, i, j, visited, grid):

        count = 1

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((i, j))

        visited[i][j] = 1

        while len(queue) != 0:

            x, y = queue.popleft()

            for xx, yy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:

                new_i = x + xx
                new_j = y + yy

                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue

                if grid[new_i][new_j] == 0:
                    continue

                if visited[new_i][new_j] == 1:
                    continue

                visited[new_i][new_j] = 1
                count += 1
                queue.append((new_i, new_j))

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        p = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and visited[r][c] == 0:

                    area = self.bfs(r, c, visited, grid)

                    p = max(p, area)

        return p