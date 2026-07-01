class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=nums[right]:
                left=mid+1
            else:
                right=mid
        for i in range(len(nums)):
            if nums[i]==target:
                return True
        return False
        