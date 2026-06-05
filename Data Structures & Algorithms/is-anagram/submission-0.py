class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ele in s:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1

        for ele in t:
            if ele in d:
                d[ele] -= 1
            else:
                d[ele] = 1

        for k in d:    
            if d[k] != 0:
                return False
        return True