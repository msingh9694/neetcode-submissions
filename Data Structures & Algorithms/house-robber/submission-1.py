
class Solution:
    def solve4(self, nums, n):
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
        return self.solve4(nums, n)
