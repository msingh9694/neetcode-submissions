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
    def solvetab(self,nums,n,dp):
        if n == 1:
            return nums[0]
        n=len(nums)
        dp=[0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            incl=dp[i-2]+nums[i]
            excl=dp[i-1]+0
            dp[i] = max(incl, excl)
        return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        #n=len(nums)
        # ans=self.solve(nums,n-1)
        # return ans
        #dp=[-1]*(n)
        #return self.solvemem(nums,n-1,dp)
        n=len(nums)
        dp=[0]*n
        dp=nums[0]
        return self.solvetab(nums,n,dp)
        
