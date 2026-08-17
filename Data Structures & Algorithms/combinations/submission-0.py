class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subset = []

        def solve(start):
            if len(subset) == k:
                result.append(subset.copy())
                return

            for i in range(start, n + 1):
                subset.append(i)
                solve(i + 1)
                subset.pop()

        solve(1)
        return result