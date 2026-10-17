
from typing import List

class Solution:

    # 1. Recursion
    def solve(self, cost, n):
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        return cost[n] + min(
            self.solve(cost, n - 1),
            self.solve(cost, n - 2)
        )

    # 2. Memoization
    def solve2(self, cost, n, dp):
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        if dp[n] != -1:
            return dp[n]

        dp[n] = cost[n] + min(
            self.solve2(cost, n - 1, dp),
            self.solve2(cost, n - 2, dp)
        )
        return dp[n]

    # 3. Tabulation
    def solve3(self, cost, n):
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])

    # 4. Space-optimized DP
    def solve4(self, cost, n):
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return self.solve4(cost, n)
