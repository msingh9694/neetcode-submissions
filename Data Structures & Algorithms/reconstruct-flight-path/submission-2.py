class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = {}

        # Build adjacency list
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        # Sort destinations in reverse order
        for src in adj:
            adj[src].sort(reverse=True)

        res = []

        def dfs(src):
            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")

        return res[::-1]