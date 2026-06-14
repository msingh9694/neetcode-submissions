class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                seen =set()
                for k in range(j + 1, len(nums)):
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:
                        temp = sorted([nums[i], nums[j], nums[k], fourth])

                        if temp not in l:
                            l.append(temp)

                    seen.add(nums[k])

        return l