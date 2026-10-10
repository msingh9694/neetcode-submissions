import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minH = [(grid[0][0], 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == n - 1 and c == n - 1:
                return t

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nc < 0 or
                    nr >= n or nc >= n or
                    (nr, nc) in visited):
                    continue

                new_time = max(t, grid[nr][nc])
                heapq.heappush(minH, (new_time, nr, nc))

        return -1