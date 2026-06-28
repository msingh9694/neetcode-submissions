class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)-1):
            if target>=nums[i] and target<=nums[i+1]:
                return i+1
        if target<=nums[0]:
            return 0
        return len(nums)
        
            
        