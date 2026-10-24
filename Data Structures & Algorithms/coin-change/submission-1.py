from typing import List

class Solution:
    def solve(self, coins, amount, dp):
        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        if dp[amount] != -1:
            return dp[amount]

        mini = float('inf')

        for coin in coins:
            recursionAns = self.solve(coins, amount - coin, dp)

            if recursionAns != float('inf'):
                mini = min(mini, 1 + recursionAns)

        dp[amount] = mini
        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        ans = self.solve(coins, amount, dp)

        if ans == float('inf'):
            return -1

        return ans