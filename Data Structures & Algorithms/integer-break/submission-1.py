class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def solve(n):

            if n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]

            ans = 0

            for i in range(1, n):

                ans = max(ans, i * (n-i))

                ans = max(ans, i * solve(n-i))

            dp[n] = ans

            return dp[n]

        return solve(n)