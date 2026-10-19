class Solution:
    def solve4(self, nums, n):
        prev2 = 0
        prev1 = 0

        for i in range(n):
            incl = prev2 + nums[i]
            excl = prev1 + 0

            ans = max(incl, excl)

            prev2 = prev1
            prev1 = ans

        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        first = []
        second = []

        for i in range(n):
            if i != n - 1:
                first.append(nums[i])

            if i != 0:
                second.append(nums[i])

        p = max(
            self.solve4(first, len(first)),
            self.solve4(second, len(second))
        )

        return p