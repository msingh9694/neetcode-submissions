class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p=[]
        for i in range(len(nums)-k+1):
            max1=nums[i]
            for j in range(i,i+k):
                max1=max(max1,nums[j])
            p.append(max1)
        return p




        