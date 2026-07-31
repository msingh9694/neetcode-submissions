class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p=sorted(nums)
        for i in range(len(p)):
            q=len(p)-k
        return p[q]
            
            

    
        
        
            

