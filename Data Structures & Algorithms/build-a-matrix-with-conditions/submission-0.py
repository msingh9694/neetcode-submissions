
from typing import List
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topological_sort(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1

            queue = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)

            order = []

            while queue:
                node = queue.popleft()
                order.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            if len(order) != k:
                return []

            return order

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_position = {}
        col_position = {}

        for i in range(k):
            row_position[row_order[i]] = i
            col_position[col_order[i]] = i

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r = row_position[num]
            c = col_position[num]
            matrix[r][c] = num

        return matrix
