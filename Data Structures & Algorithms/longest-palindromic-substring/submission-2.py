class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        start = 0
        maxlen = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if length > maxlen:
                            start = i
                            maxlen = length

        return s[start:start + maxlen]