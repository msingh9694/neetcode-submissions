class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p = {}
        left = 0
        ans = 0
        max_freq = 0

        for right in range(len(s)):
            p[s[right]] = p.get(s[right], 0) + 1

            max_freq = max(max_freq, p[s[right]])

            while (right - left + 1) - max_freq > k:
                p[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        