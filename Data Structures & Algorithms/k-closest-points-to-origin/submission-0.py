class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p=[]
        for point in points:
            x=point[0]
            y=point[1]
            d=x*x+y*y
            p.append([d,point])
        p.sort()
        ans=[]
        for i in range(k):
            ans.append(p[i][1])
        return ans