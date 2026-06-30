class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=(right+left)//2
            sum=0
            for ele in piles:
                sum+=(ele+mid-1)//mid
            if sum<=h:
                right=mid-1
            else:
                left=mid+1
        return left

            





        