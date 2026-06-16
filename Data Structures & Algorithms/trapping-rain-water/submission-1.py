class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0

        for i in range(len(height)):
            l = 0
            r = 0

            for j in range(i + 1):
                l = max(l, height[j])

            for j in range(i, len(height)):
                r= max(r, height[j])

            count += min(l, r) - height[i]

        return count

            
        