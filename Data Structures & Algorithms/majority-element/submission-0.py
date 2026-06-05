class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        p={}
        for i in range(len(nums)):
            if nums[i] in p:
                p[nums[i]]+=1
            else:
                p[nums[i]]=1
        for j in p:
            if p[j]>len(nums)/2:
                return j
            

        