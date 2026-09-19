from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        grid_copy=deepcopy(grid)
        queue = deque()
        fresh_cnt = 0

        # Find all rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0

        # BFS
        while queue and fresh_cnt > 0:

            # Number of rotten oranges at current minute
            total_rotten = len(queue)

            for _ in range(total_rotten):

                i, j = queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    new_i = i + dx
                    new_j = j + dy

                    # Boundary check
                    if new_i < 0 or new_i >= rows:
                        continue

                    if new_j < 0 or new_j >= cols:
                        continue

                    # Only fresh oranges can become rotten
                    if grid[new_i][new_j] != 1:
                        continue

                    grid[new_i][new_j] = 2
                    fresh_cnt -= 1
                    queue.append((new_i, new_j))

            minutes += 1

        if fresh_cnt > 0:
            return -1

        return minutes