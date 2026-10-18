class Solution:
    def tribonacci(self, n: int) -> int:
        prev1=1
        prev2=1
        prev3=0
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        for i in range(2,n):
            curr=prev1+prev2+prev3
            prev3=prev2
            prev2=prev1
            prev1=curr
        return curr
        
        
        
        
        
        