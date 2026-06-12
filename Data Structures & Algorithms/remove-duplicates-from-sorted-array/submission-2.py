class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p={}
        for i in nums:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        result=[]
        for ele in p:
            result.append(ele)
        for i in range(len(result)): # modify nums
            nums[i] = result[i]
        return len(result)


        