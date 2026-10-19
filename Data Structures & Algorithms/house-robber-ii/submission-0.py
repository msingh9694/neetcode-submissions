
class Solution:
    def solve(self, nums, n):
        if n == 0:
            return 0

        prev2 = 0
        prev1 = 0

        for i in range(n):
            incl = prev2 + nums[i]
            excl = prev1

            ans = max(incl, excl)

            prev2 = prev1
            prev1 = ans

        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        first = nums[:-1]   # Exclude last house
        second = nums[1:]   # Exclude first house

        return max(
            self.solve(first, len(first)),
            self.solve(second, len(second))
        )
