class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d={}
        for ele in s:
            if ele in d1:
                d1[ele] += 1
            else:
                d1[ele] = 1

        for ele in t:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1

           
        if d== d1:
            return True
        return False