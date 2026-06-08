class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        p = {}
        count = 1

        nums = sorted(nums)

        for t in range(len(nums) - 1):
            if nums[t] == nums[t + 1]:
                count += 1
            else:
                p[nums[t]] = count
                count = 1

        p[nums[-1]] = count

        l = []

        for key in p:
            if p[key] > len(nums) // 3:
                l.append(key)

        return l



        