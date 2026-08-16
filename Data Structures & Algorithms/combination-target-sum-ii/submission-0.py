class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, total, subset):
            if total == 0:
                result.append(subset.copy())
                return

            if total < 0:
                return

            for i in range(index, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates are sorted, no later value can work
                if candidates[i] > total:
                    break

                subset.append(candidates[i])

                backtrack(i + 1, total - candidates[i], subset)

                subset.pop()

        backtrack(0, target, [])
        return result

        