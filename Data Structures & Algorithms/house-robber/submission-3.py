class Solution:
    def solvemem(self,nums,n,dp):
        if n<0:
            return 0
        if n==0:
            return nums[0]
        if dp[n]!=-1:
            return dp[n]
        incl=self.solvemem(nums,n-2,dp)+nums[n]
        excl=self.solvemem(nums,n-1,dp)+0
        dp[n]=max(incl,excl)
        return dp[n]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        # ans=self.solve(nums,n-1)
        # return ans
        dp=[-1]*(n)
        return self.solvemem(nums,n-1,dp)
        


        