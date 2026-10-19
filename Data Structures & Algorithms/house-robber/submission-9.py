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
    def solvetab(self,nums,n):
        if n == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        n=len(nums)
        for i in range(2,n):
            incl=prev2+nums[i]
            excl=prev1+0
            ans = max(incl, excl)
            prev2=prev1
            prev1=ans
        return prev1
    def rob(self, nums: List[int]) -> int:
        #n=len(nums)
        # ans=self.solve(nums,n-1)
        # return ans
        #dp=[-1]*(n)
        #return self.solvemem(nums,n-1,dp)
        n=len(nums)
        return self.solvetab(nums,n)
        
