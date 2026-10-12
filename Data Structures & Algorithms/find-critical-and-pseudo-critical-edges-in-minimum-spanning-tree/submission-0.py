from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # Store original edge indices
        new_edges = []

        for i in range(len(edges)):
            u, v, weight = edges[i]
            new_edges.append([u, v, weight, i])

        # Sort edges by weight
        new_edges.sort(key=lambda x: x[2])

        # Function to find parent
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        # Kruskal's algorithm
        def kruskal(n, edges, skip=-1, force=-1):
            parent = list(range(n))
            rank = [0] * n

            cost = 0
            count = 0

            # Force an edge to be included
            if force != -1:
                for u, v, weight, idx in edges:
                    if idx == force:
                        pu = find(parent, u)
                        pv = find(parent, v)

                        if pu != pv:
                            parent[pu] = pv
                            cost += weight
                            count += 1
                        break

            # Process remaining edges
            for u, v, weight, idx in edges:

                if idx == skip or idx == force:
                    continue

                pu = find(parent, u)
                pv = find(parent, v)

                if pu != pv:
                    parent[pu] = pv
                    cost += weight
                    count += 1

                if count == n - 1:
                    break

            # A spanning tree must have n - 1 edges
            if count != n - 1:
                return float("inf")

            return cost

        # Find the minimum spanning tree cost
        mst_cost = kruskal(n, new_edges)

        critical = []
        pseudo_critical = []

        for u, v, weight, idx in new_edges:

            # Exclude this edge
            cost_without = kruskal(n, new_edges, skip=idx)

            if cost_without > mst_cost:
                critical.append(idx)

            else:
                # Force this edge into the MST
                cost_with = kruskal(n, new_edges, force=idx)

                if cost_with == mst_cost:
                    pseudo_critical.append(idx)

        return [critical, pseudo_critical]
        