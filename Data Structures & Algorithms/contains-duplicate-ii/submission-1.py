class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p = {}

        for i in range(len(nums)):
            if nums[i] in p:
                if i - p[nums[i]] <= k:
                    return True

            p[nums[i]] = i

        return False