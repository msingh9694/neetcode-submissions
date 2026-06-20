class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p = []

        for num in arr:
            p.append((abs(num - x), num))

        p.sort()

        ans = []
        for i in range(k):
            ans.append(p[i][1])

        ans.sort()
        return ans