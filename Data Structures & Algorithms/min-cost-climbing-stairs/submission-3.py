
from typing import List

class Solution:
    def solve(self, cost, n):  # recursion
                            # memonization
                            # tabularization
                            # tabuler optimization
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        ans = cost[n] + min(self.solve(cost, n - 1),
                            self.solve(cost, n - 2))
        return ans

    def solve2(self, cost, n, dp):
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        if dp[n] != -1:
            return dp[n]

        dp[n] = cost[n] + min(self.solve2(cost, n - 1, dp),
                              self.solve2(cost, n - 2, dp))
        return dp[n]
    def solve3(self, cost, n, dp):
        dp=[1]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])
    def solve4(self, cost, n):
        prev2=cost[0]
        prev1=cost[1]
        for i in range(2,n):
            curr=cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=curr

        return min(prev1,prev2)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #n = len(cost)
        #dp = [-1] * n

        #ans = min(self.solve2(cost, n - 1, dp),
                  #self.solve2(cost, n - 2, dp))
        #return ans
        n=len(cost)
        return self.solve4(cost,n)
