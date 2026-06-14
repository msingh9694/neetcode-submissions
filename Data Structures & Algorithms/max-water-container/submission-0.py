class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1=0
        for i in range(len(heights)):
            minh=heights[i]
            for j in range(i+1,len(heights)):
                area=min(heights[i],heights[j])*(j-i)
                max1=max(max1,area)
        return max1


        