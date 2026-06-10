class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if 1 not in nums:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                continue

            if nums[i + 1] == nums[i]:
                continue

            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

        return nums[-1] + 1
        