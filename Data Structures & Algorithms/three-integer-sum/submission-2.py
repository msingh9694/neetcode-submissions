class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third in seen:
                    temp = sorted([nums[i], nums[j], third])

                    if temp not in l:
                        l.append(temp)

                seen.add(nums[j])

        return l