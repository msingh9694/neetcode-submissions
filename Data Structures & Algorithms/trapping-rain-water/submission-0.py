class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(len(height)):
            left_max = 0
            right_max = 0

            for j in range(i + 1):
                left_max = max(left_max, height[j])

            for j in range(i, len(height)):
                right_max = max(right_max, height[j])

            water += min(left_max, right_max) - height[i]

        return water

            
        