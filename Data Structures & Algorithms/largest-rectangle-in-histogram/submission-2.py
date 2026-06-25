class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr=[]
        max1=0
        for i in range(len(heights)):
            p=heights[i]
            for j in range(i,len(heights)):
                p=min(p,heights[j])
                area=p*(j-i+1)
                max1=max(max1,area)
        return max1
            
        