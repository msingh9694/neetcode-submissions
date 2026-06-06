class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.nums=nums
        ans=[]
        for i in range(len(self.nums)):
            product=1
            for j in range(len(self.nums)):
                if i!=j:
                    product*=self.nums[j]
            ans.append(product)
        return ans
             
        