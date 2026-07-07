class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p={}
        for ele in nums:
            if ele in p:
                p[ele]+=1
            else:
                p[ele]=1
        for i in p:
            if p[i]>1:
                return i
                

        
        