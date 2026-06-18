class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        left = 0
        p = []

        for i in range(len(nums)):
            count += nums[i]

            while count >= target:
                p.append(i - left + 1)
                count -= nums[left]
                left += 1

        if len(p) == 0:
            return 0

        return min(p)