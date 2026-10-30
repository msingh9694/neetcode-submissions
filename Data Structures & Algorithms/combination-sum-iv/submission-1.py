from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [-1] * (target + 1)

        def solve(target):
            # Base case
            if target == 0:
                return 1

            if target < 0:
                return 0

            # Already calculated
            if dp[target] != -1:
                return dp[target]

            ans = 0

            for num in nums:
                ans += solve(target - num)

            dp[target] = ans

            return dp[target]

        return solve(target)