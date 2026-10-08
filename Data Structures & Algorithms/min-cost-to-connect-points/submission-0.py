class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        # Minimum cost to connect each point
        minDist = [float('inf')] * n

        # Start from point 0
        minDist[0] = 0

        visited = [False] * n

        res = 0

        for _ in range(n):

            # Find the unvisited point with minimum cost
            cur = -1

            for i in range(n):
                if not visited[i] and (cur == -1 or minDist[i] < minDist[cur]):
                    cur = i

            # Add this point to MST
            visited[cur] = True
            res += minDist[cur]

            # Update distances of remaining points
            x1, y1 = points[cur]

            for i in range(n):

                if not visited[i]:

                    x2, y2 = points[i]

                    dist = abs(x1 - x2) + abs(y1 - y2)

                    minDist[i] = min(minDist[i], dist)

        return res
        