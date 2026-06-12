class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = {}

        for x in nums:
            if x not in p:
                p[x] = 1

        i = 0
        for ele in p:
            nums[i] = ele
            i += 1

        return i