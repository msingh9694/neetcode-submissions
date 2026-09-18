class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:] = unique
        return len(unique)