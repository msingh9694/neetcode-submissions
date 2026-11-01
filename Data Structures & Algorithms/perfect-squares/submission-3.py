class Solution:

    def solve(self, n):
        if n == 0:
            return 0

        ans = n

        for i in range(1, int(n**0.5) + 1):
            square = i * i
            ans = min(ans, 1 + self.solve(n - square))

        return ans

    def solvemem(self, n, dp):
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        ans = n

        for i in range(1, int(n**0.5) + 1):
            square = i * i
            ans = min(ans, 1 + self.solvemem(n - square, dp))

        dp[n] = ans
        return dp[n]

    def solvetab(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                square = j * j
                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]

    def numSquares(self, n: int) -> int:
        return self.solvetab(n)