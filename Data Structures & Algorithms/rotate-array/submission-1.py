class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        l = nums[-k:] + nums[:-k]

        for i in range(len(nums)):
            nums[i] = l[i]