class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p={}
        count=1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        for t in range(len(nums)-1):
            if nums[t]==nums[t+1]:
                count+=1
            else:
                p[nums[t]]=count
                count=1
        p[nums[-1]] = count
        l=[]
        for i in range(k):
            maxvalue = -10000
            maxkey = -100000
            for d in p:
                if p[d] > maxvalue:
                    maxkey = d
                    maxvalue = p[d]
            p[maxkey] = -1
            l.append(maxkey)
        return l
                    



        