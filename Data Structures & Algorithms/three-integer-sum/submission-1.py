class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third in seen:
                    ans.add(tuple(sorted([nums[i], nums[j], third])))

                seen.add(nums[j])

        return [list(x) for x in ans]
        