class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = {
            'a': a,
            'b': b,
            'c': c
        }

        ans = ""

        while True:
            best = ""

            # Find the character with the highest remaining frequency
            for ch in freq:
                if freq[ch] == 0:
                    continue

                # Skip if it would create three consecutive same characters
                if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                    continue

                if best == "" or freq[ch] > freq[best]:
                    best = ch

            # No valid character can be added
            if best == "":
                break

            ans += best
            freq[best] -= 1

        return ans