class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]

                ok = True

                for ch in set(t):
                    if sub.count(ch) < t.count(ch):
                        ok = False
                        break

                if ok:
                    if ans == "" or len(sub) < len(ans):
                        ans = sub

        return ans