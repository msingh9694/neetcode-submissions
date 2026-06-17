class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in p and p[s[right]] >= left:
                left = p[s[right]] + 1

            p[s[right]] = right
            ans = max(ans, right - left + 1)

        return ans