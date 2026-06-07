class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        count = 1
        ans = 1

        for p in range(len(nums) - 1):
            if nums[p + 1] - nums[p] == 1:
                count += 1
            elif nums[p + 1] - nums[p] == 0:
                continue
            else:
                ans = max(ans, count)
                count = 1

        ans = max(ans, count)
        return ans