from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        maxi = nums[0]

        n = len(nums)

        for i in range(n):
            prod = prod * nums[i]
            maxi = max(maxi, prod)

            if prod == 0:
                prod = 1

        prod = 1

        for i in range(n - 1, -1, -1):
            prod = prod * nums[i]
            maxi = max(maxi, prod)

            if prod == 0:
                prod = 1

        return maxi