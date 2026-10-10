
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        # Step 1: Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Invalid prefix case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the first different character
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Step 2: DFS with cycle detection
        visit = {}  # True = current path, False = fully processed
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]  # True means cycle detected

            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
            return False

        # Step 3: Visit every character
        for c in adj:
            if dfs(c):
                return ""

        # Step 4: Reverse topological order
        res.reverse()
        return "".join(res)
