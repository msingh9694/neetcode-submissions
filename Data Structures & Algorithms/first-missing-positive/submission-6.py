class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 0
        nums = sorted(nums)

        if 1 not in nums:
            return 1

        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                continue

            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1

            elif nums[i + 1] - nums[i] == 1 or nums[i + 1] - nums[i] == 0:
                count += 1

        return nums[-1] + 1
            


        



        