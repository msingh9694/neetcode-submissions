class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        ans=1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        
        for p in range(len(nums)-1):
            if nums[p+1]-nums[p]==1  or nums[p+1]-nums[p]==-1:
                count += 1
            
            if nums[p+1] - nums[p] == 0:
                continue
            if nums[p+1] - nums[p] > 1:
                ans = max(ans, count)
                count = 1
        ans = max(ans,count)
        
        return ans



        